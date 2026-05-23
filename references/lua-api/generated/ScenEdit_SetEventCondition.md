# ScenEdit_SetEventCondition

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetEventCondition.html](https://commandlua.github.io/assets/Function_ScenEdit_SetEventCondition.html)  
> 爬取时间: 2026-05-23 10:35:34  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetEventCondition
                    (EventDescriptionOrID, options)


This function Sets
                    the
                    Condition
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
Condition description/name or GUID
- mode =
string
"add", "remove", "replace"
Mode to perform
- description =
string
Condition description/name or GUID

### Returns


conditions
{} of
mode
string
Mode performed
xml
string
Condition details in XML - new details if mode is 'add', previous details if mode is 'remove' or 'replace'

- mode
string
Mode performed
- xml
string
Condition details in XML - new details if mode is 'add', previous details if mode is 'remove' or 'replace'
`ScenEdit_SetEventCondition('MyEvent',{mode = 'replace', description = 'MyCondition')`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
