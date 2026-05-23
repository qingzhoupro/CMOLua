# ScenEdit_GetTimeOfDay

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetTimeOfDay.html](https://commandlua.github.io/assets/Function_ScenEdit_GetTimeOfDay.html)  
> 爬取时间: 2026-05-23 10:36:49  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetTimeOfDay ( table )


This function retrieves the current time of day at a location
The location can be an unit (guid or side/name) or a position (latitude,longitude).
Only one pair is required to identify the location for the TimeOfDay.


### Parameters

- table
{}
side =
string
Side name/guid
unitname =
string
Unit name
guid =
string
Unit guid
latitude =
string
Unit guid
longitude =
string
Unit guid
- side =
string
Side name/guid
- unitname =
string
Unit name
- guid =
string
Unit guid
- latitude =
string
Unit guid
- longitude =
string
Unit guid

### Returns

- tod
number
Time of day number [0=Day, 2=Night, 3=Dawn, 4=Dusk]
- localtime
string
Local time
- zulutime
string
Local time
- TOD
string
Time of day text
`local u = ScenEdit_GetTimeOfDay( {side='NATO', unitname='FFG Dispair'} )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
