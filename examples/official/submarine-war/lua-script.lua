--[[
  File: examples/official/submarine-war/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - Based on Matrix Games CMO Lua API documentation
  - Reference: commandops.github.io and commandlua.github.io

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

-- 潜艇战案例
-- ⚠️ DBID 需通过 MCP query_dbid 查询
-- 参考: commandops.github.io 和 CMO_Lua函数_Unit.md, CMO_Lua函数_Events.md
-- 场景：蓝方反潜舰艇巡逻，红方潜艇试图突破封锁

-- =============================================
-- 1. 创建阵营
-- =============================================
ScenEdit_AddSide({name="Blue", posture="H"})
ScenEdit_AddSide({name="Red", posture="H"})
ScenEdit_SetSidePosture("Blue", "Red", "H")
ScenEdit_SetSidePosture("Red", "Blue", "H")

-- =============================================
-- 2. 创建蓝方反潜舰艇
-- =============================================

-- 阿利伯克级驱逐舰 (DBID=2278) - 反潜主力
local ddg1 = ScenEdit_AddUnit({
    side="Blue",
    type="Ship",
    name="USS Arleigh Burke",
    dbid=2278,
    latitude="35.5",
    longitude="140.0"
})
ddg1.group = "ASW Group"

-- 佩里级护卫舰 (DBID=1769) - 反潜协助
local ffg = ScenEdit_AddUnit({
    side="Blue",
    type="Ship",
    name="USS Taylor",
    dbid=1769,
    latitude="35.3",
    longitude="140.2"
})
ffg.group = "ASW Group"

-- =============================================
-- 3. 创建蓝方反潜巡逻机
-- =============================================

-- S-3B Viking (DBID=3521) - 反潜巡逻机
for i = 1, 2 do
    ScenEdit_AddUnit({
        type="Aircraft",
        side="Blue",
        name="S-3B #" .. i,
        dbid=3521,
        loadoutid=0,
        base="ASW Base"
    })
end

-- =============================================
-- 4. 创建红方潜艇
-- =============================================

-- 基洛级潜艇 (DBID=2221) - 常规动力潜艇
local sub1 = ScenEdit_AddUnit({
    side="Red",
    type="Submarine",
    name="Kilo-1",
    dbid=2221,
    latitude="34.0",
    longitude="142.0",
    manualAltitude=50  -- 巡逻深度
})

-- 洛杉矶级潜艇 (DBID=2209) - 核动力攻击潜艇
local sub2 = ScenEdit_AddUnit({
    side="Red",
    type="Submarine",
    name="Los Angeles-1",
    dbid=2209,
    latitude="33.5",
    longitude="143.0",
    manualAltitude=100
})

-- =============================================
-- 5. 创建反潜巡逻任务
-- =============================================

-- 参考点定义巡逻区域
ScenEdit_AddReferencePoint({side="Blue", name="ASW-Zone-1", lat="35.5", lon="141.0", highlighted=true})
ScenEdit_AddReferencePoint({side="Blue", name="ASW-Zone-2", lat="35.5", lon="139.0", highlighted=true})
ScenEdit_AddReferencePoint({side="Blue", name="ASW-Zone-3", lat="34.5", lon="139.0", highlighted=true})
ScenEdit_AddReferencePoint({side="Blue", name="ASW-Zone-4", lat="34.5", lon="141.0", highlighted=true})

-- 创建 ASW 巡逻任务
ScenEdit_AddMission({
    side="Blue",
    name="ASW - 反潜巡逻",
    type="Patrol",
    subtype="ASW"
})

-- 设置巡逻区域
ScenEdit_SetMission("Blue", "ASW - 反潜巡逻", {
    zone={"ASW-Zone-1", "ASW-Zone-2", "ASW-Zone-3", "ASW-Zone-4"}
})

-- 分配舰艇到反潜任务
ScenEdit_AssignUnitToMission("USS Arleigh Burke", "ASW - 反潜巡逻")
ScenEdit_AssignUnitToMission("USS Taylor", "ASW - 反潜巡逻")

-- =============================================
-- 6. 设置 EMCON（电磁管控）
-- =============================================

-- 反潜巡逻舰艇：被动声纳 + 主动雷达
ScenEdit_SetEMCON("Unit", "USS Arleigh Burke", "Radar=Active;Sonar=Passive")

-- 潜艇：完全静默
ScenEdit_SetEMCON("Unit", "Kilo-1", "Sonar=Passive")
ScenEdit_SetEMCON("Unit", "Los Angeles-1", "Sonar=Passive")

-- =============================================
-- 7. 创建检测事件
-- =============================================
ScenEdit_SetEvent("潜艇检测事件", {mode="add", IsRepeatable=1})

-- 触发器：检测到潜艇
ScenEdit_SetTrigger({
    mode="add",
    type="UnitDetected",
    name="Submarine Detected",
    side="Blue",
    TargetType="Submarine"
})

-- 动作：发送告警
ScenEdit_SetAction({
    mode="add",
    type="LuaScript",
    name="ASW Alert",
    ScriptText=[[
local contact = ScenEdit_UnitC()
local detector = ScenEdit_UnitX()
ScenEdit_SpecialMessage("Blue", 
    "⚠️ 反潜告警\n".
    "检测到潜艇: " .. (contact and contact.name or "未知") .. "\n".
    "由: " .. (detector and detector.name or "未知") .. "\n".
    "位置: " .. (contact and contact.latitude or "?") .. ", " .. (contact and contact.longitude or "?"))
]]
})

ScenEdit_SetEventTrigger("潜艇检测事件", {mode="add", name="Submarine Detected"})
ScenEdit_SetEventAction("潜艇检测事件", {mode="add", name="ASW Alert"})

print("潜艇战场景已创建完成")
print("蓝方: 2x ASW Ship, 2x S-3B 反潜机")
print("红方: 1x Kilo, 1x Los Angeles")