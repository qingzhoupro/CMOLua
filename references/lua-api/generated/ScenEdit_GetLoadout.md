# ScenEdit_GetLoadout

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetLoadout.html](https://commandlua.github.io/assets/Function_ScenEdit_GetLoadout.html)  
> 爬取时间: 2026-05-23 10:33:57  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetLoadout ( loadoutinfo )


This function retrieves the loadout details of an aircraft.
                    For the aircraft current loadout, use a
loadoutid
=0 or omit it to get the current
                    loadout status (e.g. number of weapons left)

`loadoutid`

UnitX can be used as the
unitname>
if in a triggered event

`unitname>`

### Parameters

- table
{}
unitname =
string
The name/GUID of the unit
LoadoutID =
number
The loadout database id; 0 = use the current loadout
- unitname =
string
The name/GUID of the unit
- LoadoutID =
number
The loadout database id; 0 = use the current loadout

### Returns


Loadout
Loadout wrapper

`local u = ScenEdit_GetLoadout( { unitname='Test flight' } )
if u.weapons[1].wpn_current == 0 then
print( "Out of " .. u.weapons[1].wpn_name)
end`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
