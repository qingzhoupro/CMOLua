# ScenEdit_CreateMissionFlightPlan

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_CreateMissionFlightPlan.html](https://commandlua.github.io/assets/Function_ScenEdit_CreateMissionFlightPlan.html)  
> 爬取时间: 2026-05-23 10:34:49  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_CreateMissionFlightPlan
                    (SideName, MissionName, options)


This function creates flights for a mission.


### Parameters

- SideName
string
The mission side
- MissionName
string
The mission name/guid
- options
{} of
DATEONTARGET =
string
The mission time on target day, YYYY/MM/DD
TIMEONTARGET  =
string
The mission time on target, HH:MM:SS
or
TAKEOFFDATE =
string
The mission takeoff day, YYYY/MM/DD
TAKEOFFTIME  =
string
The mission takeoff time, HH:MM:SS
- DATEONTARGET =
string
The mission time on target day, YYYY/MM/DD
- TIMEONTARGET  =
string
The mission time on target, HH:MM:SS
- TAKEOFFDATE =
string
The mission takeoff day, YYYY/MM/DD
- TAKEOFFTIME  =
string
The mission takeoff time, HH:MM:SS

### Returns

- Returns all the flights on the mission.
Currently only returns the first flight, will be fixed in a upcoming release.

### Example

`ScenEdit_CreateMissionFlightPlan('Blue', 'Strike', {DATEONTARGET = '2025/08/01', TIMEONTARGET = '12:00:00'})`

### Example

`ScenEdit_CreateMissionFlightPlan('Blue', 'Strike', {TAKEOFFDATE = '2025/08/01', TAKEOFFTIME = '08:00:00'})`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
