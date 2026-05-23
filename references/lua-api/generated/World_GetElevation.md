# World_GetElevation

> 官方文档来源: [https://commandlua.github.io/assets/Function_World_GetElevation.html](https://commandlua.github.io/assets/Function_World_GetElevation.html)  
> 爬取时间: 2026-05-23 10:36:26  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### World_GetElevation
                    ( table )


This function returns
                    the
                    elevation
                    in
                    meters
                    of
                    a
                    given
                    point


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


number
The elevation of the point in meters. Altitude (+) or depth (-).

`local value = World_GetElevation ( { latitude = '-37.8307390636104', longitude = '144.932549348204' } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
