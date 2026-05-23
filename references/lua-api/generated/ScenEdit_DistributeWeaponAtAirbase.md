# ScenEdit_DistributeWeaponAtAirbase

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_DistributeWeaponAtAirbase.html](https://commandlua.github.io/assets/Function_ScenEdit_DistributeWeaponAtAirbase.html)  
> 爬取时间: 2026-05-23 10:34:32  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_DistributeWeaponAtAirbase ( table )


The function's purpose is to distribute a number of weapons across the magazine(s) in a group (typically an airbase)


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
The weapon database ID
number =
number
Number to be added
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
The weapon database ID
- number =
number
Number to be added

### Returns

- None

### Example

`ScenEdit_DistributeWeaponAtAirbase ( { side='NATO', unitname='Hamburg AF', wpn_dbid=773,  number=50} )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
