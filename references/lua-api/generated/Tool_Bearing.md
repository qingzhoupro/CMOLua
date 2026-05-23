# Tool_Bearing

> 官方文档来源: [https://commandlua.github.io/assets/Function_Tool_Bearing.html](https://commandlua.github.io/assets/Function_Tool_Bearing.html)  
> 爬取时间: 2026-05-23 10:36:19  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### Tool_Bearing
                    ( fromHere, toHere)


This function returns the
                    bearing
                    between
                    two points,
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
                    latitude/longitude
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
Unit/Contact guid or a location point

### Returns


number (0-360)
The
                    bearing from 'here' to 'there'.

`local b = Tool_Bearing('8269b881-20ce-4f2e-baa0-6823e46d55a4', '004aa55d-d553-428d-a727-26853737c8f4' )`
`local b = Tool_Bearing( { latitude='33.1991547589118', longitude='138.376876749942' }, '8269b881-20ce-4f2e-baa0-6823e46d55a4' )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
