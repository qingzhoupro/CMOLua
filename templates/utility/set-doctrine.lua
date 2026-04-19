-- 设置作战条令模板
-- 参考: CMO_Lua函数_Unit.md - ScenEdit_SetDoctrine
-- 变量说明：
-- {{TYPE}} - 类型：side / mission / unitname / guid
-- {{NAME}} - 对象名称/GUID
-- {{MISSION_NAME}} - 任务名称（可选，用于 mission 类型）
-- {{DOCTRINE_KEY}} - 条令设置键
-- {{DOCTRINE_VALUE}} - 条令值

-- 设置作战条令
ScenEdit_SetDoctrine({
    {{TYPE}}="{{NAME}}",
    mission="{{MISSION_NAME}}"
}, {
    {{DOCTRINE_KEY}}="{{DOCTRINE_VALUE}}"
})

-- 常用条令设置：
-- 
-- 使用核武器
-- use_nuclear_weapons="yes" / "no" / "only"
-- 
-- 攻击模糊目标
-- engage_ambiguous_targets="optimistic" / "pessimistic" / "ignore"
-- 
-- 攻击不友好目标
-- engage_non_hostile_targets="yes" / "no"
-- 
-- 燃油告警
-- fuel_loiter_low=50  -- 留空燃油告警百分比
-- fuel_joker=80  -- Joker 燃油百分比
-- fuel_bingo=20  -- Bingo 燃油百分比
-- 
-- 武器消耗
-- weapon_state="winchester"  -- 消耗完武器后返航
-- weapon_state="shotgun25"  -- 消耗 25% 后返航
-- 
-- 雷达使用
-- radar_always_active_for_weapons="yes" / "no"
-- 
-- 声纳使用
-- sonar_always_active_for_weapons="yes" / "no"

-- 示例：侧级设置
-- ScenEdit_SetDoctrine({side="Blue"}, {
--     use_nuclear_weapons="no",
--     engage_ambiguous_targets="optimistic"
-- })

-- 示例：任务级设置
-- ScenEdit_SetDoctrine({side="Blue", mission="Strike Mission"}, {
--     weapon_state="winchester",
--     fuel_joker=60
-- })

-- 示例：单元级设置
-- ScenEdit_SetDoctrine({side="Blue", unitname="F-16 #1"}, {
--     engage_non_hostile_targets="no"
-- })