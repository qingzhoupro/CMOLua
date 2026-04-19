--[[
  File: examples/contributed/auto-track-zone/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - Automatic search zone logic inspired by CMO Community Scripts
  - Reference point manipulation based on Matrix Games API

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

# 自动搜索跟踪区域

> 本文件为参考代码，用户需根据实际想定修改占位符后方可运行。

---

## 核心 API

| 函数 | 说明 |
|------|------|
| `ScenEdit_AddReferencePoint({...})` | 创建参考点 |
| `ScenEdit_SetReferencePoint({...})` | 更新参考点坐标 |
| `ScenEdit_AddMission({...})` | 创建巡逻任务 |
| `ScenEdit_SetMission("Side","Name",{zone={}})` | 关联任务区域 |
| `ScenEdit_GetContacts("SideName")` | 获取敌方接触列表 |
| `Tool_Range(guid1, guid2)` | 计算两单位间距离 |

---

## 实现步骤

### 步骤 1：创建初始参考点（一次性）

```lua
-- ⚠️ 替换为实际阵营名
local SIDE = "{{SIDE}}"
local RP_PREFIX = "{{RP_PREFIX}}"  -- 参考点名称前缀，如 "反潜巡逻区"

-- 创建 4 个初始参考点（构成矩形巡逻区）
-- AI 助手提示：初始位置可任意设置，程序会自动更新到目标位置

ScenEdit_AddReferencePoint({side = SIDE, name = RP_PREFIX .. "-1", lat = 25.0, lon = 120.0, highlighted = true})
ScenEdit_AddReferencePoint({side = SIDE, name = RP_PREFIX .. "-2", lat = 25.0, lon = 121.0, highlighted = true})
ScenEdit_AddReferencePoint({side = SIDE, name = RP_PREFIX .. "-3", lat = 26.0, lon = 121.0, highlighted = true})
ScenEdit_AddReferencePoint({side = SIDE, name = RP_PREFIX .. "-4", lat = 26.0, lon = 120.0, highlighted = true})

print("参考点已创建: " .. RP_PREFIX .. "-1 ~ " .. RP_PREFIX .. "-4")
```

### 步骤 2：创建巡逻任务并关联区域

```lua
-- AI 助手提示：
-- 巡逻类型选择：
--   - "NAVAL" 海上巡逻
--   - "ASW" 反潜巡逻
--   - "AAW" 防空巡逻

ScenEdit_AddMission({
    side = SIDE,
    name = "{{MISSION_NAME}}",
    type = "Patrol",
    subtype = "ASW"  -- ⚠️ 根据任务类型修改：NAVAL/ASW/AAW/LAND
})

ScenEdit_SetMission(SIDE, "{{MISSION_NAME}}", {
    zone = {RP_PREFIX .. "-1", RP_PREFIX .. "-2", RP_PREFIX .. "-3", RP_PREFIX .. "-4"}
})

print("巡逻任务已创建并关联区域")
```

### 步骤 3：核心函数 autotrack()

```lua
-- ============================================================
-- 自动调整参考点到目标位置
-- 以目标为中心，range_ 为半径，计算正方形巡逻区
-- ============================================================
-- @param lat_target  目标纬度
-- @param lon_target  目标经度
-- @param range_      搜索范围（度），0.1° ≈ 6 海里
-- @param side_       阵营
-- @param name_p      参考点名称前缀
-- ============================================================
function autotrack(lat_target, lon_target, range_, side_, name_p)
    local lat1 = lat_target - range_
    local lon1 = lon_target - range_

    local lat2 = lat_target - range_
    local lon2 = lon_target + range_

    local lat3 = lat_target + range_
    local lon3 = lon_target + range_

    local lat4 = lat_target + range_
    local lon4 = lon_target - range_

    local name1 = name_p .. "-1"
    local name2 = name_p .. "-2"
    local name3 = name_p .. "-3"
    local name4 = name_p .. "-4"

    ScenEdit_SetReferencePoint({side = side_, name = name1, lat = lat1, lon = lon1, highlighted = true})
    ScenEdit_SetReferencePoint({side = side_, name = name2, lat = lat2, lon = lon2, highlighted = true})
    ScenEdit_SetReferencePoint({side = side_, name = name3, lat = lat3, lon = lon3, highlighted = true})
    ScenEdit_SetReferencePoint({side = side_, name = name4, lat = lat4, lon = lon4, highlighted = true})
end
```

### 步骤 4：事件触发脚本（定时扫描并更新）

```lua
-- ============================================================
-- 定时事件脚本（建议触发间隔 30~60 秒）
-- AI 助手提示：创建事件时选择 "定期时间触发"
-- ============================================================

-- ⚠️ 配置参数
local DETECTING_SIDE = "{{SIDE}}"      -- 执行探测的阵营
local RP_PREFIX = "{{RP_PREFIX}}"       -- 参考点前缀
local SEARCH_RANGE = 0.1                -- 搜索范围（度）

function updateSearchZone()
    local contacts = ScenEdit_GetContacts(DETECTING_SIDE)

    if not contacts or #contacts == 0 then
        return
    end

    -- 遍历接触，寻找目标类型
    for i, contact in ipairs(contacts) do
        -- ⚠️ 根据需要修改目标类型筛选条件
        if contact.type == "Submarine" then
            autotrack(
                contact.latitude,
                contact.longitude,
                SEARCH_RANGE,
                DETECTING_SIDE,
                RP_PREFIX
            )
            print("巡逻区已调整到: " .. contact.latitude .. ", " .. contact.longitude .. " [" .. contact.name .. "]")
            break  -- 只处理第一个匹配目标
        end
    end
end

updateSearchZone()
```

---

## 接触类型参考

| `contact.type` | 含义 |
|---------------|------|
| `"Submarine"` | 潜艇 |
| `"Air"` | 空中目标 |
| `"Ship"` | 水面舰艇 |
| `"Facility"` | 地面设施 |
| `"Ground"` | 地面单位 |

---

## 范围参考

| range 值 | 约等于 |
|---------|--------|
| 0.05 | 3 海里 |
| 0.1 | 6 海里 |
| 0.15 | 9 海里 |
| 0.2 | 12 海里 |
| 0.5 | 30 海里 |

---

## 占位符说明

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{{SIDE}}` | 阵营名称 | `"Blue"` |
| `{{RP_PREFIX}}` | 参考点前缀 | `"反潜巡逻区"` |
| `{{MISSION_NAME}}` | 巡逻任务名称 | `"ASW Patrol"` |
