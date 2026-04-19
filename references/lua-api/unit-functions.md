# 单位函数详解

> 参考: CMO_Lua函数_Unit.md, Functions.md

## ScenEdit_AddUnit

添加新单位到场景。

```lua
ScenEdit_AddUnit({
    type = "Aircraft",     -- 单位类型 (Aircraft/Ship/Submarine/Facility)
    unitname = "F-16 #1",  -- 单位名称 (必须唯一)
    side = "Blue",         -- 阵营名称
    dbid = 3785,           -- 数据库 ID
    -- 坐标：支持 latitude / longitude（完整）或 lat / lon（官方别名）
    lat = "35.0",         -- 纬度（lat 是官方支持的简写）
    lon = "127.0",         -- 经度（lon 是官方支持的简写）
    altitude = "5000",     -- 高度（飞机用，默认米；可用 "5000 FT" 指定英尺）
    loadoutid = 332,      -- 挂载 ID（飞机用）
    base = "Osan AB",     -- 基地名称（可选，指定后自动采用基地坐标）
    manualAltitude = 50,   -- 潜航深度（潜艇用，正数）
    proficiency = "Regular", -- 熟练度
    -- 自定义 GUID（可选）
    guid = "自定义-GUID-36字符"
})
```

**参数说明**:
- `type`: Aircraft, Ship, Submarine, Facility
- `latitude/lat` 与 `longitude/lon` 均有效，lon 是官方别名
- `altitude`: 仅飞机有效，默认米；`"5000 FT"` 表示英尺
- `manualAltitude`: 仅潜艇有效，正数表示下潜深度
- `loadoutid`（小写 l）: Aircraft 挂载 ID，与 `LoadoutID`（大写 L）均有效

**返回值**: Unit wrapper 或 nil

---

## ScenEdit_GetUnit

获取单位信息。

```lua
-- 方式1：通过名称和阵营
local unit = ScenEdit_GetUnit({
    side = "Blue",
    unitname = "F-16 #1"
})

-- 方式2：通过 GUID
local unit = ScenEdit_GetUnit({
    guid = "unit-guid-here"
})
```

**返回值**: Unit wrapper

```lua
unit = {
    type = "Aircraft",
    name = "F-16 #1",
    side = "Blue",
    guid = "...",
    class = "F-16C Block 50",
    proficiency = "Regular",
    latitude = "35.0",
    longitude = "127.0",
    altitude = "5000",
    heading = "0",
    speed = "400",
    fuel = {
        {current = 3000, max = 4000, name = "AviationFuel", type = 2001}
    }
}
```

---

## ScenEdit_SetUnit

设置单位属性。

```lua
ScenEdit_SetUnit({
    guid = "unit-guid",
    speed = 20,
    heading = 180,
    altitude = "10000"
})
```

---

## ScenEdit_DeleteUnit

删除单位（不触发事件）。

```lua
-- 通过名称删除
ScenEdit_DeleteUnit({
    side = "Blue",
    unitname = "F-16 #1"
})

-- 包含编队删除
ScenEdit_DeleteUnit({
    side = "Blue",
    unitname = "Group #1"
}, true)  -- true = 包含子单位
```

---

## ScenEdit_KillUnit

摧毁单位（触发事件）。

```lua
ScenEdit_KillUnit({
    side = "Blue",
    unitname = "F-16 #1"
})
```

---

## ScenEdit_SetLoadout

设置飞机挂载。

```lua
ScenEdit_SetLoadout({
    unitname = "F-16 #1",
    LoadoutID = 332,  -- 挂载数据库 ID
    TimeToReady_Minutes = 30
})
```

---

## ScenEdit_GetLoadout

获取飞机挂载信息。

```lua
local loadout = ScenEdit_GetLoadout({
    unitname = "F-16 #1",
    LoadoutID = 0  -- 0 = 当前挂载
})

print(loadout.weapons[1].wpn_name)  -- 武器名称
print(loadout.weapons[1].wpn_current)  -- 当前数量
```

---

## ScenEdit_FillMagsForLoadout

为基地填充弹药。

```lua
ScenEdit_FillMagsForLoadout({
    unit = "Osan AB",
    loadoutid = 332,
    quantity = 48  -- 填充数量
})
```

