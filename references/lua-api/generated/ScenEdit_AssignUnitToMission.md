# ScenEdit_AssignUnitToMission

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_AssignUnitToMission.html](https://commandlua.github.io/assets/Function_ScenEdit_AssignUnitToMission.html)  
> 爬取时间: 2026-05-23 10:34:44  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_AssignUnitToMission (unitname, mission, escort)


This function assign a unit to a mission.
The 'UnitX' can be used as the unitname.


### Parameters

- unitname
string
The name/GUID of the unit to assign
- mission
string
The mission name/GUID to assign to
- escort
True/False
If the mission is a strike one, then assign unit to the 'Escort' for the strike [Default=False]

### Returns


True/False
True if Successful

`ScenEdit_AssignUnitToMission( "Bar #1", "Strike" )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
