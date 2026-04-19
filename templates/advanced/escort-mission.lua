-- 护航任务模板
-- 参考: https://commandops.github.io/
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{ESCORT_MISSION_NAME}} - 护航任务名称
-- {{STRIKE_MISSION_NAME}} - 被护航的打击任务名称

-- 创建打击任务（需要被护航）
ScenEdit_AddMission({
    side="{{SIDE}}",
    name="{{STRIKE_MISSION_NAME}}",
    type="Strike",
    subtype="LAND"
})

-- 创建护航任务
ScenEdit_AddMission({
    side="{{SIDE}}",
    name="{{ESCORT_MISSION_NAME}}",
    type="Strike",
    subtype="AIR"
})

-- 设置护航任务为护航角色
ScenEdit_SetMission("{{SIDE}}", "{{ESCORT_MISSION_NAME}}", {
    escort=true,  -- 护航任务
    package="{{STRIKE_MISSION_NAME}}"  -- 关联到打击任务
})

-- 示例：
-- 1. 创建打击任务
-- ScenEdit_AddMission({
--     side="Blue",
--     name="Strike Mission",
--     type="Strike",
--     subtype="LAND"
-- })
-- 
-- 2. 创建护航任务
-- ScenEdit_AddMission({
--     side="Blue",
--     name="Escort CAP",
--     type="Strike",
--     subtype="AIR"
-- })
-- 
-- 3. 设置护航关系
-- ScenEdit_SetMission("Blue", "Escort CAP", {
--     escort=true,
--     package="Strike Mission"
-- })