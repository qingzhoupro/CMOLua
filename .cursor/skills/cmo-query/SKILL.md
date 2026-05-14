---
doc_id: CMO-SKILL-QUERY-001
title: DBID 查询技能
description: 如何通过 MCP 查询正确的 DBID 和 LoadoutID
---

# DBID 查询技能

## MCP 函数

| 函数 | 用途 |
|------|------|
| `cmo_intelligent_query()` | 自然语言 → SQL |
| `cmo_query()` | 精确匹配 |
| `cmo_search()` | 名称搜索 |
| `read_query()` | 直接 SQL |

## 查询示例

```python
# 自然语言查询
cmo_intelligent_query("F-16C 战斗机的 DBID")
# → {"dbid": 1719, "name": "F-16C Fighting Falcon"}

# 搜索名称
cmo_search("F-16", "aircraft")
# → [{"dbid": 1719, "name": "F-16C"}, ...]

# SQL 验证
read_query("SELECT dbid, name FROM DataAircraft WHERE dbid = 1719")
```

## LoadoutID 查询

```python
cmo_query("F-16C 默认挂载")
# 返回 LoadoutID 数值

# SQL 直接查
read_query("SELECT ID FROM DataAircraftLoadouts WHERE ComponentID = 1719")
```

## 数据表参考

| 表 | 说明 |
|---|------|
| `DataAircraft` | 飞机 DBID、名称、类型 |
| `DataShip` | 舰艇 DBID、名称、类型 |
| `DataSubmarine` | 潜艇 |
| `DataWeapon` | 武器射程、速度 |

## 枚举值

- NATO = 2060
- YearDecommissioned = 0 (现役)
- Hypothetical = 'False' (非虚构)
