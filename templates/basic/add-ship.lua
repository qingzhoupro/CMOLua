-- 添加舰艇模板
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{UNIT_NAME}} - 单位名称
-- {{DBID}} - 舰艇 DBID（通过 MCP 查询获得）
-- {{LATITUDE}} - 纬度
-- {{LONGITUDE}} - 经度
-- {{HEADING}} - 航向（度，可选）
-- {{SPEED}} - 速度（节，可选）

ScenEdit_AddUnit({
    side="{{SIDE}}",
    type="Ship",
    name="{{UNIT_NAME}}",
    dbid={{DBID}},
    latitude="{{LATITUDE}}",
    longitude="{{LONGITUDE}}"
})

-- 设置航向和速度（可选）
-- local ship = ScenEdit_GetUnit({name="{{UNIT_NAME}}"})
-- ship.heading = {{HEADING}}
-- ship.speed = {{SPEED}}

-- 示例：添加宙斯盾驱逐舰
-- ScenEdit_AddUnit({
--     side="Blue",
--     type="Ship",
--     name="USS Arleigh Burke",
--     dbid=2278,
--     latitude="35.0",
--     longitude="129.1"
-- })