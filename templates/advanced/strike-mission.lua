-- 打击任务模板
-- 参考: https://commandops.github.io/ 和 CMO_Lua函数_Mission.md
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{MISSION_NAME}} - 任务名称
-- {{TARGET_SIDE}} - 目标阵营
-- {{WEAPON_TYPE}} - 打击类型：AIR / LAND / SEA / SUB

-- 创建打击任务
ScenEdit_AddMission({
    side="{{SIDE}}",
    name="{{MISSION_NAME}}",
    type="Strike",
    subtype="{{WEAPON_TYPE}}"
})

-- 设置任务攻击选项
ScenEdit_SetMission("{{SIDE}}", "{{MISSION_NAME}}", {
    attackee="{{TARGET_SIDE}}",  -- 指定目标阵营
   掖护zone_射程_=150  -- 巡逻区域半径（海里）
})

-- 示例：创建对地打击任务
-- ScenEdit_AddMission({
--     side="Blue",
--     name="Strike - Enemy Base",
--     type="Strike",
--     subtype="LAND"
-- })
-- ScenEdit_SetMission("Blue", "Strike - Enemy Base", {
--     attackee="Red",
--     patrolzone_radius=100
-- })

-- 示例：创建对海打击任务
-- ScenEdit_AddMission({
--     side="Blue",
--     name="Maritime Strike",
--     type="Strike",
--     subtype="SEA"
-- })
-- ScenEdit_SetMission("Blue", "Maritime Strike", {
--     attackee="Red"
-- })