# Tool_Range

> 官方文档来源: [https://commandlua.github.io/assets/Function_Tool_Range.html](https://commandlua.github.io/assets/Function_Tool_Range.html)  
> 爬取时间: 2026-05-23 10:36:17  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### Tool_Range
                    (fromHere, toHere [,useSlant])


This function returns the
                    range
                    between
                    points,
                    which
                    can
                    be
                    a
                    GUID
                    of
                    a
                    unit/contact
                    or
                    a
                    latitude/longitude (with optional altitude)
                    point.


### Parameters

- fromHere
string
or
{
                            }

                            of
latitude =
latitude
longitude =
longitude
altitude =
altitude
Unit/Contact guid or a location point
- toHere
string
or
{
                            }

                            of
latitude =
latitude
longitude =
longitude
altitude =
altitude
Unit/Contact guid or a location point
- useSlant
true
Optional - calculate the slant distance accounting for altitde instead of the default horizontal distance

### Returns


number
The
                    horizontal/slant
                    distance
                    in
                    NM

`local d = Tool_Range('8269b881-20ce-4f2e-baa0-6823e46d55a4', '004aa55d-d553-428d-a727-26853737c8f4' )`
`local d = Tool_Range( { latitude='33.1991547589118', longitude='138.376876749942' }, '8269b881-20ce-4f2e-baa0-6823e46d55a4')`
`-- variable f and t are two units to measure distance from
local fromHereT = {lat = f.latitude, lon = f.longitude, alt = f.altitude}
local toHereT = {lat = t.latitude, lon = t.longitude, alt = t.altitude}
print(fromHereT); print(toHereT);
local r = Tool_Range(fromHereT, toHereT )
print('Horizontal = ' .. r .. ' NM')
local s = Tool_Range(fromHereT, toHereT, true)
print('Slant = ' .. s .. ' NM')
{ alt = 10972.7998046875, lat = 34.5290743576973, lon = 137.785119524452 }
{ lon = 137.513824433095, lat = 34.446853815832, alt = 9144 }
Horizontal = 14.311404540966 NM
Slant = 14.34543132782 NM`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
