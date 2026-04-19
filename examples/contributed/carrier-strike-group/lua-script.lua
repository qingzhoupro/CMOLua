--[[
  File: examples/contributed/carrier-strike-group/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - CSG composition based on US Navy doctrine (publicly available)
  - World_GetPointFromBearing logic from Matrix Games CMO Lua API documentation
  - Carrier air wing configuration from publicly available military sources

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

# 航母打击群自动生成

> 本文件为参考代码，用户需根据实际想定修改占位符后方可运行。

---

## 核心概念

### 航母打击群（CSG）战术编成

```
        [核潜艇]
           |
           | 50海里
           |
[巡洋舰]----[CV]----[驱逐舰]
   |       40海里      |
 30海里   [补给舰]    25海里
   |        10海里     |
[驱逐舰]----[CV]----[驱逐舰]
           |
           |
        [核潜艇]
           50海里
```

### World_GetPointFromBearing 原理

以某点为圆心，根据方位角和距离计算目标点的经纬度：
- `CV1.heading + 角度` → 确定相对航母的方向
- `DISTANCE` → 确定距离（海里）
- `BEARING` → 确定方位角

---

## 模块 A：创建阵营

```lua
-- ============================================================
-- 模块 A：创建阵营
-- ============================================================

-- ⚠️ 配置参数
local SIDES = {
    {side = "{{SIDE_A}}", awareness = "Normal", proficiency = "Regular"},
    {side = "{{SIDE_B}}", awareness = "Normal", proficiency = "Regular"},
    {side = "{{SIDE_C}}", awareness = "Normal", proficiency = "Regular"}
}

-- 设置阵营函数
function F_SetupSides(X_sides)
    for k, v in ipairs(X_sides) do
        print("创造阵营: " .. v.side)
        ScenEdit_AddSide({side = v.side})
        ScenEdit_SetSideOptions({
            side = v.side,
            awareness = v.awareness,
            proficiency = v.proficiency
        })
    end
    ScenEdit_MsgBox("创造各阵营成功", 1)
end

-- 运行
F_SetupSides(SIDES)

-- 设置阵营关系
ScenEdit_SetSidePosture(SIDES[1].side, SIDES[2].side, "H")  -- A vs B 敌对
ScenEdit_SetSidePosture(SIDES[2].side, SIDES[1].side, "H")
ScenEdit_SetSidePosture(SIDES[1].side, SIDES[3].side, "U")  -- A vs C 不友好
ScenEdit_SetSidePosture(SIDES[2].side, SIDES[3].side, "U")  -- B vs C 不友好
ScenEdit_SetSidePosture(SIDES[3].side, SIDES[1].side, "U")
ScenEdit_SetSidePosture(SIDES[3].side, SIDES[2].side, "U")
```

---

## 模块 B：创建航母

```lua
-- ============================================================
-- 模块 B：创建航母及舰载机联队
-- ⚠️ 航母 DBID 需通过 query_dbid 查询
-- ============================================================

local CV_NAME = "{{CV_NAME}}"  -- 航母名称
-- ⚠️ 航母所属阵营（与模块 A 的 {{SIDE_B}} 保持一致）
local CV_SIDE = "{{CV_SIDE}}"

-- 1. 创建航母
-- ⚠️ 航母 DBID（数字）
local CV = ScenEdit_AddUnit({
    side = CV_SIDE,
    type = "Ship",
    name = CV_NAME,
    heading = 0,
    dbid = {{CV_DBID}},  -- 如 2593（尼米兹级）
    Latitude = {{CV_LAT}},
    Longitude = {{CV_LON}},
    holdfire = true,
    speed = 0
})
ScenEdit_MsgBox("创造航母成功: " .. CV_NAME, 1)

-- 2. 创建舰载机联队
-- ⚠️ 每个机型的 DBID 和 loadoutid 需通过 MCP 查询

-- 舰载战斗机 #1-4（F/A-18C + AGM-154A JSOW）
for i = 1, 4 do
    ScenEdit_AddUnit({
        side = CV_SIDE,
        type = "Air",
        name = "{{SQUADRON_1}} #" .. i,
        loadoutid = {{LOADOUT_JSOW}},
        dbid = {{F18C_DBID}},
        base = CV_NAME
    })
end

-- 舰载战斗机 #5-8（F/A-18C + AGM-154C JSOW）
for i = 5, 8 do
    ScenEdit_AddUnit({
        side = CV_SIDE,
        type = "Air",
        name = "{{SQUADRON_2}} #" .. (i - 4),
        loadoutid = {{LOADOUT_JSOW_C}},
        dbid = {{F18C_DBID}},
        base = CV_NAME
    })
end

-- 舰载攻击机 #1-12（F/A-18F + AIM-120D）
for i = 1, 12 do
    ScenEdit_AddUnit({
        side = CV_SIDE,
        type = "Air",
        name = "{{SQUADRON_3}} #" .. i,
        loadoutid = {{LOADOUT_AIM120}},
        dbid = {{F18F_DBID}},
        base = CV_NAME
    })
end

-- 舰载直升机 #1-6（MH-60R + MK54）
for i = 1, 6 do
    ScenEdit_AddUnit({
        side = CV_SIDE,
        type = "Air",
        name = "{{SQUADRON_4}} #" .. i,
        loadoutid = {{LOADOUT_MK54}},
        dbid = {{MH60_DBID}},
        base = CV_NAME
    })
end

print("舰载机联队创建完成")
```

---

## 模块 C：创建编队属舰

```lua
-- ============================================================
-- 模块 C：创建 CSG 编队属舰
-- 以航母为圆心，按战术阵位部署
-- ⚠️ 各舰种 DBID 需通过 query_dbid 查询
-- ============================================================

local CV_HEADING = CV.heading  -- 继承航母航向

-- 1. 计算各舰相对航母的方位和距离
-- AI 助手提示：World_GetPointFromBearing 用于计算目标点经纬度

-- 防空巡洋舰（前方 40 海里）
local pos_CG = World_GetPointFromBearing({
    LATITUDE = CV.latitude,
    LONGITUDE = CV.longitude,
    DISTANCE = 40,
    BEARING = (CV_HEADING + 0) % 360
})

-- 驱逐舰1（前方偏左 30°，25 海里）
local pos_DDG1 = World_GetPointFromBearing({
    LATITUDE = CV.latitude,
    LONGITUDE = CV.longitude,
    DISTANCE = 25,
    BEARING = (CV_HEADING + 330) % 360
})

-- 驱逐舰2（前方偏右 30°，25 海里）
local pos_DDG2 = World_GetPointFromBearing({
    LATITUDE = CV.latitude,
    LONGITUDE = CV.longitude,
    DISTANCE = 25,
    BEARING = (CV_HEADING + 30) % 360
})

-- 驱逐舰3（后方偏左 60°，30 海里）
local pos_DDG3 = World_GetPointFromBearing({
    LATITUDE = CV.latitude,
    LONGITUDE = CV.longitude,
    DISTANCE = 30,
    BEARING = (CV_HEADING + 120) % 360
})

-- 补给舰（近距一侧 10 海里）
local pos_AOE = World_GetPointFromBearing({
    LATITUDE = CV.latitude,
    LONGITUDE = CV.longitude,
    DISTANCE = 10,
    BEARING = (CV_HEADING + 180) % 360
})

-- 2. 创建属舰
-- ⚠️ 各舰 DBID（数字）需通过 query_dbid 查询

-- 巡洋舰
ScenEdit_AddUnit({
    Side = CV_SIDE,
    Type = "Ship",
    Name = "{{CG_NAME}}",
    dbid = {{CG_DBID}},
    Latitude = pos_CG.latitude,
    Longitude = pos_CG.longitude,
    Heading = CV_HEADING
})

-- 驱逐舰 1
ScenEdit_AddUnit({
    Side = CV_SIDE,
    Type = "Ship",
    Name = "{{DDG_NAME_1}}",
    dbid = {{DDG_DBID}},
    Latitude = pos_DDG1.latitude,
    Longitude = pos_DDG1.longitude,
    Heading = CV_HEADING
})

-- 驱逐舰 2
ScenEdit_AddUnit({
    Side = CV_SIDE,
    Type = "Ship",
    Name = "{{DDG_NAME_2}}",
    dbid = {{DDG_DBID}},
    Latitude = pos_DDG2.latitude,
    Longitude = pos_DDG2.longitude,
    Heading = CV_HEADING
})

-- 驱逐舰 3
ScenEdit_AddUnit({
    Side = CV_SIDE,
    Type = "Ship",
    Name = "{{DDG_NAME_3}}",
    dbid = {{DDG_DBID}},
    Latitude = pos_DDG3.latitude,
    Longitude = pos_DDG3.longitude,
    Heading = CV_HEADING
})

-- 补给舰
ScenEdit_AddUnit({
    Side = CV_SIDE,
    Type = "Ship",
    Name = "{{AOE_NAME}}",
    dbid = {{AOE_DBID}},
    Latitude = pos_AOE.latitude,
    Longitude = pos_AOE.longitude,
    Heading = CV_HEADING
})

ScenEdit_MsgBox("CSG 编队创建成功", 1)
```

---

## 舰载机联队参考配置

| 机种 | 数量 | 典型挂载 |
|------|------|---------|
| F/A-18E/F 战斗攻击机 | 24 架 | AIM-120 + JSOW / JDAM |
| F-35C 联合攻击机 | 20 架（最新配置） | AIM-120 + GBU-31 |
| E-2D 预警机 | 4-6 架 | — |
| EA-18G 电子战飞机 | 4-6 架 | AGM-88 + AIM-120 |
| MH-60R 反潜直升机 | 10 架 | MK54 鱼雷 |
| MQ-25A 无人加油机 | 2-4 架 | — |
| C-2A 运输机 | 2 架 | — |

---

## 占位符说明

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{{SIDE_A}}` | 第一阵营名称 | `"Red"` |
| `{{SIDE_B}}` | 第二阵营名称 | `"Blue"` |
| `{{SIDE_C}}` | 第三阵营名称 | `"Green"` |
| `{{CV_NAME}}` | 航母名称 | `"CV-77 乔治布什号"` |
| `{{CV_LAT}}` | 航母纬度（数字） | `24.27` |
| `{{CV_LON}}` | 航母经度（数字） | `127.58` |
| `{{CV_DBID}}` | 航母 DBID（数字） | `2593` |
| `{{F18C_DBID}}` | F/A-18C DBID（数字） | `555` |
| `{{F18F_DBID}}` | F/A-18F DBID（数字） | `965` |
| `{{MH60_DBID}}` | MH-60 DBID（数字） | `4356` |
| `{{CG_DBID}}` | 巡洋舰 DBID（数字） | `2339` |
| `{{DDG_DBID}}` | 驱逐舰 DBID（数字） | `2348` |
| `{{AOE_DBID}}` | 补给舰 DBID（数字） | `897` |
| `{{LOADOUT_JSOW}}` | JSOW 挂载 ID（数字） | `3766` |
| `{{SQUADRON_N}}` | 中队名称 | `"VFA-37 公牛中队"` |
