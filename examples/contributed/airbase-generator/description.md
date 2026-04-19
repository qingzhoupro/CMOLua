# 机场设施自动生成

> 📖 **配套文章**：[【CMO 智能指控系列】如何实现生成空军基地](https://mp.weixin.qq.com/s/og319vkri74IbdzsiSpW8w)（公众号：海空兵棋与AI）

## 场景描述

通过参数化函数自动创建完整的机场设施组，包含跑道、滑行道、进入点、停机坪、弹药库等，所有设施自动归组。

> 公众号文章详细讲解了机场各组成部分的作用（跑道、停机坪、弹药库等），以及压制机场作战的 5 个注意事项：摧毁机库、识别停驻飞机、销毁弹药库、阻塞跑道进入点、直接压制跑道。

## 适用场景

- 批量创建机场
- 基地快速部署
- 大型场景初始化

## 前置条件

- 已安装 CMO MCP 并可查询 DBID
- 已知目标位置的经纬度

## DBID 查询

各设施 DBID 需通过 MCP 查询，不同 CMO 数据库版本可能不同：

```lua
-- 使用 MCP query_dbid 查询：
query_dbid("跑道") 或 query_dbid("runway")
query_dbid("滑行道") 或 query_dbid("taxiway")
query_dbid("进入点") 或 query_dbid("access point")
query_dbid("停机坪") 或 query_dbid("tarmac")
query_dbid("弹药库") 或 query_dbid("ammo")
```

## 核心 API

| 函数 | 说明 |
|------|------|
| `ScenEdit_AddUnit({type='Facility', group=})` | 创建设施并归组 |
| `unit.group = name` | 将单位加入设施组 |

---

> 📢 更多 CMO Lua 编程案例见公众号 **海空兵棋与AI**，配套想定已分享至知识星球**兵推圈**。
