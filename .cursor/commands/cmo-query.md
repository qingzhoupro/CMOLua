---
doc_id: CMO-CMD-QUERY-001
trigger: /cmo-query
title: 数据库查询
description: 通过 MCP 查询 CMO 数据库
---

# /cmo-query - 数据库查询

## 可用函数

| 函数 | 说明 | 示例 |
|------|------|------|
| `cmo_intelligent_query()` | 自然语言查询 | `cmo_intelligent_query("现役驱逐舰")` |
| `cmo_query()` | 精确查询 | `cmo_query("F-16C 的 DBID")` |
| `cmo_search()` | 名称搜索 | `cmo_search("Arleigh Burke", "ship")` |
| `read_query()` | 直接 SQL | `read_query("SELECT * FROM DataShip")` |

## 数据表

- `DataAircraft` - 飞机
- `DataShip` - 舰艇
- `DataSubmarine` - 潜艇
- `DataGroundUnit` - 地面单位
- `DataFacility` - 设施
- `DataWeapon` - 武器

## 枚举表

- `EnumOperatorCountry` - 国家 (ID → Description)
- `EnumShipType` - 舰型
- `EnumAircraftType` - 机型
- `EnumGroundUnitCategory` - 地面单位类别

## 常用枚举值

| 名称 | ID | 说明 |
|------|-----|------|
| NATO | 2060 | 北约聚合组织 |
| 现役 | YearDecommissioned=0 | 非虚构现役 |

参考 → `.cursor/skills/cmo-query/SKILL.md`
