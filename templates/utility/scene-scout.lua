---
doc_id: CMO-TEMPLATE-SCOUT-001
title: 场景侦察脚本
description: 获取当前 CMO 场景的全量信息，用于 AI 生成精准代码
---

# 场景侦察脚本

将以下代码完整复制到 CMO Lua 控制台执行，然后将输出结果完整粘贴回给 AI。

AI 会根据输出内容生成基于你当前场景的精准 Lua 代码，而不是使用占位符。

## scene-scout.lua

```lua
-- scene-scout-v5.lua
-- 用法：复制到 CMO Lua 控制台执行
-- 全量整合版：完整保留全局状态、天气、阵营概况，并完美修复真实单元(Units)类型解包

print("=== CMO 场景全局侦察报告 (V5-全量无损版) ===")

-- 1. 获取场景基础状态
print("场景标题: " .. tostring(GetScenarioTitle()))
print("场景是否已开始: " .. tostring(ScenEdit_GetScenHasStarted()))

-- 2. 获取当前天气快照
local weather = ScenEdit_GetWeather()
if weather then
    print(string.format("环境天气: 温度 %s°C | 云量 %d%% | 海况 %s 级", 
        tostring(weather.temp), math.floor((weather.undercloud or 0) * 100), tostring(weather.seastate)))
end
print("")

-- 3. 获取所有阵营及其得分、控制权状态
local sides = VP_GetSides()
print("【阵营积分与控制概况】")
for _, side in ipairs(sides) do
    local is_human = false
    pcall(function() is_human = ScenEdit_GetSideIsHuman(side.name) end)
    local score = 0
    pcall(function() score = ScenEdit_GetScore(side.name) end)
    print(string.format("  - [%s] 阵营得分: %s | 控制方: %s", side.name, tostring(score), is_human and "人类玩家" or "AI 电脑"))
end
print("")

-- 4. 各阵营任务清册 (安全过滤)
print("【各阵营任务清册】")
for _, side in ipairs(sides) do
    local success, missions = pcall(ScenEdit_GetMissions, side.name)
    if success and missions and #missions > 0 then
        print("  - 阵营 [" .. side.name .. "] 当前编组任务:")
        for _, m in ipairs(missions) do
            print("    * 任务名: " .. tostring(m.name) .. " | GUID: " .. tostring(m.guid or m.objectid))
        end
    else
        print("  - 阵营 [" .. side.name .. "] 无可用或可读任务。")
    end
end
print("")

-- 5. 获取各阵营己方真实单元 (Units) - 引入真实 Wrapper 转换
print("【各阵营真实单元 (Units) 扫描】")
for _, side in ipairs(sides) do
    local units = side.units
    if units and #units > 0 then
        print("  - 阵营 [" .. side.name .. "] 实际拥有单元数: " .. #units)
        
        -- 限制展示前 5 个进行结构示例
        local max_unit_dump = math.min(#units, 5)
        for i = 1, max_unit_dump do
            local raw_u = units[i]
            local u_guid = raw_u.guid or raw_u.objectid
            
            -- 通过全局 ScenEdit_GetUnit 将轻量指针显式转换为功能完整的真实的 Unit 包装器对象
            local get_u_success, real_unit = pcall(ScenEdit_GetUnit, { guid = u_guid })
            
            local u_name = raw_u.name or "未命名实体"
            local u_type = "未知大类"
            local u_class = "未知型号"
            
            if get_u_success and real_unit then
                -- 成功解包，提取官方合规的类目和大类属性
                u_type = real_unit.category or "未知大类"
                u_class = real_unit.classname or "未知型号"
            end
            
            print(string.format("    * [己方单位] %s | 大类: %s | 级别型号: %s | GUID: %s", 
                tostring(u_name), tostring(u_type), tostring(u_class), tostring(u_guid)))
        end
        
        if #units > 5 then
            print("    * ... 其余 " .. (#units - 5) .. " 个己方单元已省略。")
        end
    else
        print("  - 阵营 [" .. side.name .. "] 视点下无直接控制的单元。")
    end
end
print("")

-- 6. 安全扫描已知接触情报 (Contacts) - 防御 nil 拼接与视点隔离
print("【各阵营已知接触情报 (Contacts)】")
for _, side in ipairs(sides) do
    local contacts = side.contacts 
    if contacts and #contacts > 0 then
        print("  - 阵营 [" .. side.name .. "] 总计探测到目标数: " .. #contacts)
        
        local max_dump = math.min(#contacts, 5)
        for i = 1, max_dump do
            local target = contacts[i]
            local con_guid = target.guid or target.objectid or target.ObjectID
            local safe_guid_str = tostring(con_guid)
            
            if con_guid then
                local get_success, a_contact = pcall(VP_GetContact, { guid = safe_guid_str })
                if get_success and a_contact then
                    local name = a_contact.name or "未知接触"
                    local contact_type_desc = a_contact.type_description or "未分类接触"
                    print(string.format("    * [探测解析成功] 目标: %s | 情报分类: %s | GUID: %s", 
                        tostring(name), tostring(contact_type_desc), safe_guid_str))
                else
                    print("    * [视点隔离/仅知实体] 接触 GUID: " .. safe_guid_str)
                end
            else
                print("    * [警告] 该接触快照中未包含有效的 ID 字段")
            end
        end
        
        if #contacts > 5 then
            print("    * ... 阵营 [" .. side.name .. "] 其余 " .. (#contacts - 5) .. " 个已知接触目标已省略。")
        end
    else
        print("  - 阵营 [" .. side.name .. "] 当前没有已建立的敌情接触。")
    end
end
print("")

print("=== 侦察报告执行完毕 ===")
```