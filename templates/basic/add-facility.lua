-- 添加设施模板
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{UNIT_NAME}} - 单位名称
-- {{DBID}} - 设施 DBID（通过 MCP 查询获得）
-- {{LATITUDE}} - 纬度
-- {{LONGITUDE}} - 经度
-- {{AUTODETECTABLE}} - 是否可被探测：true / false

ScenEdit_AddUnit({
    side="{{SIDE}}",
    type="Facility",
    name="{{UNIT_NAME}}",
    dbid={{DBID}},
    latitude="{{LATITUDE}}",
    longitude="{{LONGITUDE}}",
    autodetectable={{AUTODETECTABLE}}
})

-- 示例：添加机场跑道
-- ScenEdit_AddUnit({
--     side="Blue",
--     type="Facility",
--     name="Main Runway",
--     dbid=35,  -- 跑道 DBID
--     latitude="35.0",
--     longitude="129.0",
--     autodetectable=true
-- })

-- 示例：添加雷达站
-- ScenEdit_AddUnit({
--     side="Blue",
--     type="Facility",
--     name="Early Warning Radar",
--     dbid=1385,
--     latitude="35.1",
--     longitude="129.1",
--     autodetectable=false
-- })