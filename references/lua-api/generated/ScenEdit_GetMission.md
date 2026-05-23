# ScenEdit_GetMission

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetMission.html](https://commandlua.github.io/assets/Function_ScenEdit_GetMission.html)  
> 爬取时间: 2026-05-23 10:34:36  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetMission ( SideNameOrId, MissionNameOrId)


This function retrieves the specific mission details


### Parameters

- SideNameOrId
string
The side name/guid
- MissionNameOrId
string
The mission name/guid

### Returns


Mission
The mission wrapper if the it exists or
nil
otherwise.

`nil`
`local mission = ScenEdit_GetMission( 'USA', 'CV CAP Left' )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
