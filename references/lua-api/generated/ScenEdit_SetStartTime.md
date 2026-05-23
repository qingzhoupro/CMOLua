# ScenEdit_SetStartTime

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetStartTime.html](https://commandlua.github.io/assets/Function_ScenEdit_SetStartTime.html)  
> 爬取时间: 2026-05-23 10:36:51  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetStartTime
                    ( table )


This function Sets
                    the
                    scenario start
                    date/time.
The default format of the date is MMDDYYYY. It can be changed by using the 'dateformat' parameter.


### Parameters

- table
{} of
date =
string
Scenario start date as 'MM:DD:YYYY' or 'MM.DD.YYYY'.
time =
string
Scenario start time as 'HH:MM:SS' or 'HH.MM.SS'
duration =
string
Length of scenario as 'days:hours:minutes'
dateformat =
value
"DDMMYYYY"
"MMDDYYYY"
"YYYYMMDD"
Overriding format of the date

| date = | string | Scenario start date as 'MM:DD:YYYY' or 'MM.DD.YYYY'. |
| --- | --- | --- |
| time = | string | Scenario start time as 'HH:MM:SS' or 'HH.MM.SS' |
| duration = | string | Length of scenario as 'days:hours:minutes' |
| dateformat = | value"DDMMYYYY""MMDDYYYY""YYYYMMDD" | Overriding format of the date |


### Returns


number
Scenario start time in seconds

`ScenEdit_SetStartTime({Date=
"2.12.2007"
, Time=
"22.46.23"
, Duration=
"60.5:0:0"
})`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
