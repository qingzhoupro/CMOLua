--[[
  File: examples/contributed/lancet-drone-attack/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI

  Third-Party Acknowledgments:
  - Drone attack patterns inspired by CMO Community Script examples
  - Target detection logic based on Matrix Games API

  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]

# Lancet 巡飞弹攻击模拟

> 本文件为参考代码，用户需根据实际想定修改占位符后方可运行。

---

## 核心 API

| 函数 | 说明 |
|------|------|
| `ScenEdit_GetContacts("Side")` | 获取敌方接触列表 |
| `Tool_Range(guid1, guid2)` | 计算两单位间距离（海里） |
| `ScenEdit_SetUnit({...})` | 移动单位到指定位置 |
| `ScenEdit_KillUnit({guid=})` | 摧毁单位 |
| `ScenEdit_MsgBox(msg, type)` | 显示消息 |

---

## 实现步骤

### 步骤 1：在想定中添加巡飞弹单位

在编辑器中添加巡飞弹单位（如 Lancet、Hero 等巡飞弹），记下：
- 单位名称（或 GUID）
- 所属阵营

### 步骤 2：确定目标筛选条件

| 目标类型 | 关键词示例 |
|---------|-----------|
| 海马斯火箭炮 | `"HIMARS"`, `"M142"` |
| 防空系统 | `"SAM"`, `"Patriot"` |
| 雷达站 | `"Radar"` |
| 坦克 | `"Tank"`, `"M1"` |

### 步骤 3：获取单位 GUID

```lua
-- 在 Lua 控制台执行以下代码，获取单位的完整 GUID
-- ⚠️ 替换单位名称

local u = ScenEdit_GetUnit({name = "{{UNIT_NAME}}"})
print("GUID: " .. u.guid)
print("Name: " .. u.name)
print("Type: " .. u.type)
```

### 步骤 4：编写攻击脚本

```lua
-- ============================================================
-- 巡飞弹攻击系统
-- ⚠️ 将下方占位符替换为实际值
-- ============================================================

-- ⚠️ 配置参数
local ATTACKER_SIDE = "{{SIDE}}"            -- 攻击方阵营（用于获取接触）
local ATTACKER_GUID = "{{ATTACKER_GUID}}"   -- 巡飞弹单位 GUID
local TARGET_PATTERN = "{{TARGET_PATTERN}}"  -- 目标名称关键词
local ATTACK_RANGE = 3                      -- 攻击距离（海里）

-- 主攻击函数
-- AI 助手提示：Lua 不支持 Unicode 标识符，函数名用英文
function LancetsAttack()
    -- 获取攻击单位
    local attacker = ScenEdit_GetUnit({guid = ATTACKER_GUID})
    if not attacker then
        print("Attack unit not found, please check GUID")
        return
    end

    -- 获取敌方接触
    local contacts = ScenEdit_GetContacts(ATTACKER_SIDE)
    if not contacts or #contacts == 0 then
        return  -- 未发现目标，静默退出
    end

    -- 遍历接触寻找目标
    for i, contact in ipairs(contacts) do
        -- 按名称关键词匹配
        if string.find(contact.name, TARGET_PATTERN) then
            -- 计算距离
            local distance = Tool_Range(ATTACKER_GUID, contact.guid)

            if distance <= ATTACK_RANGE then
                -- 移动攻击弹到目标位置
                ScenEdit_SetUnit({
                    guid = ATTACKER_GUID,
                    latitude = contact.latitude,
                    longitude = contact.longitude,
                    altitude = 0
                })

                -- 摧毁双方（模拟同归于尽）
                ScenEdit_KillUnit({guid = ATTACKER_GUID})
                ScenEdit_KillUnit({guid = contact.guid})

                print("Attack successful! Target destroyed")
                return
            else
                print("Target out of range: " .. distance .. " nm (max: " .. ATTACK_RANGE .. ")")
            end
        end
    end
end

-- 执行
LancetsAttack()
```

---

## 事件触发版本

建议配合定期事件持续扫描目标：

```lua
-- ============================================================
-- 定时事件脚本（建议间隔 1~5 秒）
-- 在编辑器中创建事件：
--   触发条件：定期时间 → 3 秒
--   动作：Lua 脚本 → 本函数
-- ============================================================

function LancetsAttackEvent()
    local contacts = ScenEdit_GetContacts("{{SIDE}}")
    if not contacts or #contacts == 0 then
        return
    end

    for i, contact in ipairs(contacts) do
        if string.find(contact.name, "{{TARGET_PATTERN}}") then
            local distance = Tool_Range("{{ATTACKER_GUID}}", contact.guid)
            if distance <= {{ATTACK_RANGE}} then
                ScenEdit_SetUnit({
                    guid = "{{ATTACKER_GUID}}",
                    latitude = contact.latitude,
                    longitude = contact.longitude,
                    altitude = 0
                })
                ScenEdit_KillUnit({guid = "{{ATTACKER_GUID}}"})
                ScenEdit_KillUnit({guid = contact.guid})
                return
            end
        end
    end
end

LancetsAttackEvent()
```

---

## 占位符说明

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{{SIDE}}` | 攻击方阵营（获取接触用） | `"Blue"` |
| `{{ATTACKER_GUID}}` | 巡飞弹单位 GUID | 完整 GUID 字符串 |
| `{{TARGET_PATTERN}}` | 目标名称关键词 | `"HIMARS"`, `"SAM"` |
| `{{ATTACK_RANGE}}` | 攻击距离（海里，数字） | `3` |
