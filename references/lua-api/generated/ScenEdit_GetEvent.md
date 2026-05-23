# ScenEdit_GetEvent

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetEvent.html](https://commandlua.github.io/assets/Function_ScenEdit_GetEvent.html)  
> 爬取时间: 2026-05-23 10:35:22  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetEvent ( EventDescriptionOrID, level )


This function returns the properties of an event; the full set of triggers, conditions and actions, or just limited to a subset.


Level
is optional and defaults to all details if not supplied.

`Level`

The event can be extracted in XML format by adding '10' to the level.
The XML can then be used in
ScenEdit_SetEvent()
to import details into an event


### Parameters

- EventDescriptionOrID
string
The event name/guid to retrieve
- level
number
1 = triggers
2 = conditions
3 = actions
4 = event
The detail to return from the function.

### Returns


Event
The event wrapper containing the details

`local u = ScenEdit_GetEvent( 'Unit destroyed' )`
`local u = ScenEdit_GetEvent( 'Unit destroyed', 3 )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
