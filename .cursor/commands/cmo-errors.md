---
doc_id: CMO-CMD-ERRORS-001
trigger: /cmo-errors
title: 错误教训收集
description: 错误教训收集入口，支持交互式收集和快速添加
---

# /cmo-errors - 错误教训收集

错误教训收集入口。遇到新错误时使用此命令记录，防止同类错误重复发生。

## 使用方式

| 命令 | 说明 |
|------|------|
| `/cmo-errors` | 交互式收集模式（引导式录入） |
| `/cmo-errors add` | 快速添加当前错误 |
| `/cmo-errors list` | 查看已有教训列表 |
| `/cmo-errors review` | 复习近期教训 |

## 交互式收集流程

当用户输入 `/cmo-errors` 时，引导用户完成以下步骤：

1. **输入错误信息** — 粘贴 Lua 报错内容或描述错误现象
2. **输入错误原因** — 分析为什么会出错
3. **输入正确做法** — 正确的代码或操作是什么
4. **选择教训分类** — 从三大根因中选择：
   - `1` — Lua 幻觉（API/参数名编造）
   - `2` — 地理坐标（经纬度/altitude 错误）
   - `3` — 意图理解（需求理解偏差）
5. **生成教训 ID** — 自动生成唯一 ID，如 `教训-USER-001`
6. **写入教训库** — 自动追加到 `memory/cold/lesson-root-causes.md`
7. **更新索引** — 自动追加到 `memory/cold/lesson-index.md`

## 快速添加流程

当用户输入 `/cmo-errors add` 时，使用简化流程：

1. 读取用户粘贴的错误信息
2. 识别教训分类（根据错误关键字自动推断）
3. 生成教训 ID
4. 写入教训库

## 自动捕获机制

当 AI 检测到以下模式时，主动询问用户是否记录教训：

```
检测到报错模式：[错误信息]

是否记录此教训？
- 输入 y 继续收集
- 输入 n 跳过
```

### 自动捕获的正则模式

```regex
# Lua 报错格式
ScenEdit_\w+.*:\s*,?(.+)

# 关键词
记住|记录|这(个)是?教训|报错|错误信息|出错了|Missing|Invalid|doesn't exist
```

## 教训格式

收集的教训格式：

```
**教训-[ID]** | [触发条件] | [错误信息] | [正确做法] | [自检项]
```

示例：

```
**教训-USER-001** | 添加 Aircraft 单元时 | Missing LoadoutID | Aircraft 必须通过 MCP 查询 LoadoutID | 检查 LoadoutID 参数存在
```

## 三大根因分类说明

| 分类 | 典型错误 |
|------|---------|
| **Lua 幻觉** | 错误的函数名、错误的参数格式、编造的 API |
| **地理坐标** | lat/lon 而非 latitude/longitude、altitude 单位混淆 |
| **意图理解** | 遗漏必要步骤（LoadoutID）、遗漏阵营创建 |

详细教训 → `memory/cold/lesson-root-causes.md`
教训索引 → `memory/cold/lesson-index.md`
