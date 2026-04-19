# 作战条令详解

> 参考: Functions.md - ScenEdit_SetDoctrine

## ScenEdit_SetDoctrine

设置作战条令。

```lua
ScenEdit_SetDoctrine({
    side = "Blue"                  -- 阵营（必填）
    unitname = "F-16 #1"           -- 单位名称（可选）
    mission = "CAP Mission"        -- 任务名称（可选）
}, {
    -- 条令参数
})
```

**优先级**（从高到低）：
1. Unit/GROUP 级别
2. Mission 级别
3. Side 级别

---

## 常用条令参数

### 核武器使用

```lua
ScenEdit_SetDoctrine({side = "Blue"}, {
    use_nuclear_weapons = "no"    -- "yes", "no", "only"
})
```

| 值 | 说明 |
|----|------|
| `no` | 禁止使用核武器 |
| `yes` | 允许使用核武器 |
| `only` | 仅使用核武器 |

---

### 攻击决策

```lua
ScenEdit_SetDoctrine({side = "Blue"}, {
    engage_ambiguous_targets = "optimistic",  -- 攻击模糊目标
    engage_non_hostile_targets = "no"          -- 攻击非敌对目标
})
```

**engage_ambiguous_targets**:
| 值 | 说明 |
|----|------|
| `optimistic` | 乐观（当作敌对攻击） |
| `pessimistic` | 悲观（不攻击） |
| `ignore` | 忽略 |

**engage_non_hostile_targets**:
| 值 | 说明 |
|----|------|
| `yes` | 攻击 |
| `no` | 不攻击 |

---

### 燃油管理

```lua
ScenEdit_SetDoctrine({
    side = "Blue",
    mission = "Strike Mission"
}, {
    fuel_joker = 70,   -- Joker 燃油百分比
    fuel_bingo = 30    -- Bingo 燃油百分比
})
```

| 参数 | 说明 |
|------|------|
| `fuel_joker` | 留空告警百分比 |
| `fuel_bingo` | 紧急返航百分比 |

---

### 武器消耗

```lua
ScenEdit_SetDoctrine({
    side = "Blue",
    mission = "Strike Mission"
}, {
    weapon_state = "winchester"
})
```

| 值 | 说明 |
|----|------|
| `winchester` | 消耗完武器后返航 |
| `shotgun25` | 消耗 25% 后返航 |
| `shotgun50` | 消耗 50% 后返航 |

---

### 雷达/声纳使用

```lua
ScenEdit_SetDoctrine({side = "Blue"}, {
    radar_always_active_for_weapons = "yes",
    sonar_always_active_for_weapons = "no"
})
```

---

### 加油配置

```lua
ScenEdit_SetDoctrine({side = "Blue"}, {
    refuel_unplanned = "yes",      -- 允许非计划加油
    refuel_prefer_tankers = "yes"  -- 优先使用加油机
})
```

---

### 武器控制状态

```lua
ScenEdit_SetDoctrine({side = "Blue"}, {
    weapon_control = "Free"       -- "Free", "Tight", "Hold"
})
```

| 值 | 说明 |
|----|------|
| `Free` | 自由开火 |
| `Tight` | 谨慎开火 |
| `Hold` | 禁止开火 |

---

## 完整示例

```lua
-- 侧级条令
ScenEdit_SetDoctrine({side = "Blue"}, {
    use_nuclear_weapons = "no",
    engage_ambiguous_targets = "optimistic",
    engage_non_hostile_targets = "no",
    weapon_control = "Free"
})

-- 打击任务条令
ScenEdit_SetDoctrine({
    side = "Blue",
    mission = "Strike Mission"
}, {
    fuel_joker = 70,
    fuel_bingo = 30,
    weapon_state = "winchester",
    radar_always_active_for_weapons = "yes"
})

-- 防空巡逻条令
ScenEdit_SetDoctrine({
    side = "Blue",
    mission = "AAW Patrol"
}, {
    fuel_joker = 60,
    weapon_state = "shotgun50",
    weapon_control = "Tight"
})
```

---

## 获取当前条令

```lua
local doctrine = ScenEdit_GetDoctrine({side = "Blue"})
print(doctrine.use_nuclear_weapons)
print(doctrine.fuel_joker)
```