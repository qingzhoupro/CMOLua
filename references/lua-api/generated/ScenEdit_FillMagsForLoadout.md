# ScenEdit_FillMagsForLoadout

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_FillMagsForLoadout.html](https://commandlua.github.io/assets/Function_ScenEdit_FillMagsForLoadout.html)  
> 爬取时间: 2026-05-23 10:34:10  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_FillMagsForLoadout (table, loadoutid,  quantity)


This function adds to a unit's magazine(s) the aircraft stores in the loadout.


### Parameters

- table
{}
side =
string
The side name/guid of the unit
unitname =
string
The unit name/guid with the magazine
guid =
string
The unit name/guid with the magazine
- loadoutid
number
The database id of the loadout
- quantity
number
The number of 'packs' in the loadout to add
- side =
string
The side name/guid of the unit
- unitname =
string
The unit name/guid with the magazine
- guid =
string
The unit name/guid with the magazine

### Returns


Table {} of
string
A table of success/failure messages from adding the stores

`ScenEdit_FillMagsForLoadout(
{unit='
RAF Lakenheath
', loadoutid=45162, quantity=12}
)`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
