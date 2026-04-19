r"""
实现自然语音查询CMO游戏 DBID MCP 服务器
基于 FastMCP 框架，支持自然语言查询装备数据库
by 海空兵棋与AI公众号 2019-2026

参考: sqlite_explorer.py
"""

from pathlib import Path
import sqlite3
import os
from typing import List, Dict, Any, Optional
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("CMO-DBID-Explorer")

# 数据库路径 - 从环境变量读取，默认为 mcp/db/DB3K_514.db3
def get_db_path() -> Path:
    env_path = os.environ.get('SQLITE_DB_PATH')
    if env_path:
        return Path(env_path)
    # 默认路径：与 server.py 同级的 db 目录
    default_path = Path(__file__).parent / "db" / "DB3K_514.db3"
    return default_path

DB_PATH = get_db_path()


class SQLiteConnection:
    """SQLite 连接管理器"""
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.conn: Optional[sqlite3.Connection] = None
        
    def __enter__(self):
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.row_factory = sqlite3.Row
        return self.conn
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()


def validate_db_exists():
    """验证数据库是否存在"""
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"数据库文件未找到: {DB_PATH}\n"
            "请将 CMO 数据库文件 (如 DB3K_511.db3) 复制到此目录。\n"
            f"期望路径: {DB_PATH}"
        )


def contains_multiple_statements(sql: str) -> bool:
    """检查 SQL 是否包含多个语句"""
    in_single_quote = False
    in_double_quote = False
    for char in sql:
        if char == "'" and not in_double_quote:
            in_single_quote = not in_single_quote
        elif char == '"' and not in_single_quote:
            in_double_quote = not in_double_quote
        elif char == ';' and not in_single_quote and not in_double_quote:
            return True
    return False


@mcp.tool()
def query_dbid(query: str, limit: int = 50) -> List[Dict[str, Any]]:
    """
    自然语言查询 DBID

    Args:
        query: 自然语言查询，如 "美国战斗机" 或 "F-22"
        limit: 返回结果数量限制，默认 50

    Returns:
        包含 DBID、装备名称、国家等信息的列表
    """
    validate_db_exists()

    query = query.strip()

    # 检测是否是 SELECT 语句（用户可能直接输入 SQL）
    if query.lower().startswith('select'):
        return read_query(query, limit=limit)

    # 构建自然语言搜索 SQL
    # CMO 数据库表结构: DataAircraft, DataShip, DataSubmarine, DataFacility
    search_pattern = f"%{query}%"
    all_results = []

    try:
        with SQLiteConnection(DB_PATH) as conn:
            cursor = conn.cursor()

            # 搜索飞机
            cursor.execute("""
                SELECT
                    a.ID as dbid,
                    a.Name as name,
                    'Aircraft' as type,
                    a.OperatorCountry as country,
                    a.Comments as description
                FROM DataAircraft a
                WHERE a.Name LIKE ? OR a.Comments LIKE ?
                LIMIT ?
            """, (search_pattern, search_pattern, limit))
            for row in cursor.fetchall():
                all_results.append(dict(row))

            # 搜索舰艇
            cursor.execute("""
                SELECT
                    s.ID as dbid,
                    s.Name as name,
                    'Ship' as type,
                    s.OperatorCountry as country,
                    s.Comments as description
                FROM DataShip s
                WHERE s.Name LIKE ? OR s.Comments LIKE ?
                LIMIT ?
            """, (search_pattern, search_pattern, limit))
            for row in cursor.fetchall():
                all_results.append(dict(row))

            # 搜索潜艇
            cursor.execute("""
                SELECT
                    sub.ID as dbid,
                    sub.Name as name,
                    'Submarine' as type,
                    sub.OperatorCountry as country,
                    sub.Comments as description
                FROM DataSubmarine sub
                WHERE sub.Name LIKE ? OR sub.Comments LIKE ?
                LIMIT ?
            """, (search_pattern, search_pattern, limit))
            for row in cursor.fetchall():
                all_results.append(dict(row))

            # 搜索设施
            cursor.execute("""
                SELECT
                    f.ID as dbid,
                    f.Name as name,
                    'Facility' as type,
                    f.OperatorCountry as country,
                    f.Comments as description
                FROM DataFacility f
                WHERE f.Name LIKE ? OR f.Comments LIKE ?
                LIMIT ?
            """, (search_pattern, search_pattern, limit))
            for row in cursor.fetchall():
                all_results.append(dict(row))

            return all_results[:limit]

    except sqlite3.OperationalError as e:
        return fallback_query(query, limit)


