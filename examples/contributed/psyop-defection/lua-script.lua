--[[
  File: examples/contributed/psyop-defection/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - Psychological operations concepts based on CMO Community Script patterns
  - Side/unit enumeration methods from Matrix Games API documentation

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

# 心理战：随机劝降敌方单位

> 本文件为参考代码，用户需根据实际想定修改占位符后方可运行。

---

## 核心 API

| 函数 | 说明 |
|------|------|
| `VP_GetSide({Side="SideName"})` | 获取某阵营所有单位列表 |
| `ScenEdit_GetUnit({guid=})` | 通过 GUID 获取单位详细信息 |
| `string.match(str, pattern)` | 模糊匹配单位名称 |
| `math.random(n)` | 随机返回 1~n 的整数 |
| `ScenEdit_SetUnitSide({side, guid, newside})` | 改变单位阵营 |

---

## 实现步骤

### 步骤 1：确定目标阵营和关键词

在编辑器中确认：
- 目标阵营名称（如 Red、Blue 或自定义阵营）
- 要筛选的单位名称关键词（如部队编号 `"21st"`、部队类型 `"SAM"` 等）

### 步骤 2：确定劝降后归属

劝降后的阵营可以是：
- `"Civilian"` — 转为平民（退出战斗）
- `"Neutral"` — 转为中立
- 其他自定义阵营

### 步骤 3：编写劝降脚本

```lua
-- ============================================================
-- 心理战劝降系统
-- AI 助手提示：关键词使用 string.match() 模糊匹配
-- ============================================================

-- ⚠️ 配置参数（请根据实际想定修改）
local TARGET_SIDE = "{{ENEMY_SIDE}}"      -- 敌方阵营名称
local KEYWORD = "{{UNIT_KEYWORD}}"         -- 单位名称关键词（模糊匹配）
local NEW_SIDE = "Civilian"                -- 劝降后归属阵营

-- 劝降函数
-- @param targetSide  敌方阵营名
-- @param keyword     名称筛选关键词
-- @param newSide     劝降后阵营
-- @param maxFlip     最大劝降数量
-- @return 实际劝降数量, 筛选到的总数
function psyopDefection(targetSide, keyword, newSide, maxFlip)
    -- 获取敌方所有单位
    local sideUnits = VP_GetSide({Side = targetSide}).units
    local targetUnits = {}

    -- 遍历并筛选匹配关键词的单位
    for i = 1, #sideUnits do
        local unit = ScenEdit_GetUnit({guid = sideUnits[i].guid})
        if string.match(unit.name, keyword) ~= nil then
            table.insert(targetUnits, unit)
        end
    end

    -- 随机确定劝降数量
    local numToFlip = math.random(#targetUnits)
    numToFlip = math.min(numToFlip, maxFlip)

    -- 执行劝降
    local actualFlip = 0
    for k = 1, numToFlip do
        ScenEdit_SetUnitSide({
            side = targetSide,
            guid = targetUnits[k].guid,
            newside = newSide
        })
        actualFlip = actualFlip + 1
    end

    return actualFlip, #targetUnits
end
```

---

## 事件触发脚本

```lua
-- ============================================================
-- 事件触发脚本（配合定期时间触发器）
-- AI 助手提示：建议触发间隔 30 分钟以上，避免劝降过快
-- ============================================================

-- ⚠️ 每次触发时修改关键词或阵营
-- 示例：每隔一段时间劝降部分 {{UNIT_KEYWORD}} 单位

local flipped, total = psyopDefection(
    "{{ENEMY_SIDE}}",   -- 敌方阵营
    "{{UNIT_KEYWORD}}",  -- 筛选关键词
    "Civilian",          -- 劝降后阵营
    5                    -- 最多劝降 5 个
)

print("心理战效果：" .. flipped .. "/" .. total .. " 个单位已叛变")
```

---

## 关键词参考

| 关键词示例 | 匹配对象 |
|-----------|---------|
| `"21st"` | 含"21st"的部队（如"21st Motor Infantry"） |
| `"SAM"` | 防空单位 |
| `"Battalion"` | 营级单位 |
| `"Infantry"` | 步兵单位 |
| `"Tank"` | 坦克单位 |

---

## 占位符说明

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{{ENEMY_SIDE}}` | 敌方阵营名称 | `"Red"`, `"Blue"` |
| `{{UNIT_KEYWORD}}` | 单位名称关键词 | `"21st"`, `"SAM"` |
| `"Civilian"` | 劝降后阵营 | `"Civilian"`, `"Neutral"` |
