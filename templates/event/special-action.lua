-- 特殊动作模板
-- 参考: CMO_Lua函数_Events.md - ScenEdit_AddSpecialAction
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{ACTION_NAME}} - 动作名称
-- {{DESCRIPTION}} - 动作描述

-- 创建特殊动作
local LfCR = '\r\n'  -- Lua 脚本换行符

-- 构建 Lua 脚本
local myScript = '-- 特殊动作脚本' .. LfCR ..
    'local unit = ScenEdit_UnitX()' .. LfCR ..
    'print("执行特殊动作")' .. LfCR ..
    'ScenEdit_MsgBox("特殊动作已执行!", 1)' .. LfCR

-- 添加特殊动作
ScenEdit_AddSpecialAction({
    Side="{{SIDE}}",
    ActionNameOrID="{{ACTION_NAME}}",
    description="{{DESCRIPTION}}",
    IsActive=true,
    IsRepeatable=true,
    ScriptText=myScript
})

-- 示例：创建侦察特殊动作
-- local script = '\r\n' ..
--     'local side = ScenEdit_PlayerSide()' .. '\r\n' ..
--     'local units = VP_GetSide({Side=side})' .. '\r\n' ..
--     'for i=1, #units.units do' .. '\r\n' ..
--     '    local u = ScenEdit_GetUnit({guid=units.units[i].guid})' .. '\r\n' ..
--     '    print(u.name .. " - 位置: " .. u.latitude .. ", " .. u.longitude)' .. '\r\n' ..
--     'end' .. '\r\n'
-- 
-- ScenEdit_AddSpecialAction({
--     Side="Blue",
--     ActionNameOrID="scout_action",
--     description="侦察报告 - 显示所有单位位置",
--     IsActive=true,
--     IsRepeatable=true,
--     ScriptText=script
-- })

-- 示例：创建加油特殊动作
-- local refuelScript = '\r\n' ..
--     'local u = ScenEdit_UnitX()' .. '\r\n' ..
--     'if u then' .. '\r\n' ..
--     '    ScenEdit_RefuelUnit({side=u.side, unitname=u.name})' .. '\r\n' ..
--     '    ScenEdit_MsgBox("单位 " .. u.name .. " 开始加油", 1)' .. '\r\n' ..
--     'end' .. '\r\n'
-- 
-- ScenEdit_AddSpecialAction({
--     Side="Blue",
--     ActionNameOrID="refuel_action",
--     description="紧急加油 - 为选中单位加油",
--     IsActive=true,
--     IsRepeatable=true,
--     ScriptText=refuelScript
-- })