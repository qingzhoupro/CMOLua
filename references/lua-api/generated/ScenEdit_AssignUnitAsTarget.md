# ScenEdit_AssignUnitAsTarget

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_AssignUnitAsTarget.html](https://commandlua.github.io/assets/Function_ScenEdit_AssignUnitAsTarget.html)  
> 爬取时间: 2026-05-23 10:34:47  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_AssignUnitAsTarget (AUNameOrIDOrTable,
                    MissionNameOrID)


This function assigns targets to a Strike mission target list.
The target list can be (a) one single unit/contact name/guid, or (b) a table of unit/contact name/guid


'UnitX' as the triggering unit, can be used as the unit name.
Contacts can also be assigned. Refer to the VP_ functions for details


### Parameters

- AUNameOrIDOrTable
string
or
table {}
The name/GUID of the unit, or a table of unit/contact name/GUID to add
- MissionNameOrID
string
The strike mission name/guid to be updated

### Returns


table {} of
string
A table of target GUIDs that were added

`ScenEdit_AssignUnitAsTarget( {'target1', 'target2' }, 'Land strike' )`
`ScenEdit_AssignUnitAsTarget('UnitX', 'Land strike' )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
