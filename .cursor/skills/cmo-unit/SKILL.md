---
doc_id: CMO-SKILL-UNIT-001
title: Unit 操作技能
description: ScenEdit_AddUnit 的正确用法
---

# Unit 操作技能

## 函数签名

```lua
ScenEdit_AddUnit({
  side = "Blue",        -- 阵营名称
  type = "Aircraft",     -- 单位类型
  name = "F-16C #1",    -- 单位名称
  dbid = 1719,          -- 数据库 ID (必须通过 MCP 查询)
  LoadoutID = 2230,     -- Aircraft 必须有
  latitude = 35.6762,   -- 纬度
  longitude = 139.6503, -- 经度
  altitude = 9144,      -- 高度 (米)
  heading = 0,          -- 朝向 (度)
  speed = 500           -- 速度 (节)
})
```

## type 有效值

| 值 | 说明 | 错误示例 |
|---|------|---------|
| `Aircraft` | 飞机 | `Air`, `Plane` |
| `Ship` | 舰艇 | `Naval`, `boat` |
| `Submarine` | 潜艇 | `Sub`, `underwater` |
| `Facility` | 设施 | `Base`, `Ground` |
| `GroundUnit` | 地面单位 | `Infantry`, `Tank` |

## 常见错误

### Missing LoadoutID
```lua
-- 错误
ScenEdit_AddUnit({type = "Aircraft", dbid = 1719})

-- 正确
ScenEdit_AddUnit({type = "Aircraft", dbid = 1719, LoadoutID = 2230})
```

### Invalid unit type
```lua
-- 错误
ScenEdit_AddUnit({type = "Air"})

-- 正确
ScenEdit_AddUnit({type = "Aircraft"})
```

### Invalid latitude/longitude
```lua
-- 错误
ScenEdit_AddUnit({lat = 35, lon = 139})

-- 正确
ScenEdit_AddUnit({latitude = 35.0, longitude = 139.0})
```
