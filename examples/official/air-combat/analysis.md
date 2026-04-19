# 空战拦截案例 - 代码解析

## 1. 阵营创建

```lua
ScenEdit_AddSide({name="Blue", posture="H"})
```

- `posture="H"` 表示初始态度为 Hostile（敌对）
- 需要双向设置敌对关系

## 2. 空军基地结构

```lua
local runway = ScenEdit_AddUnit({
    type="Facility",
    side="Blue",
    name="Osan AB - Runway",
    dbid=35,
    latitude="37.5",
    longitude="127.0",
    autodetectable=true
})
runway.group = "Osan AB"
```

关键点：
- `autodetectable=true` 表示跑道可被探测
- `group` 属性将设施分组
- 基地设施用于飞机部署

## 3. 飞机部署

```lua
for i = 1, 8 do
    ScenEdit_AddUnit({
        type="Aircraft",
        side="Blue",
        name="F-16C #" .. i,
        dbid=3785,
        loadoutid=332,
        base="Osan AB"
    })
end
```

关键参数：
- `type`: 必须是 "Aircraft" 或 "Air"
- `dbid`: 飞机数据库 ID（从 MCP 查询）
- `loadoutid`: 挂载配置 ID
- `base`: 指定基地名称

## 4. CAP 任务创建

```lua
ScenEdit_AddMission({
    side="Blue",
    name="CAP - 空中截击",
    type="Strike",
    subtype="AIR"
})
ScenEdit_SetMission("Blue", "CAP - 空中截击", {
    zone={"CAP-1", "CAP-2", "CAP-3", "CAP-4"},
    patrolType="FighterCAP"
})
```

- `type="Strike"`, `subtype="AIR"` = 空中截击
- `zone` 使用参考点定义巡逻区域

## 5. 作战条令设置

```lua
ScenEdit_SetDoctrine({side="Blue"}, {
    engage_non_hostile_targets="no",
    fuel_joker=70
})
```

常用条令：
- `engage_non_hostile_targets`: "yes"/"no"
- `fuel_joker`: 百分比（留空告警）
- `weapon_state`: "winchester"（消耗完返航）