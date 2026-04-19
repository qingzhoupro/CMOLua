# 事件函数详解

> 参考: CMO_Lua函数_Events.md, Functions.md

## 事件系统概述

CMO 事件系统由三部分组成：
- **Trigger (触发器)**: 事件触发条件
- **Condition (条件)**: 事件执行前置条件
- **Action (动作)**: 事件触发后执行的操作

---

## ScenEdit_SetEvent

创建或更新事件。

```lua
ScenEdit_SetEvent("Event Name", {
    mode = "add",           -- add/remove/update
    IsActive = true,        -- 是否激活
    IsRepeatable = 1,       -- 是否可重复 (1=是, 0=否)
    IsShown = true,        -- 是否显示
    Probability = 100     -- 触发概率 (0-100)
})
```

---

## ScenEdit_SetTrigger

创建或更新触发器。

```lua
ScenEdit_SetTrigger({
    mode = "add",
    description = "Trigger Name",
    type = "Time"  -- 触发器类型
})
```

**触发器类型**:

| 类型 | 说明 | 额外参数 |
|------|------|----------|
| `Time` | 时间触发 | `Time="30"` (分钟) |
| `UnitDestroyed` | 单位被摧毁 | `side`, `TargetType` |
| `UnitDamaged` | 单位受损 | `side`, `TargetType` |
| `UnitDetected` | 检测到单位 | `side`, `TargetType` |
| `EnteredArea` | 进入区域 | `side`, `description` |
| `ExitedArea` | 离开区域 | `side`, `description` |
| `ContactGone` | 接触消失 | `side` |
| `WeaponImpact` | 武器命中 | `side` |
| `MissionComplete` | 任务完成 | `side`, `mission` |
| `MissionFailed` | 任务失败 | `side`, `mission` |

```lua
-- 时间触发器
ScenEdit_SetTrigger({
    mode = "add",
    type = "Time",
    Time = "30"
})

-- 单位被摧毁触发器
ScenEdit_SetTrigger({
    mode = "add",
    type = "UnitDestroyed",
    side = "Blue",
    TargetType = "Air"  -- Air, Surface, Submarine, Facility
})

-- 检测触发器
ScenEdit_SetTrigger({
    mode = "add",
    type = "UnitDetected",
    side = "Blue",
    TargetType = "Submarine"
})
```

---

## ScenEdit_SetCondition

创建或更新条件。

```lua
ScenEdit_SetCondition({
    mode = "add",
    description = "Condition Name",
    type = "LuaScript"  -- 条件类型
})
```

**条件类型**:
- `LuaScript`: Lua 脚本条件
- `TimePeriod`: 时间周期
- `UnitInArea`: 区域内单位
- `ScoreLevel`: 分数等级

```lua
-- Lua 脚本条件
ScenEdit_SetCondition({
    mode = "add",
    type = "LuaScript",
    ScriptText = "return unit.speed > 20"
})
```

---

## ScenEdit_SetAction

创建或更新动作。

```lua
ScenEdit_SetAction({
    mode = "add",
    description = "Action Name",
    type = "LuaScript",
    ScriptText = "print('Action triggered!')"
})
```

**动作类型**:

| 类型 | 说明 |
|------|------|
| `LuaScript` | 执行 Lua 脚本 |
| `SpecialAction` | 执行特殊动作 |
| `MarkUnit` | 标记单位 |
| `Sound` | 播放声音 |
| `AddScore` | 添加分数 |

```lua
-- Lua 脚本动作
ScenEdit_SetAction({
    mode = "add",
    type = "LuaScript",
    ScriptText = [[
local u = ScenEdit_UnitX()
ScenEdit_SpecialMessage("Blue", "事件触发: " .. u.name)
]]
})

-- 添加分数动作
ScenEdit_SetAction({
    mode = "add",
    type = "AddScore",
    score = 100,
    side = "Blue"
})
```

---

## ScenEdit_SetEventTrigger

关联触发器到事件。

```lua
ScenEdit_SetEventTrigger("Event Name", {
    mode = "add",
    name = "Trigger Name"
})
```

---

## ScenEdit_SetEventCondition

关联条件到事件。

```lua
ScenEdit_SetEventCondition("Event Name", {
    mode = "add",
    name = "Condition Name"
})
```

---

## ScenEdit_SetEventAction

关联动作到事件。

```lua
ScenEdit_SetEventAction("Event Name", {
    mode = "add",
    name = "Action Name"
})
```

---

## 事件相关函数

### ScenEdit_EventX

获取触发事件的 Event 对象。

```lua
local event = ScenEdit_EventX()
print(event.name)
print(event.probability)
event.probability = 50  -- 修改触发概率
```

### ScenEdit_UnitX

获取触发事件的单位。

```lua
local unit = ScenEdit_UnitX()
print("触发单位: " .. unit.name)
```

### ScenEdit_UnitC

获取检测到的接触。

```lua
local contact = ScenEdit_UnitC()
print("接触: " .. contact.name)
print("类型: " .. contact.type)
```

### ScenEdit_UnitY

获取特殊事件相关的单位。

```lua
local y = ScenEdit_UnitY()
-- 返回:
-- - 检测事件的检测单元
-- - 损坏事件的伤害源单元
print("相关单位: " .. y.unit.name)
print("传感器: " .. y.sensor[1].name)
```

---

## 特殊动作 (Special Action)

### ScenEdit_AddSpecialAction

添加特殊动作。

```lua
local LfCR = '\r\n'
local script = 
    '-- 显示选中单位信息' .. LfCR ..
    'local u = ScenEdit_UnitX()' .. LfCR ..
    'if u then' .. LfCR ..
    '    print(u.name)' .. LfCR ..
    'end'

ScenEdit_AddSpecialAction({
    Side = "Blue",
    ActionNameOrID = "show_info",
    description = "显示单位信息",
    IsActive = true,
    IsRepeatable = true,
    ScriptText = script
})
```

### ScenEdit_ExecuteSpecialAction

执行特殊动作。

```lua
ScenEdit_ExecuteSpecialAction("show_info")
```

### ScenEdit_GetSpecialAction

获取特殊动作信息。

```lua
local sa = ScenEdit_GetSpecialAction({
    side = "Blue",
    ActionNameOrID = "show_info"
})

-- 列出所有特殊动作
local all = ScenEdit_GetSpecialAction({
    side = "Blue",
    mode = "list"
})
```

---

## 完整事件示例

```lua
-- 创建事件
ScenEdit_SetEvent("单位损失告警", {mode="add", IsRepeatable=1})

-- 创建触发器
ScenEdit_SetTrigger({
    mode = "add",
    type = "UnitDestroyed",
    side = "Blue"
})

-- 创建动作
ScenEdit_SetAction({
    mode = "add",
    type = "LuaScript",
    ScriptText = [[
local unit = ScenEdit_UnitX()
local score = ScenEdit_GetScore(unit.side)
ScenEdit_SpecialMessage(unit.side, 
    "单位损失: " .. unit.name)
]]
})

-- 关联
ScenEdit_SetEventTrigger("单位损失告警", {mode="add", type="UnitDestroyed"})
ScenEdit_SetEventAction("单位损失告警", {mode="add", type="LuaScript"})
```