-- 创建参考点模板
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{RP_NAME}} - 参考点名称
-- {{LATITUDE}} - 纬度
-- {{LONGITUDE}} - 经度
-- {{HIGHLIGHTED}} - 是否高亮：true / false

ScenEdit_AddReferencePoint({
    side="{{SIDE}}",
    name="{{RP_NAME}}",
    lat="{{LATITUDE}}",
    lon="{{LONGITUDE}}",
    highlighted={{HIGHLIGHTED}}
})

-- 示例：创建多个参考点
-- ScenEdit_AddReferencePoint({side="Blue", name="RP-1", lat="35.0", lon="129.0", highlighted=true})
-- ScenEdit_AddReferencePoint({side="Blue", name="RP-2", lat="35.1", lon="129.1", highlighted=true})
-- ScenEdit_AddReferencePoint({side="Blue", name="RP-3", lat="35.1", lon="129.0", highlighted=true})
-- ScenEdit_AddReferencePoint({side="Blue", name="RP-4", lat="35.0", lon="129.1", highlighted=true})

-- 示例：创建相对参考点
-- ScenEdit_AddReferencePoint({
--     side="Blue",
--     name="RP-5",
--     RelativeTo="RP-1",  -- 相对于 RP-1
--     bearing=90,         -- 方位角（度）
--     distance=10,        -- 距离（海里）
--     highlighted=true
-- })