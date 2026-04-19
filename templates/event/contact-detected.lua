-- 接触检测事件模板
-- 参考: CMO_Lua函数_Events.md 和 CMO_Lua函数_Contact.md
-- 变量说明：
-- {{EVENT_NAME}} - 事件名称
-- {{SIDE}} - 监听阵营
-- {{CONTACT_TYPE}} - 接触类型：Air / Surface / Submarine

-- 创建事件
ScenEdit_SetEvent("{{EVENT_NAME}}", {mode="add", IsRepeatable=1})

-- 创建触发器：检测到接触
ScenEdit_SetTrigger({
    mode="add",
    type="UnitDetected",
    name="Contact Detected Trigger",
    side="{{SIDE}}",
    TargetType="{{CONTACT_TYPE}}"
})

-- 获取触发事件的单位（检测者）
local detector = ScenEdit_UnitX()
-- 获取接触本身
local contact = ScenEdit_UnitC()
-- 获取被检测的单位（如果是损坏事件）
local damageSource = ScenEdit_UnitY()

-- 在此处理检测逻辑
if contact then
    print("检测到接触: " .. contact.name)
    print("类型: " .. contact.type)
    print("识别级别: " .. contact.identification_level)
end

-- 关联到事件
ScenEdit_SetEventTrigger("{{EVENT_NAME}}", {mode="add", name="Contact Detected Trigger"})

-- 示例：检测到空中接触时发送消息
-- ScenEdit_SetEvent("Air Contact Detected", {mode="add", IsRepeatable=1})
-- ScenEdit_SetTrigger({
--     mode="add",
--     type="UnitDetected",
--     name="Air Contact",
--     side="Blue",
--     TargetType="Air"
-- })
-- ScenEdit_SetAction({
--     mode="add",
--     type="LuaScript",
--     name="Log Contact",
--     ScriptText='local c = ScenEdit_UnitC()\nScenEdit_SpecialMessage("Blue", "发现空中接触: " .. c.name)'
-- })
-- ScenEdit_SetEventTrigger("Air Contact Detected", {mode="add", name="Air Contact"})
-- ScenEdit_SetEventAction("Air Contact Detected", {mode="add", name="Log Contact"})