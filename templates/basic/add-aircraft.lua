-- 添加飞机模板
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{UNIT_NAME}} - 单位名称
-- {{DBID}} - 装备 DBID（通过 MCP 查询获得，英文查询）
-- {{LOADOUT_ID}} - 挂载 ID（通过数据库查询，必须为数值）
-- {{BASE}} - 基地名称（可选）
-- {{LATITUDE}} - 纬度
-- {{LONGITUDE}} - 经度
-- {{ALTITUDE}} - 高度（米）

-- 方式1：指定基地
ScenEdit_AddUnit({
    side="{{SIDE}}",
    type="Aircraft",
    name="{{UNIT_NAME}}",
    dbid={{DBID}},
    LoadoutID={{LOADOUT_ID}},
    base="{{BASE}}"
})

-- 方式2：指定位置
ScenEdit_AddUnit({
    side="{{SIDE}}",
    type="Aircraft",
    name="{{UNIT_NAME}}",
    dbid={{DBID}},
    LoadoutID={{LOADOUT_ID}},
    latitude="{{LATITUDE}}",
    longitude="{{LONGITUDE}}",
    altitude="{{ALTITUDE}}"
})

-- 示例：添加 F-16 到 Blue 阵营
-- ScenEdit_AddUnit({
--     side="Blue",
--     type="Aircraft",
--     name="F-16 #1",
--     dbid=3785,
--     LoadoutID=332,
--     base="Osan AFB"
-- })

-- 示例：添加 F-16 到指定位置
-- ScenEdit_AddUnit({
--     side="Blue",
--     type="Aircraft",
--     name="F-16 #2",
--     dbid=3785,
--     LoadoutID=332,
--     latitude="35.0",
--     longitude="129.1",
--     altitude="5000"
-- })
