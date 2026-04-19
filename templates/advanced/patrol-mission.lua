-- 巡逻任务模板
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{MISSION_NAME}} - 任务名称
-- {{MISSION_TYPE}} - 巡逻类型：ASW / NAVAL / AAW / LAND / MIXED / SEAD
-- {{RP_NAMES}} - 参考点名称表（用于定义巡逻区域）

-- 创建巡逻任务
ScenEdit_AddMission({
    side="{{SIDE}}",
    name="{{MISSION_NAME}}",
    type="Patrol",
    subtype="{{MISSION_TYPE}}"
})

-- 设置巡逻区域（使用参考点定义）
ScenEdit_SetMission("{{SIDE}}", "{{MISSION_NAME}}", {
    patrolzone={
        "{{RP_POINT1}}",
        "{{RP_POINT2}}",
        "{{RP_POINT3}}",
        "{{RP_POINT4}}"
    },
    onethirdrule=false  -- 不使用三分之一规则
})

-- 示例：创建海上巡逻
-- ScenEdit_AddMission({
--     side="Blue",
--     name="Sea Patrol",
--     type="Patrol",
--     subtype="NAVAL"
-- })
-- ScenEdit_SetMission("Blue", "Sea Patrol", {
--     patrolzone={"RP-1", "RP-2", "RP-3", "RP-4"},
--     onethirdrule=false
-- })