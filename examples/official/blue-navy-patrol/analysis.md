# 代码解析：蓝方海军巡逻

## 1. 阵营创建

```lua
ScenEdit_AddSide({name="Blue", posture="H"})
ScenEdit_SetSideOptions({side="Blue", awareness="Normal", proficiency="Regular"})
```

- `ScenEdit_AddSide()`: 创建阵营，`posture="H"` 表示初始设为敌对
- `ScenEdit_SetSideOptions()`: 设置阵营选项
  - `awareness`: 感知级别（Normal=正常）
  - `proficiency`: 熟练度（Regular=普通）

## 2. 态度设置

```lua
ScenEdit_SetSidePosture("Blue", "Red", "H")
```

设置 Blue 对 Red 的态度为 Hostile（敌对）。

## 3. 单位创建

```lua
ScenEdit_AddUnit({
    side="Blue",
    type="Ship",
    name="USS Arleigh Burke",
    dbid=2278,
    latitude="35.0",
    longitude="129.1"
})
```

关键参数：
- `side`: 所属阵营
- `type`: 单位类型（Ship/Aircraft/Submarine/Facility）
- `name`: 单位名称（需唯一）
- `dbid`: 装备数据库 ID
- `latitude/longitude`: 位置

## 4. 任务创建

```lua
ScenEdit_AddMission({
    side="Blue",
    name="Sea Patrol",
    type="Patrol",
    subtype="NAVAL"
})
```

巡逻任务子类型：
- `NAVAL`: 海上巡逻
- `ASW`: 反潜巡逻
- `AAW`: 防空巡逻

## 5. 分配单位到任务

```lua
ScenEdit_AssignUnitToMission("USS Arleigh Burke", "Sea Patrol")
```

将单位分配到指定任务。

## DBID 参考

| 装备 | DBID |
|------|------|
| Arleigh Burke (DDG-51) | 2278 |
| FFG-7 Oliver Hazard Perry | 1769 |
| 巡逻艇 (PB-90) | 601 |