---
doc_id: CMO-CMD-UNIT-001
trigger: /cmo-unit
title: 快速添加单位
description: 快速生成单个单位的 Lua 代码
---

# /cmo-unit - 快速添加单位

## 执行步骤

1. 解析单位类型（Aircraft/Ship/Submarine/Facility/GroundUnit）
2. 通过 MCP 查询 DBID
3. Aircraft 查询 LoadoutID
4. 生成 ScenEdit_AddUnit 代码
5. 自检清单验证

## MCP 调用

```python
# 查询 DBID
cmo_intelligent_query("F-16C 战斗机的 DBID")
# 查询 LoadoutID
cmo_query("F-16C 的挂载方案")
```

## 输出模板

```lua
ScenEdit_AddUnit({
  side = "Blue",
  type = "Aircraft",
  name = "F-16C #1",
  dbid = 1719,
  LoadoutID = 2230,
  latitude = 35.6762,
  longitude = 139.6503,
  altitude = 9144,
  heading = 0,
  speed = 500
})
```

## 错误检查

- [ ] DBID 存在
- [ ] Aircraft 有 LoadoutID
- [ ] type 正确
- [ ] 坐标有效

参考 → `.cursor/skills/cmo-unit/SKILL.md`
