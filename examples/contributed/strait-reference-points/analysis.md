# 海峡参考点案例 - 代码解析

## 参考点数量

每个海峡 4 个点（构成矩形区域），共 9 个海峡：
- 9 × 4 = **36 个参考点**

## 坐标系说明

- 经纬度使用十进制格式（正数 = 北纬/东经）
- 可直接传入 `ScenEdit_AddReferencePoint`

## 实用建议

1. **按需选择**：不一定需要全部9个海峡，选择战略相关的即可
2. **命名规范**：采用 `海峡名-数字` 格式，便于关联任务 zone
3. **巡逻任务关联**：

```lua
-- 创建巡逻任务并关联海峡区域
ScenEdit_AddMission({
    side = "Blue",
    name = "宫古海峡巡逻",
    type = "Patrol",
    subtype = "NAVAL"
})

ScenEdit_SetMission("Blue", "宫古海峡巡逻", {
    zone = {"宫古海峡-1", "宫古海峡-2", "宫古海峡-3", "宫古海峡-4"}
})
```

## 布雷封锁应用

```lua
-- 在海峡布雷
-- ⚠️ DBID 需通过 query_dbid("水雷") 查询
local result = ScenEdit_AddMinefield({
    side = "{{SIDE}}",
    dbid = {{MINE_DBID}},  -- 水雷 DBID（通过 MCP 查询）
    number = 50,
    delay = 60000,
    area = {"{{STRAIT_NAME}}-1", "{{STRAIT_NAME}}-2", "{{STRAIT_NAME}}-3", "{{STRAIT_NAME}}-4"}
})
print("布雷数量: " .. result)
```
