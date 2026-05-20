---
doc_id: CMO-SKILL-UNIT-001
title: Unit 操作技能
description: ScenEdit_AddUnit 的正确用法，支持场景上下文感知
references:
  - references/lua-api/Functions.md
  - references/lua-api/CMO_Lua函数_Unit.md
---

# Unit 操作技能

> **重要：所有 API 用法必须以官方文档为准，不得编造函数名或参数格式。**
>
> 官方参考: `Functions.md` → `ScenEdit_AddUnit`

## 空白场景须知

**重要：在空白场景中添加单元前，必须先创建阵营。**

直接调用 `ScenEdit_AddUnit({ side = "Red", ... })` 会报错：`Side 'Red' doesn't exist`

正确顺序：
1. `ScenEdit_AddSide({side="Red"})` — 创建阵营（官方 API）
2. `ScenEdit_SetSidePosture("Red","Blue","H")` — 设置敌对关系（官方 API）
3. `ScenEdit_AddUnit()` — 添加单元

---

## 场景上下文检测

**重要：在生成单元操作代码前，先了解当前场景中已有的单元。**

### 检测逻辑

1. 检查 `memory/skill/scenario-context.md` 是否有内容
2. 有内容时：从上下文读取已有单元名称，避免创建重名单元
3. 无内容时：询问用户场景状态，或引导用户执行 scene-scout.lua

### 场景侦察脚本

当需要获取场景信息时，让用户执行：

```lua
print("=== CMO 场景侦察报告 ===")
print("场景名称: " .. GetScenarioTitle())
print("")
local sides = VP_GetSides()
if not sides or #sides == 0 then
    print("【空白场景】未检测到任何阵营")
    print("=== 侦察完成 ===")
    return
end
print("【阵营列表】")
for i, side in ipairs(sides) do
    local isHuman = ScenEdit_GetSideIsHuman(side.name)
    print("  " .. i .. ". " .. side.name .. " (人类控制: " .. tostring(isHuman) .. ")")
end
print("")
for _, side in ipairs(sides) do
    print("【单元 - " .. side.name .. "】")
    local sideObj = VP_GetSide({side=side.name})
    local unitCount = 0
    if sideObj and sideObj.units then
        for _, u in ipairs(sideObj.units) do
            unitCount = unitCount + 1
            print("  - 名称: " .. u.name)
            print("    类型: " .. u.type .. " | DBID: " .. (u.dbid or "N/A"))
            print("    GUID: " .. u.guid)
            print("    位置: " .. u.latitude .. ", " .. u.longitude)
        end
    end
    if unitCount == 0 then print("  (无单元)") end
end
print("")
print("=== 侦察完成 ===")
```

---

## Step 0.5: 经验教训查询（按需）

根据 unit type 加载对应教训，避免重复犯错。

### 查询逻辑

1. 识别用户需求的 unit type
2. 从 `memory/cold/lesson-index.md` 匹配教训 ID
3. 从 `memory/cold/lesson-root-causes.md` 只加载相关教训（约 3-5 行）
4. 注入到 `memory/hot/session.md` 的「本次防错提醒」区

### Unit Type → 教训映射

| Unit Type | 需加载的教训 ID |
|-----------|----------------|
| Aircraft | LOADOUTID, ALTITUDE-UNIT, DEPRECATED-DBID |
| Ship | DEPRECATED-DBID |
| Submarine | DEPRECATED-DBID |
| GROUND UNIT | GROUND-UNIT-TYPE, FACILITY-TERRAIN |
| Facility | FACILITY-TERRAIN |

### 输出到 hot/session.md

```markdown
## 本次防错提醒

<!-- 根据 unit type 注入教训要点 -->
```

---

## 函数签名

```lua
ScenEdit_AddUnit({
  side = "Blue",
  type = "Aircraft",
  name = "F-16C #1",
  dbid = 1719,
  LoadoutID = 2230,
  latitude = 35.6762,
  longitude = 139.6503,
  altitude = 9144,
  heading = 0,
  speed = 500
})
```

---

## type 有效值

