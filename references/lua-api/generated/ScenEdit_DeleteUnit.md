# ScenEdit_DeleteUnit

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_DeleteUnit.html](https://commandlua.github.io/assets/Function_ScenEdit_DeleteUnit.html)  
> 爬取时间: 2026-05-23 10:33:51  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_DeleteUnit (table, include)


This function will delete a unit( and any attached units) and no event is triggered.


### Parameters

- include
True/False
If a group, delete the attached units
- table
{}
side =
string
The side name/GUID of the unit
unitname =
or
guid =
string
The unit name/guid to delete.
- side =
string
The side name/GUID of the unit
- unitname =
or
guid =
string
The unit name/guid to delete.

### Returns


True/False
True if successful

`ScenEdit_DeleteUnit( { side="United States", unitname="USS Abcd" } )`
`ScenEdit_DeleteUnit( { side="United States", unitname="TaskForce #1", 'true' } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
