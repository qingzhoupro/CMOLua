-- 空军基地完整模板
-- 参考: CMO 常用lua函数.txt - 机场建设部分
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{BASE_NAME}} - 基地名称
-- {{LATITUDE}} - 基地纬度
-- {{LONGITUDE}} - 基地经度
-- {{RUNWAY_DBID}} - 跑道 DBID
-- {{NUM_AIRCRAFT}} - 飞机数量
-- {{AIRCRAFT_DBID}} - 飞机 DBID
-- {{LOADOUT_ID}} - 挂载 ID

-- 随机数函数
function RandomFloat(min, max, escala)
    if min ~= nil and max ~= nil and escala ~= nil then
        return math.random(min * (10 ^ escala), max * (10 ^ escala)) / (10 ^ escala)
    end
    return nil
end

-- 添加跑道
local runway = ScenEdit_AddUnit({
    type="Facility",
    side="{{SIDE}}",
    name="Main Runway",
    dbid={{RUNWAY_DBID}},
    latitude="{{LATITUDE}}",
    longitude="{{LONGITUDE}}",
    autodetectable=true
})
runway.group = "{{BASE_NAME}}"

-- 机场设施表 (DBID -> 名称)
local airfield = {
    [3] = "Control Tower",           -- 控制塔
    [217] = "Tarmac Space",        -- 停机坪
    [68] = "Aircraft Hangar",       -- 机库
    [353] = "Runway Access",        -- 跑道入口
    [1393] = "Fuel Tank",           -- 燃料库
    [1423] = "Taxiway",             -- 滑行道
    [322] = "Ammo Bunker"           -- 弹药库
}

-- 添加强制设施
for dbid, name in pairs(airfield) do
    local latOffset = RandomFloat(-0.0003, 0.0003, 13) or 0
    local lonOffset = RandomFloat(-0.0003, 0.0003, 13) or 0
    
    local facility = ScenEdit_AddUnit({
        type="Facility",
        side="{{SIDE}}",
        name=name,
        dbid=dbid,
        latitude="{{LATITUDE}}" + latOffset,
        longitude="{{LONGITUDE}}" + lonOffset,
        autodetectable=false
    })
    facility.group = "{{BASE_NAME}}"
end

-- 添加飞机（如果指定了）
if {{NUM_AIRCRAFT}} > 0 then
    for i = 1, {{NUM_AIRCRAFT}} do
        local aircraft = ScenEdit_AddUnit({
            type="Aircraft",
            side="{{SIDE}}",
            name="Aircraft #" .. i,
            dbid={{AIRCRAFT_DBID}},
            loadoutid={{LOADOUT_ID}},
            base="{{BASE_NAME}}"
        })
    end
    
    -- 填充弹药
    ScenEdit_FillMagsForLoadout({
        unit="{{BASE_NAME}}",
        loadoutid={{LOADOUT_ID}},
        quantity=48
    })
end

-- 示例：创建蓝方空军基地
-- local runway = ScenEdit_AddUnit({
--     type="Facility",
--     side="Blue",
--     name="Osan AB",
--     dbid=35,
--     latitude="35.0",
--     longitude="129.0",
--     autodetectable=true
-- })
-- runway.group = "Osan AB"
-- 
-- -- 添加 F-16
-- for i = 1, 12 do
--     ScenEdit_AddUnit({
--         type="Aircraft",
--         side="Blue",
--         name="F-16 #" .. i,
--         dbid=3785,
--         loadoutid=332,
--         base="Osan AB"
--     })
-- end
-- 
-- ScenEdit_FillMagsForLoadout({
--     unit="Osan AB",
--     loadoutid=332,
--     quantity=48
-- })