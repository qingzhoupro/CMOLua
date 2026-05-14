---
doc_id: CMO-SKILL-DEBUG-001
title: Debug 调试技能
description: Lua 代码调试和问题排查
---

# Debug 调试技能

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

遇到新错误 → 追加到 `errors/index.md`
