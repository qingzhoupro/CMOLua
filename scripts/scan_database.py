#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据库结构扫描器
将 CMO 数据库的所有表和字段保存到本地文件
"""

import json
import sqlite3
import sys
from pathlib import Path
from datetime import datetime

# 获取项目根目录（向上两级）
PROJECT_ROOT = Path(__file__).parent.parent.resolve()

# 数据库路径 - 优先从环境变量或 .env 文件读取
def get_db_path():
    """获取数据库路径，按优先级：环境变量 > .env > mcp/db/*.db3"""
    import os

    # 1. 环境变量
    env_path = os.environ.get("SQLITE_DB_PATH")
    if env_path and Path(env_path).exists():
        return env_path

    # 2. .env 文件
    env_file = PROJECT_ROOT / ".env"
    if env_file.exists():
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("SQLITE_DB_PATH="):
                    path = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if Path(path).exists():
                        return path

    # 3. 自动发现
    db_dir = PROJECT_ROOT / "mcp" / "db"
    if db_dir.exists():
        candidates = sorted(db_dir.glob("*.db3"), key=lambda x: x.stat().st_mtime, reverse=True)
        if candidates:
            return str(candidates[0])

    return None

DB_PATH = get_db_path()
OUTPUT_DIR = PROJECT_ROOT / "database_schema"

if not DB_PATH:
    print("=" * 60)
    print("错误: 未找到数据库文件")
    print("=" * 60)
    print()
    print("请运行以下命令进行配置:")
    print("  python scripts/config.py --interactive")
    print()
    print("或手动设置环境变量:")
    print("  Windows: set SQLITE_DB_PATH=D:\\path\\to\\DB3K_514.db3")
    print("  Linux/Mac: export SQLITE_DB_PATH=/path/to/DB3K_514.db3")
    print()
    sys.exit(1)

def scan_database():
    """扫描数据库，返回完整的结构信息"""
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # 获取所有表
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")
    tables = [row["name"] for row in cursor.fetchall()]
    
    schema_data = {
        "metadata": {
            "database": DB_PATH,
            "scanned_at": datetime.now().isoformat(),
            "table_count": len(tables)
        },
        "tables": {}
    }
    
    # 枚举数据缓存
    enum_data = {}
    
    for table_name in tables:
        # 获取表结构
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [dict(row) for row in cursor.fetchall()]
        
        # 获取行数
        try:
            cursor.execute(f"SELECT COUNT(*) as cnt FROM {table_name}")
            row_count = cursor.fetchone()["cnt"]
        except:
            row_count = 0
        
        # 获取 CREATE SQL
        cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        create_sql = cursor.fetchone()["sql"] or ""
        
        schema_data["tables"][table_name] = {
            "columns": columns,
            "row_count": row_count,
            "create_sql": create_sql,
            "primary_key": [col["name"] for col in columns if col["pk"] == 1]
        }
        
        # 收集枚举数据
        if table_name.startswith("Enum"):
            cursor.execute(f"SELECT * FROM {table_name}")
            enum_data[table_name] = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    
    # 添加枚举数据
    schema_data["enumerations"] = enum_data
    
    return schema_data


def save_schema(schema_data):
    """保存结构数据到文件"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. 保存完整 JSON
    json_path = OUTPUT_DIR / "full_schema.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(schema_data, f, ensure_ascii=False, indent=2)
    print(f"✓ 完整结构: {json_path}")
    
    # 2. 生成 Markdown 文档
    md_path = OUTPUT_DIR / "schema_documentation.md"
    
    md_content = f"""# CMO 数据库结构文档

> 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
> 
> 数据库: `{DB_PATH}`
> 
> 共 {schema_data['metadata']['table_count']} 张表

---

## 目录

"""
    
    # 按类别分组
    categories = {
        "数据表 (Data*)": [],
        "枚举表 (Enum*)": [],
        "其他": []
    }
    
    for table_name in schema_data["tables"]:
        if table_name.startswith("Data"):
            categories["数据表 (Data*)"].append(table_name)
        elif table_name.startswith("Enum"):
            categories["枚举表 (Enum*)"].append(table_name)
        else:
            categories["其他"].append(table_name)
    
    # 生成目录
    for category, tables in categories.items():
        if tables:
            md_content += f"\n### {category}\n\n"
            for table in sorted(tables):
                md_content += f"- [{table}](#{table.lower().replace('*', '').replace('_', '').replace(' ', '')})  \n"
    
    # 详细表结构
    md_content += "\n\n---\n\n## 详细表结构\n\n"
    
    for table_name, table_info in sorted(schema_data["tables"].items()):
        md_content += f"\n### {table_name}\n\n"
        md_content += f"**行数**: {table_info['row_count']}  \n"
        md_content += f"**主键**: {', '.join(table_info['primary_key']) if table_info['primary_key'] else '无'}\n\n"
        
        # 列信息表格
        md_content += "| 列名 | 类型 | 可为空 | 默认值 | 主键 |\n"
        md_content += "|------|------|--------|--------|------|\n"
        
        for col in table_info["columns"]:
            md_content += f"| {col['name']} | {col['type']} | {'否' if col['notnull'] else '是'} | {col['dflt_value'] or '-'} | {'✓' if col['pk'] else '-'} |\n"
        
        # 如果是枚举表，添加值列表
        if table_name in schema_data.get("enumerations", {}):
            enum_values = schema_data["enumerations"][table_name]
            if enum_values:
                md_content += f"\n**枚举值** ({len(enum_values)} 个):\n\n"
                md_content += "| ID | 描述 |\n"
                md_content += "|-----|------|\n"
                for ev in enum_values[:50]:  # 最多显示50条
                    desc = str(ev.get('Description') or ev.get('description') or ev.get('desc') or '-')
                    md_content += f"| {ev.get('ID', ev.get('id', '-'))} | {desc} |\n"
                if len(enum_values) > 50:
                    md_content += f"\n_... 共 {len(enum_values)} 个值_\n"
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"✓ Markdown 文档: {md_path}")
    
    # 3. 保存每个枚举表为单独的 CSV
    for enum_name, enum_values in schema_data.get("enumerations", {}).items():
        if enum_values:
            csv_path = OUTPUT_DIR / f"{enum_name}.csv"
            if enum_values:
                headers = list(enum_values[0].keys())
                with open(csv_path, "w", encoding="utf-8") as f:
                    f.write(",".join(headers) + "\n")
                    for row in enum_values:
                        values = [str(row.get(h, '')) for h in headers]
                        f.write(",".join(values) + "\n")
            print(f"✓ 枚举表: {csv_path}")
    
    # 4. 保存快速参考文件
    quick_ref = {
        "核心数据表": {
            "DataAircraft": "飞机数据 - ID, Name, Type, OperatorCountry, YearCommissioned, YearDecommissioned",
            "DataShip": "舰艇数据 - ID, Name, Type, OperatorCountry, YearCommissioned, YearDecommissioned",
            "DataSubmarine": "潜艇数据 - ID, Name, Type, OperatorCountry, YearCommissioned, YearDecommissioned",
            "DataGroundUnit": "地面单位 - ID, Name, Category, OperatorCountry, YearCommissioned, YearDecommissioned",
            "DataWeapon": "武器数据 - ID, Name, Type, AirRangeMax, SurfaceRangeMax, MaxSpeed",
            "DataFacility": "地面设施 - ID, Name, Category, Type, OperatorCountry, YearCommissioned"
        },
        "关键枚举表": {
            "EnumOperatorCountry": "国家代码对照 - ID -> Description",
            "EnumShipType": "舰型代码 - ID -> Description",
            "EnumAircraftType": "飞机类型代码 - ID -> Description",
            "EnumAircraftCategory": "飞机类别 - ID -> Description",
            "EnumGroundUnitCategory": "地面单位类别 - ID -> Description",
            "EnumFacilityCategory": "设施类别 - ID -> Description",
            "EnumWeaponType": "武器类型 - ID -> Description"
        },
        "查询规则": {
            "现役单位": "YearDecommissioned = 0",
            "虚构单位": "Hypothetical = 'False'",
            "国家过滤": "JOIN EnumOperatorCountry ON OperatorCountry = ID",
            "NATO国家": "OperatorCountry = 2060"
        }
    }
    
    ref_path = OUTPUT_DIR / "quick_reference.json"
    with open(ref_path, "w", encoding="utf-8") as f:
        json.dump(quick_ref, f, ensure_ascii=False, indent=2)
    print(f"✓ 快速参考: {ref_path}")
    
    return schema_data


if __name__ == "__main__":
    print("=" * 60)
    print("CMO 数据库结构扫描器")
    print("=" * 60)
    print(f"数据库: {DB_PATH}")
    print()
    
    schema = scan_database()
    save_schema(schema)
    
    print()
    print("=" * 60)
    print("扫描完成!")
    print("=" * 60)
