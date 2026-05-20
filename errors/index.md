---
doc_id: CMO-ERROR-001
title: 报错记录库
description: AI 生成 Lua 代码时常见错误汇总
type: error-handbook
version: 1.1.0
updated: 2026-05-19
---

# 报错记录库 | Error Record

> AI 生成 Lua 代码时常见错误汇总。每次遇到新错误，必须先追加到本文件，再输出修复方案。

---

## 一、Missing 'LoadoutID'

**错误信息：**
```
ScenEdit_AddUnit 0 : Missing 'LoadoutID'
```

**原因：** `ScenEdit_AddUnit` 添加 Aircraft（飞机）时，`LoadoutID` 参数被省略或拼写错误。

**正确写法：**

```lua
-- ❌ 错误（均报错 Missing 'LoadoutID'）：
ScenEdit_AddUnit({side = "Blue", type = "Aircraft", ...})
ScenEdit_AddUnit({side = "Blue", type = "Aircraft", loadoutid = 332})    -- 小写 l/i
ScenEdit_AddUnit({side = "Blue", type = "Aircraft", loadout = "F-16C"})  -- 字符串类型

-- ✅ 正确：
ScenEdit_AddUnit({side = "Blue", type = "Aircraft", dbid = {{DBID}}, LoadoutID = {{LOADOUT_ID}}, ...})
```

**LoadoutID 查询步骤（MCP read_query）：**
```sql
SELECT ID FROM DataAircraftLoadouts WHERE ComponentID = {{DBID}};
```
返回的 `ID` 即为 `LoadoutID`（数值，非字符串）。

---

## 二、The requested object has been deprecated in the database

**错误信息：**
```
ScenEdit_AddUnit 0 : ,The requested object has been deprecated in the database
```

**原因：** DBID 不存在或已被官方弃用（CMO 数据库更新后某些 DBID 失效）。

**解决步骤：**
1. 确认 DBID 是通过 MCP 查询得到的，不是编造的
2. 用 `read_query` 查询 DBID 是否真实存在于数据库：
```sql
SELECT dbid, name FROM platforms WHERE dbid = {{DBID}};
```
3. 如返回空，说明该 DBID 确实不存在，重新通过 MCP 查询正确的 DBID

---

## 三、Invalid latitude/longitude value

**错误信息：**
```
ScenEdit_AddUnit 0 : Invalid latitude value
```

**原因：** 坐标参数名拼写错误或值超出范围（纬度 ±90，经度 ±180）。

**正确写法：**
```lua
-- ✅ 正确（参数名必须完全匹配）：
ScenEdit_AddUnit({latitude = 35.6762, longitude = 139.6503})

-- ❌ 错误（常见拼写错误）：
ScenEdit_AddUnit({lat = 35.6762, lon = 139.6503})      -- 参数名错误
ScenEdit_AddUnit({Latitude = 35.6762, Longitude = 139.6503})  -- 大写也可，但不是标准写法
```

---

## 四、Invalid unit type 'xxx'

**错误信息：**
```
ScenEdit_AddUnit 0 : Invalid unit type 'Air'
```

**原因：** `type` 参数使用了非标准值。

**正确 type 值（严格区分大小写和空格）：**

| 单位类型 | 正确写法 | 错误写法 |
|---------|---------|---------|
| 飞机 | `Aircraft` | `Air`, `Plane` |
| 舰艇 | `Ship` | `Naval`, `boat` |
| 潜艇 | `Submarine` | `sub`, `Sub`, `underwater` |
| 地面单位 | `GROUND UNIT` | `GroundUnit`, `GROUNDUNIT`, `Ground Unit` |
| 设施 | `Facility` | `Ground`, `base` |

