--[[
  File: examples/contributed/strait-reference-points/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - Geographic coordinates based on public nautical charts and academic sources

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

# 亚太主要海峡参考点

> 本文件为参考代码，用户需根据实际想定修改占位符后方可运行。

---

## 使用说明

### 步骤 1：确认要使用的海峡

根据想定场景选择需要的海峡（不一定全部使用）：

| 编号 | 海峡 | 地区 | 战略价值 |
|------|------|------|---------|
| 1 | 宗谷海峡 | 日本北海道 | 俄日通道 |
| 2 | 津轻海峡 | 日本本州/北海道 | 太平洋通道 |
| 3 | 朝鲜海峡 | 韩国/日本 | 东海通道 |
| 4 | 大隅海峡 | 日本九州 | 东海通道 |
| 5 | 吐噶喇海峡 | 日本群岛 | 东海通道 |
| 6 | 宫古海峡 | 日本/台湾之间 | **西太平洋主通道** |
| 7 | 与那国海峡 | 日本最西端 | **最近台湾通道** |
| 8 | 巴士海峡 | 台湾/菲律宾 | 太平洋通道 |
| 9 | 马六甲海峡 | 东南亚 | 世界最重要通道 |

### 步骤 2：替换阵营名称

```lua
-- ⚠️ 将下方代码中的 "{{SIDE}}" 替换为实际阵营名称
-- 例如：local sideName = "Blue"

local sideName = "{{SIDE}}"  -- ← 修改为实际阵营名
```

### 步骤 3：按需注释不需要的海峡

将不需要的海峡代码块用 `--` 注释掉。

---

## 完整代码（选择性使用）

```lua
-- ============================================================
-- 亚太主要海峡参考点
-- 使用前：替换 {{SIDE}} 为实际阵营名称
-- 按需注释掉不需要的海峡代码块
-- ============================================================
local sideName = "{{SIDE}}"  -- ← 修改为实际阵营名

-- ============================================================
-- 1. 宗谷海峡 (Soya Strait)
-- 日本北海道与俄罗斯萨哈林之间
-- ============================================================
ScenEdit_AddReferencePoint({side = sideName, name = "宗谷海峡-1", latitude = 45.50, longitude = 141.90})
ScenEdit_AddReferencePoint({side = sideName, name = "宗谷海峡-2", latitude = 45.50, longitude = 142.00})
ScenEdit_AddReferencePoint({side = sideName, name = "宗谷海峡-3", latitude = 45.65, longitude = 142.00})
ScenEdit_AddReferencePoint({side = sideName, name = "宗谷海峡-4", latitude = 45.65, longitude = 141.90})

-- ============================================================
-- 2. 津轻海峡 (Tsugaru Strait)
-- 日本本州与北海道之间
-- ============================================================
ScenEdit_AddReferencePoint({side = sideName, name = "津轻海峡-1", latitude = 41.15, longitude = 140.50})
ScenEdit_AddReferencePoint({side = sideName, name = "津轻海峡-2", latitude = 41.15, longitude = 140.90})
ScenEdit_AddReferencePoint({side = sideName, name = "津轻海峡-3", latitude = 41.35, longitude = 140.90})
ScenEdit_AddReferencePoint({side = sideName, name = "津轻海峡-4", latitude = 41.35, longitude = 140.50})

-- ============================================================
-- 3. 朝鲜海峡 (Korea Strait)
-- 朝鲜半岛与日本之间
-- ============================================================
ScenEdit_AddReferencePoint({side = sideName, name = "朝鲜海峡-1", latitude = 34.00, longitude = 129.00})
ScenEdit_AddReferencePoint({side = sideName, name = "朝鲜海峡-2", latitude = 34.00, longitude = 129.50})
ScenEdit_AddReferencePoint({side = sideName, name = "朝鲜海峡-3", latitude = 34.50, longitude = 129.50})
ScenEdit_AddReferencePoint({side = sideName, name = "朝鲜海峡-4", latitude = 34.50, longitude = 129.00})

-- ============================================================
-- 4. 大隅海峡 (Osumi Strait)
-- 日本九州与大隅群岛之间
-- ============================================================
ScenEdit_AddReferencePoint({side = sideName, name = "大隅海峡-1", latitude = 31.00, longitude = 130.70})
ScenEdit_AddReferencePoint({side = sideName, name = "大隅海峡-2", latitude = 31.00, longitude = 130.90})
ScenEdit_AddReferencePoint({side = sideName, name = "大隅海峡-3", latitude = 31.30, longitude = 130.90})
ScenEdit_AddReferencePoint({side = sideName, name = "大隅海峡-4", latitude = 31.30, longitude = 130.70})

-- ============================================================
-- 5. 吐噶喇海峡 (Tokara Strait)
-- 日本大隅群岛与奄美群岛之间
-- ============================================================
ScenEdit_AddReferencePoint({side = sideName, name = "吐噶喇海峡-1", latitude = 29.70, longitude = 129.00})
ScenEdit_AddReferencePoint({side = sideName, name = "吐噶喇海峡-2", latitude = 29.70, longitude = 129.20})
ScenEdit_AddReferencePoint({side = sideName, name = "吐噶喇海峡-3", latitude = 29.90, longitude = 129.20})
ScenEdit_AddReferencePoint({side = sideName, name = "吐噶喇海峡-4", latitude = 29.90, longitude = 129.00})

-- ============================================================
-- 6. 宫古海峡 (Miyako Strait)
-- 日本宫古岛与八重山群岛之间，西太平洋重要通道
-- ============================================================
ScenEdit_AddReferencePoint({side = sideName, name = "宫古海峡-1", latitude = 24.30, longitude = 125.20})
ScenEdit_AddReferencePoint({side = sideName, name = "宫古海峡-2", latitude = 24.30, longitude = 125.50})
ScenEdit_AddReferencePoint({side = sideName, name = "宫古海峡-3", latitude = 24.60, longitude = 125.50})
ScenEdit_AddReferencePoint({side = sideName, name = "宫古海峡-4", latitude = 24.60, longitude = 125.20})

-- ============================================================
-- 7. 与那国海峡 (Yonaguni Strait)
-- 日本与那国岛与台湾之间，最近中国大陆的日本海峡
-- ============================================================
ScenEdit_AddReferencePoint({side = sideName, name = "与那国海峡-1", latitude = 24.30, longitude = 122.90})
ScenEdit_AddReferencePoint({side = sideName, name = "与那国海峡-2", latitude = 24.30, longitude = 123.10})
ScenEdit_AddReferencePoint({side = sideName, name = "与那国海峡-3", latitude = 24.50, longitude = 123.10})
ScenEdit_AddReferencePoint({side = sideName, name = "与那国海峡-4", latitude = 24.50, longitude = 122.90})

-- ============================================================
-- 8. 巴士海峡 (Bashi Channel)
-- 台湾与菲律宾巴丹群岛之间
-- ============================================================
ScenEdit_AddReferencePoint({side = sideName, name = "巴士海峡-1", latitude = 20.50, longitude = 121.50})
ScenEdit_AddReferencePoint({side = sideName, name = "巴士海峡-2", latitude = 20.50, longitude = 122.00})
ScenEdit_AddReferencePoint({side = sideName, name = "巴士海峡-3", latitude = 21.00, longitude = 122.00})
ScenEdit_AddReferencePoint({side = sideName, name = "巴士海峡-4", latitude = 21.00, longitude = 121.50})

-- ============================================================
-- 9. 马六甲海峡 (Strait of Malacca)
-- 印度尼西亚与马来西亚之间，世界最重要能源通道
-- ============================================================
ScenEdit_AddReferencePoint({side = sideName, name = "马六甲海峡-1", latitude = 2.00, longitude = 100.50})
ScenEdit_AddReferencePoint({side = sideName, name = "马六甲海峡-2", latitude = 2.00, longitude = 101.00})
ScenEdit_AddReferencePoint({side = sideName, name = "马六甲海峡-3", latitude = 2.50, longitude = 101.00})
ScenEdit_AddReferencePoint({side = sideName, name = "马六甲海峡-4", latitude = 2.50, longitude = 100.50})

print("参考点创建完成。请根据需要关联巡逻/布雷任务。")
```

---

## 关联巡逻任务

创建参考点后，可在编辑器中手动关联巡逻任务，或用以下代码：

```lua
-- AI 助手提示：
-- 巡逻类型：NAVAL（海上）、ASW（反潜）、AAW（防空）
-- 巡逻类型需与任务实际分配的单位类型匹配

ScenEdit_SetMission("{{SIDE}}", "{{PATROL_MISSION_NAME}}", {
    zone = {"宫古海峡-1", "宫古海峡-2", "宫古海峡-3", "宫古海峡-4"}
})
```

---

## 占位符说明

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{{SIDE}}` | 阵营名称 | `"Blue"` |
| `{{PATROL_MISSION_NAME}}` | 巡逻任务名称 | `"Miyako Strait Patrol"` |
