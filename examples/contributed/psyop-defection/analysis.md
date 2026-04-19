# 心理战案例 - 代码解析

## 核心函数解析

### 1. VP_GetSide()
```lua
VP_GetSide({Side = "{{SIDE}}"})
```
- 返回阵营所有单元列表
- 注意：`VP_GetSide` 和 `ScenEdit_GetSide` 不同，前者返回单元列表

### 2. string.match()
```lua
string.match(unit.name, "{{KEYWORD}}")
```
- 模糊匹配单位名称
- 只要名称中包含关键词即匹配
- 支持正则表达式

### 3. math.random()
```lua
math.random(#targetUnits)
```
- 随机返回 1 ~ 列表长度的整数
- 实现心理战"随机叛变"的不确定性效果

### 4. ScenEdit_SetUnitSide()
```lua
ScenEdit_SetUnitSide({
    side = "{{ENEMY_SIDE}}",
    guid = targetUnits[k].guid,
    newside = "{{NEW_SIDE}}"
})
```
- 改变单位阵营
- 通过 GUID 精确定位单位

## 心理战设计原理

1. **不确定性**：使用 `math.random()` 模拟战场心理战的不确定性
2. **针对性**：`string.match()` 精准定位特定部队
3. **渐进性**：分批劝降，逐步瓦解敌军士气
