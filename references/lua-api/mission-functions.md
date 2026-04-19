# 任务函数详解

> 参考: CMO_Lua函数_Mission.md, Functions.md

## ScenEdit_AddMission

创建新任务。

```lua
ScenEdit_AddMission(
    "{{SIDE}}",           -- 阵营名称
    "{{MISSION_NAME}}",   -- 任务名称
    "{{MISSION_TYPE}}",   -- 任务类型
    {}                    -- 任务选项
)
```

**任务类型 (MissionType)**:
- `Strike` - 打击任务
- `Patrol` - 巡逻任务
- `Support` - 支援任务
- `Ferry` - 转场任务
- `Mining` - 布雷任务
- `Mineclearing` - 扫雷任务
- `Cargo` - 运输任务

**巡逻子类型 (Patrol Subtype)**:
- `ASW` - 反潜巡逻
- `NAVAL` - 海上巡逻
- `AAW` - 防空巡逻
- `LAND` - 对地巡逻
- `MIXED` - 混合巡逻
- `SEAD` - 压制防空
- `SEA` - 海上控制

**打击子类型 (Strike Subtype)**:
- `AIR` - 空战
- `LAND` - 对地打击
- `SEA` - 对海打击
- `SUB` - 反潜打击

```lua
-- 示例：创建 CAP 任务
ScenEdit_AddMission("Blue", "CAP Mission", "Strike", {
    type = "AIR"
})

-- 示例：创建 ASW 巡逻
ScenEdit_AddMission("Blue", "ASW Patrol", "Patrol", {
    type = "ASW",
    zone = {"RP-1", "RP-2", "RP-3", "RP-4"}
})

-- 示例：创建布雷任务
ScenEdit_AddMission("Blue", "Mining Operation", "Mining", {
    type = "NAVAL",
    zone = {"Mine-1", "Mine-2"}
})
```

---

## ScenEdit_GetMission

获取任务信息。

```lua
local mission = ScenEdit_GetMission({
    side = "Blue",
    name = "CAP Mission"
})

-- 或通过 GUID
local mission = ScenEdit_GetMission({
    guid = "mission-guid"
})
```

**返回值**:
```lua
mission = {
    name = "CAP Mission",
    side = "Blue",
    guid = "...",
    type = "Strike",
    subtype = "AIR",
    isactive = true,
    unitlist = {"guid1", "guid2"},  -- 分配的单元 GUID
    patrolzone = {"RP-1", "RP-2"}
}
```

---

## ScenEdit_SetMission

设置任务属性。

```lua
ScenEdit_SetMission("Blue", "CAP Mission", {
    patrolzone = {"RP-1", "RP-2", "RP-3", "RP-4"},
    patrolType = "FighterCAP",
    onethirdrule = false,
    attackee = "Red"
})
```

**常用属性**:
- `patrolzone`: 巡逻区域参考点列表
- `patrolType`: "FighterCAP", "AreaCAP", "TargetPatrol"
- `onethirdrule`: 是否使用三分之一规则
- `attackee`: 目标阵营（打击任务）
- `flightSize`: 飞行编队大小

---

## ScenEdit_DeleteMission

删除任务。

```lua
ScenEdit_DeleteMission({
    side = "Blue",
    name = "Old Mission"
})
```

---

## ScenEdit_AssignUnitToMission

分配单位到任务。

```lua
-- 分配单个单元
ScenEdit_AssignUnitToMission("F-16 #1", "CAP Mission")

-- 指定任务类型
ScenEdit_AssignUnitToMission("F-16 #1", {
    missionName = "Strike Mission",
    missionType = "Strike"
})
```

---

## ScenEdit_RemoveUnitAsTarget

移除目标单位。

```lua
ScenEdit_RemoveUnitAsTarget({
    mission = "Strike Mission",
    unitname = "Target #1"
})
```

---

## ScenEdit_AssignUnitAsTarget

分配目标单位。

```lua
ScenEdit_AssignUnitAsTarget({
    mission = "Strike Mission",
    unitname = "Enemy Base"
})
```

---

## ScenEdit_GetMissions

获取所有任务。

```lua
local missions = ScenEdit_GetMissions()
for i, m in ipairs(missions) do
    print(m.name .. " - " .. m.type)
end
```

---

## ScenEdit_CreateMissionFlightPlan

创建任务飞行计划。

```lua
ScenEdit_CreateMissionFlightPlan({
    side = "Blue",
    mission = "Strike Mission",
    flightplan = {
        {latitude = 35.0, longitude = 127.0, TypeOf = "TakeOff"},
        {latitude = 36.0, longitude = 128.0, TypeOf = "IP"},
        {latitude = 37.0, longitude = 129.0, TypeOf = "Target"},
        {latitude = 36.0, longitude = 128.0, TypeOf = "Egress"},
        {latitude = 35.0, longitude = 127.0, TypeOf = "Land"}
    }
})
```

---

## ScenEdit_ExportMission

导出任务。

```lua
local xml = ScenEdit_ExportMission({
    side = "Blue",
    name = "CAP Mission"
})
```

---

## ScenEdit_ImportMission

导入任务。

```lua
ScenEdit_ImportMission({
    side = "Blue",
    xml = missionXML
})
```

---

## 任务包 (Task Pool)

### 创建任务包

```lua
-- 创建打击池
ScenEdit_AddMission("Blue", "Strike Pool", "Strike", {
    category = "taskpool",
    type = "LAND",
    pool = "strike pool"
})
```

### 创建包

```lua
-- 在打击池下创建包
ScenEdit_AddMission("Blue", "Package 1", "Strike", {
    category = "package",
    type = "LAND",
    pool = "strike pool"
})
```

### 护航任务

```lua
-- 创建护航任务
ScenEdit_AddMission("Blue", "Escort CAP", "Strike", {
    type = "AIR",
    escort = true,
    package = "Package 1"  -- 关联到包
})
```