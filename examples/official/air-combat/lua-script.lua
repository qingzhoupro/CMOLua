--[[
  File: examples/official/air-combat/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - Based on Matrix Games CMO Lua API documentation
  - Reference: commandops.github.io and commandlua.github.io

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

-- 空战拦截案例
-- ⚠️ DBID 需通过 MCP query_dbid 查询
-- 参考: commandops.github.io 和 CMO_Lua函数_Unit.md, CMO_Lua函数_Mission.md
-- 场景：蓝方空军基地部署战斗机，执行空中拦截任务

-- =============================================
-- 1. 创建阵营和敌对关系
-- =============================================
ScenEdit_AddSide({name="Blue", posture="H"})
ScenEdit_AddSide({name="Red", posture="H"})
ScenEdit_SetSidePosture("Blue", "Red", "H")
ScenEdit_SetSidePosture("Red", "Blue", "H")

-- =============================================
-- 2. 创建空军基地
-- =============================================

-- 主跑道
local runway = ScenEdit_AddUnit({
    type="Facility",
    side="Blue",
    name="Osan AB - Runway",
    dbid=35,
    latitude="37.5",
    longitude="127.0",
    autodetectable=true
})
runway.group = "Osan AB"

-- 滑行道
local taxiway = ScenEdit_AddUnit({
    type="Facility",
    side="Blue",
    name="Taxiway",
    dbid=1423,
    latitude="37.5",
    longitude="127.0",
    autodetectable=false
})
taxiway.group = "Osan AB"

-- 机库
local hangar = ScenEdit_AddUnit({
    type="Facility",
    side="Blue",
    name="Hangar #1",
    dbid=68,
    latitude="37.5",
    longitude="127.01",
    autodetectable=false
})
hangar.group = "Osan AB"

-- 燃料库
local fuel = ScenEdit_AddUnit({
    type="Facility",
    side="Blue",
    name="Fuel Storage",
    dbid=1393,
    latitude="37.5",
    longitude="126.99",
    autodetectable=false
})
fuel.group = "Osan AB"

-- =============================================
-- 3. 添加蓝方战斗机 (DBID 通过 MCP query_dbid() 查询)
-- =============================================

-- F-16C (DBID=3785) - 多用途战斗机
for i = 1, 8 do
    ScenEdit_AddUnit({
        type="Aircraft",
        side="Blue",
        name="F-16C #" .. i,
        dbid=3785,
        loadoutid=332,
        base="Osan AB"
    })
end

-- F-15C (DBID=3784) - 空中优势战斗机
for i = 1, 4 do
    ScenEdit_AddUnit({
        type="Aircraft",
        side="Blue",
        name="F-15C #" .. i,
        dbid=3784,
        loadoutid=16934,
        base="Osan AB"
    })
end

-- KC-135 (DBID=3514) - 加油机
ScenEdit_AddUnit({
    type="Aircraft",
    side="Blue",
    name="KC-135 #1",
    dbid=3514,
    loadoutid=0,
    base="Osan AB"
})

-- =============================================
-- 4. 创建空中拦截任务
-- =============================================

-- 参考点定义拦截区域
ScenEdit_AddReferencePoint({side="Blue", name="CAP-1", lat="38.0", lon="128.0", highlighted=true})
ScenEdit_AddReferencePoint({side="Blue", name="CAP-2", lat="38.0", lon="126.0", highlighted=true})
ScenEdit_AddReferencePoint({side="Blue", name="CAP-3", lat="37.0", lon="126.0", highlighted=true})
ScenEdit_AddReferencePoint({side="Blue", name="CAP-4", lat="37.0", lon="128.0", highlighted=true})

-- 创建 CAP 任务
ScenEdit_AddMission({
    side="Blue",
    name="CAP - 空中截击",
    type="Strike",
    subtype="AIR"
})

-- 设置巡逻区域
ScenEdit_SetMission("Blue", "CAP - 空中截击", {
    zone={"CAP-1", "CAP-2", "CAP-3", "CAP-4"},
    patrolType="FighterCAP"  -- 战斗机 CAP
})

-- 分配 F-15C 到 CAP 任务
ScenEdit_AssignUnitToMission("F-15C #1", "CAP - 空中截击")
ScenEdit_AssignUnitToMission("F-15C #2", "CAP - 空中截击")

-- =============================================
-- 5. 添加红方入侵飞机
-- =============================================

-- MiG-29 (DBID=2702) - 红方战斗机
ScenEdit_AddUnit({
    type="Aircraft",
    side="Red",
    name="MiG-29 #1",
    dbid=2702,
    loadoutid=3,
    latitude="37.5",
    longitude="130.0",
    altitude="5000"
})

-- Su-25 (DBID=4600) - 红方攻击机
ScenEdit_AddUnit({
    type="Aircraft",
    side="Red",
    name="Su-25 #1",
    dbid=4600,
    loadoutid=3,
    latitude="37.0",
    longitude="129.5",
    altitude="3000"
})

-- =============================================
-- 6. 设置作战条令
-- =============================================

-- 蓝方设置：攻击不友好目标
ScenEdit_SetDoctrine({side="Blue"}, {
    engage_non_hostile_targets="no",
    engage_ambiguous_targets="optimistic"
})

-- CAP 任务设置：Joker 燃油 70%
ScenEdit_SetDoctrine({side="Blue", mission="CAP - 空中截击"}, {
    fuel_joker=70,
    weapon_state="winchester"
})

print("空战拦截场景已创建完成")
print("蓝方：8x F-16C + 4x F-15C (CAP) + 1x KC-135")
print("红方：1x MiG-29 + 1x Su-25")