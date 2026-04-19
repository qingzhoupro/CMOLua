-- 条件-动作对模板
-- 参考: CMO_Lua函数_Events.md
-- 变量说明：
-- {{EVENT_NAME}} - 事件名称
-- {{CONDITION_TYPE}} - 条件类型
-- {{ACTION_TYPE}} - 动作类型

-- 创建事件
ScenEdit_SetEvent("{{EVENT_NAME}}", {mode="add", IsRepeatable=1})

-- 创建条件
ScenEdit_SetCondition({
    mode="add",
    type="{{CONDITION_TYPE}}",
    name="{{CONDITION_NAME}}",
    -- 根据条件类型添加参数
    side="{{SIDE}}"
})

-- 创建动作
ScenEdit_SetAction({
    mode="add",
    type="{{ACTION_TYPE}}",
    name="{{ACTION_NAME}}",
    ScriptText="{{LUA_SCRIPT}}"
})

-- 关联到事件
ScenEdit_SetEventCondition("{{EVENT_NAME}}", {mode="add", name="{{CONDITION_NAME}}"})
ScenEdit_SetEventAction("{{EVENT_NAME}}", {mode="add", name="{{ACTION_NAME}}"})

-- 常用条件类型：
-- Time - 时间条件
-- UnitDestroyed - 单位被摧毁
-- UnitDamaged - 单位受损
-- UnitDetected - 检测到单位
-- EnteredArea - 进入区域
-- ExitedArea - 离开区域
-- ContactGone - 接触消失
-- WeaponImpact - 武器命中
-- MissionComplete - 任务完成
-- MissionFailed - 任务失败

-- 示例：时间条件 + 发送消息
-- ScenEdit_SetEvent("30分钟情报更新", {mode="add", IsRepeatable=1})
-- ScenEdit_SetCondition({
--     mode="add",
--     type="Time",
--     name="30分钟",
--     Time="30"
-- })
-- ScenEdit_SetAction({
--     mode="add",
--     type="LuaScript",
--     name="情报更新",
--     ScriptText='ScenEdit_SpecialMessage("Blue", "30分钟已过，情报更新")'
-- })
-- ScenEdit_SetEventCondition("30分钟情报更新", {mode="add", name="30分钟"})
-- ScenEdit_SetEventAction("30分钟情报更新", {mode="add", name="情报更新"})

-- 示例：单位摧毁条件 + 扣分
-- ScenEdit_SetEvent("单位损失", {mode="add", IsRepeatable=1})
-- ScenEdit_SetTrigger({
--     mode="add",
--     type="UnitDestroyed",
--     name="蓝方单位被摧毁",
--     side="Blue"
-- })
-- ScenEdit_SetAction({
--     mode="add",
--     type="LuaScript",
--     name="更新分数",
--     ScriptText='local u = ScenEdit_UnitX()\nlocal score = ScenEdit_GetScore(u.side)\nScenEdit_SetScore(u.side, score - 100)'
-- })
-- ScenEdit_SetEventTrigger("单位损失", {mode="add", name="蓝方单位被摧毁"})
-- ScenEdit_SetEventAction("单位损失", {mode="add", name="更新分数"})