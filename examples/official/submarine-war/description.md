# 潜艇战案例

## 场景描述

蓝方舰队在海域执行反潜巡逻任务，红方潜艇试图突破封锁。
蓝方部署驱逐舰、护卫舰和反潜巡逻机构成多层反潜体系。

## 场景参数

| 参数 | 值 |
|------|-----|
| 蓝方舰队位置 | (35.5, 140.0) |
| 反潜区域 | 4 个参考点定义 |
| 红方潜艇进入点 | (34.0, 142.0) |

## 涉及函数

- `ScenEdit_AddUnit()` - 添加舰艇和潜艇
- `ScenEdit_AddMission()` - 创建反潜巡逻
- `ScenEdit_SetEMCON()` - 设置电磁管控
- `ScenEdit_SetEvent()` - 创建检测事件
- `ScenEdit_SetTrigger()` - 设置触发器

## Lua 语法要点

1. **潜艇类型**：`type="Submarine"`
2. **深度设置**：`manualAltitude`（正数为下潜深度）
3. **EMCON 格式**：`"Radar=Active;Sonar=Passive"`
4. **检测事件**：`type="UnitDetected"`, `TargetType="Submarine"`