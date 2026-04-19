-- 创建阵营模板
-- 变量说明：
-- {{SIDE_NAME}} - 阵营名称
-- {{AWARENESS}} - 感知级别：Normal / Blind / AutoSideID / AutoSideAndUnitID / Omniscient
-- {{PROFICIENCY}} - 熟练度：Novice / Cadet / Regular / Veteran / Ace
-- {{POSTURE}} - 态度：H (Hostile) / F (Friendly) / N (Neutral) / U (Unfriendly)

-- 创建阵营
ScenEdit_AddSide({name="{{SIDE_NAME}}"})

-- 设置阵营选项
ScenEdit_SetSideOptions({
    side="{{SIDE_NAME}}",
    awareness="{{AWARENESS}}",
    proficiency="{{PROFICIENCY}}"
})

-- 如果需要设置与其他阵营的关系
-- ScenEdit_SetSidePosture("{{SIDE_NAME}}", "OtherSide", "{{POSTURE}}")

-- 示例用法：
-- ScenEdit_AddSide({name="Blue"})
-- ScenEdit_SetSideOptions({side="Blue", awareness="Normal", proficiency="Regular"})