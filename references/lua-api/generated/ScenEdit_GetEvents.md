# ScenEdit_GetEvents

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetEvents.html](https://commandlua.github.io/assets/Function_ScenEdit_GetEvents.html)  
> 爬取时间: 2026-05-23 10:35:24  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetEvents (level)


This function returns the properties of all event; the full set of triggers, conditions and actions, or just limited to a subset.


Level
is optional and defaults to all details if not supplied.

`Level`

### Parameters

- level
number
1 = triggers
2 = conditions
3 = actions
4 = event
The detail to return from the function.

### Returns


Table {} of
Event
Event wrappers

`local u = ScenEdit_GetEvents( 1 )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
