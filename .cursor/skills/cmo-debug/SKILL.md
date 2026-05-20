---
doc_id: CMO-SKILL-DEBUG-001
title: Debug 调试技能
description: Lua 代码调试和问题排查
---

# Debug 调试技能

## Step 0.5: 教训速查

遇到报错时，先从教训库快速定位根因。

### 常见报错 → 教训映射

| 报错关键字 | 教训 ID | 说明 |
|-----------|---------|------|
| Missing 'LoadoutID' | LOADOUTID | Aircraft 必须有 LoadoutID |
| Invalid unit type | GROUND-UNIT-TYPE | type="GROUND UNIT"（全大写+空格） |
| Invalid latitude/longitude | LATITUDE-PARAM | 坐标参数名用 latitude/longitude |
| deprecated in the database | DEPRECATED-DBID | 必须通过 MCP 查询 DBID |
| This point appears to be underwater | FACILITY-TERRAIN | Facility 只能在陆地放置 |
| Side 'xxx' doesn't exist | SIDE-NOT-EXIST | 空白场景必须先创建阵营 |

完整教训库 → `memory/cold/lesson-root-causes.md`
教训索引 → `memory/cold/lesson-index.md`

---

## 调试输出

```lua
print("Debug: Unit created")
print("DBID: " .. tostring(dbid))
```

## 常见错误

| 错误信息 | 原因 | 解决 |
|----------|------|------|
| Missing 'LoadoutID' | Aircraft 缺 LoadoutID | 添加 LoadoutID |
| Invalid unit type | type 值错误 | 用 Aircraft/Ship/Submarine |
| Invalid latitude | 坐标参数名错误 | 用 latitude/longitude |
| DBID not found | DBID 不存在 | 用 MCP 重新查询 |

## 验证步骤

1. MCP 查询 DBID
2. MCP 查询 LoadoutID
3. 检查 type 拼写
4. 检查坐标参数名
5. 检查阵营是否存在

## 错误记录

遇到新错误 → 使用 `/cmo-errors` 命令收集教训，追加到 `memory/cold/lesson-root-causes.md`
