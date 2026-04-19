# 案例库索引

## 概述

本目录包含 CMO Lua 代码案例，分为官方示例和用户自定义。

## 官方案例 (official/)

| 案例             | 描述         | 难度 |
| ---------------- | ------------ | ---- |
| blue-navy-patrol | 蓝方海军巡逻 | 基础 |
| air-combat       | 空战拦截     | 基础 |
| submarine-war    | 潜艇战       | 中级 |
| composite        | 合成作战     | 高级 |

## 用户自定义 (contributed/)

用户可自定义自己的案例。详见 `contributed/README.md`。

### 贡献案例列表

| 案例                     | 描述                     | 分类   | 配套公众号文章                                                                                                                       |
| ------------------------ | ------------------------ | ------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| cyber-ew-operations      | 网电作战：网络中断与恢复 | 电子战 | [通信干扰？](https://mp.weixin.qq.com/s/n0aNY_MJbHIADN8rjfTYpQ)                                                                         |
| psyop-defection          | 心理战：随机劝降敌方单位 | 心理战 | [马里乌波尔心理战场景](https://mp.weixin.qq.com/s/jo0JHSDHdLvVqSZov3mQOA)                                                               |
| auto-track-zone          | 自动搜索跟踪区域调整     | 战术   | [无人机自动跟踪水面舰艇](https://mp.weixin.qq.com/s/GqFpmZ2f9BeAL4-bBcsX9w)                                                             |
| airbase-generator        | 机场设施自动生成         | 战术   | [如何实现生成空军基地](https://mp.weixin.qq.com/s/og319vkri74IbdzsiSpW8w)                                                               |
| carrier-strike-group     | 航母打击群自动生成       | 战术   | [生成1艘美国航母](https://mp.weixin.qq.com/s/axXqNTYUaeqw80rJ6i9dAA) / [生成航母打击群](https://mp.weixin.qq.com/s/CdLuTTbVfghVf8VpeQavlQ) |
| submarine-tracking-intel | 潜艇追踪与情报系统       | 战术   | —                                                                                                                                   |
| strait-reference-points  | 亚太主要海峡参考点       | 地缘   | —                                                                                                                                   |
| mine-laying              | 布雷封锁任务             | 战术   | —                                                                                                                                   |
| lancet-drone-attack      | Lancet 巡飞弹攻击模拟    | 战术   | —                                                                                                                                   |
| multi-side-battle        | 多阵营对阵关系设置       | 基础   | —                                                                                                                                   |
| track-export             | 飞机轨迹记录与导出       | 工具   | —                                                                                                                                   |
| missile-signature        | 导弹特征修改（仅开发版） | 高级   | —                                                                                                                                   |

> 📢 配套想定已分享至**兵推圈**知识星球，更多内容见公众号 **海空兵棋与AI**。

## 使用方法

1. 查看 `description.md` 了解场景和配套公众号文章
2. 阅读 `lua-script.lua` 获取完整代码
3. 参考 `analysis.md` 理解代码逻辑
4. 在 CMO Lua Console 中执行测试

## 许可证

本项目遵循 **CC BY-NC-ND 4.0**（知识共享-署名-非商业-禁止演绎）协议。详见项目根目录 `LICENSE.md`。

## 贡献指南

用户可贡献新案例：

1. 提供可运行的 Lua 代码（含许可证头）
2. 编写场景描述（含公众号链接）
3. 添加代码解析
4. 保存到 `contributed/` 目录

详见 `CONTRIBUTING.md`。
