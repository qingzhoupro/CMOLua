# ScenEdit_KillUnit

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_KillUnit.html](https://commandlua.github.io/assets/Function_ScenEdit_KillUnit.html)  
> 爬取时间: 2026-05-23 10:33:53  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_KillUnit
                    (table)


This function kills an
                    unit....and
                    triggers any
                    events.


### Parameters

- table
{}
side =
string
The side name/GUID of the unit
unitname =
string
The name of unit
guid =
string
The GUID of the unit
- side =
string
The side name/GUID of the unit
- unitname =
string
The name of unit
- guid =
string
The GUID of the unit

### Returns


True
True if successful, or
nil
otherwise

`nil`
`local a = ScenEdit_KillUnit( { side='SideA', unitname='ship'} )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
