# 工具函数详解

> 参考: Functions.md, CMO 常用lua函数.txt

## 场景信息函数

### GetScenarioTitle

获取场景标题。

```lua
local title = GetScenarioTitle()
print("场景: " .. title)
```

---

### ScenEdit_GetScenHasStarted

检查场景是否已开始。

```lua
local started = ScenEdit_GetScenHasStarted()
if started then
    print("场景已开始")
end
```

---

### ScenEdit_CurrentTime

获取当前时间。

```lua
local time = ScenEdit_CurrentTime()
print("当前时间: " .. time)

-- 返回格式: "2023-01-15 12:30:00"
```

---

### ScenEdit_CurrentLocalTime

获取本地当前时间。

```lua
local localTime = ScenEdit_CurrentLocalTime()
print("本地时间: " .. localTime)
```

---

### ScenEdit_GetDateTimeTicks

获取时间戳。

```lua
local ticks = ScenEdit_GetDateTimeTicks()
print("时间戳: " .. ticks)
```

---

### ScenEdit_SetStartTime

设置场景开始时间。

```lua
ScenEdit_SetStartTime("2023-01-15 06:00:00")
```

---

### ScenEdit_SetTime

设置场景当前时间。

```lua
ScenEdit_SetTime("2023-01-15 12:00:00")
```

---

## 分数函数

### ScenEdit_GetScore

获取分数。

```lua
local score = ScenEdit_GetScore("Blue")
print("分数: " .. score)
```

---

### ScenEdit_SetScore

设置分数。

```lua
ScenEdit_SetScore("Blue", 1000)
ScenEdit_SetScore("Red", 800)
```

---

### ScenEdit_AddCustomLoss

添加自定义损失。

```lua
ScenEdit_AddCustomLoss({
    side = "Blue",
    loss = 50,
    description = "单位被摧毁"
})
```

---

## 场景控制

### ScenEdit_EndScenario

结束场景。

```lua
ScenEdit_EndScenario("Blue", "Victory - All objectives completed")
```

---

### Command_SaveScen

保存场景。

```lua
local result = Command_SaveScen()
if result == "" then
    print("保存成功")
end
```

---

## 天气函数

### ScenEdit_GetWeather

获取天气信息。

```lua
local weather = ScenEdit_GetWeather({
    latitude = "35.0",
    longitude = "127.0"
})

print("云层: " .. weather.cloud)
print("风速: " .. weather.wind_speed)
```

---

### ScenEdit_SetWeather

设置天气。

```lua
ScenEdit_SetWeather({
    type = "Manual",
    cloud = 3,
    wind_speed = 15,
    wind_direction = 180,
    precipitation = "Rain"
})
```

---

## UI 函数

### ScenEdit_MsgBox

显示消息框。

```lua
ScenEdit_MsgBox("Hello World!", 1)  -- 1 = 确定按钮
ScenEdit_MsgBox("Continue?", 2)       -- 2 = 确定/取消
```

---

### ScenEdit_InputBox

显示输入框。

```lua
local input = ScenEdit_InputBox("Enter unit name:", "Default Name")
if input then
    print("输入: " .. input)
end
```

---

### ScenEdit_SpecialMessage

发送特殊消息。

```lua
ScenEdit_SpecialMessage("Blue", "目标已被摧毁!")
ScenEdit_SpecialMessage("Blue", "<h2>任务更新</h2><p>第二阶段开始</p>")
```

---

### ScenEdit_CreateBarkNotification_Geo

创建地理通知。

```lua
ScenEdit_CreateBarkNotification_Geo({
    latitude = "35.0",
    longitude = "127.0",
    message = "SAM 雷达开启!"
})
```

---

### UI_SetCameraView

设置摄像机视角。

```lua
UI_SetCameraView({
    latitude = 35.0,
    longitude = 127.0,
    altitude = 5000,
    pitch = 45,
    yaw = 180
})
```

---

## 存储函数

### ScenEdit_SetKeyValue

设置存储值。

```lua
ScenEdit_SetKeyValue("mission_phase", "2")
ScenEdit_SetKeyValue("score", tostring(100))
```

---

### ScenEdit_GetKeyValue

获取存储值。

```lua
local phase = ScenEdit_GetKeyValue("mission_phase")
local score = tonumber(ScenEdit_GetKeyValue("score"))
```

---

### ScenEdit_ClearKeyValue

清除存储值。

```lua
ScenEdit_ClearKeyValue("old_key")
```

---

## 其他函数

### GetBuildNumber

获取构建号。

```lua
local build = GetBuildNumber()
print("构建: " .. build)
```

---

### ScenEdit_SelectedUnits

获取选中的单位。

```lua
local units = ScenEdit_SelectedUnits()
for i, u in ipairs(units) do
    print("选中: " .. u.name)
end
```

---

### ScenEdit_RunScript

运行脚本。

```lua
ScenEdit_RunScript("print('Hello from script!')")
```

---

### Tool_EmulateNoConsole

模拟无控制台模式。

```lua
Tool_EmulateNoConsole()

-- 之后的错误不会显示
local u = ScenEdit_GetUnit({name="NotExist"})
-- 即使不存在也不会抛出异常
```

---

## 实用工具脚本

### 遍历所有单位

```lua
function printAllUnits()
    local sides = ScenEdit_GetSides()
    for i, side in ipairs(sides) do
        local vpSide = VP_GetSide({Side=side.name})
        if vpSide and vpSide.units then
            print("\n阵营: " .. side.name)
            for j, unit in ipairs(vpSide.units) do
                print("  - " .. unit.name .. " (" .. unit.type .. ")")
            end
        end
    end
end
```

### 单位巡逻

```lua
function patrolArea(unitName, zonePoints)
    local unit = ScenEdit_GetUnit({name=unitName})
    if unit then
        unit.speed = 20
        unit.throttle = "Loiter"
        print("单位 " .. unitName .. " 开始巡逻")
    end
end
```

### 批量设置 EMCON

```lua
function setSideEMCON(sideName, emcon)
    local vpSide = VP_GetSide({Side=sideName})
    if vpSide and vpSide.units then
        for i, unit in ipairs(vpSide.units) do
            ScenEdit_SetEMCON("Unit", unit.name, emcon)
        end
    end
end

-- 使用: setSideEMCON("Blue", "Radar=Passive;Sonar=Active")
```