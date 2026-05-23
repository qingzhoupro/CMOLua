# ScenEdit_DeleteMission

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_DeleteMission.html](https://commandlua.github.io/assets/Function_ScenEdit_DeleteMission.html)  
> 爬取时间: 2026-05-23 10:34:40  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_DeleteMission (SideNameOrId, MissionNameOrId)


This function will delete a mission from the side and unassign any units attached to it.


### Parameters

- SideNameOrId
string
The side name/guid
- MissionNameOrId
string
The side's mission name/guid

### Returns


True/False
True if successful

`local mission = ScenEdit_DeleteMission( 'USA', 'Marker strike' )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
