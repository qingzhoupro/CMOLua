--[[
  File: examples/official/composite/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - Based on Matrix Games CMO Lua API documentation
  - Reference: commandops.github.io and commandlua.github.io

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

-- 合成作战案例
-- ⚠️ DBID 需通过 MCP query_dbid 查询
-- 参考: commandops.github.io 和 CMO_Lua函数_Unit.md, CMO_Lua函数_Mission.md
-- 场景：蓝方执行两栖登陆作战，整合海军、空军和陆军力量

-- =============================================
-- 1. 创建阵营
-- =============================================
ScenEdit_AddSide({name="Blue", posture="H"})
ScenEdit_AddSide({name="Red", posture="H"})
ScenEdit_SetSidePosture("Blue", "Red", "H")
ScenEdit_SetSidePosture("Red", "Blue", "H")

-- =============================================
-- 2. 蓝方海军力量
-- =============================================

-- 黄蜂级两栖攻击舰 (DBID=3562)
local lhd = ScenEdit_AddUnit({
    side="Blue",
    type="Ship",
    name="USS Wasp",
    dbid=3562,
    latitude="35.0",
    longitude="140.0"
})

-- 圣安东尼奥级船坞登陆舰 (DBID=6054)
local lpd = ScenEdit_AddUnit({
    side="Blue",
    type="Ship",
    name="USS San Antonio",
    dbid=6054,
    latitude="35.1",
    longitude="140.1"
})

-- 宙斯盾驱逐舰护航 (DBID=2278)
ScenEdit_AddUnit({
    side="Blue",
    type="Ship",
    name="USS Chancellorsville",
    dbid=2278,
    latitude="35.2",
    longitude="140.2"
})

-- =============================================
-- 3. 蓝方空中力量
-- =============================================

-- AV-8B Harrier (DBID=3518) - 鹞式攻击机
for i = 1, 6 do
    ScenEdit_AddUnit({
        type="Aircraft",
        side="Blue",
        name="AV-8B #" .. i,
        dbid=3518,
        loadoutid=0,
        base="USS Wasp"
    })
end

-- F-35B (DBID=6440) - 第五代战斗机
for i = 1, 4 do
    ScenEdit_AddUnit({
        type="Aircraft",
        side="Blue",
        name="F-35B #" .. i,
        dbid=6440,
        loadoutid=0,
        base="USS Wasp"
    })
end

-- MH-60S (DBID=3534) - 海上直升机
for i = 1, 4 do
    ScenEdit_AddUnit({
        type="Aircraft",
        side="Blue",
        name="MH-60S #" .. i,
        dbid=3534,
        loadoutid=0,
        base="USS San Antonio"
    })
end

-- =============================================
-- 4. 蓝方登陆部队
-- =============================================

-- 装甲运兵车 (DBID=754) - 步兵战车
for i = 1, 8 do
    local apc = ScenEdit_AddUnit({
        side="Blue",
        type="Facility",
        name="APC #" .. i,
        dbid=754,
        latitude="35.0",
        longitude="140.0"
    })
    -- 设置为可卸载
    apc.group = "Landing Force"
end

-- 海军陆战队 (DBID=2541) - 步兵单位
local marines = ScenEdit_AddUnit({
    side="Blue",
    type="Facility",
    name="Marine Platoon #1",
    dbid=2541,
    latitude="35.0",
    longitude="140.0"
})
marines.group = "Landing Force"

-- =============================================
-- 5. 创建任务
-- =============================================

-- 参考点定义登陆区域
ScenEdit_AddReferencePoint({side="Blue", name="LZ-Beach", lat="35.2", lon="140.3", highlighted=true})

-- 创建打击任务（压制敌方）
ScenEdit_AddMission({
    side="Blue",
    name="Naval Strike - 压制射击",
    type="Strike",
    subtype="LAND"
})

-- 创建对地支援任务
ScenEdit_AddMission({
    side="Blue",
    name="CAS - 近距离空中支援",
    type="Strike",
    subtype="LAND"
})

-- 分配飞机到支援任务
ScenEdit_AssignUnitToMission("AV-8B #1", "CAS - 近距离空中支援")
ScenEdit_AssignUnitToMission("F-35B #1", "Naval Strike - 压制射击")

-- =============================================
-- 6. 红方防御力量
-- =============================================

-- Sa-15 防空导弹 (DBID=2313) - 短程防空
ScenEdit_AddUnit({
    side="Red",
    type="Facility",
    name="SA-15 #1",
    dbid=2313,
    latitude="35.3",
    longitude="140.4",
    autodetectable=true
})

-- 岸防炮 (DBID=2010)
ScenEdit_AddUnit({
    side="Red",
    type="Facility",
    name="Coastal Battery",
    dbid=2010,
    latitude="35.25",
    longitude="140.35",
    autodetectable=true
})

-- 红方巡逻艇 (DBID=601)
ScenEdit_AddUnit({
    side="Red",
    type="Ship",
    name="Patrol Boat #1",
    dbid=601,
    latitude="35.1",
    longitude="140.5"
})

-- =============================================
-- 7. 设置作战条令
-- =============================================

-- 蓝方：不限制开火
ScenEdit_SetDoctrine({side="Blue"}, {
    engage_non_hostile_targets="yes",
    use_nuclear_weapons="no"
})

-- 压制任务：消耗模式
ScenEdit_SetDoctrine({side="Blue", mission="Naval Strike - 压制射击"}, {
    weapon_state="winchester",
    fuel_joker=50
})

-- =============================================
-- 8. 事件：单位被摧毁
-- =============================================
ScenEdit_SetEvent("单位损失报告", {mode="add", IsRepeatable=1})

ScenEdit_SetTrigger({
    mode="add",
    type="UnitDestroyed",
    name="蓝方损失",
    side="Blue"
})

ScenEdit_SetAction({
    mode="add",
    type="LuaScript",
    name="损失日志",
    ScriptText=[[
local unit = ScenEdit_UnitX()
local attacker = ScenEdit_UnitY()
local side = ScenEdit_PlayerSide()
local score = ScenEdit_GetScore(side)

print("[损失] " .. unit.name .. " 被摧毁")
print("[分数] " .. score)

-- 发送消息
ScenEdit_SpecialMessage(side, 
    "⚠️ 单位损失\n" ..
    unit.name .. " 已被摧毁\n" ..
    "剩余分数: " .. score)
]]
})

ScenEdit_SetEventTrigger("单位损失报告", {mode="add", name="蓝方损失"})
ScenEdit_SetEventAction("单位损失报告", {mode="add", name="损失日志"})

print("合成作战场景已创建完成")
print("蓝方: LHD+LPD+DDG, 10x Air, 9x Landing Force")
print("红方: SA-15, 岸防炮, 巡逻艇")