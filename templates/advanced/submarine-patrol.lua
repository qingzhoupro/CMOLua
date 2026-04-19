-- 潜艇巡逻模板
-- 参考: https://commandops.github.io/ 和 CMO_Lua函数_Unit.md
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{UNIT_NAME}} - 潜艇名称
-- {{DBID}} - 潜艇 DBID
-- {{MISSION_NAME}} - 巡逻任务名称
-- {{LATITUDE}} - 巡逻区域纬度
-- {{LONGITUDE}} - 巡逻区域经度

-- 添加潜艇
ScenEdit_AddUnit({
    side="{{SIDE}}",
    type="Submarine",
    name="{{UNIT_NAME}}",
    dbid={{DBID}},
    latitude="{{LATITUDE}}",
    longitude="{{LONGITUDE}}",
    manualAltitude=50  -- 巡逻深度（米）
})

-- 创建反潜巡逻任务（红方视角）
ScenEdit_AddMission({
    side="{{SIDE}}",
    name="{{MISSION_NAME}}",
    type="Patrol",
    subtype="ASW"
})

-- 分配潜艇到巡逻任务
ScenEdit_AssignUnitToMission("{{UNIT_NAME}}", "{{MISSION_NAME}}")

-- 设置潜艇为被动模式（节省燃料）
ScenEdit_SetEMCON("Unit", "{{UNIT_NAME}}", "Sonar=Passive")

-- 示例：添加洛杉矶级潜艇到反潜巡逻
-- ScenEdit_AddUnit({
--     side="Blue",
--     type="Submarine",
--     name="USS La Jolla",
--     dbid=2209,
--     latitude="35.0",
--     longitude="130.0",
--     manualAltitude=100
-- })
-- ScenEdit_AddMission({
--     side="Blue",
--     name="ASW Patrol",
--     type="Patrol",
--     subtype="ASW"
-- })
-- ScenEdit_AssignUnitToMission("USS La Jolla", "ASW Patrol")
-- ScenEdit_SetEMCON("Unit", "USS La Jolla", "Sonar=Passive")