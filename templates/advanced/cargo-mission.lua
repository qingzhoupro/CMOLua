-- 运输任务模板
-- 参考: https://commandops.github.io/
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{UNIT_NAME}} - 运输单位名称
-- {{UNIT_DBID}} - 运输单位 DBID
-- {{CARGO_TYPE}} - 货物类型
-- {{CARGO_DBID}} - 货物 DBID
-- {{CARGO_QTY}} - 货物数量
-- {{DESTINATION}} - 目的地基地名称

-- 添加运输单位
ScenEdit_AddUnit({
    side="{{SIDE}}",
    type="Ship",
    name="{{UNIT_NAME}}",
    dbid={{UNIT_DBID}},
    latitude="{{LATITUDE}}",
    longitude="{{LONGITUDE}}"
})

-- 装载货物
ScenEdit_UpdateUnitCargo({
    guid=unit.guid,
    mode="add_cargo",
    cargo={{CARGO_QTY}}, {{CARGO_DBID}}
})

-- 创建运输任务
ScenEdit_AddMission({
    side="{{SIDE}}",
    name="{{MISSION_NAME}}",
    type="Cargo",
    destination="{{DESTINATION}}"
})

-- 分配单位到任务
ScenEdit_AssignUnitToMission("{{UNIT_NAME}}", "{{MISSION_NAME}}")

-- 示例：运输部队
-- 1. 添加运输船
-- local transport = ScenEdit_AddUnit({
--     side="Blue",
--     type="Ship",
--     name="Transport Ship",
--     dbid=5031,
--     latitude="35.0",
--     longitude="129.0"
-- })
-- 
-- 2. 装载货物（步兵 DBID=2541）
-- ScenEdit_UpdateUnitCargo({
--     guid=transport.guid,
--     mode="add_cargo",
--     cargo={5, 2541}
-- })
-- 
-- 3. 创建运输任务
-- ScenEdit_AddMission({
--     side="Blue",
--     name="Amphibious Assault",
--     type="Cargo",
--     destination="Landing Zone"
-- })
-- 
-- 4. 分配任务
-- ScenEdit_AssignUnitToMission("Transport Ship", "Amphibious Assault")