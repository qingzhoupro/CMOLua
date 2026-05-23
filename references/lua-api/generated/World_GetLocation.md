# World_GetLocation

> 官方文档来源: [https://commandlua.github.io/assets/Function_World_GetLocation.html](https://commandlua.github.io/assets/Function_World_GetLocation.html)  
> 爬取时间: 2026-05-23 10:36:28  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### World_GetLocation
                    ( table )


This function returns details of a given position. These details are similar to what is shown by the map cursor box.


### Parameters

- table
{
                            }
latitude =
latitude
The latitude of the point
longitude =
longitude
The longitude of the point
- latitude =
latitude
The latitude of the point
- longitude =
longitude
The longitude of the point

### Returns

- altitude
number
Altitude (+) or depth (-)
- layer
{
                            }

                            of
Layer information
ceiling
number
floor
number
strength
number
- cz
{
                            }

                            of
Convergence zone information
1
number
2
number
3
number
4
number
- slope
number
The slope rating (0 - 100)
- cover
{
                            }

                            of
Cover information
text
string
The description of the cover at location
value
number
The numeric value of the cover at location (need table of value/description)
- ceiling
number
- floor
number
- strength
number
- 1
number
- 2
number
- 3
number
- 4
number
- text
string
The description of the cover at location
- value
number
The numeric value of the cover at location (need table of value/description)
`local position_data = World_GetLocation ( { latitude = '-37.8307390636104', longitude = '144.932549348204' } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
