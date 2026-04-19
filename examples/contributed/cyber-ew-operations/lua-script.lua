--[[
  File: examples/contributed/cyber-ew-operations/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - Network disruption mechanics based on Matrix Games CMO Lua API documentation
  - Some patterns inspired by CMO Community Scripts (credited in source)

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

# 网电作战：网络中断与恢复

> 本文件为参考代码，用户需根据实际想定修改占位符后方可运行。

---

## 核心 API

| 函数 | 说明 |
|------|------|
| `ScenEdit_SetUnit({outOfComms="True"})` | 中断指定单位的网络连接 |
| `ScenEdit_SetUnit({outOfComms="False"})` | 恢复指定单位的网络连接 |
| `ScenEdit_MsgBox(msg, type)` | 显示消息框 |
| `ScenEdit_SetEvent(name, {IsActive=})` | 启用/禁用事件 |

---

## 场景 1：手动网络中断

### 实现步骤

**步骤 1：确认目标单位名称**
在 CMO 编辑器中查看要断网的单位完整名称（如雷达站、通信基站等），记下精确名称。

**步骤 2：执行网络中断**
```lua
-- ⚠️ 以下单位名称为示例，请替换为实际想定中的名称
-- AI 助手提示：使用 Ctrl+F 在编辑器中搜索单位名称

-- 中断通信
ScenEdit_SetUnit({side = "{{TARGET_SIDE}}", name = "{{UNIT_NAME_1}}", outOfComms = "True"})
ScenEdit_SetUnit({side = "{{TARGET_SIDE}}", name = "{{UNIT_NAME_2}}", outOfComms = "True"})
-- 可继续添加更多单位...

ScenEdit_MsgBox("网络攻击成功！部分 {{TARGET_SIDE}} 单位通信中断", 1)
```

**步骤 3：执行网络恢复**
```lua
-- 恢复通信
ScenEdit_SetUnit({side = "{{TARGET_SIDE}}", name = "{{UNIT_NAME_1}}", outOfComms = "False"})
ScenEdit_SetUnit({side = "{{TARGET_SIDE}}", name = "{{UNIT_NAME_2}}", outOfComms = "False"})

ScenEdit_MsgBox("{{TARGET_SIDE}} 通信网络已恢复", 1)
```

---

## 场景 2：定时自动恢复

### 实现步骤

**步骤 1：创建中断事件（想定加载时触发）**
```lua
-- 网络攻击效果
ScenEdit_SetUnit({side = "{{TARGET_SIDE}}", name = "{{RADAR_UNIT_1}}", outOfComms = "True"})
ScenEdit_SetUnit({side = "{{TARGET_SIDE}}", name = "{{RADAR_UNIT_2}}", outOfComms = "True"})
ScenEdit_SetUnit({side = "{{TARGET_SIDE}}", name = "{{RADAR_UNIT_3}}", outOfComms = "True"})
ScenEdit_SetUnit({side = "{{TARGET_SIDE}}", name = "{{RADAR_UNIT_4}}", outOfComms = "True"})

ScenEdit_MsgBox("网络攻击成功！{{TARGET_SIDE}} 雷达组网中断", 1)

-- ⚠️ 在编辑器中手动创建事件，名称为 "网络恢复"
-- 触发条件：定期时间，间隔如 3600 秒（1小时）
-- 激活事件让恢复脚本等待触发
```

**步骤 2：创建恢复事件（在编辑器中手动创建）**

```
事件名称：网络恢复
触发条件：定期时间 → 3600 秒（或自定义时长）
动作（Lua）：
```

```lua
-- 恢复所有被中断的单位
ScenEdit_SetUnit({side = "{{TARGET_SIDE}}", name = "{{RADAR_UNIT_1}}", outOfComms = "False"})
ScenEdit_SetUnit({side = "{{TARGET_SIDE}}", name = "{{RADAR_UNIT_2}}", outOfComms = "False"})
ScenEdit_SetUnit({side = "{{TARGET_SIDE}}", name = "{{RADAR_UNIT_3}}", outOfComms = "False"})
ScenEdit_SetUnit({side = "{{TARGET_SIDE}}", name = "{{RADAR_UNIT_4}}", outOfComms = "False"})

ScenEdit_MsgBox("{{TARGET_SIDE}} 启用备用通信，雷达组网恢复", 1)
```

---

## 通用函数模板

```lua
-- ============================================================
-- 网络中断/恢复通用函数
-- ============================================================

-- 中断指定阵营的多个单位网络
-- @param side       阵营名称
-- @param unitNames  单位名称数组
function networkBlackout(side, unitNames)
    for i, name in ipairs(unitNames) do
        ScenEdit_SetUnit({side = side, name = name, outOfComms = "True"})
    end
end

-- 恢复指定阵营的多个单位网络
-- @param side       阵营名称
-- @param unitNames  单位名称数组
function networkRestore(side, unitNames)
    for i, name in ipairs(unitNames) do
        ScenEdit_SetUnit({side = side, name = name, outOfComms = "False"})
    end
end

-- 示例用法
local targetUnits = {
    "{{UNIT_NAME_1}}",
    "{{UNIT_NAME_2}}"
}

-- 中断网络
networkBlackout("{{TARGET_SIDE}}", targetUnits)

-- 恢复网络（通常由事件触发）
-- networkRestore("{{TARGET_SIDE}}", targetUnits)
```

---

## 占位符说明

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{{TARGET_SIDE}}` | 目标阵营名称 | `"Red"`, `"Blue"` |
| `{{UNIT_NAME_N}}` | 单位精确名称 | `"SAM Site Alpha"` |
| `{{RADAR_UNIT_N}}` | 雷达单位名称 | `"Ground Radar #1"` |
