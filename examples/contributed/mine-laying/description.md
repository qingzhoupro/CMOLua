# 布雷封锁任务

## 场景描述

使用 `ScenEdit_AddMinefield()` 在指定区域布雷，可配合海峡参考点实现封锁效果。

## 适用场景

- 港口封锁布雷
- 海峡封锁布雷
- 区域拒止（A2AD）
- 水雷战演练

## 前置条件

- 参考点区域已创建（4个点）
- 布雷方阵营存在
- 布雷方拥有布雷装备（如布雷机、布雷艇）

## ⚠️ DBID 查询

布雷前需查询实际水雷 DBID：
```
使用 MCP query_dbid 查询，例如：
- query_dbid("水雷") 或 query_dbid("mine")
- query_dbid("沉底水雷")
- query_dbid("锚雷")
```

## 核心函数

```lua
ScenEdit_AddMinefield({
    side = "{{SIDE}}",
    dbid = {{MINE_DBID}},       -- 水雷 DBID（通过 MCP 查询）
    number = {{NUM}},           -- 布雷数量
    delay = {{DELAY}},           -- 布雷延迟（毫秒）
    area = {"RP1", "RP2", "RP3", "RP4"}  -- 参考点名称
})
```

---

> 📢 更多 CMO Lua 编程案例见公众号 **海空兵棋与AI**，配套想定已分享至知识星球**兵推圈**。
