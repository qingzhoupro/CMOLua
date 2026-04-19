-- 添加单位模板（通用）
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{UNIT_TYPE}} - 单位类型：Aircraft / Ship / Submarine / Facility
-- {{UNIT_NAME}} - 单位名称
-- {{DBID}} - 装备 DBID（通过 MCP 查询获得）
-- {{LATITUDE}} - 纬度
-- {{LONGITUDE}} - 经度
-- {{ALTITUDE}} - 高度（飞机用，米）

ScenEdit_AddUnit({
    side="{{SIDE}}",
    type="{{UNIT_TYPE}}",
    name="{{UNIT_NAME}}",
    dbid={{DBID}},
    latitude="{{LATITUDE}}",
    longitude="{{LONGITUDE}}"
    -- altitude="{{ALTITUDE}}"  -- 飞机需要
})

-- 示例：添加飞机
-- ScenEdit_AddUnit({
--     side="Blue",
--     type="Aircraft",
--     name="F-16 #1",
--     dbid=3785,
--     latitude="35.0",
--     longitude="129.0",
--     altitude="5000"
-- })

-- 示例：添加舰艇
-- ScenEdit_AddUnit({
--     side="Blue",
--     type="Ship",
--     name="Destroyer #1",
--     dbid=2278,
--     latitude="35.0",
--     longitude="129.0"
-- })