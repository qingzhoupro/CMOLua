# ScenEdit_SetZone

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetZone.html](https://commandlua.github.io/assets/Function_ScenEdit_SetZone.html)  
> 爬取时间: 2026-05-23 10:36:11  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetZone
                    (sideName, zoneType, table)


This function updates a
                    non-navigation
                    or
                    exclusion
                    zone for a side.
You only need
                    to
                    pass
                    the
                    parameters that need to be updated.


### Parameters

- sideName
string
Side
                        name/GUID
- zoneType
number
0 = non-navigation, 1 = exclusion, 2 = custom environment, -925 = standard
The type of zone
- table
{
                            }

                            of
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
table {
                                        }
list of core unit types ('SHIP', 'AIRCRAFT', etc) affected
Zone applies to these core unit types
markAs =
posture
Units entering the zone are treated as (posture towards them) [exclusion zone only]
relativeto =
string
The unit name/guid that all the RP(s) relate to, if required
areaColor =
string
The zone color to show as a HTML color code
rename =
string
Description to change zone to
area =
{
                                    }

                                    of multiple
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
type
Fixed (0) or Rotating (1)
Bearing aspect of the reference point
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
table {
                                        }
list of core unit types ('SHIP', 'AIRCRAFT', etc) affected
Zone applies to these core unit types
- markAs =
posture
Units entering the zone are treated as (posture towards them) [exclusion zone only]
- relativeto =
string
The unit name/guid that all the RP(s) relate to, if required
- areaColor =
string
The zone color to show as a HTML color code
- rename =
string
Description to change zone to
- area =
{
                                    }

                                    of multiple
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
type
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
type
Fixed (0) or Rotating (1)
Bearing aspect of the reference point

### Returns


Zone
The update Zone object

`local zone = ScenEdit_SetZone( 'sideA', 0, { rename = 'new zone', affects = {'ship', 'submarine'} } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
