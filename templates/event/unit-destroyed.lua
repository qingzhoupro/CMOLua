-- 单位被摧毁事件模板
-- 触发条件：当单位被摧毁时

-- 获取触发事件的单位
local destroyed_unit = ScenEdit_UnitX()

-- 检查单位是否存在（可能已被删除）
if destroyed_unit ~= nil then
    -- 输出日志
    print("[单位被摧毁] " .. destroyed_unit.name .. 
          " (" .. destroyed_unit.classname .. 
          ") 由 " .. destroyed_unit.side)
    
    -- 发送特殊消息
    ScenEdit_SpecialMessage(destroyed_unit.side, 
        "<h3>单位损失</h3>" ..
        "<p>" .. destroyed_unit.name .. " 已被摧毁</p>")
    
    -- 示例：如果是特定单位类型
    -- if destroyed_unit.type == "Ship" then
    --     print("舰艇损失: " .. destroyed_unit.name)
    -- end
    
    -- 示例：更新分数
    -- local currentScore = ScenEdit_GetScore(destroyed_unit.side)
    -- ScenEdit_SetScore(destroyed_unit.side, currentScore - 100)
end