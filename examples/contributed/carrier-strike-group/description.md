# 航母打击群自动生成

> 📖 **配套文章**：
> - [【CMO 智能指控系列】如何生成1艘美国航母](https://mp.weixin.qq.com/s/axXqNTYUaeqw80rJ6i9dAA)
> - [【CMO 智能指控系列】如何生成航母打击群（CSG）](https://mp.weixin.qq.com/s/CdLuTTbVfghVf8VpeQavlQ)
> （公众号：海空兵棋与AI）

## 场景描述

通过参数化函数自动创建完整的航母打击群，包含：
- 航母本体及舰载机联队
- 编队舰艇（防空驱逐舰、巡洋舰、补给舰）
- 以航母为圆心按战术阵位部署属舰

> 公众号文章详细介绍了美航母打击群的战术编成：1 艘防空巡洋舰在航母前方 40 海里处警戒，其余驱逐舰距航母 8-10 海里环状铺开，1 艘补给舰在近距一侧，1-2 艘攻击型核潜艇在沿途/后方 50 海里警戒。

## 适用场景

- 批量创建 CSG
- 大型海战场景初始化
- 联军海上作战演练

## 前置条件

- 已安装 CMO MCP 并可查询 DBID
- 已知目标位置的经纬度

## DBID 查询

```lua
-- 使用 MCP query_dbid 查询
query_dbid("航母") 或 query_dbid("carrier")
query_dbid("驱逐舰") 或 query_dbid("destroyer")
query_dbid("巡洋舰") 或 query_dbid("cruiser")
query_dbid("补给舰") 或 query_dbid("aoe")
query_dbid("舰载机") 或 query_dbid("fa-18")
query_dbid("直升机") 或 query_dbid("mh-60")
```

## 核心 API

| 函数 | 说明 |
|------|------|
| `ScenEdit_AddUnit({type='Ship'})` | 创建舰艇单位 |
| `ScenEdit_AddUnit({type='Air', base=})` | 创建舰载机（指定航母为基地） |
| `World_GetPointFromBearing({...})` | 根据方位和距离计算经纬度 |
| `unit.heading` | 获取/设置单位航向 |

---

## 编队阵位参考

| 舰种 | 相对航母位置 |
|------|------------|
| 防空巡洋舰 | 前方 40 海里 |
| 驱逐舰 | 前方/两侧 25-30 海里 |
| 补给舰 | 近距一侧 10 海里 |
| 攻击型核潜艇 | 后方/沿途 50 海里 |

---

> 📢 更多 CMO Lua 编程案例见公众号 **海空兵棋与AI**，配套想定已分享至知识星球**兵推圈**。
