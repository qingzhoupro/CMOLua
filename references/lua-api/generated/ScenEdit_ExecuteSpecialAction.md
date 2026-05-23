# ScenEdit_ExecuteSpecialAction

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_ExecuteSpecialAction.html](https://commandlua.github.io/assets/Function_ScenEdit_ExecuteSpecialAction.html)  
> 爬取时间: 2026-05-23 10:38:41  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_ExecuteSpecialAction (eventNameOrId)


This function executes a Lua Special action script but does not show results.


### Parameters

- eventNameOrId
string
The name/guid of the event action

### Returns


string
"Ok" on execution or nothing.

`local event = ScenEdit_ExecuteSpecialAction('My action')`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
