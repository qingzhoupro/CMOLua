# ScenEdit_SetEventTrigger

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetEventTrigger.html](https://commandlua.github.io/assets/Function_ScenEdit_SetEventTrigger.html)  
> 爬取时间: 2026-05-23 10:35:32  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetEventTrigger
                    (EventDescriptionOrID,options)


This function Sets
                    the
                    Trigger
                    of
                    an Event.


### Parameters

- EventDescriptionOrID
string
Event GUID or Description
- options
{} of
mode =
string
"add", "remove", "replace"
Mode to perform
description =
string
Trigger description/name or GUID
- mode =
string
"add", "remove", "replace"
Mode to perform
- description =
string
Trigger description/name or GUID

### Returns


triggers
{} of
mode
string
Mode performed
xml
string
Trigger details in XML - new details if mode is 'add', previous details if mode is 'remove' or 'replace'

- mode
string
Mode performed
- xml
string
Trigger details in XML - new details if mode is 'add', previous details if mode is 'remove' or 'replace'
`ScenEdit_SetEventTrigger('MyEvent',{mode = 'add', description = 'MyNewTrigger')`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
