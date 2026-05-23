---
doc_id: CMO-LUA-SKILL-001
title: CMO Lua Skill - 核心入口
description: CMO 兵棋 Lua 代码生成的核心规则和 MCP 验证
trigger_keywords:
  - /cmo
  - /lua
  - 生成兵棋场景
  - ScenEdit_AddUnit
---

# CMO Lua Skill - 核心入口

> 精简版入口文件。详细工作流 → `.cursor/skills/`

## Step 0: MCP 验证（必须）

```python
cmo_intelligent_query("F-16C 战斗机的 DBID")
```
MCP 不可用时立即告知用户。

## 铁律（6条红线）

| # | 规则 | 错误 | 正确 |
|---|------|------|------|
| 1 | Aircraft 必须有 `LoadoutID`（大写，数值） | `loadout = "xxx"` | `LoadoutID = 2230` |
| 2 | DBID 必须通过 MCP 查询 | `dbid = 9999` | `dbid = 1719` |
| 3 | type 必须精确匹配 | `type = "Air"` | `type = "Aircraft"` |
| 4 | 坐标参数名正确 | `lat = 35, lon = 139` | `latitude = 35.0` |
| 5 | altitude 单位是米 | `altitude = 30000` | `altitude = 9144` |
| 6 | 阵营必须已创建 | `side = "China"` | 先 `ScenEdit_AddSide()` |

**正确 type 值：** `Aircraft` / `Ship` / `Submarine` / `Facility` / `GroundUnit`

## MCP 调用指南

| 场景 | 函数 |
|------|------|
| 自然语言查询 | `cmo_intelligent_query()` |
| 精确 DBID | `cmo_query()` |
| 名称搜索 | `cmo_search()` |
| SQL 验证 | `read_query()` |

**枚举：** NATO=2060, 现役=YearDecommissioned=0, 非虚构=Hypothetical='False'

## 自审清单

- [ ] DBID 通过 MCP 查询
- [ ] Aircraft 有 LoadoutID
- [ ] type 拼写正确
- [ ] latitude/longitude 参数正确
- [ ] altitude 单位是米
- [ ] 阵营已存在

## 输出规范

**产物必须保存到 `outputs/` 目录**，不得直接输出到其他位置。

| 产物类型 | 输出路径 |
|---------|---------|
| Lua 脚本文件 | `outputs/*.lua` |
| 场景配置文件 | `outputs/scenarios/` |
| 侦察脚本 | `outputs/scout/` |
| 其他产物 | `outputs/misc/` |

> `outputs/` 目录本身由 git 跟踪，目录内文件通过 `.gitignore` 排除，不提交到远程。

## 参考

- `.cursor/skills/cmo-auto/` - 完整工作流
- `.cursor/skills/cmo-query/` - DBID 查询
- `errors/index.md` - 教训库
- `references/lua-api/` - Lua API