```lua
-- ✅ 正确：
ScenEdit_AddUnit({type = "Aircraft", ...})
ScenEdit_AddUnit({type = "Ship", ...})
ScenEdit_AddUnit({type = "Submarine", ...})
ScenEdit_AddUnit({type = "Facility", ...})
ScenEdit_AddUnit({type = "GROUND UNIT", ...})  -- 全大写，空格分隔

-- ❌ 错误（均报 Invalid unit type）：
ScenEdit_AddUnit({type = "Air"})
ScenEdit_AddUnit({type = "GroundUnit"})        -- 不是有效值
ScenEdit_AddUnit({type = "GROUNDUNIT"})        -- 不是有效值
ScenEdit_AddUnit({type = "Ground Unit"})      -- 不是有效值
```

## 五、side 'xxx' does not exist

**错误信息：**
```
ScenEdit_SetUnit ... side 'xxx' does not exist
```

**原因：** 阵营未创建，或名称拼写不一致（CMO 中阵营名区分大小写）。

**解决：**
1. 先创建阵营：`ScenEdit_AddSide({side = "Blue"})`
2. 确认 `side` 参数与创建时完全一致（包括大小写和空格）

---

## 六、No unit found with DBID/Name

**错误信息：**
```
ScenEdit_GetUnit() returned nothing - no unit found
```

**原因：** 查询条件（DBID 或 name）对应的单位不存在。

**解决：** 用 MCP `query_dbid` 重新确认 DBID，或用 `read_query` 验证数据库中存在该单位。

---

## 七、GUID 格式错误

**错误信息：**
```
Invalid GUID format
```

**原因：** GUID 必须是标准 UUID 格式（36 字符，8-4-4-4-12）。

**正确写法：**
```lua
-- ✅ 正确：
ScenEdit_GetUnit({guid = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"})

-- ❌ 错误（常见 AI 编造）：
ScenEdit_GetUnit({guid = "12345"})
ScenEdit_GetUnit({guid = "unit-001"})
```

---

## 八、参数名大小写混用

**常见错误参数名对照表：**

| 正确参数名 | AI 常误写为 |
|-----------|------------|
| `LoadoutID` | `loadoutid`, `loadout_id`, `loadoutID`, `Loadout` |
| `latitude` | `Lat`, `LAT`, `lat` |
| `longitude` | `Lon`, `LON`, `lon` |
| `altitude` | `Alt`, `ALT`, `alt` |
| `guid` | `GUID`, `Guid` |
| `dbid` | `DBID`, `Dbid` |
| `side` | `Side`, `SIDE` |
| `name` | `Name`, `NAME` |
| `type` | `Type`, `TYPE` |

---

## 九、Facility（地面设施）不需要 LoadoutID

**重要例外：** `type = "Facility"`（机场、雷达站等）**不需要** `LoadoutID`，添加时省略此参数即可。

```lua
-- ✅ Facility 正确写法（不需要 LoadoutID）：
ScenEdit_AddUnit({
    side = "Blue",
    type = "Facility",
    dbid = 35,  -- 跑道 DBID
    name = "Runway",
    latitude = 35.6762,
    longitude = 139.6503
})

-- ❌ Aircraft 必须有 LoadoutID：
ScenEdit_AddUnit({
    side = "Blue",
    type = "Aircraft",
    dbid = 3785,
    LoadoutID = 332,
    ...
})
```

---

## 十、altitude 默认单位是米，不是英尺

**常见错误**：
```lua
-- ❌ 误以为默认是英尺，导致飞机高度极低无法起飞
ScenEdit_AddUnit({..., altitude = 500})  -- 实际只有 500 米

-- ✅ 默认米，如果要英尺必须加 FT 后缀
ScenEdit_AddUnit({..., altitude = 5000})     -- 5000 米
ScenEdit_AddUnit({..., altitude = "5000 FT"}) -- 5000 英尺 ≈ 1524 米
```

---

## 十一、loadoutid（小写）与 LoadoutID（大写）

CMO Lua API 中两均可，但 `ScenEdit_AddUnit` 中推荐使用 `LoadoutID`（大写 I）。

```lua
-- ✅ 均可
ScenEdit_AddUnit({..., LoadoutID = 332})    -- 大写（推荐）
ScenEdit_AddUnit({..., loadoutid = 332})    -- 小写（也有效）

-- ❌ 字符串类型会报错
ScenEdit_AddUnit({..., LoadoutID = "332"})  -- 必须是数值
```

