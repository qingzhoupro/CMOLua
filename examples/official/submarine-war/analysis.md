# 潜艇战案例 - 代码解析

## 1. 潜艇添加

```lua
local sub1 = ScenEdit_AddUnit({
    side="Red",
    type="Submarine",
    name="Kilo-1",
    dbid=2221,
    latitude="34.0",
    longitude="142.0",
    manualAltitude=50  -- 50米深度
})
```

关键参数：
- `type="Submarine"` - 单位类型
- `dbid` - 潜艇数据库 ID
- `manualAltitude` - 潜航深度（米），正数表示下潜

## 2. 电磁管控设置

```lua
ScenEdit_SetEMCON("Unit", "USS Arleigh Burke", "Radar=Active;Sonar=Passive")
```

EMCON 格式说明：
- `Radar=Active/Passive` - 雷达状态
- `Sonar=Active/Passive` - 声纳状态
- `OECM=Active/Passive` - 电子对抗
- `Inherit` - 继承上级设置

## 3. 反潜巡逻任务

```lua
ScenEdit_AddMission({
    side="Blue",
    name="ASW - 反潜巡逻",
    type="Patrol",
    subtype="ASW"
})
```

- `subtype="ASW"` - 反潜巡逻类型

## 4. 事件系统

```lua
ScenEdit_SetEvent("潜艇检测事件", {mode="add", IsRepeatable=1})

ScenEdit_SetTrigger({
    mode="add",
    type="UnitDetected",
    side="Blue",
    TargetType="Submarine"
})
```

- `type="UnitDetected"` - 单元检测触发器
- `TargetType="Submarine"` - 只检测潜艇

## 5. 获取事件信息

```lua
local contact = ScenEdit_UnitC()  -- 获取接触
local detector = ScenEdit_UnitX()  -- 获取检测单位
local damageSource = ScenEdit_UnitY()  -- 获取伤害源
```

- `UnitC()` - 检测到的接触
- `UnitX()` - 触发事件的单位
- `UnitY()` - 检测到的单位