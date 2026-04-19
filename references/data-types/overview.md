# 数据类型总览

## 概述

本文档列出 CMO Lua API 中使用的数据类型。

## 基本类型

CMO 使用 Lua 的基本类型：string, number, boolean, table。

## CMO 特有类型

### 1. 高度 (Altitude)

高度可以是米或英尺：
- `"100 FT"` - 英尺
- `"100 M"` - 米
- `"100"` - 米（默认）

```lua
{altitude = "5000 M"}
{altitude = "10000 FT"}
{altitude = "3000"}  -- 默认米
```

### 2. 经纬度 (Latitude/Longitude)

纬度格式：
- 数字：`24.587`（正数北纬，负数南纬）
- 带方向：`"S 60.20.10"` 或 `"-60.336"`

经度格式：
- 数字：`118.021`（正数东经，负数西经）
- 带方向：`"W 60.20.10"` 或 `"-60.336"`

```lua
{latitude = "24.587", longitude = "118.021"}
{latitude = "-35.5", longitude = "145.0"}
```

### 3. 单位类型 (UnitType)

| 代码 | 类型 |
|------|------|
| 1 | Aircraft |
| 2 | Ship |
| 3 | Submarine |
| 4 | Facility |
| 5 | Aimpoint |
| 6 | Weapon |
| 7 | Satellite |
| 8 | Ground unit |

```lua
{type = "Aircraft"}
{type = "Ship"}
{type = "Submarine"}
{type = "Facility"}
```

### 4. 态度/立场 (Stance)

设置阵营对另一阵营的态度：

| 代码 | 描述 | 快捷键 |
|------|------|--------|
| H | Hostile（敌对） | H |
| F | Friendly（友好） | F |
| N | Neutral（中立） | N |
| U | Unfriendly（不友好） | U |
| X | Unknown（未知） | X |

```lua
ScenEdit_SetSidePosture("Blue", "Red", "H")  -- Blue 对 Red 敌对
ScenEdit_SetSidePosture("Blue", "Green", "F")  -- Blue 对 Green 友好
```

### 5. 熟练度 (Proficiency)

| 代码 | 描述 |
|------|------|
| 0 | Novice（新手） |
| 1 | Cadet（学员） |
| 2 | Regular（普通） |
| 3 | Veteran（老兵） |
| 4 | Ace（王牌） |

```lua
ScenEdit_SetSideOptions({side="Blue", proficiency="Veteran"})
```

### 6. 感知级别 (Awareness)

| 代码 | 描述 |
|------|------|
| -1 | Blind（盲目） |
| 0 | Normal（正常） |
| 1 | AutoSideID |
| 2 | AutoSideAndUnitID |
| 3 | Omniscient（全知） |

```lua
ScenEdit_SetSideOptions({side="Blue", awareness="Normal"})
```

### 7. 任务类型 (MissionType)

**打击任务 (Strike)**
- `AIR` - 空战
- `LAND` - 对地打击
- `SEA` - 对海打击
- `SUB` - 反潜打击

**巡逻任务 (Patrol)**
- `ASW` - 反潜巡逻
- `NAVAL` - 海上巡逻
- `AAW` - 防空巡逻
- `LAND` - 对地巡逻
- `MIXED` - 混合巡逻
- `SEAD` - 压制防空
- `SEA` - 海上控制

**其他**
- `Support` - 支援
- `Ferry` - 转场
- `Mining` - 布雷
- `Mineclearing` - 扫雷
- `Cargo` - 运输

```lua
ScenEdit_AddMission({side="Blue", name="CAP", type="Strike", subtype="AIR"})
ScenEdit_AddMission({side="Blue", name="ASW Patrol", type="Patrol", subtype="ASW"})
```

### 8. 速度/高度预设 (Presets)

**油门预设**
| 代码 | 描述 |
|------|------|
| 0 | FullStop |
| 1 | Loiter |
| 2 | Cruise |
| 3 | Full |
| 4 | Flank |
| 5 | None |

**深度预设**
| 代码 | 描述 |
|------|------|
| 0 | None |
| 1 | Periscope |
| 2 | Shallow |
| 3 | OverLayer |
| 4 | UnderLayer |
| 5 | MaxDepth |
| 6 | Surface |

**高度预设**
| 代码 | 描述 |
|------|------|
| 0 | None |
| 1 | MinAltitude |
| 2 | Low1000 |
| 3 | Low2000 |
| 4 | Medium12000 |
| 5 | High25000 |
| 6 | High36000 |
| 7 | MaxAltitude |

### 9. 武器控制状态 (WeaponControl)

| 代码 | 描述 |
|------|------|
| 0 | Free（自由开火） |
| 1 | Tight（谨慎开火） |
| 2 | Hold（禁止开火） |

### 10. 作战条令参数 (Doctrine)

详见 `doctrine.md`

### 11. 燃料类型 (Fuel)

| 代码 | 类型 |
|------|------|
| 2001 | AviationFuel（航空燃油） |
| 3001 | DieselFuel（柴油） |
| 3003 | GasFuel（汽油） |

### 12. GUID

全局唯一标识符，32字符，用于精确引用单位。

```lua
local u = ScenEdit_GetUnit({guid="3b28032f-446d-43a1-bc49-4f88f5fb1cc1"})
```

### 13. 航路点类型 (Waypoint)

| 代码 | 类型 |
|------|------|
| 00 | ManualPlottedCourseWaypoint |
| 01 | PatrolStation |
| 02 | TerminalPoint |
| 10 | Target |
| 14 | Refuel |
| 15 | TakeOff |
| 18 | Land |

```lua
course = {
    {latitude=lat, longitude=lon, TypeOf="ManualPlottedCourseWaypoint"},
    {latitude=lat2, longitude=lon2, TypeOf="Target"}
}
```