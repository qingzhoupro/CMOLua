--[[
  File: examples/contributed/track-export/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - Track recording concepts based on Matrix Games CMO API documentation

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

# 飞机轨迹记录与导出

> 本文件为参考代码，用户需根据实际想定修改占位符后方可运行。

---

## ⚠️ 重要限制

CMO 商业版**不支持 Lua IO 操作**（`io.open`、`io.write` 等），无法自动写入 CSV 文件。

替代方案：
1. 使用全局变量存储轨迹数据
2. 通过 `print()` 输出到 Lua 控制台
3. 手动复制并保存为 CSV

---

## 核心 API

| 函数 | 说明 |
|------|------|
| `ScenEdit_GetUnit({name=})` | 获取单位位置信息 |
| `ScenEdit_CurrentTime()` | 获取当前时间戳 |
| `print(string)` | 输出到 Lua 控制台 |
| `table.concat(t, sep)` | 合并表为字符串 |

---

## 实现步骤

### 步骤 1：在想定中添加飞机单位

在编辑器中添加需追踪的飞机，记下准确名称。

### 步骤 2：创建轨迹记录脚本（想定的 Lua 脚本事件）

```lua
-- ============================================================
-- 轨迹记录系统
-- 触发方式：配合定期事件，每隔一定时间调用 RecordTrackData()
-- ============================================================

-- 全局轨迹存储
TrackData = {
    headers = {"Name", "Latitude", "Longitude", "Altitude", "Heading", "Speed", "Time"},
    records = {}
}

-- 获取飞机位置
-- @param unitName 单位名称（⚠️ 需与编辑器中名称完全一致）
function GetAircraftPosition(unitName)
    local aircraft = ScenEdit_GetUnit({name = unitName})
    if aircraft then
        return {
            aircraft.name,
            aircraft.latitude,
            aircraft.longitude,
            aircraft.altitude,
            aircraft.heading,
            aircraft.speed,
            ScenEdit_CurrentTime()
        }
    end
    return nil
end

-- 记录一条数据
-- @param unitName 单位名称
function RecordTrackData(unitName)
    local pos = GetAircraftPosition(unitName)
    if pos then
        table.insert(TrackData.records, pos)
        print("已记录: " .. unitName)
    else
        print("未找到单位: " .. unitName)
    end
end

-- 输出 CSV 格式
function PrintTrackDataAsCSV()
    print("=== 轨迹数据 ===")
    print(table.concat(TrackData.headers, ","))
    for _, record in ipairs(TrackData.records) do
        print(table.concat(record, ","))
    end
    print("=== 共 " .. #TrackData.records .. " 条 ===")
end

-- 清除数据
function ClearTrackData()
    TrackData.records = {}
    print("轨迹数据已清除")
end
```

### 步骤 3：创建定期记录事件（编辑器中手动创建）

```
事件名称：轨迹记录
触发条件：定期时间 → {{INTERVAL}} 秒（建议 10~60 秒）
动作：Lua 脚本 → RecordTrackData("{{AIRCRAFT_NAME}}")
```

### 步骤 4：导出数据（想定运行后）

在 Lua 控制台执行：

```lua
PrintTrackDataAsCSV()
```

复制控制台输出，粘贴到文本编辑器，保存为 `.csv` 文件。

---

## 批量记录多个单位

```lua
-- 在编辑器中创建事件，动作脚本：
local unitsToTrack = {
    "{{AIRCRAFT_NAME_1}}",
    "{{AIRCRAFT_NAME_2}}",
    "{{AIRCRAFT_NAME_3}}"
}

for i, name in ipairs(unitsToTrack) do
    RecordTrackData(name)
end
```

---

## 初始化提示

在想定加载时执行一次，显示使用说明：

```lua
ScenEdit_MsgBox(
    "轨迹记录器已就绪\n" ..
    "已注册单位: {{AIRCRAFT_NAME}}\n" ..
    "请在编辑器中创建定期事件触发 RecordTrackData()",
    0
)
```

---

## 占位符说明

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{{AIRCRAFT_NAME}}` | 飞机精确名称 | `"F-16C #1"` |
| `{{INTERVAL}}` | 记录间隔（秒，数字） | `30` |
