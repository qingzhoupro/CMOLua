-- 创建任务模板
-- 变量说明：
-- {{SIDE}} - 阵营名称
-- {{MISSION_NAME}} - 任务名称
-- {{MISSION_TYPE}} - 任务类型：
--   Strike: AIR / LAND / SEA / SUB
--   Patrol: ASW / NAVAL / AAW / LAND / MIXED / SEAD / SEA
--   Support / Ferry / Mining / Mineclearing / Cargo
-- {{SUBTYPE}} - 子类型（可选）
-- {{DESCRIPTION}} - 任务描述（可选）

ScenEdit_AddMission({
    side="{{SIDE}}",
    name="{{MISSION_NAME}}",
    type="{{MISSION_TYPE}}",
    subtype="{{SUBTYPE}}",
    description="{{DESCRIPTION}}"
})

-- 示例：创建空中拦截任务
-- ScenEdit_AddMission({
--     side="Blue",
--     name="CAP - 空中截击",
--     type="Strike",
--     subtype="AIR"
-- })

-- 示例：创建海上巡逻任务
-- ScenEdit_AddMission({
--     side="Blue",
--     name="Sea Patrol",
--     type="Patrol",
--     subtype="NAVAL"
-- })

-- 示例：创建对地打击任务
-- ScenEdit_AddMission({
--     side="Blue",
--     name="Strike Mission",
--     type="Strike",
--     subtype="LAND"
-- })