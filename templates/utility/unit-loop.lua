-- 单位遍历模板
-- 遍历指定任务中的所有单位

-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{MISSION_NAME}} - 任务名称

-- 获取任务
local m = ScenEdit_GetMission("{{SIDE}}", "{{MISSION_NAME}}")

-- 遍历任务中的单位
for i = 1, #m.unitlist do
    local u = ScenEdit_GetUnit({guid=m.unitlist[i]})
    
    -- 在此处处理每个单位
    print(u.name)
    
    -- 示例：设置熟练度
    -- ScenEdit_SetUnit({guid=u.guid, proficiency="Veteran"})
    
    -- 示例：检查单位类型
    -- if u.type == "Aircraft" then
    --     print("飞机: " .. u.name)
    -- elseif u.type == "Ship" then
    --     print("舰艇: " .. u.name)
    -- end
end

-- 示例：遍历所有单位
-- local side = VP_GetSide({Side="{{SIDE}}"})
-- for i = 1, #side.units do
--     local u = ScenEdit_GetUnit({guid=side.units[i].guid})
--     print(u.name .. " - " .. u.type)
-- end