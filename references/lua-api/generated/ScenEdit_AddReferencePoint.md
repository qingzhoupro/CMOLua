# ScenEdit_AddReferencePoint

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_AddReferencePoint.html](https://commandlua.github.io/assets/Function_ScenEdit_AddReferencePoint.html)  
> 爬取时间: 2026-05-23 10:35:59  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_AddReferencePoint (table)


This function creates one or more reference point(s) as defined by the table.


It can take a single new referrnce point, or a table of new reference points. The table
must
contain at least a side, and one set of latitude and longitude, or the side and an area defined by one or more latitude and longitude values.
This is mainly because Reference Points are recorded by side; the same named RP might exist on more than one side which can lead to confusion.
Points can also be relative to a specified unit based on bearing and distance. This applies to ALL the rp(s) in the function call, and the unit name/GUID that the RP(s) are relative to has to be on the same side.


### Parameters

- table
{}
The reference point details to be created.
*** Note that the area is only required if you are adding more than one RP in one go.
area =
{} of multiple
bearing =
number (0-360)
Bearing from the 'relative' unit
bearingtype =
bearing
Fixed (0) or Rotating (1)
Bearing aspect of the reference point
color =
string
The color name or HTML code to mark the new reference point
distance =
distance
Distance from the 'relative' unit
highlighted =
True/False
True if the reference point should be selected
latitude =
latitude
The latitude of the new reference point
locked =
True/False
True if the reference point is locked
longitude =
longitude
The longitude of the new reference point
name =
string
The name of the new reference point
bearing =
number (0-360)
Bearing from the 'relative' unit
bearingtype =
bearing
Fixed (0) or Rotating (1)
Bearing aspect of the reference point
color =
string
The color name or HTML code to mark the new reference point
distance =
distance
Distance from the 'relative' unit
highlighted =
True/False
True if the reference point should be selected
latitude =
latitude
The latitude of the new reference point
locked =
True/False
True if the reference point is locked
longitude =
longitude
The longitude of the new reference point
name =
string
The name of the new reference point
relativeto =
string
The unit name/guid that all the RP(s) relate to, if required
relativeto_contact =
string
The contact name/guid that all the RP(s) relate to, if required
relativeto_rp =
string
The RP name/guid that all the RP(s) relate to, if required
side =
string
The side the reference point is visible to
- bearing =
number (0-360)
Bearing from the 'relative' unit
- bearingtype =
bearing
Fixed (0) or Rotating (1)
Bearing aspect of the reference point
- color =
string
The color name or HTML code to mark the new reference point
- distance =
distance
Distance from the 'relative' unit
- highlighted =
True/False
True if the reference point should be selected
- latitude =
latitude
The latitude of the new reference point
- locked =
True/False
True if the reference point is locked
- longitude =
longitude
The longitude of the new reference point
- name =
string
The name of the new reference point

### Returns


ReferencePoint
A reference point wrapper for the new reference point, or the last one in the area if supplied.

`ScenEdit_AddReferencePoint( {side="United States", name="Downed Pilot", latitude=0.1, longitude=4, highlighted=true, color='red' } )`
`ScenEdit_AddReferencePoint( {side='sidea', RelativeTo='USN Dewey', bearing=45 ,distance=20, clear=true } )`
`ScenEdit_AddReferencePoint( {side="United States", name="Downed Pilot Area", area = { {latitude=10, longitude=4, highlighted=true},
{latitude=15, longitude=4, highlighted=true}, {latitude=20, longitude=4} } } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