---

## ScenEdit_SetEMCON

设置电磁管控。

```lua
-- 阵营级
ScenEdit_SetEMCON("Side", "Blue", "Radar=Active;Sonar=Passive")

-- 任务级
ScenEdit_SetEMCON("Mission", "ASW Patrol", "Inherit;Sonar=Active")

-- 单元级
ScenEdit_SetEMCON("Unit", "USS Arleigh Burke", "Radar=Active")

-- 编队级
ScenEdit_SetEMCON("Group", "Destroyer Squadron 1", "Radar=Passive")
```

**EMCON 格式**: `"Radar=Active;Sonar=Passive;OECM=Active"`
- `Active/Passive`: 主动/被动模式
- `Inherit`: 继承上级设置

---

## ScenEdit_SetDoctrine

设置作战条令。

```lua
-- 侧级条令
ScenEdit_SetDoctrine({side = "Blue"}, {
    use_nuclear_weapons = "no",
    engage_ambiguous_targets = "optimistic",
    engage_non_hostile_targets = "no"
})

-- 任务级条令
ScenEdit_SetDoctrine({
    side = "Blue",
    mission = "Strike Mission"
}, {
    weapon_state = "winchester",
    fuel_joker = 70,
    fuel_bingo = 30
})

-- 单元级条令
ScenEdit_SetDoctrine({
    side = "Blue",
    unitname = "F-16 #1"
}, {
    radar_always_active_for_weapons = "yes"
})
```

**常用条令参数**:
- `use_nuclear_weapons`: "yes", "no", "only"
- `engage_ambiguous_targets`: "optimistic", "pessimistic", "ignore"
- `engage_non_hostile_targets`: "yes", "no"
- `fuel_joker`: 百分比（留空告警）
- `fuel_bingo`: 百分比（紧急返航）
- `weapon_state`: "winchester", "shotgun25", "shotgun50"

---

## ScenEdit_RefuelUnit

为单位加油。

```lua
-- 自动寻找加油机
ScenEdit_RefuelUnit({
    side = "Blue",
    unitname = "F-16 #1"
})

-- 指定加油机
ScenEdit_RefuelUnit({
    side = "Blue",
    unitname = "F-16 #1",
    tanker = "KC-135 #1"
})

-- 指定加油任务
ScenEdit_RefuelUnit({
    side = "Blue",
    unitname = "F-16 #1",
    missions = {"Refueling Mission"}
})
```

---

## ScenEdit_AddReloadsToUnit

添加武器补给。

```lua
-- 添加导弹
ScenEdit_AddReloadsToUnit({
    side = "Blue",
    unitname = "USS Arleigh Burke",
    wpn_dbid = 1575,  -- AIM-120
    number = 4
})

-- 移除武器
ScenEdit_AddReloadsToUnit({
    side = "Blue",
    unitname = "USS Arleigh Burke",
    wpn_dbid = 1575,
    number = 2,
    remove = true
})

-- 填充到最大
ScenEdit_AddReloadsToUnit({
    side = "Blue",
    unitname = "USS Arleigh Burke",
    wpn_dbid = 1575,
    fillout = true
})
```

---

## ScenEdit_AddWeaponToUnitMagazine

添加武器到弹药库。

```lua
ScenEdit_AddWeaponToUnitMagazine({
    unitname = "USS Wasp",
    wpn_dbid = 1575,
    number = 20,
    maxcap = 50
})
```

---

## ScenEdit_MergeUnits

合并选中的单位。

```lua
local merged = ScenEdit_MergeUnits()
```

---

## ScenEdit_SplitUnit

分离单位（拆分为各组件）。

```lua
local components = ScenEdit_SplitUnit({
    name = "APC Group #1",
    guid = "unit-guid"
})
```

---

## ScenEdit_UpdateUnit

更新单位组件（传感器、挂载、武器、通讯等）。

