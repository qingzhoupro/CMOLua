# ScenEdit_ImportMission

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_ImportMission.html](https://commandlua.github.io/assets/Function_ScenEdit_ImportMission.html)  
> 爬取时间: 2026-05-23 10:34:53  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_ImportMission
                    (SideNameOrId,MissionNameOrId)


This function imports a mission's parameters as a XML file in folder Command_base/Defaults.
[Experimental as this should really be treated like an attachment so can be imported with Scenario]


### Parameters

- SideNameOrId
string
The side to import to
- MissionNameOrId
string
The mission name in the folder. The imported file will be 'MissionNameOrId.XML'.

### Returns


table {}
string
A table of mission GUIDs that were exported.

`local mission = ScenEdit_ImportMission('USA', 'Marker strike')`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
