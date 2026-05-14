---
doc_id: CMO-SKILL-SIDE-001
title: Side 阵营技能
description: 阵营创建和管理
---

# Side 阵营技能

## 创建阵营

```lua
ScenEdit_AddSide({
  name = "Blue",
  side = "Blue Force",
  orientation = "friendly"
})

ScenEdit_AddSide({
  name = "Red",
  side = "Red Force",
  orientation = "hostile"
})
```

## 预设阵营

| 名称 | 用途 |
|------|------|
| `Blue` | 蓝方（友军） |
| `Red` | 红方（敌军） |
| `Green` | 绿方（中立） |
| `Neutral` | 中立方 |

## Side 关系设置

```lua
ScenEdit_SetSideRelations({
  side_a = "Blue",
  side_b = "Red",
  relation = "hostile"
})

ScenEdit_SetSideRelations({
  side_a = "Blue",
  side_b = "Green",
  relation = "friendly"
})
```

## 检查 Side 是否存在

场景中的 side 可通过 `ScenEdit_GetSides()` 获取。