```lua
-- 添加传感器
ScenEdit_UpdateUnit({
    guid = "unit-guid",
    mode = "add_sensor",
    dbid = 3352  -- 传感器 DBID
})

-- 移除传感器
ScenEdit_UpdateUnit({
    guid = "unit-guid",
    mode = "remove_sensor",
    dbid = 3352,
    sensorid = "sensor-guid"
})

-- 添加 dock 设施
ScenEdit_UpdateUnit({
    guid = "unit-guid",
    mode = "add_dock_facility",
    dbid = 19
})

-- 添加/移除/修改燃料
ScenEdit_UpdateUnit({
    guid = "unit-guid",
    mode = "add_fuel",
    fuel = {"GasFuel", 5000}  -- {燃料类型, 数量}
})

-- 添加武器到挂架
ScenEdit_UpdateUnit({
    guid = "unit-guid",
    mode = "add_weapon",
    dbid = 1575,  -- 武器 DBID
    mountid = "mount-guid"
})
```

**mode 常用值**:
- `add_sensor` / `remove_sensor`: 添加/移除传感器
- `add_mount` / `remove_mount`: 添加/移除挂架
- `add_weapon` / `remove_weapon`: 添加/移除武器
- `add_dock_facility` / `remove_dock_facility`: 添加/移除停靠设施
- `add_fuel` / `remove_fuel`: 添加/移除燃料
- `delta`: 从 .ini 文件更新单位

---

## ScenEdit_SetUnitSide

将单位转移到另一个阵营（心理战、投降、接管场景）。

```lua
ScenEdit_SetUnitSide({
    side = "Ukraine",          -- 原阵营
    unitname = "Unit Name",     -- 单位名称
    -- 或使用 guid：
    guid = "unit-guid",
    newside = "Russia"          -- 目标阵营
})
```

**使用场景**:
- 心理战：敌方单位随机投降转平民
- 电子战：无人机被接管后转属己方
- 海军叛逃：舰艇临阵起义

**示例（随机劝降）**:
```lua
local con = ScenEdit_GetContacts("Red")
for k, contact in ipairs(con) do
    if contact.type == "Mobile Unit" then
        ScenEdit_SetUnitSide({
            side = "Red",
            guid = contact.guid,
            newside = "Civilian"
        })
    end
end
```

---

## ScenEdit_SetUnit（outOfComms 网络中断）

设置单位通讯状态，用于模拟网络战/电子干扰效果。

```lua
-- 网络中断（通讯中断）
ScenEdit_SetUnit({
    side = "Blue",
    unitname = "F-16 #1",
    outOfComms = "True"   -- 或 true
})

-- 网络恢复
ScenEdit_SetUnit({
    side = "Blue",
    unitname = "F-16 #1",
    outOfComms = "False"  -- 或 false
})
```

**使用场景**:
- 网络攻击导致雷达站失联
- 电子干扰切断通讯链
- Starlink 等备用通信恢复

**注意**: `outOfComms = true` 会使单位失去共享态势感知，只能依靠自身传感器。

---

## ScenEdit_KillUnit

摧毁单位（触发事件）。

```lua
ScenEdit_KillUnit({
    side = "Blue",
    unitname = "F-16 #1"
})

-- 或通过 guid
ScenEdit_KillUnit({
    guid = "unit-guid"
})
```

---

## ScenEdit_SetUnitDamage

设置单位损伤状态（火灾/进水/部件损坏）。

```lua
ScenEdit_SetUnitDamage({
    side = "Blue",
    unitname = "USS Arleigh Burke",
    fires = 1,        -- 火灾等级 (0-4)
    flood = 2,         -- 进水等级 (0-4)
    dp = 50,           -- 剩余伤害点
    -- 损坏特定部件
    components = {
        {"rudder", "Medium"},           -- {部件名, 损坏程度}
        {"type", "sensor", 1}           -- {随机损坏, 类型, 数量}
    }
})
```

---

## ScenEdit_ClearAllAircraft

清除机场所有飞机（批量卸载）。

```lua
ScenEdit_ClearAllAircraft({
    unit = "Osan AB"   -- 机场名称
})
```

---

## ScenEdit_DistributeWeaponAtAirbase

为机场分配武器到弹药库。

```lua
ScenEdit_DistributeWeaponAtAirbase({
    unit = "Osan AB",
    wpn_dbid = 1575,  -- AIM-120 DBID
    quantity = 48
})
```