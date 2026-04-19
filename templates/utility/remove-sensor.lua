-- 移除传感器模板
-- 参考: CMO_Lua函数_Unit.md - ScenEdit_UpdateUnit
-- 变量说明：
-- {{UNIT_GUID}} - 单位 GUID
-- {{SENSOR_DBID}} - 传感器 DBID

-- 移除特定传感器
ScenEdit_UpdateUnit({
    guid="{{UNIT_GUID}}",
    mode="remove_sensor",
    dbid={{SENSOR_DBID}}
})

-- 移除所有雷达
-- ScenEdit_UpdateUnit({
--     guid="{{UNIT_GUID}}",
--     mode="remove_sensor",
--     dbid=3352  -- 通用雷达 DBID
-- })

-- 常用传感器 DBID：
-- 3352 - APS-145 雷达 (E-3 Sentry)
-- 937 - AN/SPY-1 雷达 (宙斯盾舰)
-- 444 - AN/SPY-1 雷达 (阿利伯克)

-- 示例：移除宙斯盾舰的反舰雷达（降低被发现概率）
-- ScenEdit_UpdateUnit({
--     guid="unit-guid-here",
--     mode="remove_sensor",
--     dbid=444
-- })