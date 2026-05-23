# ScenEdit_GetMissions

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetMissions.html](https://commandlua.github.io/assets/Function_ScenEdit_GetMissions.html)  
> 爬取时间: 2026-05-23 10:34:42  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetMissions ( SideNameOrId)


This function retrieves the mission details of a side


### Parameters

- SideNameOrId
string
The side name/guid

### Returns


{
                        }

                        of multiple
Mission
The mission wrapper if the it exists or
nil
otherwise.

`nil`
`local missions = ScenEdit_GetMissions( 'USA' )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
