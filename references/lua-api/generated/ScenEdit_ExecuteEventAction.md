# ScenEdit_ExecuteEventAction

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_ExecuteEventAction.html](https://commandlua.github.io/assets/Function_ScenEdit_ExecuteEventAction.html)  
> 爬取时间: 2026-05-23 10:35:44  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_ExecuteEventAction (EventDescriptionOrID)


This function executes an event action Lua script but does not show the results.


### Parameters

- EventDescriptionOrID
string
The description/guid of the event action

### Returns


string
"Ok" on execution or nothing.

`local event = ScenEdit_ExecuteEventAction('My action')`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
