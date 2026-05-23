# ScenEdit_SetEvent

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetEvent.html](https://commandlua.github.io/assets/Function_ScenEdit_SetEvent.html)  
> 爬取时间: 2026-05-23 10:35:21  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetEvent
                    (EventDescriptionOrID, options)


This function sets the attributes of an event.
Use the SetEventAction/Trigger/Condition to associate those to the event.


### Parameters

- EventDescriptionOrID
string
Event GUID or Description
- options
{} of
mode =
string
"add", "remove", "update"
Mode to perform
description =
string
Event description
newname =
string
New name for event if renaming the event. Not suggested as it can cause issues if scripts are using event names to perform tasks on.
isActive =
True/False
Event active
isShown =
True/False
Event is shown
IsRepeatable =
True/False
Event can repeat
Probability =
Number 0 -100
Event can repeat
- mode =
string
"add", "remove", "update"
Mode to perform
- description =
string
Event description
- newname =
string
New name for event if renaming the event. Not suggested as it can cause issues if scripts are using event names to perform tasks on.
- isActive =
True/False
Event active
- isShown =
True/False
Event is shown
- IsRepeatable =
True/False
Event can repeat
- Probability =
Number 0 -100
Event can repeat

### Returns


Event
The event wrapper containing the details

`ScenEdit_SetEvent('MyEvent',{mode = 'remove')`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
