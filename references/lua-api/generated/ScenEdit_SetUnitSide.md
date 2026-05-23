# ScenEdit_SetUnitSide

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetUnitSide.html](https://commandlua.github.io/assets/Function_ScenEdit_SetUnitSide.html)  
> 爬取时间: 2026-05-23 10:34:16  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetUnitSide
                    ( table )


This function Changes
                    the
                    side
                    of
                    a
                    unit.
Passing a group
                    will
                    change the
                    attached
                    units too


### Parameters

- table
{
                            }
side =
string
The side name/GUID of the unit
unitname =
string
The name of unit
guid =
string
The GUID of the unit
newSide =
string
The name/guid to change the 'unit' to
- side =
string
The side name/GUID of the unit
- unitname =
string
The name of unit
- guid =
string
The GUID of the unit
- newSide =
string
The name/guid to change the 'unit' to
`ScenEdit_SetUnitSide({side=
'Old Side'
, name=
'Eagle #1'
, newside=
'New Side'
})`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
