# 潜艇追踪与情报系统

## 场景描述

模拟 SSBN（弹道导弹核潜艇）的创建、追踪、加分机制，以及跨阵营情报传递链路：
1. 随机生成 SSBN 巡逻区
2. 持续追踪目标并计分
3. LINK-16 / 卫星数据链（特殊动作触发）
4. 跨阵营传递位置情报

> 本案例源自公众号对德尔塔 IV 级弹道导弹核潜艇（SSBN）的战术分析。该艇配备 VM-4 压水反应堆，轮机舱采用独立隔音设计，全艇安装消声器，可在水下持续值班。配合 CMO 事件系统，可模拟反潜巡逻队对 SSBN 的持续跟踪，以及 LINK-16 数据链的上浮建立与下潜断开。

## 适用场景

- 反潜作战（ASW）
- 战略核潜艇追踪演练
- 情报系统仿真
- 跨阵营通信模拟

## 前置条件

- 需要 MCP 查询潜艇 DBID
- 部分功能需要已知单位 GUID

## DBID 查询

```lua
-- 使用 MCP query_dbid 查询
query_dbid("潜艇") 或 query_dbid("submarine")
query_dbid("核潜艇")
query_dbid("SSBN")
query_dbid("德尔塔级")
```

## 核心 API

| 函数 | 说明 |
|------|------|
| `World_GetCircleFromPoint({...})` | 在某点周围生成圆形随机点 |
| `ScenEdit_AddReferencePoint({...})` | 创建参考点 |
| `ScenEdit_SetKeyValue(k, v)` | 存储键值对（跨脚本共享） |
| `ScenEdit_GetKeyValue(k)` | 读取键值 |
| `ScenEdit_GetContacts("Side")` | 获取接触列表 |
| `ScenEdit_SetSidePosture(A, B, rel)` | 设置阵营关系 |
| `ScenEdit_SetSpecialAction(...)` | 设置特殊动作 |
| `ScenEdit_GetScore()` / `ScenEdit_SetScore()` | 获取/设置分数 |

---

> 📢 更多 CMO Lua 编程案例见公众号 **海空兵棋与AI**，配套想定已分享至知识星球**兵推圈**。
