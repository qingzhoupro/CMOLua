--[[
  File: examples/contributed/missile-signature/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - Missile signature manipulation based on Matrix Games CMO Lua API
  - CSV data processing patterns from standard Lua I/O examples

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
  - Commercial edition does not support Lua IO operations.
--]]

# 导弹特征修改

> 本文件为参考代码。
>
> ⚠️ **CMO 商业版不支持 Lua IO 操作**（`io.open`、`io.write` 等），无法读取外部 CSV 文件。本案例仅供 **CMO 开发版/服务器版** 用户参考。
>
> 商业版用户请在编辑器中直接预设导弹特征参数。

---

## 核心 API

| 函数 | 说明 |
|------|------|
| `VP_GetSide({Side=""})` | 获取阵营所有单位 |
| `ScenEdit_GetUnit({guid=})` | 获取单位详情 |
| `ScenEdit_SetUnit({movebylua=true,...})` | 移动单位（含 movebylua=true） |
| `unit.xsection` | 设置雷达/红外特征（仅开发版） |

---

## 特征参数说明

### 雷达散射截面（RCS）

| 参数 | 说明 | 单位 |
|------|------|------|
| RCSFront | 前向 RCS | dBsm |
| RCSRear | 后向 RCS | dBsm |
| RCSSide | 侧向 RCS | dBsm |
| RCSTop | 顶部 RCS | dBsm |

CMO 中 RCS 需转换为线性值：`math.pow(10, dBsm / 10)`

### 红外特征

| 参数 | 说明 |
|------|------|
| IRFront | 前向红外强度 |
| IRRear | 后向红外强度 |
| IRSide | 侧向红外强度 |
| IRTop | 顶部红外强度 |

---

## 实现步骤（开发版）

### 步骤 1：准备 CSV 数据文件

创建 CSV 文件（列号需根据实际数据调整）：

```csv
time,pitch,yaw,roll,lon,lat,altitude,RCS_Top,RCS_Rear,RCS_Front,RCS_Side,IR_Top,IR_Rear,IR_Front,IR_Side
1,0.5,45.0,0.0,118.5,24.5,5000,-10,-15,-5,-8,1.2,0.8,2.1,1.0
2,0.6,45.2,0.1,118.6,24.6,5100,-10,-15,-5,-8,1.2,0.8,2.1,1.0
```

### 步骤 2：获取导弹 GUID

```lua
-- 在编辑器中添加导弹单位后，运行以下代码获取 GUID
-- ⚠️ 替换为实际阵营名

local missileGuid = nil
local sideUnits = VP_GetSide({Side = "{{SIDE}}"}).units

for i = 1, #sideUnits do
    local unit = ScenEdit_GetUnit({guid = sideUnits[i].guid})
    if unit.type == "Weapon" then
        missileGuid = unit.guid
        print("导弹 GUID: " .. missileGuid .. " | 名称: " .. unit.name)
        break
    end
end
```

### 步骤 3：CSV 读取函数（开发版）

```lua
-- 字符串分割
function split(line, delimiter)
    local result = {}
    string.gsub(line, '[^' .. delimiter .. ']+', function(w)
        table.insert(result, w)
    end)
    return result
end

-- 读取 CSV 数据
-- ⚠️ ⚠️ ⚠️ 商业版不支持 IO，CSV 路径仅供开发版使用
local CSV_PATH = "{{CSV_PATH}}"  -- 例如: "C:\\Data\\missile_traj.csv"

function loadMissileCSV(filePath)
    local file = io.open(filePath, "r")
    if not file then
        print("无法打开: " .. filePath)
        return nil
    end

    local data = {}
    local idx = 0
    for line in file:lines() do
        if idx ~= 0 then
            local col = split(line, ",")
            data[idx] = {
                -- ⚠️ CSV 列号需根据实际数据文件调整，下为示例格式：
                -- time,pitch,yaw,roll,lon,lat,altitude,...
                --   1    2    3    4   5   6     7  ...
                latitude  = tonumber(col[6]),   -- 第6列：纬度
                longitude = tonumber(col[5]),   -- 第5列：经度
                altitude  = tonumber(col[7]) * 1000,  -- 第7列：高度（km→m）
                pitch     = tonumber(col[2]),
                yaw       = tonumber(col[3]),
                roll      = tonumber(col[4]),
                rcsSide   = tonumber(col[11]),
                rcsRear   = tonumber(col[10]),
                rcsTop    = tonumber(col[9]),
                rcsFront  = tonumber(col[10]),
                irSide    = tonumber(col[15]),
                irRear    = tonumber(col[14]),
                irTop     = tonumber(col[13]),
                irFront   = tonumber(col[14])
            }
        end
        idx = idx + 1
    end
    file:close()
    return data
end
```

### 步骤 4：应用特征（定时事件触发）

```lua
-- ============================================================
-- 定时事件触发脚本
-- 事件设置：定期时间，间隔 1~3 秒
-- ============================================================

local missileGuid = "{{MISSIL_GUID}}"   -- ⚠️ 从步骤2获取
local trajectoryData = nil              -- 加载一次
local trajIndex = 1

function initTrajectory()
    -- ⚠️ 商业版会失败，仅开发版可用
    trajectoryData = loadMissileCSV("{{CSV_PATH}}")
    return trajectoryData ~= nil
end

function applyMissileState()
    if not trajectoryData or not trajectoryData[trajIndex] then
        print("轨迹数据已用完")
        return false
    end

    local d = trajectoryData[trajIndex]
    local unit = ScenEdit_GetUnit({guid = missileGuid})
    if not unit then return false end

    -- 移动导弹
    ScenEdit_SetUnit({
        guid = missileGuid,
        movebylua = true,
        latitude = d.latitude,
        longitude = d.longitude,
        altitude = d.altitude
    })

    -- 设置 RCS
    unit.xsection = {
        [1] = {
            Side   = math.pow(10, d.rcsSide / 10),
            Rear   = math.pow(10, d.rcsRear / 10),
            Top    = math.pow(10, d.rcsTop / 10),
            Front  = math.pow(10, d.rcsFront / 10),
            SigType = "Radar_A_D_Band"
        }
    }

    -- 设置红外特征
    unit.xsection = {
        [1] = {
            Side   = d.irSide,
            Rear   = d.irRear,
            Top    = d.irTop,
            Front  = d.irFront,
            SigType = "InfraredDetectionRange"
        }
    }

    trajIndex = trajIndex + 1
    return true
end

-- 初始化（想定加载时执行一次）
initTrajectory()
```

---

## 商业版替代方案

CMO 商业版无法读取外部 CSV，建议：

1. **编辑器预设**：在编辑器中直接设置导弹特征参数
2. **简化硬编码**：将少量特征数据直接写在 Lua 代码中
3. **开发版调试**：仅在开发版调试想定，完成后导出

---

## 占位符说明

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{{SIDE}}` | 导弹所属阵营 | `"Red"` |
| `{{MISSIL_GUID}}` | 导弹单位 GUID | 完整 GUID 字符串 |
| `{{CSV_PATH}}` | CSV 文件路径 | `"C:\\Data\\traj.csv"` |
