#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CMO SQLite Intelligent Explorer MCP Server
==========================================
真正智能的自然语言 SQL 生成器

核心设计理念：
1. 零硬编码 - 所有映射（国家、组织、类型）都从数据库查询
2. LLM 驱动 - 利用 AI 大模型进行意图识别和 SQL 生成
3. 自适应 - 启动时自动扫描数据库结构

环境变量
--------
SQLITE_DB_PATH : SQLite 数据库文件路径（必须设置）
OPENAI_API_KEY : OpenAI API Key（可选，不设置则使用 Claude）
"""

import os
import re
import json
import sqlite3
import anthropic
import openai
from pathlib import Path
from typing import List, Dict, Any, Optional
from fastmcp import FastMCP

mcp = FastMCP("CMO_Intelligent_DB")

# =============================================================================
# 配置
# =============================================================================

DB_PATH: Optional[str] = os.environ.get("SQLITE_DB_PATH")
OPENAI_API_KEY: Optional[str] = os.environ.get("OPENAI_API_KEY")
ANTHROPIC_API_KEY: Optional[str] = os.environ.get("ANTHROPIC_API_KEY")

if not DB_PATH:
    raise ValueError(
        "SQLITE_DB_PATH environment variable must be set.\n"
        "Example:\n"
        "  Windows: set SQLITE_DB_PATH=D:\\path\\to\\DB3K_514.db3"
    )

# =============================================================================
# 数据库连接
# =============================================================================

class SQLiteConn:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._schema_cache: Optional[Dict[str, Any]] = None
        
    def _ensure_db(self) -> None:
        if not Path(self.db_path).exists():
            raise FileNotFoundError(f"数据库文件不存在: {self.db_path}")
    
    def execute(self, query: str, limit: int = 100) -> List[Dict[str, Any]]:
        self._ensure_db()
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            cursor = conn.cursor()
            if "limit" not in query.lower():
                query = f"{query.rstrip(';')} LIMIT {limit}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        finally:
            conn.close()
    
    def get_tables(self) -> List[str]:
        rows = self.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name",
            limit=500
        )
        return [r["name"] for r in rows if not r["name"].startswith("sqlite_")]
    
    def get_columns(self, table: str) -> List[Dict[str, Any]]:
        self._ensure_db()
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({table})")
            return [dict(row) for row in cursor.fetchall()]
        finally:
            conn.close()
    
    def get_schema(self, refresh: bool = False) -> Dict[str, Any]:
        """获取完整数据库结构（带缓存）"""
        if self._schema_cache and not refresh:
            return self._schema_cache
        
        tables = self.get_tables()
        schema = {}
        
        for table in tables:
            try:
                columns = self.get_columns(table)
                # 获取表描述（从表名推断）
                schema[table] = {
                    "columns": {col["name"]: col["type"] for col in columns},
                    "primary_key": [col["name"] for col in columns if col["pk"] == 1],
                    "row_count": self.execute(f"SELECT COUNT(*) as cnt FROM {table}", limit=1)[0]["cnt"]
                }
            except Exception:
                continue
        
        self._schema_cache = schema
        return schema
    
    def get_enum_values(self, enum_table: str) -> List[Dict[str, Any]]:
        """获取枚举表的全部值"""
        try:
            return self.execute(f"SELECT * FROM {enum_table}", limit=1000)
        except Exception:
            return []
    
    def search_by_name(self, name: str, table: str, limit: int = 10) -> List[Dict[str, Any]]:
        """按名称搜索"""
        return self.execute(
            f"SELECT * FROM {table} WHERE Name LIKE ? LIMIT {limit}",
            limit=limit
        )


db = SQLiteConn(DB_PATH)

# =============================================================================
# 智能 SQL 生成器（LLM 驱动）
# =============================================================================

class IntelligentSQLGenerator:
    """
    利用 AI 大模型进行自然语言到 SQL 的智能转换
    
    设计原则：
    1. 不硬编码任何国家/组织映射
    2. 让 AI 自己理解数据库结构
    3. 支持 NATO、五眼联盟等组织的智能展开
    """
    
    # 系统提示词模板
    SYSTEM_PROMPT = """你是一个 CMO（Command: Modern Operations）数据库的 SQL 查询生成器。

## 数据库结构
你将收到数据库的完整表结构。用户的自然语言问题需要转换为 SQL 查询。

