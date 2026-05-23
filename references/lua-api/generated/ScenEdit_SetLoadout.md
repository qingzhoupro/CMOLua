# ScenEdit_SetLoadout

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetLoadout.html](https://commandlua.github.io/assets/Function_ScenEdit_SetLoadout.html)  
> 爬取时间: 2026-05-23 10:33:55  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetLoadout
                    (table)


This function Sets
                    the
                    loadout
                    for
                    a aircraft
                    unit


### Parameters

- table
{} of
unitname =
string
Unit description/name or GUID to update. Can use 'UnitX' here if in an Event Action
LoadoutID =
number
The ID of the new loadout; 0 = use the current loadout
TimeToReady_Minutes =
number
How many minutes until the loadout is ready (default = database loadout time) (_optional_)
IgnoreMagazines =
True/False
If the new loadout should rely on the magazines having the right weapons ready (default = false) (_optional_)
ExcludeOptionalWeapons =
True/False
Exclude optional weapons from loadout (default = false) (_optional_)
Wpn_DBID =
number
Weapon DB number - required if WPN_GUID is not supplied
Wpn_GUID =
string
Actual weapon to update - DBID is not required as this take precedence (_optional_)
Number =
number
Number to change current weapon load by (sign ignored)
Remove =
True/False
Deduct 'number' rather than add
- unitname =
string
Unit description/name or GUID to update. Can use 'UnitX' here if in an Event Action
- LoadoutID =
number
The ID of the new loadout; 0 = use the current loadout
- TimeToReady_Minutes =
number
How many minutes until the loadout is ready (default = database loadout time) (_optional_)
- IgnoreMagazines =
True/False
If the new loadout should rely on the magazines having the right weapons ready (default = false) (_optional_)
- ExcludeOptionalWeapons =
True/False
Exclude optional weapons from loadout (default = false) (_optional_)
- Wpn_DBID =
number
Weapon DB number - required if WPN_GUID is not supplied
- Wpn_GUID =
string
Actual weapon to update - DBID is not required as this take precedence (_optional_)
- Number =
number
Number to change current weapon load by (sign ignored)
- Remove =
True/False
Deduct 'number' rather than add

### Returns


boolean
True

`ScenEdit_SetLoadout( {unitname=....} )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
