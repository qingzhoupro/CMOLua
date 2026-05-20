---
doc_id: CMO-CMD-UNIT-001
trigger: /cmo-unit
title: 快速添加单位
description: 快速生成单个单位的 Lua 代码，支持场景上下文感知
---

# /cmo-unit - 快速添加单位

## 执行步骤

1. **场景上下文检测** - 检查是否有场景信息，无则询问
2. 解析单位类型（Aircraft/Ship/Submarine/Facility/GroundUnit）
3. 通过 MCP 查询 DBID
4. Aircraft 查询 LoadoutID
5. 生成 ScenEdit_AddUnit 代码
6. 自检清单验证

## 场景上下文检测

生成代码前，先确认当前场景状态：

```
有场景上下文 → 基于真实数据生成（无占位符）
无场景上下文 → 询问用户，或让用户执行 /cmo-scene 获取
空白场景   → 直接生成
```

## MCP 调用

```python
# 查询 DBID
cmo_intelligent_query("F-16C 战斗机的 DBID")
# 查询 LoadoutID
cmo_query("F-16C 的挂载方案")
```

## 输出模板

**有场景上下文时（示例）：**

```lua
ScenEdit_AddUnit({
  side = "Blue",           -- 从场景上下文读取真实阵营名称
  type = "Aircraft",
  name = "F-16C #2",      -- 检查已有单元，避免重名
  dbid = 1719,             -- 通过 MCP 查询获取
  LoadoutID = 2230,        -- 通过 MCP 查询获取
  latitude = 35.6762,
  longitude = 139.6503,
  altitude = 9144,
  heading = 0,
  speed = 500
})
```

**空白场景时可使用示例值，但需注明需替换。**

## 错误检查

- [ ] DBID 存在（通过 MCP 验证）
- [ ] Aircraft 有 LoadoutID
- [ ] type 参数正确（Aircraft/Ship/Submarine/Facility/GroundUnit）
- [ ] 坐标参数名正确 (latitude / longitude，非 lat / lon)
- [ ] altitude 单位是米
- [ ] 阵营名称与场景一致
- [ ] 单位名称不与现有单元冲突

## API 正确语法

| 功能 | 错误写法 | 正确写法 |
|------|---------|---------|
| 阵营列表 | `ScenEdit_GetSides()` | `VP_GetSides()` |
| 阵营单元 | `ScenEdit_GetUnits({side=...})` | `VP_GetSide({side="xxx"}).units` |
| 任务列表 | `ScenEdit_GetMissions()` | `ScenEdit_GetMissions("阵营名")` |
| 参考点 | `ScenEdit_ReferencePoints(side)` | `ScenEdit_GetReferencePoints({side="xxx"})` |

参考 → `.cursor/skills/cmo-unit/SKILL.md`
