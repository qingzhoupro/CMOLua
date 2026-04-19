--[[
  File: examples/contributed/multi-side-battle/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - Multi-side scenario setup based on Matrix Games CMO Lua API documentation

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

# 三方对阵：多阵营关系设置

> 本文件为参考代码，用户需根据实际想定修改占位符后方可运行。

---

## 核心 API

| 函数 | 说明 |
|------|------|
| `ScenEdit_AddSide({name="", posture=""})` | 创建阵营 |
| `ScenEdit_SetSideOptions({side="", awareness="", proficiency=""})` | 设置阵营属性 |
| `ScenEdit_SetSidePosture("A","B","H/F/N/U")` | 设置阵营间关系 |

---

## 阵营态度代码

| 代码 | 态度 | 说明 |
|------|------|------|
| `"H"` | Hostile | 敌对（开火授权） |
| `"F"` | Friendly | 友好 |
| `"N"` | Neutral | 中立 |
| `"U"` | Unfriendly | 不友好 |
| `"X"` | Unknown | 未知 |

---

## 感知级别（Awareness）

| 值 | 说明 |
|------|------|
| `"Blind"` | 盲目（完全无感知） |
| `"Normal"` | 正常感知 |
| `"AutoSideID"` | 自动识别阵营 |
| `"Omniscient"` | 全知（观察者/导调视角） |

---

## 熟练度（Proficiency）

| 值 | 说明 |
|------|------|
| `"Novice"` | 新手（AI 反应迟缓） |
| `"Cadet"` | 学员 |
| `"Regular"` | 普通（默认） |
| `"Veteran"` | 老兵 |
| `"Ace"` | 王牌（AI 反应迅速） |

---

## 实现步骤

### 步骤 1：规划阵营结构

在想定编辑器中规划：
- 有哪些阵营？
- 谁和谁敌对？
- 是否有中立方？
- 各阵营 AI 熟练度？

### 步骤 2：创建阵营

```lua
-- ============================================================
-- 创建阵营
-- AI 助手提示：posture 为初始态度，后续可用 SetSidePosture 修改
-- ============================================================

-- 示例 A：三方对阵
ScenEdit_AddSide({name = "{{SIDE_A}}", posture = "H"})  -- 敌对
ScenEdit_AddSide({name = "{{SIDE_B}}", posture = "H"})  -- 敌对
ScenEdit_AddSide({name = "{{SIDE_C}}", posture = "N"})  -- 中立
```

### 步骤 3：设置阵营感知和熟练度

```lua
-- 设置 {{SIDE_A}} 阵营
ScenEdit_SetSideOptions({
    side = "{{SIDE_A}}",
    awareness = "Normal",     -- 正常感知
    proficiency = "Regular"   -- 普通 AI 熟练度
})

-- 设置 {{SIDE_B}} 阵营
ScenEdit_SetSideOptions({
    side = "{{SIDE_B}}",
    awareness = "Normal",
    proficiency = "Regular"
})

-- 设置中立/观察方 {{SIDE_C}}
ScenEdit_SetSideOptions({
    side = "{{SIDE_C}}",
    awareness = "Omniscient", -- 全知（导调视角）
    proficiency = "Veteran"   -- 老兵 AI
})
```

### 步骤 4：设置阵营关系（双向）

```lua
-- ⚠️ 阵营关系必须双向设置，否则只有单向生效

-- A vs B：敌对
ScenEdit_SetSidePosture("{{SIDE_A}}", "{{SIDE_B}}", "H")
ScenEdit_SetSidePosture("{{SIDE_B}}", "{{SIDE_A}}", "H")

-- C 与 A、B 均中立
ScenEdit_SetSidePosture("{{SIDE_C}}", "{{SIDE_A}}", "N")
ScenEdit_SetSidePosture("{{SIDE_C}}", "{{SIDE_B}}", "N")
```

---

## 完整模板

```lua
-- ============================================================
-- 多阵营对阵模板
-- ⚠️ 替换下方占位符为实际阵营名称
-- ============================================================

-- 1. 创建阵营（初始态度）
ScenEdit_AddSide({name = "{{SIDE_1}}", posture = "H"})
ScenEdit_AddSide({name = "{{SIDE_2}}", posture = "H"})
ScenEdit_AddSide({name = "{{SIDE_3}}", posture = "N"})  -- 中立

-- 2. 设置感知和熟练度
ScenEdit_SetSideOptions({side = "{{SIDE_1}}", awareness = "Normal", proficiency = "Regular"})
ScenEdit_SetSideOptions({side = "{{SIDE_2}}", awareness = "Normal", proficiency = "Regular"})
ScenEdit_SetSideOptions({side = "{{SIDE_3}}", awareness = "Omniscient", proficiency = "Veteran"})

-- 3. 设置阵营关系
ScenEdit_SetSidePosture("{{SIDE_1}}", "{{SIDE_2}}", "H")
ScenEdit_SetSidePosture("{{SIDE_2}}", "{{SIDE_1}}", "H")

ScenEdit_SetSidePosture("{{SIDE_3}}", "{{SIDE_1}}", "N")
ScenEdit_SetSidePosture("{{SIDE_3}}", "{{SIDE_2}}", "N")

print("多阵营对阵设置完成")
```

---

## 占位符说明

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{{SIDE_1}}` | 第一阵营名称 | `"Red"` |
| `{{SIDE_2}}` | 第二阵营名称 | `"Blue"` |
| `{{SIDE_3}}` | 第三阵营名称（可选） | `"Green"` |
