---
doc_id: CMO-CMD-MISSION-001
trigger: /cmo-mission
title: 任务生成
description: 生成巡逻、攻击、侦察等任务
---

# /cmo-mission - 任务生成

## 任务类型

| 类型 | 说明 |
|------|------|
| `patrol` | 巡逻任务 |
| `strike` | 对地攻击 |
| `escort` | 护航 |
| ` intercept` | 拦截 |
| `sub-ops` | 潜艇作战 |

## 执行步骤

1. 确定任务类型
2. 选择执行单位
3. 定义目标区域（经纬度）
4. 设置任务参数
5. 生成 Lua 代码

## 模板

```lua
-- 巡逻任务
ScenEdit_AssignUnitToMission("F-16C #1", "CAP Patrol")
```

参考 → `.cursor/skills/cmo-mission/SKILL.md`
