# ScenEdit_DeleteReferencePoint

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_DeleteReferencePoint.html](https://commandlua.github.io/assets/Function_ScenEdit_DeleteReferencePoint.html)  
> 爬取时间: 2026-05-23 10:36:07  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_DeleteReferencePoint (table)


This function will delete a reference point.
It will check the side's normal RPs, and then the Non_Nav and Exclusion Zones for a match.
Note that there is no check to see if the RP is actively being used before removing.


### Parameters

- table
{}
side =
string
The side name/guid
name =
or
guid =
string
The reference point name/guid to delete.
- side =
string
The side name/guid
name =
or
guid =
string
The reference point name/guid to delete.

### Returns


True/False
True if successful

`ScenEdit_DeleteReferencePoint( { side="United States", name='RP-1' } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
