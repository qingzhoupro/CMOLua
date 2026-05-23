# VP_GetSide

> 官方文档来源: [https://commandlua.github.io/assets/Function_VP_GetSide.html](https://commandlua.github.io/assets/Function_VP_GetSide.html)  
> 爬取时间: 2026-05-23 10:35:11  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### VP_GetSide
                    ( table )


This function returns the Side
                    object
                    from
                    the
                    perspective
                    of
                    the
                    player.


### Parameters

- table
{
                            }
side =
string
The name of the side
guid =
string
The GUID of the side
- side =
string
The name of the side
- guid =
string
The GUID of the side

### Returns


Side
The side object

`local side = VP_GetSide( { Side ='sidea' } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
