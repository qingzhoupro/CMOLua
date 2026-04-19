-- 获取单位信息模板
-- 参考: https://commandops.github.io/ 和 CMO_Lua函数_Unit.md

-- 获取单位（方式1：通过名称和阵营）
local unit = ScenEdit_GetUnit({
    side="{{SIDE}}",
    unitname="{{UNIT_NAME}}"
})

-- 获取单位（方式2：通过 GUID）
-- local unit = ScenEdit_GetUnit({
--     guid="{{UNIT_GUID}}"
-- })

-- 检查单位是否存在
if unit == nil then
    print("单位未找到: {{UNIT_NAME}}")
else
    -- 打印基本信息
    print("=== 单位信息 ===")
    print("名称: " .. unit.name)
    print("类型: " .. unit.type)
    print("阵营: " .. unit.side)
    print("DBID: " .. unit.dbid)
    print("等级: " .. unit.class)
    print("熟练度: " .. unit.proficiency)
    
    -- 位置信息
    print("\n=== 位置 ===")
    print("纬度: " .. unit.latitude)
    print("经度: " .. unit.longitude)
    print("高度: " .. unit.altitude)
    print("航向: " .. unit.heading)
    print("速度: " .. unit.speed)
    
    -- 状态信息
    print("\n=== 状态 ===")
    print("状态: " .. unit.unitstate)
    print("燃油状态: " .. unit.fuelstate)
    print("武器状态: " .. unit.weaponstate)
    
    -- 如果是飞机，检查挂载
    if unit.type == "Aircraft" then
        local loadout = ScenEdit_GetLoadout({unitname=unit.name})
        if loadout then
            print("\n=== 挂载 ===")
            for k, v in pairs(loadout.weapons) do
                print(v.wpn_name .. ": " .. v.wpn_current .. "/" .. v.wpn_max)
            end
        end
    end
    
    -- 如果是舰艇/潜艇，检查燃油
    if unit.fuel then
        print("\n=== 燃油 ===")
        for k, v in pairs(unit.fuel) do
            print(v.name .. ": " .. math.floor(v.current) .. "/" .. v.max)
        end
    end
end

-- 示例：获取并显示所有信息
-- local u = ScenEdit_GetUnit({
--     side="Blue",
--     unitname="F-16 #1"
-- })
-- if u then
--     print("F-16 #1 - 纬度: " .. u.latitude .. ", 速度: " .. u.speed)
-- end