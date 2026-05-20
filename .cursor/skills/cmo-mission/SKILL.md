---
doc_id: CMO-SKILL-MISSION-001
title: Mission 任务技能
description: 巡逻、攻击、护航等任务创建
---

# Mission 任务技能

## Step 0.5: 经验教训查询（按需）

根据场景状态加载对应教训。

### 查询逻辑

1. 检查场景是否为空（无阵营）
2. 从 `memory/cold/lesson-index.md` 匹配教训 ID
3. 从 `memory/cold/lesson-root-causes.md` 加载相关教训
4. 注入到 `memory/hot/session.md`

### 场景状态 → 教训映射

| 场景状态 | 需加载的教训 ID |
|---------|----------------|
| 空白场景 | SIDE-NOT-EXIST, SIDE-API |
| 有场景上下文 | 跳过 Step 0.5（已有经验） |

### 空白场景必读教训

- **SIDE-NOT-EXIST**: 空白场景必须先创建阵营，再添加单元
- **SIDE-API**: `ScenEdit_AddSide` 仅支持 `{side="xxx"}` 参数

---

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