def fallback_query(query: str, limit: int) -> List[Dict[str, Any]]:
    """备用查询 - 尝试 DataAircraft 表"""
    search_pattern = f"%{query}%"

    try:
        with SQLiteConnection(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT
                    ID as dbid,
                    Name as name,
                    'Aircraft' as type,
                    OperatorCountry as country
                FROM DataAircraft
                WHERE Name LIKE ? OR Comments LIKE ?
                LIMIT ?
            """, (search_pattern, search_pattern, limit))
            results = cursor.fetchall()
            if results:
                return [dict(row) for row in results]
    except sqlite3.OperationalError:
        pass

    return [{"error": "未找到匹配的装备", "query": query}]


@mcp.tool()
def read_query(sql: str, params: Optional[List[Any]] = None, fetch_all: bool = True, row_limit: int = 1000) -> List[Dict[str, Any]]:
    """
    执行 SELECT SQL 查询
    
    Args:
        sql: SELECT SQL 查询语句
        params: 可选的查询参数
        fetch_all: 是否获取所有结果
        row_limit: 最大返回行数
    
    Returns:
        查询结果列表
    """
    validate_db_exists()
    
    sql = sql.strip()
    
    # 移除尾部引号
    if sql.endswith(';'):
        sql = sql[:-1].strip()
    
    # 检查多个语句
    if contains_multiple_statements(sql):
        raise ValueError("Multiple SQL statements are not allowed")
    
    # 验证查询类型
    sql_lower = sql.lower()
    if not any(sql_lower.startswith(prefix) for prefix in ('select', 'with')):
        raise ValueError("Only SELECT queries (including WITH clauses) are allowed")
    
    params = params or []
    
    with SQLiteConnection(DB_PATH) as conn:
        cursor = conn.cursor()
        
        try:
            # 添加 LIMIT
            if 'limit' not in sql_lower:
                sql = f"{sql} LIMIT {row_limit}"
            
            cursor.execute(sql, params)
            
            if fetch_all:
                results = cursor.fetchall()
            else:
                results = [cursor.fetchone()]
                
            return [dict(row) for row in results if row is not None]
            
        except sqlite3.Error as e:
            raise ValueError(f"SQLite error: {str(e)}")


@mcp.tool()
def list_tables() -> List[str]:
    """
    列出数据库中的所有表
    
    Returns:
        表名列表
    """
    validate_db_exists()
    
    with SQLiteConnection(DB_PATH) as conn:
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                SELECT name FROM sqlite_master 
                WHERE type='table' 
                ORDER BY name
            """)
            
            return [row['name'] for row in cursor.fetchall()]
            
        except sqlite3.Error as e:
            raise ValueError(f"SQLite error: {str(e)}")


@mcp.tool()
def describe_table(table_name: str) -> List[Dict[str, str]]:
    """
    获取表的结构信息
    
    Args:
        table_name: 表名
    
    Returns:
        列信息列表（包含 name, type, notnull, dflt_value, pk）
    """
    validate_db_exists()
    
    with SQLiteConnection(DB_PATH) as conn:
        cursor = conn.cursor()
        
        try:
            # 验证表是否存在
            cursor.execute("""
                SELECT name FROM sqlite_master 
                WHERE type='table' AND name=?
            """, [table_name])
            
            if not cursor.fetchone():
                raise ValueError(f"Table '{table_name}' does not exist")
            
            # 获取表结构
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            
            return [dict(row) for row in columns]
            
        except sqlite3.Error as e:
            raise ValueError(f"SQLite error: {str(e)}")


@mcp.tool()
def get_dbid_by_name(name: str) -> Dict[str, Any]:
    """
    通过名称精确查找 DBID
    
    Args:
        name: 装备名称（如 "F-22"）
    
    Returns:
        装备信息
    """
    validate_db_exists()
    
    search_pattern = f"%{name}%"
    
    # 尝试多个表
    tables = [
        ("DataAircraft", "Aircraft"),
        ("DataShip", "Ship"),
        ("DataSubmarine", "Submarine"),
        ("DataFacility", "Facility")
    ]
    
    for table, unit_type in tables:
        try:
            sql = f"""
            SELECT
                ID as dbid,
                Name as name,
                ? as type,
                OperatorCountry as country,
                Comments as description
            FROM {table}
            WHERE Name LIKE ?
            LIMIT 1
            """
            with SQLiteConnection(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(sql, [unit_type, search_pattern])
                result = cursor.fetchone()
                
                if result:
                    return dict(result)
        except sqlite3.OperationalError:
            continue
    
    return {"error": f"未找到 '{name}' 的 DBID"}


@mcp.tool()
def get_dbid_by_country(country: str, category: Optional[str] = None, limit: int = 20) -> List[Dict[str, Any]]:
    """
    按国家查询 DBID
    
    Args:
        country: 国家名称（如 "美国"）
        category: 可选，装备类别（如 "aircraft"）
        limit: 返回数量限制
    
    Returns:
        装备列表
    """
    validate_db_exists()
    
    search_pattern = f"%{country}%"
    all_results = []
    
    try:
        with SQLiteConnection(DB_PATH) as conn:
            cursor = conn.cursor()
            
            # 飞机
            if not category or 'aircraft' in category.lower() or 'air' in category.lower():
                cursor.execute("""
                    SELECT
                        ID as dbid,
                        Name as name,
                        'Aircraft' as type,
                        OperatorCountry as country,
                        Comments as description
                    FROM DataAircraft
                    WHERE OperatorCountry LIKE ?
                    LIMIT ?
                """, (search_pattern, limit))
                for row in cursor.fetchall():
                    all_results.append(dict(row))
            
            # 舰艇
            if not category or 'ship' in category.lower() or 'naval' in category.lower() or 'boat' in category.lower():
                cursor.execute("""
                    SELECT
                        ID as dbid,
                        Name as name,
                        'Ship' as type,
                        OperatorCountry as country,
                        Comments as description
                    FROM DataShip
                    WHERE OperatorCountry LIKE ?
                    LIMIT ?
                """, (search_pattern, limit))
                for row in cursor.fetchall():
                    all_results.append(dict(row))
            
            return all_results[:limit]
            
    except sqlite3.Error as e:
        return [{"error": str(e)}]


if __name__ == "__main__":
    # 启动 MCP 服务器
    mcp.run()
