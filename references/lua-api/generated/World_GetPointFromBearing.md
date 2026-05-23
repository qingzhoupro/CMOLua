# World_GetPointFromBearing

> 官方文档来源: [https://commandlua.github.io/assets/Function_World_GetPointFromBearing.html](https://commandlua.github.io/assets/Function_World_GetPointFromBearing.html)  
> 爬取时间: 2026-05-23 10:36:24  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### World_GetPointFromBearing
                    ( table )


This function returns a location (as a set of longitude/latitude) based on bearing and distance from a point.


### Parameters

- table
{
                            }
latitude =
latitude
The latitude of the start point
longitude =
longitude
The longitude of the start point
distance =
number
The distance from the start point (NM)
bearing =
number (0-360)
The Bearing from the start point
- latitude =
latitude
The latitude of the start point
- longitude =
longitude
The longitude of the start point
- distance =
number
The distance from the start point (NM)
- bearing =
number (0-360)
The Bearing from the start point

### Returns

- latitude
latitude
The latitude of the new point
- longitude
longitude
The longitude of the new point
`local new_pos = World_GetPointFromBearing( { latitude = '-37.8307390636104', longitude = '144.932549348204',
distance = 12, bearing = 90 } )
{ Latitude = -37.8304685191991, longitude = 145.184996787893, Longitude = 145.184996787893, latitude = -37.8304685191991 }
-- Note the double entry. The mixed case was an error but not picked up for a few builds
-- lowercase names is the norm, except under specific circumstances`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
