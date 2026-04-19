-- 设置电磁管控(EMCON)模板
-- 参考: CMO_Lua函数_Unit.md - ScenEdit_SetEMCON
-- 变量说明：
-- {{TYPE}} - 类型：Side / Mission / Group / Unit
-- {{NAME}} - 对象名称
-- {{EMCON}} - EMCON 设置：
--   Radar=Active / Radar=Passive
--   Sonar=Active / Sonar=Passive
--   OECM=Active / OECM=Passive
--   Inherit（继承父级）

-- 设置 EMCON
ScenEdit_SetEMCON("{{TYPE}}", "{{NAME}}", "{{EMCON}}")

-- 常用设置示例：
-- 
-- 侧级：整个阵营雷达主动
-- ScenEdit_SetEMCON("Side", "Blue", "Radar=Active;Sonar=Passive")
-- 
-- 任务级：反潜巡逻被动声纳
-- ScenEdit_SetEMCON("Mission", "ASW Patrol", "Inherit;Sonar=Passive")
-- 
-- 单元级：单舰 ECM 主动
-- ScenEdit_SetEMCON("Unit", "USS Arleigh Burke", "Radar=Passive;OECM=Active")
-- 
-- 编队级：整个编队雷达静默
-- ScenEdit_SetEMCON("Group", "Destroyer Squadron 1", "Radar=Passive;Sonar=Passive")

-- 示例：设置红方潜艇被动模式
-- ScenEdit_SetEMCON("Unit", "Red Submarine #1", "Sonar=Passive")

-- 示例：设置蓝方舰队主动雷达
-- ScenEdit_SetEMCON("Group", "Blue Carrier Strike Group", "Radar=Active")

-- 示例：设置防空巡逻任务被动模式
-- ScenEdit_SetEMCON("Mission", "AAW Patrol", "Inherit;Radar=Passive")