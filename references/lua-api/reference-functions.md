# 参考点和区域函数详解

> 参考: Functions.md

## ScenEdit_AddReferencePoint

添加参考点。

```lua
-- 绝对位置
ScenEdit_AddReferencePoint({
    side = "Blue",
    name = "RP-1",
    lat = "35.0",
    lon = "127.0",
    highlighted = true
})

-- 相对位置
ScenEdit_AddReferencePoint({
    side = "Blue",
    name = "RP-2",
    RelativeTo = "RP-1",
    bearing = 90,    -- 方位角（度）
    distance = 10,     -- 距离（海里）
    highlighted = true
})
```

---

## ScenEdit_GetReferencePoint

获取参考点信息。

```lua
local rp = ScenEdit_GetReferencePoint({
    side = "Blue",
    name = "RP-1"
})

print(rp.latitude)
print(rp.longitude)
print(rp.highlighted)
```

---

## ScenEdit_SetReferencePoint

设置参考点属性。

```lua
ScenEdit_SetReferencePoint({
    side = "Blue",
    name = "RP-1",
    latitude = "35.5",
    longitude = "127.5",
    highlighted = false
})
```

---

## ScenEdit_DeleteReferencePoint

删除参考点。

```lua
ScenEdit_DeleteReferencePoint({
    side = "Blue",
    name = "RP-1"
})
```

---

## ScenEdit_GetReferencePoints

获取所有参考点。

```lua
local rps = ScenEdit_GetReferencePoints("Blue")

for i, rp in ipairs(rps) do
    print(rp.name .. ": " .. rp.latitude .. ", " .. rp.longitude)
end
```

---

## ScenEdit_AddZone

添加区域。

```lua
ScenEdit_AddZone({
    side = "Blue",
    name = "Patrol Zone",
    Type = " Patrol"  -- 区域类型
})
```

---

## ScenEdit_SetZone

设置区域属性。

```lua
ScenEdit_SetZone({
    side = "Blue",
    name = "Patrol Zone",
    zoneType = "Patrol",
    points = {"RP-1", "RP-2", "RP-3", "RP-4"},
    drawOnMap = true,
    showLabel = true
})
```

---

## ScenEdit_TransformZone

变换区域（移动/缩放）。

```lua
ScenEdit_TransformZone({
    side = "Blue",
    name = "Patrol Zone",
    bearing = 45,   -- 旋转角度
    distance = 5    -- 移动距离
})
```

---

## 工具函数

### Tool_Range

计算单位间距离。

```lua
local range = Tool_Range("F-16 #1", "Enemy #1", "nm")
print("距离: " .. range .. " 海里")
```

**单位**: "nm" (海里), "km" (公里), "mi" (英里)

---

### Tool_Bearing

计算方位角。

```lua
local bearing = Tool_Bearing("F-16 #1", "Enemy #1")
print("方位: " .. bearing .. " 度")
```

---

### Tool_LOS

视线检测。

```lua
local los = Tool_LOS("Radar #1", "Target #1")
if los == true then
    print("有视线")
else
    print("无视线 - " .. tostring(los))
end
```

---

### World_GetPointFromBearing

从方位距离计算点。

```lua
local point = World_GetPointFromBearing({
    latitude = 35.0,
    longitude = 127.0,
    bearing = 90,
    distance = 10,
    unit = "nm"
})

print(point.latitude)
print(point.longitude)
```

---

### World_GetLocation

获取单位位置。

```lua
local loc = World_GetLocation("F-16 #1")
print("纬度: " .. loc.latitude)
print("经度: " .. loc.longitude)
```

---

### World_GetElevation

获取地形海拔。

```lua
local elev = World_GetElevation({
    latitude = 35.0,
    longitude = 127.0
})

print("海拔: " .. elev .. " 米")
```

---

### World_GetCircleFromPoint

获取圆形点集。

```lua
local circle = World_GetCircleFromPoint({
    latitude = 35.0,
    longitude = 127.0,
    radius = 10,   -- 半径
    unit = "nm",   -- 单位
    points = 12    -- 点数量
})

for i, p in ipairs(circle) do
    print(i .. ": " .. p.latitude .. ", " .. p.longitude)
end
```

---

## 巡逻区域示例

```lua
-- 创建巡逻区域参考点
ScenEdit_AddReferencePoint({side="Blue", name="Zone-NW", lat="36.0", lon="127.0", highlighted=true})
ScenEdit_AddReferencePoint({side="Blue", name="Zone-NE", lat="36.0", lon="128.0", highlighted=true})
ScenEdit_AddReferencePoint({side="Blue", name="Zone-SE", lat="35.0", lon="128.0", highlighted=true})
ScenEdit_AddReferencePoint({side="Blue", name="Zone-SW", lat="35.0", lon="127.0", highlighted=true})

-- 创建巡逻任务
ScenEdit_AddMission({
    side="Blue",
    name="Area Patrol",
    type="Patrol",
    subtype="NAVAL"
})

-- 设置巡逻区域
ScenEdit_SetMission("Blue", "Area Patrol", {
    zone={"Zone-NW", "Zone-NE", "Zone-SE", "Zone-SW"}
})
```