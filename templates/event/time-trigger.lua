-- 时间触发器模板
-- 变量说明：
-- {{MINUTES}} - 触发时间（分钟）
-- {{SIDE}} - 接收消息的阵营
-- {{MESSAGE}} - 消息内容

-- 使用事件系统创建时间触发器
ScenEdit_SetEvent("Timer Event", {mode="add", IsRepeatable=1})

-- 创建时间触发器
ScenEdit_SetTrigger({
    mode="add",
    type="Time",
    name="Timer Trigger",
    Time="{{MINUTES}}"  -- 分钟数
})

-- 创建动作（发送消息）
ScenEdit_SetAction({
    mode="add",
    type="LuaScript",
    name="Timer Action",
    scriptText='ScenEdit_SpecialMessage("{{SIDE}}", "{{MESSAGE}}")'
})

-- 关联触发器和动作到事件
ScenEdit_SetEventTrigger("Timer Event", {mode="add", name="Timer Trigger"})
ScenEdit_SetEventAction("Timer Event", {mode="add", name="Timer Action"})

-- 示例：30分钟后发送消息
-- ScenEdit_SetEvent("30 Minute Alert", {mode="add", IsRepeatable=1})
-- ScenEdit_SetTrigger({mode="add", type="Time", name="30min", Time="30"})
-- ScenEdit_SetAction({mode="add", type="LuaScript", name="30min Action", 
--     scriptText='ScenEdit_SpecialMessage("Blue", "30 minutes elapsed!")'})
-- ScenEdit_SetEventTrigger("30 Minute Alert", {mode="add", name="30min"})
-- ScenEdit_SetEventAction("30 Minute Alert", {mode="add", name="30min Action"})