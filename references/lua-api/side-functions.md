# 阵营函数详解

> 参考: Functions.md

## ScenEdit_AddSide

创建阵营。

```lua
ScenEdit_AddSide({
    name = "Blue",
    posture = "H"  -- 初始态度
})
```

**posture 选项**:
- `H` - Hostile（敌对）
- `F` - Friendly（友好）
- `N` - Neutral（中立）
- `U` - Unfriendly（不友好）

---

## ScenEdit_RemoveSide

移除阵营。

```lua
ScenEdit_RemoveSide("Blue")
```

---

## ScenEdit_SetSidePosture

设置阵营态度。

```lua
ScenEdit_SetSidePosture("Blue", "Red", "H")
ScenEdit_SetSidePosture("Red", "Blue", "H")  -- 需要双向设置
```

---

## ScenEdit_GetSidePosture

获取阵营态度。

```lua
local posture = ScenEdit_GetSidePosture("Blue", "Red")
print(posture)  -- 返回 "H", "F", "N", "U"
```

---

## ScenEdit_SetSideOptions

设置阵营选项。

```lua
ScenEdit_SetSideOptions({
    side = "Blue",
    awareness = "Normal",     -- 感知级别
    proficiency = "Regular"   -- 熟练度
})
```

**awareness 选项**:
- `Blind` (-1) - 盲目
- `Normal` (0) - 正常
- `AutoSideID` (1) - 自动识别阵营
- `AutoSideAndUnitID` (2) - 自动识别单位和阵营
- `Omniscient` (3) - 全知

**proficiency 选项**:
- `Novice` (0)
- `Cadet` (1)
- `Regular` (2)
- `Veteran` (3)
- `Ace` (4)

---

## ScenEdit_GetSideOptions

获取阵营选项。

```lua
local options = ScenEdit_GetSideOptions("Blue")
print(options.awareness)
print(options.proficiency)
```

---

## ScenEdit_GetSideIsHuman

检查是否是人类玩家。

```lua
local isHuman = ScenEdit_GetSideIsHuman("Blue")
if isHuman then
    print("蓝方是人类玩家")
end
```

---

## ScenEdit_PlayerSide

获取玩家阵营。

```lua
local playerSide = ScenEdit_PlayerSide()
print("当前玩家: " .. playerSide)
```

---

## VP_GetSides

获取所有阵营。

```lua
local sides = VP_GetSides()

for i, side in ipairs(sides) do
    print("阵营: " .. side.name)
    print("  颜色: " .. side.color)
end
```

---

## VP_GetSide

获取特定阵营信息。

```lua
local side = VP_GetSide({Side = "Blue"})

print(side.name)
print(side.guid)

-- 单位列表
for i, unit in ipairs(side.units) do
    print("  " .. unit.name)
end
```

---

## VP_GetSides

获取所有阵营。

```lua
local sides = VP_GetSides()

for i, side in ipairs(sides) do
    print("阵营: " .. side.name)
end
```

**返回值**:
```lua
{
    { name = "Blue", guid = "..." },
    { name = "Red", guid = "..." },
    ...
}
```

---

## VP_GetSide

获取特定阵营的详细信息（含单位列表）。

```lua
local side = VP_GetSide({Side = "Blue"})

-- 阵营属性
print(side.name)
print(side.guid)

-- 遍历所有单位
for i, unit in ipairs(side.units) do
    print("  " .. unit.name .. " (" .. unit.guid .. ")")
end

-- 单位是否在区域内
local unitsInZone = side:unitsInArea({"RP-1", "RP-2", "RP-3", "RP-4"})
```

**unitsInArea()**: 返回指定参考点区域内所有单位的 GUID 列表。

---

## 完整阵营设置示例

```lua
-- 创建阵营
ScenEdit_AddSide({name="Blue", posture="F"})
ScenEdit_AddSide({name="Red", posture="H"})
ScenEdit_AddSide({name="Neutral", posture="N"})

-- 设置蓝方为人类玩家风格
ScenEdit_SetSideOptions({
    side = "Blue",
    awareness = "AutoSideAndUnitID",
    proficiency = "Veteran"
})

-- 设置态度关系
ScenEdit_SetSidePosture("Blue", "Red", "H")    -- 蓝对红敌对
ScenEdit_SetSidePosture("Red", "Blue", "H")     -- 红对蓝敌对
ScenEdit_SetSidePosture("Blue", "Neutral", "F") -- 蓝对中立友好
ScenEdit_SetSidePosture("Red", "Neutral", "N")  -- 红对中立中立
```