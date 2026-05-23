# ScenEdit_SetTime

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetTime.html](https://commandlua.github.io/assets/Function_ScenEdit_SetTime.html)  
> 爬取时间: 2026-05-23 10:36:53  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetTime
                    ( table )


This function Sets
                    the current
                    scenario
                    date/time, but allows the scenario start data to be updated as well.
Note the default format ('MM.DD.YYYY') for the public release, differs from the default mode ('DD.MM.YYYY') in the professional release.
If a scenario wants to be used between both releases, the new DATEFORMAT parameter should used to define the date passed.


### Parameters

- table
{
                            }

                            of
dateformat =
string
Formats are: 'DDMMYYYY' or 'MMDDYYYY' or 'YYYYMMDD' Note that they need to be
uppercase
.
The default format for Public versions is 'MMDDYYYY', while the Professional versions use 'DDMMYYYY' if this parameter is not supplied.
date =
string
Scenario current date as per the date format
'DD.MM.YYYY' or 'MM.DD.YYYY' or 'YYYY.MM.DD' The delimiter '.' can also be a ':'
time =
string
Scenario current time as 'HH:MM:SS' or 'HH.MM.SS'
StartDate =
string
Scenario start date as 'DD:MM:YYYY' or 'DD.MM.YYYY'.
StartTime =
string
Sceanrio start time as 'HH:MM:SS' or 'HH.MM.SS'
Duration =
string
Length of scenario as 'days:hours:minutes'
- dateformat =
string
Formats are: 'DDMMYYYY' or 'MMDDYYYY' or 'YYYYMMDD' Note that they need to be
uppercase
.
The default format for Public versions is 'MMDDYYYY', while the Professional versions use 'DDMMYYYY' if this parameter is not supplied.
- date =
string
Scenario current date as per the date format
'DD.MM.YYYY' or 'MM.DD.YYYY' or 'YYYY.MM.DD' The delimiter '.' can also be a ':'
- time =
string
Scenario current time as 'HH:MM:SS' or 'HH.MM.SS'
- StartDate =
string
Scenario start date as 'DD:MM:YYYY' or 'DD.MM.YYYY'.
- StartTime =
string
Sceanrio start time as 'HH:MM:SS' or 'HH.MM.SS'
- Duration =
string
Length of scenario as 'days:hours:minutes'

### Returns


number
Scenario current time in seconds

`ScenEdit_SetTime({Date=
"2.12.2007"
, Time=
"22.46.23"
})`
`ScenEdit_SetTime({DateFormat= "DDMMYYYY", Date=
"2.12.2007"
, Time=
"22.46.23"
})`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
