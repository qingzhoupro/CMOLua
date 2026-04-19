# 合成作战案例 - 代码解析

## 1. 多兵种单位添加

```lua
-- 海军舰艇
ScenEdit_AddUnit({
    side="Blue",
    type="Ship",
    name="USS Wasp",
    dbid=3562,
    latitude="35.0",
    longitude="140.0"
})

-- 舰载机
ScenEdit_AddUnit({
    type="Aircraft",
    side="Blue",
    name="AV-8B #1",
    dbid=3518,
    loadoutid=0,
    base="USS Wasp"  -- 部署到舰艇
})

-- 地面单位（Facility 类型）
local apc = ScenEdit_AddUnit({
    side="Blue",
    type="Facility",
    name="APC #1",
    dbid=754,
    latitude="35.0",
    longitude="140.0"
})
apc.group = "Landing Force"
```

关键点：
- `type="Facility"` 用于地面单位（车辆、步兵）
- `base` 参数用于舰载机部署到舰艇

## 2. 多任务配合

```lua
-- 压制射击任务
ScenEdit_AddMission({
    side="Blue",
    name="Naval Strike - 压制射击",
    type="Strike",
    subtype="LAND"
})

-- 近距离支援任务
ScenEdit_AddMission({
    side="Blue",
    name="CAS - 支援",
    type="Strike",
    subtype="LAND"
})

-- 分配不同飞机到不同任务
ScenEdit_AssignUnitToMission("F-35B #1", "Naval Strike - 压制射击")
ScenEdit_AssignUnitToMission("AV-8B #1", "CAS - 支援")
```

## 3. 事件系统 - 单位损失追踪

```lua
ScenEdit_SetEvent("单位损失报告", {mode="add", IsRepeatable=1})

ScenEdit_SetTrigger({
    mode="add",
    type="UnitDestroyed",
    name="蓝方损失",
    side="Blue"  -- 只追踪蓝方
})

ScenEdit_SetAction({
    mode="add",
    type="LuaScript",
    name="损失日志",
    ScriptText=[[
local unit = ScenEdit_UnitX()  -- 被摧毁的单位
local score = ScenEdit_GetScore(side)
ScenEdit_SpecialMessage(side, "单位损失: " .. unit.name)
]]
})
```

## 4. 综合协调

本案例展示了三层协调：
1. **海军**：水面舰艇提供火力支援
2. **空军**：固定翼和旋转翼飞机提供空中支援
3. **陆军**：登陆部队执行地面任务