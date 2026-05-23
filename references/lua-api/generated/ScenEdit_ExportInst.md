# ScenEdit_ExportInst

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_ExportInst.html](https://commandlua.github.io/assets/Function_ScenEdit_ExportInst.html)  
> 爬取时间: 2026-05-23 10:37:43  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_ExportInst (side, unitList, fileData)


This function export unit(s) in XML format to an INST file in folder 'ImportExport'.


If the unit to be exported is a group, then the units in the group are automatically included.
If there are differences between the unit and the 'vanilla' unit in the database, a 'delta' is created as part of the export.


### Parameters

- side
string
The name/GUID of the side owning the exported units
- unitList
{} of multiple
The units to be included in the export
string
The name/GUID of the units to be exported
- fileData
{}
The export file details.
filename =
string
The Filename is mandatory
name =
string
The name to be displayed on the in-game list
comment =
string
- string
The name/GUID of the units to be exported
- filename =
string
The Filename is mandatory
- name =
string
The name to be displayed on the in-game list
- comment =
string

### Returns


number
The number of units exported to the file, else 0

`ScenEdit_ExportInst(
'Russia'
, {
'c1a0e312-9ccc-43d1-9e6c-01899c8433d9'
}, {filename=
'ssbn_patrol.inst'
,name=
'SSBN on Patrol'
,comment=
'Russian SSBN on patrol in Barents'
})`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
