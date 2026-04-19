# 接触函数详解

> 参考: CMO_Lua函数_Contact.md, Functions.md

## ScenEdit_GetContact

获取接触详细信息。

```lua
local contact = ScenEdit_GetContact({
    side = "Blue",
    guid = "contact-guid"
})
```

**返回值**:
```lua
contact = {
    name = "Contact #1",
    guid = "...",
    type = "Air",           -- Air, Surface, Submarine
    identification_level = 2, -- 识别级别
    latitude = "35.0",
    longitude = "127.0",
    altitude = "5000",
    heading = "90",
    speed = "400",
    side = "Unknown"         -- 阵营
}
```

**识别级别**:
- 0: Unknown
- 1: KnownDomain (仅知道领域：海/空/陆)
- 2: KnownType (知道类型)
- 3: KnownClass (知道级别)
- 4: PreciseID (精确识别)

---

## ScenEdit_GetContacts

获取所有接触。

```lua
local contacts = ScenEdit_GetContacts("Blue")

for i, c in ipairs(contacts) do
    print(c.name .. " - " .. c.type .. " - " .. c.identification_level)
end
```

---

## ScenEdit_AttackContact

攻击接触。

```lua
-- 自动武器分配
ScenEdit_AttackContact("F-16 #1", "Enemy Aircraft #1")

-- 手动武器分配
ScenEdit_AttackContact("F-16 #1", "Enemy Aircraft #1", {
    mode = "ManualWeaponAlloc",
    mount = 438,      -- 挂架 DBID
    weapon = 1413,   -- 武器 DBID
    qty = 2          -- 发射数量
})

-- BOL 攻击 (无引导)
ScenEdit_AttackContact("F-16 #1", "BOL", {
    latitude = "35.5",
    longitude = "127.5"
})
```

**模式**:
- `AutoTargeted` (0): 自动目标分配
- `ManualWeaponAlloc` (1): 手动武器分配

---

## 接触处理示例

```lua
-- 获取所有空中接触
local contacts = ScenEdit_GetContacts("Blue")

for i, c in ipairs(contacts) do
    if c.type == "Air" then
        print("空中接触: " .. c.name)
        print("  识别级别: " .. c.identification_level)
        print("  位置: " .. c.latitude .. ", " .. c.longitude)
        print("  高度: " .. c.altitude)
        
        -- 根据识别级别决定行动
        if c.identification_level >= 3 then
            -- 精确识别，可以攻击
            print("  -> 可攻击")
        end
    end
end
```

**Contact 常用 Wrapper 属性**:

```lua
contact.name                    -- 接触名称
contact.guid                   -- 接触 GUID（攻击时优先使用）
contact.type                    -- 类型：Air, Surface, Submarine
contact.classification_level    -- 识别级别：0=Unknown, 1=KnownDomain, 2=KnownType, 3=KnownClass, 4=PreciseID
contact.latitude                -- 纬度
contact.longitude              -- 经度
contact.altitude               -- 高度
contact.heading                -- 航向
contact.speed                 -- 速度
contact.side                   -- 阵营（Unknown/具体名称）
contact.emissions              -- 辐射信息（ESM/Radar 检测）
contact.lastDetections         -- 最近检测信息
contact.potentialmatches       -- 潜在匹配（可推断单位类型）
contact.bda                   -- 战斗损伤评估 {FIRES, FLOOD, STRUCTURAL}

-- Wrapper 方法
contact:DropContact()                          -- 从视角阵营删除此接触
contact:inArea({"RP-1", "RP-2"})               -- 检查接触是否在区域中
```

---

## 接触与事件结合

```lua
-- 创建检测事件
ScenEdit_SetEvent("空中接触检测", {mode="add", IsRepeatable=1})

ScenEdit_SetTrigger({
    mode = "add",
    type = "UnitDetected",
    side = "Blue",
    TargetType = "Air"
})

ScenEdit_SetAction({
    mode = "add",
    type = "LuaScript",
    ScriptText = [[
local contact = ScenEdit_UnitC()
local detector = ScenEdit_UnitX()

if contact and detector then
    local msg = string.format(
        "检测到: %s\n由: %s\n位置: %s, %s\n识别级别: %d",
        contact.name,
        detector.name,
        contact.latitude,
        contact.longitude,
        contact.identification_level
    )
    ScenEdit_SpecialMessage("Blue", msg)
end
]]
})

ScenEdit_SetEventTrigger("空中接触检测", {mode="add", type="UnitDetected"})
ScenEdit_SetEventAction("空中接触检测", {mode="add", type="LuaScript"})
```