---

## 十二、单位不存在导致 nil 后继续调用属性报错

**错误信息**：
```
attempt to index a nil value
```

**原因**：`ScenEdit_GetUnit` 返回 nil 后继续访问 `.name` 等属性。

**正确写法**：
```lua
local unit = ScenEdit_GetUnit({name = "NotExist"})
if unit then
    print(unit.name)  -- 只在 unit 存在时访问
else
    print("单位不存在")
end
```

---

## 十三、ScenEdit_KillUnit vs ScenEdit_DeleteUnit 区别

| 函数 | 是否触发事件 | 适用场景 |
|------|-------------|---------|
| `ScenEdit_KillUnit` | ✅ 触发（Event 系统感知） | 模拟被击毁 |
| `ScenEdit_DeleteUnit` | ❌ 不触发 | 清理测试单位 |

---

## 十四、Type cannot be GROUNDUNIT

**错误信息：**
```
ScenEdit_AddUnit 0 : ,Type cannot be GROUNDUNIT please choose one of the following:
SHIP, SUB, AIRCRAFT, FACILITY, GROUND UNIT, SATELLITE, WEAPON
```

**原因：** `type` 值使用了 `GROUNDUNIT`（无空格）或 `GroundUnit`（小写），而正确值为 **`GROUND UNIT`**（全大写，单词之间有空格）。

**正确写法：**
```lua
-- ✅ 正确（GROUND UNIT = 全大写 + 空格）
ScenEdit_AddUnit({
    side = "Iran",
    type = "GROUND UNIT",
    name = "Coastal Radar",
    dbid = 417,
    lat = "27.22",
    lon = "56.38"
})

-- ❌ 错误（均报 "Type cannot be GROUNDUNIT"）
ScenEdit_AddUnit({type = "GROUNDUNIT"})
ScenEdit_AddUnit({type = "GroundUnit"})
ScenEdit_AddUnit({type = "Ground Unit"})
```

---

## 十五、Attempted to place facility ... This point appears to be underwater

**错误信息：**
```
ScenEdit_AddUnit 0 : ,Attempted to place facility: xxx (Class: Runway (3200m))
at coordinates: Lat: 27.18 - Lon: 56.36 . This point appears to be underwater.
Placement aborted!
```

**原因：** Facility 的 DBID 对应的是只能在陆地上放置的设施类型（如 Runway/Category 2001、Building/Category 3001），而放置坐标在 CMO 地形数据库中被判定为水下。

**Facility Category 放置规则：**

| Category | 类型 | 放置地形 |
|----------|------|---------|
| 2001 | Runway（跑道） | 仅限陆地 |
| 3001 | Building（建筑） | 仅限陆地 |
| 4050 | Water（水中结构） | 可在水中 |
| 6001 | Aerostat（气球雷达） | 陆地 |
| GroundUnit | 移动车辆/雷达车 | 任意地形 |

**解决方案：**

1. **改为 GROUND UNIT 类型**：雷达车等可放置在任意地形
   ```lua
   -- ✅ 正确：GROUND UNIT 可在任何地形放置
   ScenEdit_AddUnit({
       side = "Iran",
       type = "GROUND UNIT",
       name = "Coastal Radar",
       dbid = 417,  -- Radar (SLC-18) 等地面雷达
       lat = "27.22",
       lon = "56.38"
   })
   ```

2. **改为水中可放的 Facility**：选择 Category 4050 的设施（如 Offshore Surveillance Platform）
   ```lua
   -- ✅ 正确：Offshore Surveillance Platform 可在水中放置
   ScenEdit_AddUnit({
       side = "Iran",
       type = "Facility",
       name = "Sea Radar Station",
       dbid = 4115,  -- Structure (Offshore Surveillance Platform)
       lat = "26.92",
       lon = "56.38"
   })
   ```

3. **确保坐标在陆地上**：查阅地图确认放置点确实在陆地

