--[[
  File: examples/contributed/mine-laying/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - Minefield creation based on Matrix Games CMO Lua API documentation

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

# 布雷封锁任务

> 本文件为参考代码，用户需根据实际想定修改占位符后方可运行。

---

## 核心 API

| 函数 | 说明 |
|------|------|
| `ScenEdit_AddMinefield({...})` | 在参考点区域内布雷 |
| `ScenEdit_AddReferencePoint({...})` | 创建参考点 |
| `ScenEdit_SetMission("S","N",{zone={}})` | 关联任务区域 |

---

## 实现步骤

### 步骤 1：查询水雷 DBID

在编辑器中找到想使用的水雷装备，记下其 DBID。

**AI 助手提示**：在 CMO 中添加布雷载具（如扫雷艇、轰炸机），运行以下命令获取 DBID：
```lua
-- 使用 MCP 工具查询水雷 DBID
-- query_dbid("水雷") 或 query_dbid("mine")
```

常见水雷类型：
- 沉底水雷（Bottom Mine）
- 锚雷（Moored Mine）
- 漂雷（Drifting Mine）

### 步骤 2：创建布雷区域参考点

布雷区域需先有 4 个参考点（步骤详见 `strait-reference-points/` 案例）。

```lua
-- 示例：创建布雷区域参考点
ScenEdit_AddReferencePoint({side = "{{SIDE}}", name = "{{MINE_AREA_PREFIX}}-1", latitude = 24.30, longitude = 125.20})
ScenEdit_AddReferencePoint({side = "{{SIDE}}", name = "{{MINE_AREA_PREFIX}}-2", latitude = 24.30, longitude = 125.50})
ScenEdit_AddReferencePoint({side = "{{SIDE}}", name = "{{MINE_AREA_PREFIX}}-3", latitude = 24.60, longitude = 125.50})
ScenEdit_AddReferencePoint({side = "{{SIDE}}", name = "{{MINE_AREA_PREFIX}}-4", latitude = 24.60, longitude = 125.20})
```

### 步骤 3：执行布雷

```lua
-- ============================================================
-- 布雷封锁
-- ⚠️ 将下方占位符替换为实际值
-- ============================================================

-- ⚠️ 配置参数
local MINE_SIDE = "{{SIDE}}"                        -- 布雷方阵营
local MINE_DBID = {{MINE_DBID}}                     -- 水雷 DBID（数字，通过查询获得）
local MINE_COUNT = {{NUMBER}}                        -- 布雷数量（数字）
local MINE_DELAY = {{DELAY}}                         -- 布雷延迟（毫秒），模拟布雷载具飞行时间
local MINE_AREA = {
    "{{AREA_PREFIX}}-1",
    "{{AREA_PREFIX}}-2",
    "{{AREA_PREFIX}}-3",
    "{{AREA_PREFIX}}-4"
}  -- 参考点名称（必须已存在）

-- 执行布雷
-- AI 助手提示：delay 设为布雷载具从基地飞到布雷区域的时间（毫秒）
local laid = ScenEdit_AddMinefield({
    side = MINE_SIDE,
    dbid = MINE_DBID,
    number = MINE_COUNT,
    delay = MINE_DELAY,
    area = MINE_AREA
})

print("布雷完成，实际布雷: " .. laid .. " 枚")
```

---

## 布雷数量参考

| 封锁级别 | 布雷数量 | 说明 |
|---------|---------|------|
| 轻度 | 10–20 | 威慑性布雷 |
| 中度 | 30–50 | 有效封锁 |
| 重度 | 80+ | 完全封锁 |

---

## 布雷延迟参考

| 布雷载具 | 典型延迟 |
|---------|---------|
| 轰炸机（近距机场） | 30000–60000 ms |
| 轰炸机（远距机场） | 120000–300000 ms |
| 水雷艇 | 60000–180000 ms |

---

## 占位符说明

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{{SIDE}}` | 布雷方阵营 | `"Blue"` |
| `{{MINE_DBID}}` | 水雷 DBID（数字） | `634` |
| `{{NUMBER}}` | 布雷数量（数字） | `50` |
| `{{DELAY}}` | 布雷延迟（毫秒，数字） | `60000` |
| `{{AREA_PREFIX}}` | 布雷区域参考点前缀 | `"封锁区"` |
