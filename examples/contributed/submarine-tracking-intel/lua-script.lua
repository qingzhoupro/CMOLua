--[[
  File: examples/contributed/submarine-tracking-intel/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - SSBN patrol zone logic inspired by CMO Community Script patterns
  - KeyValue cross-script communication from Matrix Games API examples
  - LINK-16 / satellite data chain based on CMO EW mechanics

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

# 潜艇追踪与情报系统

> 本文件为参考代码，包含多个子模块，用户需根据实际想定修改占位符后方可运行。

---

## 模块总览

本案例包含以下独立模块，可单独使用：

| 模块 | 功能 |
|------|------|
| 模块 A | 创建 SSBN 巡逻区（随机生成） |
| 模块 B | 持续追踪并计分 |
| 模块 C | LINK-16 / 卫星数据链（特殊动作） |
| 模块 D | 跨阵营传递位置情报 |

---

## 模块 A：创建 SSBN 巡逻区

### 功能说明

以某点为中心，在指定半径内随机生成 SSBN 巡逻区参考点，并创建潜艇单位。

### 实现步骤

**步骤 1：查询潜艇 DBID**
```lua
-- AI 助手提示：使用 MCP 查询
query_dbid("核潜艇") 或 query_dbid("submarine")
```

**步骤 2：确认基地/触发点经纬度**

### 代码

```lua
-- ============================================================
-- 模块 A：创建 SSBN 巡逻区
-- 以指定点为中心，随机生成巡逻区参考点，创建潜艇单位
-- ============================================================

-- ⚠️ 配置参数
local CENTER_LAT = {{CENTER_LAT}}   -- 中心点纬度
local CENTER_LON = {{CENTER_LON}}   -- 中心点经度
local PATROL_RADIUS = 30            -- 巡逻区半径（海里）
local SUB_SIDE = "{{SUB_SIDE}}"     -- 潜艇所属阵营
local SUB_NAME = "{{SUB_NAME}}"     -- 潜艇名称
-- ⚠️ 潜艇 DBID 需通过 query_dbid 查询
local SUB_DBID = {{SUB_DBID}}

-- 在中心点周围生成随机圆点
local radius = math.random(0, 100)  -- 随机偏移（0-100%）
local circle = World_GetCircleFromPoint({
    latitude = CENTER_LAT,
    longitude = CENTER_LON,
    radius = radius
})

-- 取随机一个点作为 SSBN 位置
local ssbn_point = circle[math.random(1, #circle)]

-- 在 SSBN 周围生成巡逻区（4个参考点）
local inner_circle = World_GetCircleFromPoint({
    latitude = ssbn_point.Latitude,
    longitude = ssbn_point.Longitude,
    radius = PATROL_RADIUS
})

-- 每隔约 1/4 圆周取一个点（共4个）
-- 索引规律：11, 22, 33, 44（原始代码逻辑）
for i = 1, 4 do
    local idx = i * 11
    local rp = ScenEdit_AddReferencePoint({
        side = SUB_SIDE,
        name = 'SSBN Patrol Box ' .. i,
        latitude = inner_circle[idx].Latitude,
        longitude = inner_circle[idx].Longitude,
        highlighted = true
    })
    -- 将参考点 GUID 存储为键值，供其他脚本使用
    ScenEdit_SetKeyValue('SSBN_rp' .. i, rp.guid)
end

-- 创建潜艇单位
local ssbn = ScenEdit_AddUnit({
    side = SUB_SIDE,
    type = 'Submarine',
    dbid = SUB_DBID,
    name = SUB_NAME,
    latitude = ssbn_point.Latitude,
    longitude = ssbn_point.Longitude
})

-- 存储潜艇 GUID
ScenEdit_SetKeyValue('SSBN_guid', ssbn.guid)

print('SSBN 创建完成: ' .. SUB_NAME)
print('巡逻区: ' .. PATROL_RADIUS .. ' 海里')
```

---

## 模块 B：持续追踪与计分

### 功能说明

定时扫描接触列表，发现目标潜艇后持续计时，达到一定时间后加分，超过总分则结束想定。

### 实现步骤

**步骤 1：初始化参数（想定加载时执行一次）**
```lua
-- 在 Lua 脚本事件中设置想定加载时触发，执行以下初始化

flag_sub = 0        -- 是否发现目标潜艇
time_r = 0          -- 持续跟踪时间（按事件触发步长累积）
points = 0          -- 当前得分
SCORE_THRESHOLD = 100  -- 触发想定结束的总分
TRACK_THRESHOLD = 60   -- 加分所需持续跟踪时间（分钟）
SCORE_PER_TRACK = 50   -- 每次加分数

-- ⚠️ 目标阵营和名称关键词
local DETECTING_SIDE = "{{DETECTING_SIDE}}"  -- 执行探测的阵营
local SUB_KEYWORD = "{{SUB_KEYWORD}}"        -- 潜艇名称关键词（模糊匹配）
```

**步骤 2：追踪脚本（定期事件触发，建议间隔 1 分钟）**
```lua
-- ============================================================
-- 模块 B：追踪与计分
-- 配合定期事件触发（建议间隔 1 分钟）
-- ============================================================

local loc = ScenEdit_GetContacts(DETECTING_SIDE)
local n = 0
local found = false

for i, v in ipairs(loc) do
    if loc[i].type == 'Submarine' then
        -- ⚠️ 替换为实际潜艇名称关键词
        local foutN = string.find(loc[i].name, SUB_KEYWORD)
        if foutN ~= nil then
            found = true
            flag_sub = 1
            time_r = time_r + 1
            break
        end
    end
end

-- 如果本次扫描没有发现潜艇
if found == false then
    n = n + 1
end

if n == #loc then
    flag_sub = 0
    time_r = 0  -- 跟丢则重置计时
    n = 0
end

-- 加分：持续跟踪超过阈值
if time_r > TRACK_THRESHOLD then
    ScenEdit_SetScore(DETECTING_SIDE, SCORE_PER_TRACK, "稳定跟踪超过 " .. TRACK_THRESHOLD .. " 分钟，加 " .. SCORE_PER_TRACK .. " 分")
    time_r = 0
    points = ScenEdit_GetScore(DETECTING_SIDE) + points
    ScenEdit_SetScore(DETECTING_SIDE, points, "目前总分: " .. points)
end

-- 结束：超过总分阈值
if points >= SCORE_THRESHOLD then
    ScenEdit_EndScenario("{{DETECTING_SIDE}} 成功完成任务")
end
```

### 潜艇类型参考

| 接触类型 | 说明 |
|---------|------|
| `'Submarine'` | 潜艇（水下） |
| `'Air'` | 空中目标 |
| `'Ship'` | 水面舰艇 |
| `'Ground'` | 地面单位 |

---

## 模块 C：LINK-16 / 卫星数据链

### 功能说明

通过 Special Action（特殊动作）触发上浮，潜艇上浮至一定深度后建立数据链，接收跨阵营态势信息。

### 实现步骤

**步骤 1：在编辑器中创建 Special Action**
- 在潜艇单位上创建 Special Action
- 动作脚本关联本模块代码

**步骤 2：上浮触发脚本**
```lua
-- ============================================================
-- 模块 C-1：LINK-16 上浮触发（Special Action）
-- AI 助手提示：需在编辑器中为潜艇创建 Special Action
-- ============================================================

-- ⚠️ 替换为实际潜艇 GUID
local sub_guid = "{{SUB_GUID}}"

local sub = ScenEdit_GetUnit({guid = sub_guid})

-- 设定上浮深度阈值（米，负值）
local BUOY_DEPTH_THRESHOLD = -20  -- 上浮至此深度以浅则建立链接

if sub.altitude >= BUOY_DEPTH_THRESHOLD then
    -- 潜艇已在浅深度，建立链接
    ScenEdit_MsgBox('已建立卫星态势数据链路', 6)

    -- ⚠️ 设置阵营关系（使情报提供方可见于潜艇方）
    -- F = Friendly（友方，共享态势）
    ScenEdit_SetSidePosture('{{INTEL_SIDE}}', '{{SUB_SIDE}}', 'F')

    -- 激活监测事件（定时检查是否下潜）
    -- ⚠️ 在编辑器中创建名为 "监测卫星态势" 的事件
    ScenEdit_SetEvent('监测卫星态势', {isactive = true})
else
    ScenEdit_MsgBox('卫星态势数据链路断开，当前深度: ' .. sub.altitude .. 'm（需 ≤ ' .. BUOY_DEPTH_THRESHOLD .. 'm）', 6)
end
```

**步骤 3：下潜断开链接（监测事件脚本）**
```lua
-- ============================================================
-- 模块 C-2：下潜断开链接（监测事件脚本）
-- 配合定期事件触发（建议间隔 30 秒）
-- 事件名称："监测卫星态势"
-- ============================================================

-- ⚠️ ⚠️ ⚠️ 深度阈值必须在 C-2 中重复定义（Lua 全局变量需每个模块独立声明）
local BUOY_DEPTH_THRESHOLD = -20  -- 与 C-1 保持一致（米，负值）
-- ⚠️ 替换为实际潜艇 GUID
local sub_guid = "{{SUB_GUID}}"
local sub = ScenEdit_GetUnit({guid = sub_guid})

if sub.altitude < BUOY_DEPTH_THRESHOLD then
    -- 潜艇下潜，断开链接
    ScenEdit_SetSidePosture('{{INTEL_SIDE}}', '{{SUB_SIDE}}', 'N')
    ScenEdit_MsgBox('卫星态势数据链路断开，潜艇已下潜', 6)
    -- 关闭本监测事件
    ScenEdit_SetEvent('监测卫星态势', {isactive = false})
end
```

### 阵营关系代码

| 代码 | 关系 | 说明 |
|------|------|------|
| `"F"` | Friendly | 友方，共享情报和态势 |
| `"H"` | Hostile | 敌对 |
| `"N"` | Neutral | 中立，无情报共享 |
| `"U"` | Unfriendly | 不友好 |

---

## 模块 D：跨阵营传递位置情报

### 功能说明

将潜艇巡逻区参考点坐标跨阵营传递给友方（通过 KeyValue 存储 GUID，批量创建参考点）。

### 实现步骤

**步骤 1：从 KeyValue 读取巡逻区坐标并传递**
```lua
-- ============================================================
-- 模块 D-1：跨阵营传递巡逻区坐标
-- 将 {{SUB_SIDE}} 的巡逻区参考点传递给 {{INTEL_SIDE}}
-- ============================================================

-- 检查是否已传递（避免重复）
if ScenEdit_GetKeyValue('EAM_RECEIVED') ~= 'true' then
    for i = 1, 4 do
        -- 读取 {{SUB_SIDE}} 巡逻区参考点
        local ref_id = ScenEdit_GetKeyValue('SSBN_rp' .. i)
        local ref_point = ScenEdit_GetReferencePoint({
            side = '{{SUB_SIDE}}',
            guid = ref_id
        })

        -- 在 {{INTEL_SIDE}} 侧创建对应的参考点
        ScenEdit_AddReferencePoint({
            side = '{{INTEL_SIDE}}',
            name = 'Reported SSBN Patrol Zone ' .. i,
            latitude = ref_point.latitude,
            longitude = ref_point.longitude,
            highlighted = true
        })
    end
    ScenEdit_SetKeyValue('EAM_RECEIVED', 'true')
    print('SSBN 巡逻区情报已传递给 ' .. '{{INTEL_SIDE}}')
end
```

**步骤 2：传递多个潜艇位置（扩展版）**
```lua
-- ============================================================
-- 模块 D-2：传递多个潜艇位置给突破方
-- 示例：将 {{DETECTING_SIDE}} 的多个潜艇位置传递给 {{BREAKER_SIDE}}
-- ============================================================

-- ⚠️ ⚠️ ⚠️ 需先在编辑器中记录各潜艇单位的精确名称
local subUnitNames = {
    "{{SUB_UNIT_NAME_1}}",
    "{{SUB_UNIT_NAME_2}}",
    "{{SUB_UNIT_NAME_3}}",
    -- 继续添加...
}

local subUnitList = {}
for i, name in ipairs(subUnitNames) do
    local u = ScenEdit_GetUnit({
        side = '{{DETECTING_SIDE}}',
        name = name
    })
    if u then
        table.insert(subUnitList, u)
    end
end

-- 创建参考点并存储 GUID
for i = 1, #subUnitList do
    local rp = ScenEdit_AddReferencePoint({
        side = '{{BREAKER_SIDE}}',
        name = 'Submarine Location ' .. i,
        latitude = subUnitList[i].latitude,
        longitude = subUnitList[i].longitude,
        highlighted = false
    })
    ScenEdit_SetKeyValue('Sub_rp' .. i, rp.guid)
    print('潜艇 ' .. i .. ' 位置已传递: ' .. rp.guid)
end
```

**步骤 3：条件触发情报接收（上浮后）**
```lua
-- ============================================================
-- 模块 D-3：上浮后接收情报（配合 Special Action）
-- 条件：潜艇深度 ≥ -80m 且在特定时间后
-- ============================================================

local sub_guid = "{{SUB_GUID}}"
local sub = ScenEdit_GetUnit({guid = sub_guid})

if sub.altitude >= -80 then
    ScenEdit_MsgBox('满足接收情报条件', 6)

    -- 检查时间条件（可结合 ScenEdit_CurrentTime() 判断）
    -- 示例：判断是否为祖鲁时间 1200 之后
    local currentTime = ScenEdit_CurrentTime()
    if currentTime == "12:00:00" then
        -- 传递所有潜艇位置
        for i = 1, #subUnitList do
            ScenEdit_AddReferencePoint({
                side = '{{BREAKER_SIDE}}',
                name = 'Enemy Submarine Zone ' .. i,
                latitude = subUnitList[i].latitude,
                longitude = subUnitList[i].longitude,
                highlighted = true
            })
        end
        ScenEdit_MsgBox('敌方潜艇活动区域已标出', 6)
    else
        ScenEdit_MsgBox('请在祖鲁时间 12:00 后执行', 6)
    end
else
    ScenEdit_MsgBox('深度过深，不满足接收条件（当前: ' .. sub.altitude .. 'm）', 6)
end
```

---

## 占位符说明

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{{CENTER_LAT}}` | SSBN 区域中心纬度 | `51.0` |
| `{{CENTER_LON}}` | SSBN 区域中心经度 | `149.9` |
| `{{SUB_SIDE}}` | 潜艇所属阵营 | `"Red"` |
| `{{SUB_NAME}}` | 潜艇名称 | `"K-44 Ryazan"` |
| `{{SUB_DBID}}` | 潜艇 DBID（数字） | `268` |
| `{{DETECTING_SIDE}}` | 执行探测的阵营 | `"Blue"` |
| `{{SUB_KEYWORD}}` | 潜艇名称关键词（模糊匹配） | `"667BDRM"`, `"K-44"` |
| `{{SUB_GUID}}` | 潜艇单位 GUID | 完整 GUID 字符串 |
| `{{INTEL_SIDE}}` | 情报提供方阵营 | `"Satellite"` |
| `{{BREAKER_SIDE}}` | 情报接收方（突破方）阵营 | `"Red"` |
| `{{SUB_UNIT_NAME_N}}` | 潜艇精确名称 | `"SSN-501"` |
