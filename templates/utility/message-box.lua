-- 消息框模板

-- 变量说明：
-- {{MESSAGE}} - 消息内容（支持 HTML）
-- {{BUTTONS}} - 按钮数量：1=确定, 2=确定/取消

ScenEdit_MsgBox("{{MESSAGE}}", {{BUTTONS}})

-- 示例：简单消息
-- ScenEdit_MsgBox("任务完成！", 1)

-- 示例：HTML 格式消息
-- ScenEdit_MsgBox("<h2>情报报告</h2><p>发现敌方舰艇</p>", 1)

-- 示例：确认对话框
-- ScenEdit_MsgBox("确认执行攻击？", 2)