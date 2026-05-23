# ScenEdit_RemoveUnitAsTarget

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_RemoveUnitAsTarget.html](https://commandlua.github.io/assets/Function_ScenEdit_RemoveUnitAsTarget.html)  
> 爬取时间: 2026-05-23 10:34:45  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_RemoveUnitAsTarget
                    (AUNameOrIDOrTable,MissionNameOrID)


This function removes
                    target(s)
                    from
                    a
                    Strike
                    mission.


The value
                    'UnitX' can
                    be
                    used in an event
                    for AUNameOrIDOrTable.


### Parameters

- AUNameOrIDOrTable
string
The
                                name/GUID
                                of
                                the single
                                unit
or
{} of multiple
string
A
                                table
                                of
name/GUID
to
                                remove
                                from
                                target
                                list
MissionNameOrID
string
The strike
                        mission name/guid
- string
The
                                name/GUID
                                of
                                the single
                                unit
- {} of multiple
string
A
                                table
                                of
name/GUID
to
                                remove
                                from
                                target
                                list
`name/GUID`

### Returns


table {} of
string
A
                    table
                    of
                    target GUIDs
                    removed

`ScenEdit_RemoveUnitAsTarget( { 'target1','target2' }, 'Land strike' )`
`ScenEdit_RemoveUnitAsTarget( 'UnitX', 'Land strike' )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
