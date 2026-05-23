# ScenEdit_AddZone

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_AddZone.html](https://commandlua.github.io/assets/Function_ScenEdit_AddZone.html)  
> 爬取时间: 2026-05-23 10:36:09  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_AddZone (sideName, zoneType, table)


This function creates a non-navigation or exclusion zone.
The Reference Points are normally visible to the side. They can start out 'hidden' by adding 'hidden=1' to the table options.


### Parameters

- table
{}
sideName =
string
The Side name/GUID. Custom environment zones are always added to the Nature side.
zoneType =
number
0 = non-navigation, 1 = exclusion, 2 = custom environment, -925 = standard
The type of zone to add
description =
string
The Zone name
isactive =
True/False
Is the zone active?
locked =
True/False
Are Zone RPs locked?
hidden =
True/False
Are Zone RPs hidden?
affects =
table {}
list of core unit types ('SHIP', 'AIRCRAFT', etc) affected
Zone applies to these core unit types
markAs =
posture
Units entering the zone are treated as (posture towards them) [exclusion zone only]
relativeto =
string
The unit name/guid that all the RP(s) relate to, if required
area =
{} of multiple
The area defining the zone
name =
string
The name of the new reference point
latitude =
latitude
The latitude of the new reference point
longitude =
longitude
The longitude of the new reference point
highlighted =
True/False
True if the reference point should be selected
locked =
True/False
True if the reference point is locked
distance =
distance
Distance from the 'relative' unit
bearing =
number (0-360)
Bearing from the 'relative' unit
bearingtype =
bearing
Fixed (0) or Rotating (1)
Bearing aspect of the reference point
- sideName =
string
The Side name/GUID. Custom environment zones are always added to the Nature side.
- zoneType =
number
0 = non-navigation, 1 = exclusion, 2 = custom environment, -925 = standard
The type of zone to add
- description =
string
The Zone name
- isactive =
True/False
Is the zone active?
- locked =
True/False
Are Zone RPs locked?
- hidden =
True/False
Are Zone RPs hidden?
- affects =
table {}
list of core unit types ('SHIP', 'AIRCRAFT', etc) affected
Zone applies to these core unit types
- markAs =
posture
Units entering the zone are treated as (posture towards them) [exclusion zone only]
- relativeto =
string
The unit name/guid that all the RP(s) relate to, if required
- area =
{} of multiple
The area defining the zone
name =
string
The name of the new reference point
latitude =
latitude
The latitude of the new reference point
longitude =
longitude
The longitude of the new reference point
highlighted =
True/False
True if the reference point should be selected
locked =
True/False
True if the reference point is locked
distance =
distance
Distance from the 'relative' unit
bearing =
number (0-360)
Bearing from the 'relative' unit
bearingtype =
bearing
Fixed (0) or Rotating (1)
Bearing aspect of the reference point
- name =
string
The name of the new reference point
- latitude =
latitude
The latitude of the new reference point
- longitude =
longitude
The longitude of the new reference point
- highlighted =
True/False
True if the reference point should be selected
- locked =
True/False
True if the reference point is locked
- distance =
distance
Distance from the 'relative' unit
- bearing =
number (0-360)
Bearing from the 'relative' unit
- bearingtype =
bearing
Fixed (0) or Rotating (1)
Bearing aspect of the reference point

### Returns


Zone
The zone as a wrapper

`local a = ScenEdit_AddZone('sidea', 1, {description='excluding',affects={'ship'},
area={ {latitude = '34.2833063729007', longitude = '138.371434386706', name = 'RP-3136'},
{ latitude = '34.2751713567346', longitude = '139.122576855883', name = 'RP-3137'},
{ latitude = '33.823657691087', longitude = '139.111731172117', name = 'RP-3138' },
{ latitude = '33.8329383336795', longitude = '138.36485402628', name = 'RP-3139'}},
markas='unfriendly' } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
