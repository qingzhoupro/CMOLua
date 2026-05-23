# World_GetCircleFromPoint

> 官方文档来源: [https://commandlua.github.io/assets/Function_World_GetCircleFromPoint.html](https://commandlua.github.io/assets/Function_World_GetCircleFromPoint.html)  
> 爬取时间: 2026-05-23 10:36:30  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### World_GetCircleFromPoint
                    ( table )


This function returns
                    a
                    circle
                    around
                    point.


### Parameters

- table
{
                            }
latitude =
latitude
The location of the central point
longitude =
longitude
The location of the central point
numpoints =
number
The number of points to generate on the circle's arc. A minimum of 3 is required
radius =
number
The radius (NM) around the central point
- latitude =
latitude
The location of the central point
- longitude =
longitude
The location of the central point
- numpoints =
number
The number of points to generate on the circle's arc. A minimum of 3 is required
- radius =
number
The radius (NM) around the central point

### Returns

- latitude
latitude
The latitude of a point on the circle
- longitude
longitude
The longitude of a point on the circle
`local circle = World_GetCircleFromPoint( { latitude = '-37.8307390636104', longitude = '144.932549348204', numpoints = 12, radius = 50 } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
