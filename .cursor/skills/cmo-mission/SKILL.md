---
doc_id: CMO-SKILL-MISSION-001
title: Mission 任务技能
description: 巡逻、攻击、护航等任务创建
---

# Mission 任务技能

## 创建巡逻任务

```lua
-- 创建巡逻区
local patrolZone = {
  {latitude = 35.0, longitude = 139.0},
  {latitude = 36.0, longitude = 140.0},
  {latitude = 35.0, longitude = 141.0}
}

-- 分配单位到任务
ScenEdit_AssignUnitToMission("F-16C #1", "CAP Patrol")
```

## 任务类型

| 类型 | 说明 |
|------|------|
| `patrol` | 巡逻 |
| `strike` | 对地攻击 |
| `escort` | 护航 |
| `intercept` | 空中拦截 |
| `sub-ops` | 潜艇作战 |

## 分配单位

```lua
-- 分配到巡逻任务
ScenEdit_AssignUnitToMission("F-16C #1", "CAP Patrol")

-- 分配到打击任务
ScenEdit_AssignUnitToMission("F-15E #1", "Strike Mission")
```

## 常见任务模板

参考 `templates/advanced/patrol-mission.lua`
参考 `templates/advanced/strike-mission.lua`