## 核心表（最重要）
- DataAircraft: 飞机数据，OperatorCountry是国家代码
- DataShip: 舰艇数据，OperatorCountry是国家代码  
- DataSubmarine: 潜艇数据，OperatorCountry是国家代码
- DataGroundUnit: 地面单位数据，OperatorCountry是国家代码
- DataWeapon: 武器数据，包含射程(AirRangeMax等)、速度(MaxSpeed)等
- DataFacility: 地面设施数据，如机场、防空系统
- EnumOperatorCountry: 国家代码对照表 (ID=国家代码, Description=国家名)
- EnumShipType: 舰型代码表
- EnumAircraftType: 飞机类型代码表
- EnumGroundUnitCategory: 地面单位类别代码表

## 关键规则
1. YearDecommissioned=0 表示现役，非0表示退役
2. Hypothetical='False' 表示非虚构，实战使用
3. 国家查询需要 JOIN EnumOperatorCountry 表
4. NATO (ID=2060) 是一个特殊国家代码，表示北约组织

## 重要字段
- DataShip.Type 关联 EnumShipType.ID (如 DDG=Guided Missile Destroyer)
- DataAircraft.Type 关联 EnumAircraftType.ID (如 2001=Fighter)
- DataGroundUnit.Category 关联 EnumGroundUnitCategory.ID (如 2000=Armor)

## 输出格式
直接输出 JSON 格式的 SQL 查询结果，格式如下：
{
  "sql": "SELECT ...",
  "reasoning": "解释为什么这样查询",
  "tables_used": ["表名列表"],
  "confidence": 0.95
}

请用这个格式回复，不要有其他内容。"""

    def __init__(self):
        self.client = None
        self._init_llm_client()
    
    def _init_llm_client(self):
        """初始化 LLM 客户端"""
        if ANTHROPIC_API_KEY:
            self.client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
            self.model = "claude-sonnet-4-20250514"
            self.provider = "anthropic"
        elif OPENAI_API_KEY:
            openai.api_key = OPENAI_API_KEY
            self.client = openai
            self.model = "gpt-4o"
            self.provider = "openai"
        else:
            # 使用环境中的默认 API（Cursor/Trae 自带）
            try:
                self.client = anthropic.Anthropic()
                self.model = "claude-sonnet-4-20250514"
                self.provider = "anthropic"
            except Exception:
                self.client = None
                self.provider = None
    
    def generate_sql(self, question: str, schema: Dict[str, Any]) -> Dict[str, Any]:
        """生成 SQL 查询"""
        
        # 获取国家枚举（用于 LLM 理解）
        countries = db.get_enum_values("EnumOperatorCountry")
        country_info = "\n".join([
            f"- ID={c['ID']}: {c['Description']}"
            for c in countries if c.get('Description') and 'NATO' not in str(c.get('Description', ''))
        ])
        
        # 获取关键枚举
        ship_types = db.get_enum_values("EnumShipType")
        ship_type_info = "\n".join([
            f"- {t['ID']}: {t['Description']}"
            for t in ship_types if t.get('Description')
        ])[:2000]  # 限制长度
        
        aircraft_types = db.get_enum_values("EnumAircraftType")
        aircraft_type_info = "\n".join([
            f"- {t['ID']}: {t['Description']}"
            for t in aircraft_types if t.get('Description')
        ])[:2000]
        
        user_prompt = f"""## 用户问题
{question}

## 数据库中的国家列表（部分）
{country_info}

## 舰型代码（部分）
{ship_type_info}

## 飞机类型代码（部分）
{aircraft_type_info}

