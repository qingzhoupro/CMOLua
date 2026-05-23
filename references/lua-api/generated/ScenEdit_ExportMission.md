# ScenEdit_ExportMission

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_ExportMission.html](https://commandlua.github.io/assets/Function_ScenEdit_ExportMission.html)  
> 爬取时间: 2026-05-23 10:34:51  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_ExportMission (SideNameOrId, MissionNameOrId)


This function exports a mission's parameters as a XML file in folder Command_base/Defaults.


### Parameters

- SideNameOrId
string
The mission side name/guid
- MissionNameOrId
string
The mission name/guid

### Returns


table {} of
string
A table of mission GUIDs that were exported.

`local mission = ScenEdit_ExportMission( 'USA', 'Marker strike' )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
