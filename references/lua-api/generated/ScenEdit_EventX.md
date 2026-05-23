# ScenEdit_EventX

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_EventX.html](https://commandlua.github.io/assets/Function_ScenEdit_EventX.html)  
> 爬取时间: 2026-05-23 10:35:52  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_EventX ()


This function shows the current event that has been triggered.


Note that EventX() can also be used as a shortcut for ScenEdit_EventX()


### Parameters


### Returns


Event
The triggering event as a wrapper, else a
nil
is returned.

`nil`

Within a condition or action script of some event, include 'local myVar = ScenEdit_EventX()' to be able to interpret the triggering event.
Say you want to see the actions that this triggered event performs, in case you want to stop it from running again.
You would look at the table 'myVar.actions'.
If you wanted to turn off the event, then add 'myVar.isActive = false' to your script.

`local
a = ScenEdit_EventX()`

Changing the probability of the current event
... inside the Event Action script...
local a = ScenEdit_EventX()
if a.probability > 50 then
a.probability = probability - 10 -- decrease chance this event will happen again
end
...

`... inside the Event Action script...
local a = ScenEdit_EventX()
if a.probability > 50 then
a.probability = probability - 10 -- decrease chance this event will happen again
end
...`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
