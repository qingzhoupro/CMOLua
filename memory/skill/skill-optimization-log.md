---
doc_id: CMO-MEMORY-LOG-001
title: Skill 优化追踪日志
description: 记录 CMO 各 skill 的优化进度和方向
---

# Skill 优化追踪日志

## 优化目标

为每个 skill 增加**场景上下文感知**能力，减少 `{{PLACEHOLDER}}` 使用，提高生成代码的针对性和准确性。

### 核心设计原则

- **渐进性披露（Progressive Disclosure）**：场景侦察脚本不常驻上下文，仅在需要时加载
- **有状态会话**：同一轮对话内 AI 持有场景上下文，无需重复询问
- **双向可读**：场景信息输出对人类友好，AI 也能解析

### 场景上下文感知流程

```
用户请求
  → 检查 memory/skill/scenario-context.md 是否有内容
    → 有内容：直接基于真实数据生成代码（无占位符）
    → 无内容：询问用户场景状态，或让用户执行 scene-scout.lua
      → 用户粘贴侦察输出
      → AI 填充 scenario-context.md
      → 基于真实数据生成代码
```

### 场景侦察脚本

`templates/utility/scene-scout.lua` - 获取场景全量信息的标准脚本。

### API 正确语法参考（常见错误）

| 功能 | 错误写法 | 正确写法 |
|------|---------|---------|
| 场景标题 | `ScenEdit_GetScenario().name` | `GetScenarioTitle()` |
| 阵营列表 | `ScenEdit_GetSides()` | `VP_GetSides()` |
| 阵营单元 | `ScenEdit_GetUnits({side=...})` | `VP_GetSide({side="xxx"}).units` |
| 任务列表 | `ScenEdit_GetMissions()` | `ScenEdit_GetMissions("阵营名")` |
| 参考点 | `ScenEdit_ReferencePoints(side)` | `ScenEdit_GetReferencePoints({side="xxx"})` |

---

## Skill 优化状态

| Skill | 文件 | 状态 | 优先级 | 备注 |
|-------|------|------|--------|------|
| cmo-auto | `.cursor/skills/cmo-auto/SKILL.md` | 已完成 | P0 | Phase 1 - 自动生成工作流 |
| cmo-unit | `.cursor/skills/cmo-unit/SKILL.md` | 已完成 | P0 | Phase 1 - 单元操作 |
| cmo-query | `.cursor/skills/cmo-query/SKILL.md` | 待优化 | P1 | Phase 2 - DBID 查询 |
| cmo-mission | `.cursor/skills/cmo-mission/SKILL.md` | 已完成 | P1 | Phase 2 - 任务管理 |
| cmo-side | `.cursor/skills/cmo-side/SKILL.md` | 已完成 | P1 | Phase 2 - 阵营管理 |
| cmo-debug | `.cursor/skills/cmo-debug/SKILL.md` | 已完成 | P2 | Phase 2 - 调试 |
| cmo-faq | `.cursor/skills/cmo-faq/SKILL.md` | 已完成 | P2 | Phase 2 - 常见问题 |
| templates/* | `templates/**/*.lua` | 待优化 | P2 | Phase 3 - 模板文件 |

---

## 待优化方向清单

### cmo-auto (Phase 1)
- [x] 在工作流开头增加场景上下文检测逻辑
- [x] 检查 scenario-context.md 是否已有内容
- [x] 无内容时提供 scene-scout.lua 并引导用户执行
- [x] 代码生成时从 context 读取真实阵营/基地/参考点名称，移除占位符

### cmo-unit (Phase 1)
- [x] 增加单元操作前的场景上下文确认
- [x] 移除或减少 `{{SIDE}}`, `{{UNIT_NAME}}` 等占位符
- [x] 提供从场景现有单元扩展的操作示例

### cmo-query (Phase 2)
- [ ] 与 scenario-context.md 联动，查询结果自动关联到场景中的单元类型
- [ ] 增加 NATO 符号对照输出

### cmo-mission (Phase 2)
- [x] 增加 Step 0.5 经验教训查询
- [x] 增加任务创建前的参考点/巡逻区检查
- [ ] 从 context 读取已有参考点名称

### cmo-side (Phase 2)
- [x] 增加 Step 0.5 经验教训查询
- [x] 增加阵营关系查询（使用 `ScenEdit_GetSidePosture`）
- [ ] 与已有场景的阵营整合

### cmo-debug (Phase 2)
- [x] 增加 Step 0.5 教训速查链接
- [x] 更新错误记录指向 `/cmo-errors` 命令

### cmo-faq (Phase 2)
- [x] 重构为教训速查入口
- [x] 增加 Step 0.5 教训速查表格

### templates/*.lua (Phase 3)
- [ ] 将所有模板中的占位符 `{{PLACEHOLDER}}` 替换为更清晰的注释说明
- [ ] 增加场景侦察脚本调用说明

---

## 实施记录

| 日期 | 操作 | 详情 |
|------|------|------|
| 2026-05-19 | 启动优化计划 | Phase 1 启动 |
| 2026-05-19 | 创建基础设施 | scene-scout.lua, scenario-context.md, skill-optimization-log.md 创建 |
| 2026-05-19 | 改造 cmo-auto | 已完成 - 增加场景上下文检测、MCP验证、API语法参考 |
| 2026-05-19 | 改造 cmo-unit | 已完成 - 增加上下文感知、移除占位符、增加扩展示例 |
| 2026-05-19 | 发现 GROUND UNIT type 陷阱 | 教训 - `type="GroundUnit"` 报错，正确值是 `type="GROUND UNIT"`（全大写+空格） |
| 2026-05-19 | 修正所有 skill 文件中的 GROUND UNIT 错误 | 已完成 - cmo-unit、cmo-auto、errors/index.md |
| 2026-05-19 | 修正 errors/index.md 中 AddSide 错误示例 | 已完成 - 改为 `{side="xxx"}` 而非 `{name="xxx"}` |
| 2026-05-20 | 教训库三层架构 Phase 2 启动 | memory/cold/lesson-root-causes.md, lesson-index.md 创建 |
| 2026-05-20 | Step 0.5 渐进嵌入 Phase 2 完成 | cmo-auto, cmo-unit, cmo-side, cmo-mission, cmo-faq, cmo-debug 均已嵌入 |
| 2026-05-20 | 新建 cmo-errors 命令 | .cursor/commands/cmo-errors.md 创建，错误教训收集入口 |
| 2026-05-20 | 更新 README 和 install.py | 经验教学体系章节、memory 子目录结构、cmo-errors 命令 |
| 2026-05-20 | 教训库三层架构 Phase 2 完成 | 所有计划文件均已更新 |