| 值 | 说明 | 错误示例 |
|---|------|---------|
| `Aircraft` | 飞机 | `Air`, `Plane` |
| `Ship` | 舰艇 | `Naval`, `boat` |
| `Submarine` | 潜艇 | `Sub`, `underwater` |
| `Facility` | 设施（机场、跑道、平台） | `Base`, `Ground` |
| `GROUND UNIT` | 地面单位（雷达车、车辆等） | `GroundUnit`, `Ground Unit`, `GROUNDUNIT` |

> **注意：** `type` 值**严格区分大小写和空格**。`GroundUnit`、`GROUNDUNIT`、`Ground Unit` 均报错，正确值为 **`GROUND UNIT`**（全大写，单词间有空格）。

---

## 常见错误

### Missing LoadoutID

```lua
-- 错误
ScenEdit_AddUnit({type = "Aircraft", dbid = 1719})

-- 正确
ScenEdit_AddUnit({type = "Aircraft", dbid = 1719, LoadoutID = 2230})
```

### Invalid unit type

```lua
-- 错误：GroundUnit 不是有效值
ScenEdit_AddUnit({type = "GroundUnit"})

-- 正确：GROUND UNIT（全大写，空格分隔）
ScenEdit_AddUnit({type = "GROUND UNIT"})
```

### Invalid latitude/longitude

```lua
-- 错误
ScenEdit_AddUnit({lat = 35, lon = 139})

-- 正确
ScenEdit_AddUnit({latitude = 35.0, longitude = 139.0})
```

### Facility 放置地形限制

```lua
-- 错误：Runway (DBID 35, Category 2001) 只能在陆地上放置
--       如果坐标被 CMO 判定为水下，会报错：
--       "Attempted to place facility: ... This point appears to be underwater"
ScenEdit_AddUnit({
    type = "Facility",
    dbid = 35,       -- Runway (3200m)
    name = "Base",
    lat = "27.18",  -- 如果这个坐标在水中则报错
    lon = "56.36"
})

-- 正确方案 1：改用 GROUND UNIT（可在任意地形放置）
ScenEdit_AddUnit({
    type = "GROUND UNIT",  -- 全大写+空格！
    dbid = 417,            -- Radar (SLC-18)
    name = "Radar",
    lat = "27.22",
    lon = "56.38"
})

-- 正确方案 2：改用 Category 4050 的水中可放设施
ScenEdit_AddUnit({
    type = "Facility",
    dbid = 4115,  -- Structure (Offshore Surveillance Platform)
    name = "Sea Station",
    lat = "26.92",
    lon = "56.38"
})
```

---

## 上下文感知的代码生成示例

### 场景中已有 Blue 阵营和一个 F-16 单元

在现有单元基础上扩展，名称避免重复：

```lua
ScenEdit_AddUnit({
  side = "Blue",
  type = "Aircraft",
  name = "F-16C #2",
  dbid = 1719,
  LoadoutID = 2230,
  latitude = 35.6762,
  longitude = 139.6503,
  altitude = 9144,
  heading = 90,
  speed = 500
})
```

### 为已有舰艇编队添加护卫舰

```lua
ScenEdit_AddUnit({
  side = "Blue",
  type = "Ship",
  name = "DDG-51 Arleigh Burke #1",
  dbid = 2083,
  latitude = 22.0,
  longitude = 62.0,
  heading = 180,
  speed = 20
})
```

---

## API 正确语法参考（防编造检查表）

| 功能 | 错误写法 | 正确写法 |
|------|---------|---------|
| 创建阵营 | `ScenEdit_AddSide({name="R", orientation="H"})` | `ScenEdit_AddSide({side="Red"})` |
| 设置关系 | `ScenEdit_SetSideRelations({...})` | `ScenEdit_SetSidePosture("Red","Blue","H")` |
| 场景标题 | `ScenEdit_GetScenario().name` | `GetScenarioTitle()` |
| 阵营列表 | `ScenEdit_GetSides()` | `VP_GetSides()` |
| 阵营单元 | `ScenEdit_GetUnits({side=...})` | `VP_GetSide({side="xxx"}).units` |
| 任务列表 | `ScenEdit_GetMissions()` | `ScenEdit_GetMissions("阵营名")` |
| 参考点 | `ScenEdit_ReferencePoints(side)` | `ScenEdit_GetReferencePoints({side="xxx"})` |
| 地面单位 | `type = "GroundUnit"` | `type = "GROUND UNIT"` |
