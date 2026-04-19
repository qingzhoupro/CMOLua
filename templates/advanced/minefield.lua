-- 布雷任务模板
-- 参考: https://commandops.github.io/
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{MISSION_NAME}} - 布雷任务名称
-- {{RP_LIST}} - 参考点名称表

-- 创建布雷任务
ScenEdit_AddMission({
    side="{{SIDE}}",
    name="{{MISSION_NAME}}",
    type="Mining",
    subtype="NAVAL"
})

-- 设置布雷区域（使用参考点定义）
ScenEdit_SetMission("{{SIDE}}", "{{MISSION_NAME}}", {
    zone={"{{RP_1}}", "{{RP_2}}", "{{RP_3}}"}
})

-- 示例：创建港口布雷任务
-- 1. 先创建参考点
-- ScenEdit_AddReferencePoint({side="Blue", name="Mine-1", lat="34.5", lon="129.0", highlighted=true})
-- ScenEdit_AddReferencePoint({side="Blue", name="Mine-2", lat="34.6", lon="129.1", highlighted=true})
-- ScenEdit_AddReferencePoint({side="Blue", name="Mine-3", lat="34.4", lon="129.1", highlighted=true})
-- 
-- 2. 创建布雷任务
-- ScenEdit_AddMission({
--     side="Blue",
--     name="Port Mining",
--     type="Mining",
--     subtype="NAVAL"
-- })
-- 
-- 3. 设置布雷区域
-- ScenEdit_SetMission("Blue", "Port Mining", {
--     zone={"Mine-1", "Mine-2", "Mine-3"}
-- })