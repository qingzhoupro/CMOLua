# 用户贡献指南

您可以将收集到的案例放在此处。请按以下格式组织：

## 文件结构

```
contributed/
└── <案例名称>/
    ├── description.md    # 场景描述
    ├── lua-script.lua   # 完整 Lua 代码
    └── analysis.md       # 代码解析（可选）
```

## 已收录案例

| 案例 | 描述 | 分类 |
|------|------|------|
| cyber-ew-operations | 网电作战：网络中断与恢复 | 电子战 |
| psyop-defection | 心理战：随机劝降敌方单位 | 心理战 |
| auto-track-zone | 自动搜索跟踪区域调整 | 战术 |
| strait-reference-points | 亚太主要海峡参考点 | 地缘 |
| mine-laying | 布雷封锁任务 | 战术 |
| lancet-drone-attack | Lancet 巡飞弹攻击模拟 | 战术 |
| multi-side-battle | 多阵营对阵关系设置 | 基础 |
| track-export | 飞机轨迹记录与导出 | 工具 |
| missile-signature | 导弹特征修改（仅开发版） | 高级 |
| airbase-generator | 机场设施自动生成 | 战术 |
| submarine-tracking-intel | 潜艇追踪与情报系统 | 战术 |

## description.md 格式

```markdown
# <案例名称>

## 场景描述
描述场景功能和目的。

## 适用场景
- 场景 1
- 场景 2

## 前置条件
- 需要某阵营存在
- 需要特定装备
```

## lua-script.lua 格式要求

1. **不含硬编码**：所有单位名称、阵营名、GUID 等用 `{{PLACEHOLDER}}` 占位
2. **分步骤说明**：每个关键步骤有注释说明
3. **事件系统说明**：标注如何配合触发器使用
4. **MCP 查询提示**：涉及 DBID 等数据时标注需通过 MCP 查询
5. **可运行性**：代码逻辑正确，仅占位符需替换后方可执行

## 提交方式

将案例文件夹复制到 `examples/contributed/` 目录，并在 `examples/index.md` 中添加索引。
