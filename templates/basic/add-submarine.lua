-- 添加潜艇模板
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{UNIT_NAME}} - 单位名称
-- {{DBID}} - 潜艇 DBID（通过 MCP 查询获得）
-- {{LATITUDE}} - 纬度
-- {{LONGITUDE}} - 经度
-- {{DEPTH}} - 深度（米，正数）

ScenEdit_AddUnit({
    side="{{SIDE}}",
    type="Submarine",
    name="{{UNIT_NAME}}",
    dbid={{DBID}},
    latitude="{{LATITUDE}}",
    longitude="{{LONGITUDE}}",
    manualAltitude="{{DEPTH}}"
})

-- 示例：添加 688i 洛杉矶级潜艇
-- ScenEdit_AddUnit({
--     side="Blue",
--     type="Submarine",
--     name="USS Los Angeles",
--     dbid=2209,
--     latitude="35.5",
--     longitude="130.0",
--     manualAltitude="50"
-- })