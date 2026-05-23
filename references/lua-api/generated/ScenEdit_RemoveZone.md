# ScenEdit_RemoveZone

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_RemoveZone.html](https://commandlua.github.io/assets/Function_ScenEdit_RemoveZone.html)  
> 爬取时间: 2026-05-23 10:36:13  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_RemoveZone
                    (sideName, zoneType, table)


This function removes a
                    no-nav
                    or
                    exclusion
                    zone.


The RPs attached to the zone will also be removed as they are unique to the zone.


### Parameters

- sideName
string
The Side
                        name/GUID that owes the zone. Custom environment zones always belong to the Nature side.
- zoneType
number
0 = non-navigation, 1 = exclusion, 2 = custom environment, -925 = standard
The Type
                        of
                        zone
                        to
                        remove
- table
{}
Description =
string
The Zone GUID or Name or Description to identify it
- Description =
string
The Zone GUID or Name or Description to identify it

### Returns


Zone
A zone wrapper for the removed Zone

`local oldZone = ScenEdit_RemoveZone( 'Red', 0, { Description = 'my zone' } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
