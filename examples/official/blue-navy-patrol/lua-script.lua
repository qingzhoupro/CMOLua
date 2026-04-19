--[[
  File: examples/official/blue-navy-patrol/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - Based on Matrix Games CMO Lua API documentation
  - Reference: commandops.github.io and commandlua.github.io

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

-- 蓝方海军巡逻场景
-- ⚠️ DBID 需通过 MCP query_dbid 查询
-- 参考: references/lua-api/ + templates/

-- 创建蓝方阵营
ScenEdit_AddSide({name="Blue", posture="H"})
ScenEdit_SetSideOptions({side="Blue", awareness="Normal", proficiency="Regular"})

-- 创建红方阵营
ScenEdit_AddSide({name="Red", posture="H"})
ScenEdit_SetSideOptions({side="Red", awareness="Normal", proficiency="Regular"})

-- 设置双方敌对关系
ScenEdit_SetSidePosture("Blue", "Red", "H")
ScenEdit_SetSidePosture("Red", "Blue", "H")

-- 添加蓝方宙斯盾驱逐舰 (DBID: 2278 - Arleigh Burke Class)
ScenEdit_AddUnit({
    side="Blue",
    type="Ship",
    name="USS Arleigh Burke",
    dbid=2278,
    latitude="35.0",
    longitude="129.1"
})

-- 添加蓝方护卫舰 (DBID: 2279 - FFG-7)
ScenEdit_AddUnit({
    side="Blue",
    type="Ship",
    name="FFG-7 Oliver Hazard Perry",
    dbid=1769,
    latitude="35.1",
    longitude="128.9"
})

-- 创建海军巡逻任务
ScenEdit_AddMission({
    side="Blue",
    name="Sea Patrol",
    type="Patrol",
    subtype="NAVAL"
})

-- 分配舰艇到巡逻任务
ScenEdit_AssignUnitToMission("USS Arleigh Burke", "Sea Patrol")
ScenEdit_AssignUnitToMission("FFG-7 Oliver Hazard Perry", "Sea Patrol")

-- 添加红方巡逻艇
ScenEdit_AddUnit({
    side="Red",
    type="Ship",
    name="Red Patrol Boat #1",
    dbid=601,
    latitude="34.5",
    longitude="130.5"
})

print("蓝方海军巡逻场景已创建完成")