# ScenEdit_AddReloadsToUnit

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_AddReloadsToUnit.html](https://commandlua.github.io/assets/Function_ScenEdit_AddReloadsToUnit.html)  
> 爬取时间: 2026-05-23 10:34:07  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_AddReloadsToUnit (table)


This function adds, removes or fills out weapon reloads on a local mount of an unit, rather than be applied to the unit's magazine.
You can specify a particular `mount` by the GUID, or omit it and the function will try to apply the request to any `available` mounts with the `weapon`.


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
wpn_dbid =
number
The weapon database ID to be updated **MANDATORY**
mount_guid =
string
The mount GUID on the unit to be updated
number =
number
Number to be added or removed
remove =
True/False
If true, this will debuct the number of weapons from the unit/mount
fillout =
True/False
If true, this will fill out the weapon record to its maximum. The 'number' doesn't apply.
addascell =
True/False
Default true. If false, add only one weapon to a cell
- side =
string
The side name/GUID of the unit
- unitname =
string
The name of unit
- guid =
string
The GUID of the unit
- wpn_dbid =
number
The weapon database ID to be updated **MANDATORY**
- mount_guid =
string
The mount GUID on the unit to be updated
- number =
number
Number to be added or removed
- remove =
True/False
If true, this will debuct the number of weapons from the unit/mount
- fillout =
True/False
If true, this will fill out the weapon record to its maximum. The 'number' doesn't apply.
- addascell =
True/False
Default true. If false, add only one weapon to a cell

### Returns


number
The number of items added or removed

`ScenEdit_AddReloadsToUnit( { side='NATO', unitname='Mech Inf #1', wpn_dbid=773, number=1 } )`
`ScenEdit_AddReloadsToUnit( { side='NATO', unitname='Mech Inf #1', wpn_dbid=773, mount_guid='GNRIJH-0HM7B6IC7IPUR', number=5, remove=true } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
