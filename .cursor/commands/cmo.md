# CMO 命令

CMO 兵棋 Lua 代码生成的命令入口。

## 可用命令

| 命令 | 说明 |
|------|------|
| `/cmo` | 完整的 CMO Lua 代码生成工作流 |
| `/cmo-auto` | 完整工作流（详细版，含场景上下文） |
| `/cmo-scene` | 获取场景信息（侦察脚本） |
| `/cmo-unit` | 快速添加单位 |
| `/cmo-query` | 数据库查询 |
| `/cmo-mission` | 任务生成 |
| `/cmo-check` | 代码自检 |
| `/cmo-errors` | 错误教训收集 |

## 使用方式

```
/cmo 生成一个蓝方 F-16C 战斗机中队
/cmo-auto 生成完整的 CV-16C 航母打击群配置
/cmo-scene 获取当前场景信息
/cmo-unit 添加红方 055 驱逐舰到舟山海域
/cmo-query 查询现役驱逐舰
/cmo-mission 创建巡逻任务
/cmo-check 检查我生成的代码
/cmo-errors 记录一个错误教训
```

> 提示：使用 `/cmo-scene` 可以让 AI 了解当前场景状态，生成更精准的代码。空白场景可直接生成，有内容的场景建议先执行一次。

详细文档 → `.cursor/skills/cmo-auto/SKILL.md`
