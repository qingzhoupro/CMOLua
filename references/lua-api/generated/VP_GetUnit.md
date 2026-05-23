# VP_GetUnit

> 官方文档来源: [https://commandlua.github.io/assets/Function_VP_GetUnit.html](https://commandlua.github.io/assets/Function_VP_GetUnit.html)  
> 爬取时间: 2026-05-23 10:35:13  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### VP_GetUnit
                    ( table )


This function returns
                    information
                    about
                    an
                    active
                    unit
                    or
                    a contact's actual unit.


### Parameters

- table
{
                            }
side =
string
The side name/GUID of the unit
unitname =
string
The name of unit or contact
guid =
string
The GUID of the unit or contact
- unitname =
string
The name of unit or contact
- guid =
string
The GUID of the unit or contact

### Returns


Unit
The
                    wrapper of
                    the
                    unit. If a 'contact' was passed, then this is the 'actual' unit.

`local unit = VP_GetUnit( { guid = 'f4f9e0af-15c2-4582-8e80-b827c2ec2f56' } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