请生成最合适的 SQL 查询来回答用户的问题。"""

        if not self.client:
            return self._fallback_sql(question, schema)
        
        try:
            if self.provider == "anthropic":
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=1024,
                    system=self.SYSTEM_PROMPT,
                    messages=[{"role": "user", "content": user_prompt}]
                )
                result_text = response.content[0].text
            else:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": self.SYSTEM_PROMPT},
                        {"role": "user", "content": user_prompt}
                    ],
                    max_tokens=1024
                )
                result_text = response.choices[0].message.content
            
            # 解析 JSON 响应
            result = json.loads(result_text)
            return result
        except Exception as e:
            return self._fallback_sql(question, schema)
    
    def _fallback_sql(self, question: str, schema: Dict[str, Any]) -> Dict[str, Any]:
        """降级方案：基于规则的 SQL 生成"""
        q = question.lower()
        
        # 检测查询类型
        tables = []
        conditions = []
        
        # 舰艇相关
        if any(k in q for k in ["舰", "船", "ship", "carrier", "驱逐", "护卫", "航母", "cruiser", "destroyer", "frigate"]):
            tables.append("DataShip s")
            conditions.append("s.YearDecommissioned = 0")
            tables.append("EnumOperatorCountry c ON s.OperatorCountry = c.ID")
            
            # 驱逐舰
            if any(k in q for k in ["驱逐", "destroyer", "ddg", "dd "]):
                conditions.append("s.Type IN (3201, 3202, 3203)")
            
            # 航母
            if any(k in q for k in ["航母", "carrier", "cvn", "cva"]):
                conditions.append("s.Type BETWEEN 2001 AND 2011")
        
        # 飞机相关
        elif any(k in q for k in ["飞机", "aircraft", "f-", "j-", "fighter", "bomber"]):
            tables.append("DataAircraft a")
            conditions.append("a.YearDecommissioned = 0")
            tables.append("EnumOperatorCountry c ON a.OperatorCountry = c.ID")
            
            # 战斗机
            if any(k in q for k in ["战斗", "fighter", "f-22", "f-35", "f-16"]):
                conditions.append("a.Type IN (2001, 2002)")
        
        # 潜艇相关
        elif any(k in q for k in ["潜艇", "submarine", "sub"]):
            tables.append("DataSubmarine s")
            conditions.append("s.YearDecommissioned = 0")
            tables.append("EnumOperatorCountry c ON s.OperatorCountry = c.ID")
        
        # 武器相关
        elif any(k in q for k in ["导弹", "weapon", "missile", "雷达"]):
            tables.append("DataWeapon w")
            conditions.append("w.Deprecated = 'False'")
        
        # 地面单位
        elif any(k in q for k in ["坦克", "ground", "装甲", "artillery", "sam"]):
            tables.append("DataGroundUnit g")
            conditions.append("g.YearDecommissioned = 0")
            tables.append("EnumOperatorCountry c ON g.OperatorCountry = c.ID")
            
            if "坦克" in q:
                conditions.append("g.Category = 2000")
        
        # 默认查询武器
        else:
            tables.append("DataWeapon w")
        
        # 国家过滤（从问题中提取）
        for country in ["美国", "中国", "俄罗斯", "英国", "法国", "日本"]:
            if country in question or country.lower() in q:
                if "s." in "".join(tables) or "g." in "".join(tables) or "a." in "".join(tables):
                    country_en = {"美国": "United States", "中国": "China", "俄罗斯": "Russia",
                                  "英国": "United Kingdom", "法国": "France", "日本": "Japan"}.get(country, country)
                    conditions.append(f"c.Description LIKE '%{country_en}%'")
                    break
        
        # 构建 SQL
        base_table = tables[0].split()[0]
        alias = tables[0].split()[1] if len(tables[0].split()) > 1 else base_table[0].lower()
        
        sql = f"SELECT * FROM {tables[0]}"
        for t in tables[1:]:
            if "ON" in t:
                sql += f" JOIN {t}"
            else:
                sql += f", {t}"
        
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        
        sql += " LIMIT 20"
        
        return {
            "sql": sql,
            "reasoning": "Fallback: 基于关键词匹配生成",
            "tables_used": [t.split()[0] for t in tables],
            "confidence": 0.5
        }


# 全局实例
sql_generator = None

def get_generator():
    global sql_generator
    if sql_generator is None:
        sql_generator = IntelligentSQLGenerator()
    return sql_generator


# =============================================================================
# 安全 SQL 执行
# =============================================================================

def safe_select(sql: str, limit: int = 100) -> List[Dict[str, Any]]:
    """安全执行 SELECT 查询"""
    sql = sql.strip()
    ql = sql.lower()
    
    if not ql.startswith("select"):
        raise ValueError("仅允许 SELECT 查询")
    
    for kw in ["drop", "delete", "insert", "update", "create", "alter", "truncate"]:
        if kw in ql:
            raise ValueError(f"不允许的操作: {kw}")
    
    return db.execute(sql, limit)


# =============================================================================
# MCP 工具
# =============================================================================

@mcp.tool()
def cmo_intelligent_query(user_question: str) -> str:
    """智能自然语言查询（核心功能）
    
    这是最主要的查询接口。它会：
    1. 利用 AI 大模型理解用户问题
    2. 自动识别查询意图（国家、类型、时间等）
    3. 生成最优 SQL 查询
    4. 支持 NATO、五眼联盟等组织的智能展开
    
    Args:
        user_question: 自然语言问题
            示例：
            - "美军有哪些驱逐舰"
            - "北约国家的现役战斗机"
            - "中国航母的 DBID"
            - "射程最远的反舰导弹"
            - "五眼联盟的预警机"
    
    Returns:
        JSON 格式结果
    """
    try:
        schema = db.get_schema()
        generator = get_generator()
        
        # 使用 LLM 生成 SQL
        result = generator.generate_sql(user_question, schema)
        
        sql = result.get("sql", "")
        if not sql:
            return json.dumps({
                "success": False,
                "error": "无法生成 SQL 查询",
                "question": user_question
            }, ensure_ascii=False)
        
        # 执行查询
        rows = safe_select(sql)
        
        return json.dumps({
            "success": True,
            "question": user_question,
            "sql_generated": sql,
            "reasoning": result.get("reasoning", ""),
            "confidence": result.get("confidence", 0),
            "rows": rows,
            "count": len(rows),
            "ai_powered": generator.provider is not None
        }, ensure_ascii=False, indent=2)
        
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": str(e),
            "question": user_question
        }, ensure_ascii=False)


@mcp.tool()
def cmo_query(user_question: str) -> str:
    """简洁版自然语言查询（向后兼容）
    
    简化的查询接口，适合简单问题。
    """
    try:
        schema = db.get_schema()
        generator = get_generator()
        result = generator.generate_sql(user_question, schema)
        sql = result.get("sql", "")
        
        if not sql:
            return json.dumps({
                "success": False,
                "error": "无法生成 SQL"
            }, ensure_ascii=False)
        
        rows = safe_select(sql)
        
        return json.dumps({
            "success": True,
            "sql": sql,
            "rows": rows,
            "count": len(rows)
        }, ensure_ascii=False)
        
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)}, ensure_ascii=False)


@mcp.tool()
def cmo_list_tables() -> List[str]:
    """列出数据库中所有表名"""
    return db.get_tables()


@mcp.tool()
def cmo_describe_table(table_name: str) -> List[Dict[str, Any]]:
    """获取指定表的字段结构"""
    return db.get_columns(table_name)


@mcp.tool()
def cmo_get_schema(refresh: bool = False) -> Dict[str, Any]:
    """获取完整数据库结构摘要"""
    return db.get_schema(refresh=refresh)


@mcp.tool()
def cmo_get_countries() -> str:
    """获取所有国家列表"""
    countries = db.get_enum_values("EnumOperatorCountry")
    return json.dumps({
        "countries": countries,
        "count": len(countries),
        "note": "NATO (ID=2060) 是一个聚合组织，不代表单一国家"
    }, ensure_ascii=False, indent=2)


@mcp.tool()
def cmo_raw_query(sql_query: str) -> str:
    """直接执行 SELECT SQL（高级用法）
    
    Args:
        sql_query: 完整的 SELECT 语句
    """
    try:
        rows = safe_select(sql_query, limit=200)
        return json.dumps({
            "success": True,
            "rows": rows,
            "count": len(rows)
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)}, ensure_ascii=False)


@mcp.tool()
def cmo_search(name: str, unit_type: str = "") -> str:
    """按名称搜索单位
    
    Args:
        name: 单位名称（支持模糊匹配）
        unit_type: 单位类型 (aircraft/ship/submarine/ground/facility/weapon)
    """
    try:
        table_map = {
            "aircraft": "DataAircraft",
            "ship": "DataShip",
            "submarine": "DataSubmarine",
            "ground": "DataGroundUnit",
            "facility": "DataFacility",
            "weapon": "DataWeapon"
        }
        
        table = table_map.get(unit_type.lower(), "DataAircraft")
        rows = db.search_by_name(f"%{name}%", table, limit=20)
        
        return json.dumps({
            "success": True,
            "table": table,
            "name": name,
            "rows": rows,
            "count": len(rows)
        }, ensure_ascii=False, indent=2)
        
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)}, ensure_ascii=False)


# =============================================================================
# 启动
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("CMO Intelligent DB Explorer MCP Server")
    print("=" * 60)
    print(f"数据库路径: {DB_PATH}")
    print(f"数据库存在: {Path(DB_PATH).exists()}")
    print(f"LLM 驱动: {'已启用' if get_generator().provider else '未启用（使用降级方案）'}")
    print("=" * 60)
    
    # 预热：加载数据库结构
    print("正在加载数据库结构...")
    schema = db.get_schema()
    print(f"已加载 {len(schema)} 张表")
    
    mcp.run()
