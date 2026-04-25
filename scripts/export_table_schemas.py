#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
导出核心数据表的字段结构为单独的 CSV 文件
"""

import json
import csv
from pathlib import Path

INPUT_PATH = Path(__file__).parent.parent / "database_schema" / "full_schema.json"
OUTPUT_DIR = Path(__file__).parent.parent / "database_schema"

# 核心数据表
CORE_TABLES = [
    "DataAircraft",
    "DataShip",
    "DataSubmarine",
    "DataGroundUnit",
    "DataWeapon",
    "DataFacility",
    "DataAircraftLoadouts",
    "DataShipMounts",
    "DataAircraftSensors",
    "DataShipSensors",
    "DataWeaponSensors",
    "DataSensor",
    "DataMount",
    "DataMagazine",
    "DataLoadout",
    "DataLoadoutWeapons",
]

def export_data_table_schemas():
    """导出数据表的字段结构"""
    
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        schema = json.load(f)
    
    for table_name in CORE_TABLES:
        if table_name in schema["tables"]:
            table_info = schema["tables"][table_name]
            
            csv_path = OUTPUT_DIR / f"{table_name}_columns.csv"
            
            with open(csv_path, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Field Name", "Type", "Nullable", "Default", "Primary Key", "Description"])
                
                for col in table_info["columns"]:
                    # 生成字段描述
                    desc = generate_field_description(table_name, col["name"])
                    writer.writerow([
                        col["name"],
                        col["type"],
                        "Yes" if not col["notnull"] else "No",
                        col["dflt_value"] or "",
                        "Yes" if col["pk"] else "",
                        desc
                    ])
            
            print(f"✓ {table_name}: {csv_path}")


def generate_field_description(table: str, field: str) -> str:
    """生成字段描述"""
    descriptions = {
        "DataAircraft": {
            "ID": "主键/DBID",
            "Category": "类别代码 -> EnumAircraftCategory",
            "Type": "类型代码 -> EnumAircraftType",
            "Name": "飞机名称",
            "Comments": "备注说明",
            "OperatorCountry": "国家代码 -> EnumOperatorCountry",
            "OperatorService": "军种代码 -> EnumOperatorService",
            "YearCommissioned": "服役年份",
            "YearDecommissioned": "退役年份 (0=现役)",
            "Length": "长度(米)",
            "Span": "翼展(米)",
            "Height": "高度(米)",
            "WeightEmpty": "空重(kg)",
            "WeightMax": "最大起飞重量(kg)",
            "WeightPayload": "有效载荷(kg)",
            "Crew": "机组人数",
            "Agility": "敏捷性评分",
            "ClimbRate": "爬升率(米/秒)",
            "TotalEndurance": "总续航时间(分钟)",
            "Hypothetical": "是否虚构",
            "Cost": "造价",
            "DamagePoints": "生命值",
        },
        "DataShip": {
            "ID": "主键/DBID",
            "Category": "类别代码 -> EnumShipCategory",
            "Type": "舰型代码 -> EnumShipType",
            "Name": "舰艇名称",
            "Comments": "备注说明",
            "OperatorCountry": "国家代码 -> EnumOperatorCountry",
            "OperatorService": "军种代码",
            "YearCommissioned": "服役年份",
            "YearDecommissioned": "退役年份 (0=现役)",
            "Length": "船长(米)",
            "Beam": "船宽(米)",
            "Draft": "吃水深度(米)",
            "DisplacementEmpty": "空载排水量(吨)",
            "DisplacementStandard": "标准排水量(吨)",
            "DisplacementFull": "满载排水量(吨)",
            "Crew": "舰员人数",
            "MaxSeaState": "最大工作海况",
            "Hypothetical": "是否虚构",
            "Cost": "造价",
        },
        "DataSubmarine": {
            "ID": "主键/DBID",
            "Category": "类别代码",
            "Type": "类型代码",
            "Name": "潜艇名称",
            "OperatorCountry": "国家代码 -> EnumOperatorCountry",
            "YearCommissioned": "服役年份",
            "YearDecommissioned": "退役年份 (0=现役)",
            "MaxDepth": "最大下潜深度(米)",
            "DisplacementFull": "水下排水量(吨)",
            "Crew": "艇员人数",
            "Hypothetical": "是否虚构",
        },
        "DataGroundUnit": {
            "ID": "主键/DBID",
            "Category": "类别代码 -> EnumGroundUnitCategory",
            "Name": "单位名称",
            "OperatorCountry": "国家代码 -> EnumOperatorCountry",
            "YearCommissioned": "服役年份",
            "YearDecommissioned": "退役年份 (0=现役)",
            "Mass": "重量(吨)",
            "Crew": "乘员人数",
            "ArmorGeneral": "装甲等级",
            "Hypothetical": "是否虚构",
        },
        "DataWeapon": {
            "ID": "主键/DBID",
            "Name": "武器名称",
            "Type": "类型代码 -> EnumWeaponType",
            "AirRangeMax": "空射最大射程(km)",
            "SurfaceRangeMax": "面对最大射程(km)",
            "LandRangeMax": "对地最大射程(km)",
            "SubsurfaceRangeMax": "对潜最大射程(km)",
            "MaxSpeed": "最大速度(马赫或kn)",
            "Hypothetical": "是否虚构",
        },
        "DataFacility": {
            "ID": "主键/DBID",
            "Category": "类别代码 -> EnumFacilityCategory",
            "Type": "类型代码 -> EnumFacilityType",
            "Name": "设施名称",
            "OperatorCountry": "国家代码 -> EnumOperatorCountry",
            "YearCommissioned": "服役年份",
            "YearDecommissioned": "退役年份 (0=现役)",
            "Radius": "影响半径(米)",
            "Hypothetical": "是否虚构",
        },
    }
    
    return descriptions.get(table, {}).get(field, "")


if __name__ == "__main__":
    print("=" * 60)
    print("导出核心数据表字段结构")
    print("=" * 60)
    export_data_table_schemas()
    print()
    print("完成!")
