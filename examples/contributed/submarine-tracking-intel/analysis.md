# 潜艇追踪与情报系统 - 代码解析

## World_GetCircleFromPoint 原理

`World_GetCircleFromPoint` 在指定点周围生成一组等距分布的圆周点：

```lua
local circle = World_GetCircleFromPoint({
    latitude = lat,
    longitude = lon,
    radius = 100  -- 百分比，0-100
})
-- 返回一个数组，索引 1-45
```

原始代码取 `circle[1], circle[11], circle[22], circle[33], circle[44]` 作为巡逻区四角的逻辑：约每隔 1/4 圆周取一点（因为 45/4 ≈ 11）。

## KeyValue 跨脚本通信

`ScenEdit_SetKeyValue` / `ScenEdit_GetKeyValue` 提供了跨脚本、跨事件的全局数据共享机制：
- 参考点的 GUID 也可以存入 KeyValue
- 不同事件、不同脚本可通过相同的 key 读取数据
- 适用于复杂想定中的多模块协作

## 阵营关系与情报共享

| 关系 | 情报共享 |
|------|---------|
| `F` (Friendly) | 完全共享，Link-16 可用 |
| `N` (Neutral) | 不共享，隔离 |
| `H` (Hostile) | 敌对，无共享 |

LINK-16 效果依赖阵营关系的动态切换。

## 追踪加分设计原理

```
定期事件（每 1 分钟触发）
    │
    ▼
扫描接触列表
    │
    ▼
找到目标潜艇？
  是 → time_r += 1
  否 → time_r = 0
    │
    ▼
time_r > 60?
  是 → 加 50 分，重置 time_r
    │
    ▼
总分 >= 100?
  是 → 结束想定
```

## Special Action 用途

Special Action 用于手动触发的自定义动作，适合：
- 人工决策场景（如上浮决策）
- 需要玩家主动触发的效果
- UI 驱动的操作

配合事件系统可实现持续监测。
