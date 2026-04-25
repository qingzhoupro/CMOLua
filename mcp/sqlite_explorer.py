#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CMO SQLite Explorer MCP Server
==============================
基于真实数据库 schema 的自然语言 SQL 生成器。

Schema 依据 database_schema/ 目录下的 CSV 文件。
所有 SQL 均通过 JOIN 关联查询，返回人类可读的描述而非代码值。

核心表
------
- DataShip      : 舰艇     (JOIN EnumShipType + EnumOperatorCountry)
- DataAircraft   : 飞机     (JOIN EnumAircraftType + EnumOperatorCountry)
- DataSubmarine  : 潜艇     (JOIN EnumSubmarineType + EnumOperatorCountry)
- DataGroundUnit : 地面单位 (JOIN EnumGroundUnitCategory + EnumOperatorCountry)
- DataWeapon     : 武器/导弹
- DataFacility   : 地面设施 (JOIN EnumFacilityCategory + EnumOperatorCountry)
- DataAircraftLoadouts: 飞机挂载配置 (JOIN DataAircraft)

过滤规则
--------
- 现役: YearDecommissioned = 0
- 虚构: Hypothetical = 'False'
- 国家: OperatorCountry → EnumOperatorCountry.Description

环境变量
--------
SQLITE_DB_PATH : 数据库路径（可选，未设则自动发现 mcp/db/*.db3）
"""

from pathlib import Path
import sqlite3
import os
import re
import json
from typing import List, Dict, Any, Optional
from fastmcp import FastMCP

mcp = FastMCP("CMO_DBID_Lookup")

# =============================================================================
# 数据库路径解析
# =============================================================================

DB_PATH: Optional[str] = os.environ.get("SQLITE_DB_PATH")
if not DB_PATH:
    script_dir = Path(__file__).parent.resolve()
    candidates = sorted((script_dir / "db").glob("*.db3")) if (script_dir / "db").exists() else []
    if candidates:
        DB_PATH = str(candidates[0])
        print(f"[INFO] Auto-discovered DB: {DB_PATH}")
    else:
        raise ValueError(
            "SQLITE_DB_PATH must be set.\n"
            "Or place your DB3K_*.db3 file in mcp/db/ directory."
        )

# =============================================================================
# 数据库连接
# =============================================================================

class SQLiteConn:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _ensure_db(self) -> None:
        if not Path(self.db_path).exists():
            raise FileNotFoundError(f"Database not found: {self.db_path}")

    def execute(self, query: str, limit: int = 100) -> List[Dict[str, Any]]:
        self._ensure_db()
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            cur = conn.cursor()
            if "limit" not in query.lower():
                query = f"{query.rstrip(';')} LIMIT {limit}"
            cur.execute(query)
            return [dict(row) for row in cur.fetchall()]
        finally:
            conn.close()

    def get_tables(self) -> List[str]:
        return [r["name"] for r in self.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name", limit=300
        )]

    def get_columns(self, table: str) -> List[Dict[str, Any]]:
        return self.execute(f"PRAGMA table_info({table})")

    def lookup_enum(self, table: str, col: str = "Description") -> Dict[int, str]:
        rows = self.execute(f"SELECT ID, {col} FROM {table} LIMIT 500")
        return {r["ID"]: r[col] for r in rows}


db = SQLiteConn(DB_PATH)

# =============================================================================
# 枚举表缓存（启动时加载一次）
# =============================================================================

COUNTRY_MAP: Dict[int, str] = {}    # ID → 国家名称（英文）
SHIP_TYPE_MAP: Dict[int, str] = {}  # ID → 舰型描述
AIRCRAFT_TYPE_MAP: Dict[int, str] = {}
SUB_TYPE_MAP: Dict[int, str] = {}
GND_CAT_MAP: Dict[int, str] = {}
FAC_CAT_MAP: Dict[int, str] = {}
WEAPON_TYPE_MAP: Dict[int, str] = {}

def _load_enums() -> None:
    global COUNTRY_MAP, SHIP_TYPE_MAP, AIRCRAFT_TYPE_MAP, SUB_TYPE_MAP
    global GND_CAT_MAP, FAC_CAT_MAP, WEAPON_TYPE_MAP
    try:
        COUNTRY_MAP = db.lookup_enum("EnumOperatorCountry", "Description")
        SHIP_TYPE_MAP = db.lookup_enum("EnumShipType", "Description")
        try:
            AIRCRAFT_TYPE_MAP = db.lookup_enum("EnumAircraftType", "Description")
        except Exception:
            AIRCRAFT_TYPE_MAP = {}
        try:
            SUB_TYPE_MAP = db.lookup_enum("EnumSubmarineType", "Description")
        except Exception:
            SUB_TYPE_MAP = {}
        try:
            GND_CAT_MAP = db.lookup_enum("EnumGroundUnitCategory", "Description")
        except Exception:
            GND_CAT_MAP = {}
        try:
            FAC_CAT_MAP = db.lookup_enum("EnumFacilityCategory", "Description")
        except Exception:
            FAC_CAT_MAP = {}
        try:
            WEAPON_TYPE_MAP = db.lookup_enum("EnumWeaponType", "Description")
        except Exception:
            WEAPON_TYPE_MAP = {}
    except Exception as e:
        print(f"[WARN] Failed to load enum tables: {e}")

_load_enums()

# =============================================================================
# 自然语言 → 国家代码
# =============================================================================

COUNTRY_KEYWORDS: Dict[str, int] = {
    # 英文全称
    "united states": 2101, "us": 2101, "usa": 2101, "america": 2101,
    "china": 2018, "chinese": 2018,
    "russia": 2079, "russian": 2079,
    "united kingdom": 2100, "uk": 2100, "britain": 2100, "british": 2100,
    "france": 2032, "french": 2032,
    "japan": 2048, "japanese": 2048,
    "south korea": 2086, "korea": 2086, "rok": 2086,
    "north korea": 2065, "dprk": 2065,
    "germany": 2035, "german": 2035,
    "india": 2041, "indian": 2041,
    "australia": 2006, "australian": 2006,
    "italy": 2047, "italian": 2047,
    "spain": 2089, "spanish": 2089,
    "netherlands": 2061, "dutch": 2061,
    "sweden": 2091, "swedish": 2091,
    "israel": 2046, "israeli": 2046,
    "taiwan": 2094,
    "iran": 2043, "iranian": 2043,
    "iraq": 2044, "iraqi": 2044,
    "pakistan": 2069, "pakistani": 2069,
    "singapore": 2082, "singaporean": 2082,
    "indonesia": 2042, "indonesian": 2042,
    "malaysia": 2056, "malaysian": 2056,
    "thailand": 2095, "thai": 2095,
    "philippines": 2073, "filipino": 2073,
    "vietnam": 2103, "vietnamese": 2103,
    "turkey": 2097, "turkish": 2097,
    "poland": 2074, "polish": 2074,
    "ukraine": 2099, "ukrainian": 2099,
    "nato": 2060,
    # 中文简称
    "美国": 2101, "美军": 2101, "美": 2101,
    "中国": 2018, "中共": 2018, "解放军": 2018,
    "俄国": 2079, "俄罗斯": 2079, "俄军": 2079, "俄": 2079,
    "英国": 2100, "英军": 2100, "英": 2100,
    "法国": 2032, "法军": 2032, "法": 2032,
    "日本": 2048, "自卫队": 2048, "日军": 2048, "海上自卫队": 2048,
    "韩国": 2086, "韩军": 2086, "南韩": 2086, "韩": 2086,
    "朝鲜": 2065, "北韩": 2065, "朝军": 2065,
    "德国": 2035, "德军": 2035, "德": 2035,
    "印度": 2041, "印军": 2041, "印": 2041,
    "澳大利亚": 2006, "澳军": 2006, "澳洲": 2006, "澳": 2006,
    "意大利": 2047, "以军": 2047, "意": 2047,
    "以色列": 2046,
    "台湾": 2094, "台军": 2094, "中华民国": 2094,
    "北约": 2060,
}

def detect_country(q: str) -> Optional[int]:
    """从问题中检测国家，返回国家代码 ID，无则返回 None"""
    q_lower = q.lower()
    for keyword, country_id in COUNTRY_KEYWORDS.items():
        if keyword in q_lower or keyword in q:
            return country_id
    return None

# =============================================================================
# 舰型类型码
# =============================================================================

SHIP_TYPE_CODES = {
    "destroyer": [3202, 3203],   # DD, DDG — 实测 3201 不存在
    "frigate": [3302, 3303],
    "lcs": [3306],
    "corvette": [3304, 3305],
    "carrier": [2001, 2002, 2007, 2008],
    "cruiser": [3102, 3103, 3104, 3105, 3106, 3107, 3108],
    "battleship": [3001, 3002, 3003, 3004, 3005],
    "amphibious": list(range(4002, 4029)),
    "oiler": [5022, 5023, 5024, 5025, 5106],
    "mine_warfare": [6002, 6003, 6004, 6010],
    "patrol": list(range(3401, 3424)),
    "auxiliary": list(range(5001, 5045)) + list(range(5101, 5109)),
}

def detect_ship_type_codes(q: str) -> Optional[List[int]]:
    """从问题中检测舰型，返回类型码列表"""
    q_lower = q.lower()
    if any(k in q_lower for k in ["ddg", "guided missile destroyer", "zumwalt", "burke", "arleigh"]):
        return SHIP_TYPE_CODES["destroyer"] + [3203, 3208, 3209]
    if any(k in q_lower for k in ["destroyer", "驱逐舰", "驱逐", "dd ", "ddg ", "dd-"]):
        return SHIP_TYPE_CODES["destroyer"]
    if any(k in q_lower for k in ["frigate", "护卫舰", "护卫", "ffg", "ffg-"]):
        return SHIP_TYPE_CODES["frigate"]
    if any(k in q_lower for k in ["corvette", "轻护", "轻型护卫"]):
        return SHIP_TYPE_CODES["corvette"]
    if any(k in q_lower for k in ["carrier", "航母", "cvn", "cv ", "lha", "lhd"]):
        return SHIP_TYPE_CODES["carrier"] + SHIP_TYPE_CODES["amphibious"]
    if any(k in q_lower for k in ["cruiser", "巡洋舰", "巡洋", "cg-"]):
        return SHIP_TYPE_CODES["cruiser"]
    if any(k in q_lower for k in ["amphibious", "两栖", "登陆舰", "lpd", "lsd", "lst"]):
        return SHIP_TYPE_CODES["amphibious"]
    if any(k in q_lower for k in ["oiler", "补给舰", "油船", "t-ao"]):
        return SHIP_TYPE_CODES["oiler"]
    if any(k in q_lower for k in ["minesweeper", "mcm", "mho", "猎雷", "扫雷", "mine"]):
        return SHIP_TYPE_CODES["mine warfare"]
    if any(k in q_lower for k in ["escort", "护航"]):
        return SHIP_TYPE_CODES["destroyer_escort"] + SHIP_TYPE_CODES["frigate"]
    if any(k in q_lower for k in ["lcs", "littoral", "濒海", "近海巡逻"]):
        return SHIP_TYPE_CODES["lcs"] + SHIP_TYPE_CODES["patrol"]
    if any(k in q_lower for k in ["patrol", "巡逻", "pc-", "pg-", "导弹艇", "炮艇"]):
        return SHIP_TYPE_CODES["patrol"]
    if any(k in q_lower for k in ["battleship", "战列舰", "bb-"]):
        return SHIP_TYPE_CODES["battleship"]
    return None

# =============================================================================
# 飞机类型码
# =============================================================================

AIRCRAFT_CAT_CODES = {
    "fighter": [2001, 2002],     # Fixed Wing
    "fixed wing": [2001, 2002],
    "helicopter": [2003],
    "rotor": [2003],
    "tiltrotor": [2004],
    "seaplane": [2007],
    "amphibian": [2008],
    "固定翼": [2001, 2002],
    "战斗机": [2001, 2002],
    "直升机": [2003],
    "舰载机": [2002],
    "预警机": [2001],
    "轰炸机": [2001],
    "加油机": [2001, 2002],
    "运输机": [2001, 2002, 2003],
    "预警": [2001],
    "侦察": [2001],
    "电子战": [2001],
}

def detect_aircraft_cat_codes(q: str) -> Optional[List[int]]:
    q_lower = q.lower()
    for kw, codes in AIRCRAFT_CAT_CODES.items():
        if kw in q_lower:
            return codes
    return None

# =============================================================================
# 地面单位类别码
# =============================================================================

GND_CAT_CODES = {
    "tank": [2000], "坦克": [2000],
    "armor": [2000, 2500], "装甲": [2000, 2500],
    "artillery": [3000, 3010, 3020, 3110, 3120, 3200], "火炮": [3000, 3010, 3020, 3110, 3120, 3200], "炮兵": [3000, 3010, 3020],
    "sam": [6000], "防空": [6000], "地空导弹": [6000],
    "ssm": [4000], "地对地": [4000], "战术导弹": [4000],
    "infantry": [1000, 1100], "步兵": [1000, 1100], "轻步兵": [1000],
    "mortar": [3200], "迫击炮": [3200],
    "aaa": [5000], "高炮": [5000], "自行高炮": [5000],
    "recon": [10000], "侦察": [10000],
    "engineer": [7000], "工程": [7000],
    "supply": [8000], "后勤": [8000], "补给": [8000],
    "atgm": [13000], "反坦克": [13000], "反载具": [13000],
    "radar": [14000], "雷达": [14000],
    "hq": [15000], "指挥部": [15000], "指挥": [15000],
}

def detect_gnd_cat_codes(q: str) -> Optional[List[int]]:
    q_lower = q.lower()
    for kw, codes in GND_CAT_CODES.items():
        if kw in q_lower:
            return codes
    return None

# =============================================================================
# 设施类别码
# =============================================================================

FAC_CAT_CODES = {
    "air base": [9001], "airport": [9001], "机场": [9001], "空军基地": [9001], "基地": [9001],
    "runway": [2001, 2002, 2003], "跑道": [2001, 2002, 2003],
    "bunker": [3003, 3004, 3006, 3012], "永备工事": [3003, 3004], "碉堡": [3003],
    "building": [3001, 3002, 3003], "建筑": [3001, 3002],
    "underground": [3004, 3012], "地下": [3004],
    "sam site": [6000], "sam": [6000], "防空阵地": [6000], "防空导弹": [6000],
    "radar": [9001], "预警雷达": [9001], "雷达站": [9001],
    "naval base": [3001], "海军基地": [3001],
    "airstrip": [2001], "简易机场": [2001],
}

def detect_fac_cat_codes(q: str) -> Optional[List[int]]:
    q_lower = q.lower()
    for kw, codes in FAC_CAT_CODES.items():
        if kw in q_lower:
            return codes
    return None

# =============================================================================
# SQL 生成核心
# =============================================================================

def _build_in_clause(codes: List[int]) -> str:
    """构建 IN (x, y, z) 子句"""
    return f"IN ({','.join(str(c) for c in codes)})"

def gen_sql(question: str, limit: int = 15) -> str:
    """
    根据自然语言问题生成 SQL。

    返回格式: (sql, description)
    - sql: 要执行的 SQL 字符串
    - description: 查询描述（用于结果展示）
    """
    q = question.lower()
    orig_q = question

    # ----- 1. 精确 DBID / 名称查询 -----
    if re.search(r"(dbid|db_id|id.*编号|编号|代号|查询.*dbid|find.*id)", q):
        name = None
        # 从引号中提取
        m = re.search(r"['\"](.+?)['\"]", orig_q)
        if m:
            name = m.group(1).strip()
        # 从 "XXX的DBID" 提取
        if not name:
            m2 = re.search(r"(.+?)的\s*(?:dbid|编号|代号)", orig_q.strip(), re.IGNORECASE)
            if m2:
                name = m2.group(1).strip()
        # 提取英文/数字标识
        if not name:
            m3 = re.search(r"\b([A-Za-z0-9][-A-Za-z0-9]{1,25})\b", orig_q)
            if m3:
                name = m3.group(1).strip()
        if not name:
            name = orig_q.strip()

        name_like = name.replace("'", "''")

        # 根据关键词决定表
        if any(k in q for k in ["坦克", "ground", "装甲", "火炮", "自行火炮", "smash"]):
            codes = detect_gnd_cat_codes(q)
            cond = f"g.Name LIKE '%{name_like}%'"
            if codes:
                type_sql = " OR ".join([f"g.Category={c}" for c in codes])
                cond = f"({cond}) AND ({type_sql})"
            return (
                f"SELECT g.ID, g.Name, c.Description AS Country, "
                f"cat.Description AS Category, g.YearCommissioned "
                f"FROM DataGroundUnit g "
                f"LEFT JOIN EnumOperatorCountry c ON g.OperatorCountry=c.ID "
                f"LEFT JOIN EnumGroundUnitCategory cat ON g.Category=cat.ID "
                f"WHERE {cond} AND g.Hypothetical='0' "
                f"LIMIT {limit}",
                f"地面单位: {name}"
            )
        if any(k in q for k in ["舰", "ship", "船", "carrier", "destroyer", "frigate", "驱逐", "护卫"]):
            return (
                f"SELECT s.ID, s.Name, c.Description AS Country, "
                f"st.Description AS ShipType, s.YearCommissioned, s.Length, s.Crew "
                f"FROM DataShip s "
                f"LEFT JOIN EnumOperatorCountry c ON s.OperatorCountry=c.ID "
                f"LEFT JOIN EnumShipType st ON s.Type=st.ID "
                f"WHERE s.Name LIKE '%{name_like}%' AND s.Hypothetical='0' "
                f"LIMIT {limit}",
                f"舰艇: {name}"
            )
        if any(k in q for k in ["潜艇", "submarine", "潜"]):
            return (
                f"SELECT sub.ID, sub.Name, c.Description AS Country, "
                f"st.Description AS SubType, sub.YearCommissioned, sub.DisplacementFull, sub.Crew "
                f"FROM DataSubmarine sub "
                f"LEFT JOIN EnumOperatorCountry c ON sub.OperatorCountry=c.ID "
                f"LEFT JOIN EnumSubmarineType st ON sub.Type=st.ID "
                f"WHERE sub.Name LIKE '%{name_like}%' AND sub.Hypothetical='0' "
                f"LIMIT {limit}",
                f"潜艇: {name}"
            )
        if any(k in q for k in ["防空", "sam", "hawk", "patriot", "hq-", "s-300", "s-400", "天弓", "机场", "基地", "facility", "雷达"]):
            return (
                f"SELECT f.ID, f.Name, c.Description AS Country, "
                f"fc.Description AS Category, f.YearCommissioned, f.Crew "
                f"FROM DataFacility f "
                f"LEFT JOIN EnumOperatorCountry c ON f.OperatorCountry=c.ID "
                f"LEFT JOIN EnumFacilityCategory fc ON f.Category=fc.ID "
                f"WHERE f.Name LIKE '%{name_like}%' AND f.Hypothetical='0' "
                f"LIMIT {limit}",
                f"地面设施: {name}"
            )
        if any(k in q for k in ["aircraft", "飞机", "f-", "j-", "f/a-", "e-", "kc-", "预警", "轰炸", "f18", "f16", "f15", "f22", "f35", "歼"]):
            return (
                f"SELECT a.ID, a.Name, c.Description AS Country, "
                f"at.Description AS AircraftType, a.YearCommissioned, a.Span, a.MaxRange "
                f"FROM DataAircraft a "
                f"LEFT JOIN EnumOperatorCountry c ON a.OperatorCountry=c.ID "
                f"LEFT JOIN EnumAircraftType at ON a.Type=at.ID "
                f"WHERE a.Name LIKE '%{name_like}%' AND a.Hypothetical='0' "
                f"LIMIT {limit}",
                f"飞机: {name}"
            )
        # 默认按武器查
        return (
            f"SELECT w.ID, w.Name, "
            f"wt.Description AS WeaponType, w.AirRangeMax, w.SurfaceRangeMax, w.MaxSpeed "
            f"FROM DataWeapon w "
            f"LEFT JOIN EnumWeaponType wt ON w.Type=wt.ID "
            f"WHERE w.Name LIKE '%{name_like}%' AND w.Hypothetical='0' "
            f"LIMIT {limit}",
            f"武器: {name}"
        )

    # ----- 2. 国家 + 类型 -----
    country_id = detect_country(q)
    ship_codes = detect_ship_type_codes(q)
    ac_codes = detect_aircraft_cat_codes(q)
    gnd_codes = detect_gnd_cat_codes(q)
    fac_codes = detect_fac_cat_codes(q)

    has_country = country_id is not None
    has_ship = ship_codes is not None
    has_aircraft = ac_codes is not None
    has_gnd = gnd_codes is not None
    has_fac = fac_codes is not None

    # 射程/速度/参数查询 → 武器表
    if any(k in q for k in ["射程", "range", "速度", "speed", "最大速度", "航速"]):
        cols = ["w.ID", "w.Name"]
        if any(k in q for k in ["射程", "range"]):
            cols += ["w.AirRangeMax", "w.SurfaceRangeMax", "w.LandRangeMax"]
        if any(k in q for k in ["速度", "speed", "航速"]):
            cols += ["w.MaxSpeed"]
        if "速度" in q or "航速" in q or "max speed" in q:
            cols += ["w.MaxSpeed"]
        cols += ["wt.Description AS WeaponType"]

        extra = ""
        if has_country:
            extra += f" AND w.OperatorCountry={country_id}"
        if any(k in q for k in ["空射", "air-to-air", "空空"]):
            extra += " AND w.AirRangeMax > 0"
        if any(k in q for k in ["反舰", "ship-to-ship", "舰载"]):
            extra += " AND w.SurfaceRangeMax > 0"
        if any(k in q for k in ["对地", "land", "地对地", "空地"]):
            extra += " AND w.LandRangeMax > 0"
        if any(k in q for k in ["反潜", "asw", "反潜"]):
            extra += " AND w.SubsurfaceRangeMax > 0"
        if any(k in q for k in ["鱼叉", "harpoon", "鱼叉"]):
            extra += " AND w.Name LIKE '%Harpoon%'"
        if any(k in q for k in ["战斧", "tomahawk", "战斧"]):
            extra += " AND w.Name LIKE '%Tomahawk%'"
        if any(k in q for k in ["aim-120", "amraam", "流星"]):
            extra += " AND w.Name LIKE '%AMRAAM%'"
        if any(k in q for k in ["aim-9", "sidewinder", "响尾蛇"]):
            extra += " AND w.Name LIKE '%Sidewinder%'"

        col_str = ", ".join(cols)
        return (
            f"SELECT {col_str} FROM DataWeapon w "
            f"LEFT JOIN EnumWeaponType wt ON w.Type=wt.ID "
            f"WHERE w.Hypothetical='0'{extra} "
            f"LIMIT {limit}",
            "武器射程/速度参数"
        )

    # 舰艇（国家 + 类型）
    if has_ship or (has_country and any(k in q for k in ["舰", "ship", "船", "destroyer", "frigate", "carrier", "cruiser", "驱逐", "护卫", "航母", "巡洋", "两栖"])):
        codes = ship_codes if ship_codes else list(range(3200, 3300)) + list(range(2000, 2100)) + list(range(3000, 3200)) + list(range(3300, 3450)) + list(range(4000, 4030)) + list(range(5000, 5050))
        in_clause = _build_in_clause(codes)
        country_clause = f"AND s.OperatorCountry={country_id}" if has_country else ""
        active_clause = "AND s.YearDecommissioned=0" if "现役" in q or "active" in q or "in service" in q else ""
        return (
            f"SELECT DISTINCT s.ID, s.Name, c.Description AS Country, "
            f"st.Description AS ShipType, s.YearCommissioned, s.Length, s.DisplacementFull, s.Crew "
            f"FROM DataShip s "
            f"LEFT JOIN EnumOperatorCountry c ON s.OperatorCountry=c.ID "
            f"LEFT JOIN EnumShipType st ON s.Type=st.ID "
            f"WHERE s.Type {in_clause} {country_clause} {active_clause} "
            f"AND s.Hypothetical='0' "
            f"ORDER BY c.Description, st.Description, s.Name "
            f"LIMIT {limit}",
            f"舰艇 (类型过滤)"
        )

    # 飞机（国家 + 类型）
    if has_aircraft or (has_country and any(k in q for k in ["飞机", "aircraft", "f-", "j-", "f/a-", "预警", "轰炸", "直升机", "舰载机"])):
        codes = ac_codes if ac_codes else [2001, 2002, 2003, 2004]
        in_clause = _build_in_clause(codes)
        country_clause = f"AND a.OperatorCountry={country_id}" if has_country else ""
        active_clause = "AND a.YearDecommissioned=0" if "现役" in q or "active" in q else ""
        return (
            f"SELECT DISTINCT a.ID, a.Name, c.Description AS Country, "
            f"ac.Description AS AircraftType, a.YearCommissioned, a.Span, a.MaxRange "
            f"FROM DataAircraft a "
            f"LEFT JOIN EnumOperatorCountry c ON a.OperatorCountry=c.ID "
            f"LEFT JOIN EnumAircraftCategory ac ON a.Category=ac.ID "
            f"WHERE a.Category {in_clause} {country_clause} {active_clause} "
            f"AND a.Hypothetical='0' "
            f"ORDER BY c.Description, a.Name "
            f"LIMIT {limit}",
            "飞机"
        )

    # 潜艇
    if has_country and any(k in q for k in ["潜艇", "submarine", "潜", "sub"]):
        country_clause = f"AND sub.OperatorCountry={country_id}" if has_country else ""
        active_clause = "AND sub.YearDecommissioned=0" if "现役" in q or "active" in q else ""
        return (
            f"SELECT DISTINCT sub.ID, sub.Name, c.Description AS Country, "
            f"st.Description AS SubType, sub.YearCommissioned, sub.DisplacementFull, sub.MaxDepth, sub.Crew "
            f"FROM DataSubmarine sub "
            f"LEFT JOIN EnumOperatorCountry c ON sub.OperatorCountry=c.ID "
            f"LEFT JOIN EnumSubmarineType st ON sub.Type=st.ID "
            f"WHERE 1=1 {country_clause} {active_clause} "
            f"AND sub.Hypothetical='0' "
            f"ORDER BY c.Description, sub.Name "
            f"LIMIT {limit}",
            "潜艇"
        )

    # 地面单位（国家 + 类型）
    if has_gnd or (has_country and any(k in q for k in ["坦克", "装甲", "火炮", "步兵", "地面", "ground", "sam", "防空"])):
        codes = gnd_codes if gnd_codes else [2000]
        in_clause = _build_in_clause(codes)
        country_clause = f"AND g.OperatorCountry={country_id}" if has_country else ""
        active_clause = "AND g.YearDecommissioned=0" if "现役" in q or "active" in q else ""
        return (
            f"SELECT DISTINCT g.ID, g.Name, c.Description AS Country, "
            f"cat.Description AS Category, g.YearCommissioned, g.Mass, g.Crew "
            f"FROM DataGroundUnit g "
            f"LEFT JOIN EnumOperatorCountry c ON g.OperatorCountry=c.ID "
            f"LEFT JOIN EnumGroundUnitCategory cat ON g.Category=cat.ID "
            f"WHERE g.Category {in_clause} {country_clause} {active_clause} "
            f"AND g.Hypothetical='0' "
            f"ORDER BY c.Description, cat.Description, g.Name "
            f"LIMIT {limit}",
            "地面单位"
        )

    # 地面设施（国家 + 类型）
    if has_fac or (has_country and any(k in q for k in ["机场", "基地", "防空", "sam", "facility", "设施", "雷达站"])):
        codes = fac_codes if fac_codes else [9001]
        in_clause = _build_in_clause(codes)
        country_clause = f"AND f.OperatorCountry={country_id}" if has_country else ""
        active_clause = "AND f.YearDecommissioned=0" if "现役" in q or "active" in q else ""
        return (
            f"SELECT DISTINCT f.ID, f.Name, c.Description AS Country, "
            f"fc.Description AS Category, f.YearCommissioned, f.Crew, f.Radius "
            f"FROM DataFacility f "
            f"LEFT JOIN EnumOperatorCountry c ON f.OperatorCountry=c.ID "
            f"LEFT JOIN EnumFacilityCategory fc ON f.Category=fc.ID "
            f"WHERE f.Category {in_clause} {country_clause} {active_clause} "
            f"AND f.Hypothetical='0' "
            f"ORDER BY c.Description, f.Name "
            f"LIMIT {limit}",
            "地面设施"
        )

    # 武器/导弹
    if any(k in q for k in ["武器", "weapon", "导弹", "missile", "雷达", "枪", "炮", "炸弹", "bomb", " torpedo"]):
        country_clause = f"AND w.OperatorCountry={country_id}" if has_country else ""
        extra = ""
        if any(k in q for k in ["反舰", "asm", "ssm"]):
            extra = "AND w.SurfaceRangeMax > 0"
        if any(k in q for k in ["空空", "air-to-air", "aa"]):
            extra = "AND w.AirRangeMax > 0"
        if any(k in q for k in ["地对地", "cruise", "战斧"]):
            extra = "AND w.LandRangeMax > 0"
        return (
            f"SELECT DISTINCT w.ID, w.Name, wt.Description AS WeaponType, "
            f"w.AirRangeMax, w.SurfaceRangeMax, w.LandRangeMax, w.MaxSpeed "
            f"FROM DataWeapon w "
            f"LEFT JOIN EnumWeaponType wt ON w.Type=wt.ID "
            f"WHERE w.Hypothetical='0' {country_clause} {extra} "
            f"ORDER BY w.Name "
            f"LIMIT {limit}",
            "武器/导弹"
        )

    # 泛泛的国家查询
    if has_country:
        # 优先舰艇
        return (
            f"SELECT s.ID, s.Name, c.Description AS Country, "
            f"st.Description AS ShipType, s.YearCommissioned "
            f"FROM DataShip s "
            f"LEFT JOIN EnumOperatorCountry c ON s.OperatorCountry=c.ID "
            f"LEFT JOIN EnumShipType st ON s.Type=st.ID "
            f"WHERE s.OperatorCountry={country_id} AND s.Hypothetical='0' "
            f"AND s.YearDecommissioned=0 "
            f"ORDER BY st.Description, s.Name "
            f"LIMIT {limit}",
            f"{COUNTRY_MAP.get(country_id, '该国')}舰艇"
        )

    # 默认 → 武器
    return (
        f"SELECT w.ID, w.Name, wt.Description AS WeaponType, "
        f"w.AirRangeMax, w.SurfaceRangeMax, w.MaxSpeed "
        f"FROM DataWeapon w "
        f"LEFT JOIN EnumWeaponType wt ON w.Type=wt.ID "
        f"WHERE w.Hypothetical='0' AND w.AirRangeMax > 0 "
        f"ORDER BY w.AirRangeMax DESC "
        f"LIMIT {limit}",
        "武器（按空射射程排序）"
    )


def safe_select(sql: str, limit: int = 200) -> List[Dict[str, Any]]:
    sql = sql.strip()
    ql = sql.lower()
    if not ql.startswith("select"):
        raise ValueError("Only SELECT queries are allowed.")
    for kw in ["drop", "delete", "insert", "update", "create", "alter", "truncate"]:
        if kw in ql:
            raise ValueError(f"Blocked keyword: {kw}")
    return db.execute(sql, limit)

# =============================================================================
# MCP 工具
# =============================================================================

@mcp.tool()
def cmo_nl_query(user_question: str) -> str:
    """将自然语言转为 SQL 并执行，返回 CMO 数据库查询结果。

    支持的查询类型：
    - 国家 + 装备类型："美国现役驱逐舰"、"中国潜艇"、"俄罗斯防空"
    - 精确查询："F-16的DBID"、"M1A2的DBID"
    - 参数查询："鱼叉导弹射程"、"战斧最大速度"
    - 挂载查询："F/A-18C的LoadoutID"
    - 泛泛查询："中国舰艇"、"美军飞机"

    Args:
        user_question: 自然语言问题，如"美国现役驱逐舰有哪些？"

    Returns:
        JSON，含 success、sql_generated、rows、count 字段
    """
    try:
        sql, desc = gen_sql(user_question)
        rows = safe_select(sql)
        return json.dumps({
            "success": True,
            "query_description": desc,
            "sql_generated": sql,
            "question": user_question,
            "rows": rows,
            "count": len(rows)
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"success": False, "error": str(e), "question": user_question},
                          ensure_ascii=False)


@mcp.tool()
def cmo_raw_query(sql_query: str) -> str:
    """直接执行 SELECT SQL（高级用法，有安全过滤）。

    Args:
        sql_query: 完整 SELECT 语句，所有字段名用英文。
    """
    try:
        rows = safe_select(sql_query, limit=200)
        return json.dumps({"success": True, "rows": rows, "count": len(rows)},
                          ensure_ascii=False, indent=2)
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
def cmo_get_schemas() -> str:
    """获取核心表结构摘要和查询示例"""
    return """核心数据表:

1. DataShip (舰艇)
   字段: ID/Name/Type/Category/OperatorCountry/YearCommissioned/YearDecommissioned/Length/DisplacementFull/Crew
   JOIN: EnumShipType(Description), EnumOperatorCountry(Description)
   查询示例:
   SELECT s.ID, s.Name, c.Description AS Country, st.Description AS ShipType
   FROM DataShip s JOIN EnumOperatorCountry c ON s.OperatorCountry=c.ID
   JOIN EnumShipType st ON s.Type=st.ID
   WHERE c.Description='United States' AND s.YearDecommissioned=0 LIMIT 10

2. DataAircraft (飞机)
   字段: ID/Name/Type/Category/OperatorCountry/YearCommissioned/YearDecommissioned/Span/MaxRange
   JOIN: EnumAircraftType(Description), EnumAircraftCategory(Description), EnumOperatorCountry
   查询示例:
   SELECT a.ID, a.Name, c.Description AS Country, a.YearCommissioned
   FROM DataAircraft a JOIN EnumOperatorCountry c ON a.OperatorCountry=c.ID
   WHERE a.YearDecommissioned=0 LIMIT 10

3. DataSubmarine (潜艇)
   字段: ID/Name/Type/Category/OperatorCountry/YearCommissioned/YearDecommissioned/DisplacementFull/MaxDepth/Crew
   JOIN: EnumSubmarineType(Description), EnumOperatorCountry

4. DataGroundUnit (地面单位)
   字段: ID/Name/Category/OperatorCountry/YearCommissioned/YearDecommissioned/Mass/Crew
   JOIN: EnumGroundUnitCategory(Description), EnumOperatorCountry
   Category代码: 2000=坦克, 3000=火炮, 6000=SAM, 1000=步兵

5. DataWeapon (武器/导弹)
   字段: ID/Name/Type/AirRangeMax/SurfaceRangeMax/LandRangeMax/MaxSpeed
   JOIN: EnumWeaponType(Description)

6. DataFacility (地面设施)
   字段: ID/Name/Category/Type/OperatorCountry/YearCommissioned/Crew/Radius
   JOIN: EnumFacilityCategory(Description), EnumOperatorCountry
   Category代码: 9001=Air Base, 2001=Runway, 3001=Building

7. DataAircraftLoadouts (飞机挂载配置)
   字段: ID, ComponentID (即飞机 DBID)
   用于查询飞机的不同 LoadoutID

关键过滤:
- 现役: YearDecommissioned=0
- 虚构: Hypothetical='0'
- 国家: OperatorCountry → EnumOperatorCountry.ID → Description
- 舰型: Type → EnumShipType.ID → Description
  DDG=3203, DD=3202, FFG=3303, CVN=2008
"""


@mcp.tool()
def cmo_get_loadouts(aircraft_name: str) -> str:
    """查询指定飞机的所有 LoadoutID。

    Args:
        aircraft_name: 飞机名称，如 "F/A-18C" 或 "F-16C"
    """
    try:
        sql = (
            f"SELECT l.ID AS LoadoutID, l.Name AS LoadoutName, l.Comments, "
            f"a.ID AS AircraftDBID, a.Name AS AircraftName "
            f"FROM DataAircraftLoadouts l "
            f"JOIN DataAircraft a ON l.ComponentID=a.ID "
            f"WHERE a.Name LIKE '%{aircraft_name.replace(chr(39), chr(39)+chr(39))}%' "
            f"AND a.Hypothetical='0' "
            f"ORDER BY a.Name, l.ID "
            f"LIMIT 50"
        )
        rows = safe_select(sql)
        return json.dumps({
            "success": True,
            "sql_generated": sql,
            "aircraft_searched": aircraft_name,
            "loadouts": rows,
            "count": len(rows)
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)}, ensure_ascii=False)

# =============================================================================
# 启动
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CMO SQLite Explorer MCP Server")
    print("=" * 50)
    print(f"Database: {DB_PATH}")
    print(f"Exists:   {Path(DB_PATH).exists()}")
    print(f"Tables:   {len(db.get_tables())} tables loaded")
    print(f"Countries: {len(COUNTRY_MAP)} entries")
    print(f"ShipTypes: {len(SHIP_TYPE_MAP)} entries")
    print("=" * 50)
    mcp.run()
