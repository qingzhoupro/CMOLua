# ScenEdit_SetMission

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetMission.html](https://commandlua.github.io/assets/Function_ScenEdit_SetMission.html)  
> 爬取时间: 2026-05-23 10:34:38  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetMission
                    (SideName, MissionNameOrId, MissionOptions)


This function Sets
                    details
                    for
                    a
                    mission.


### Parameters

- SideName
string
The
                        mission
                        side
- MissionNameOrId
string
The
                        mission
                        name/guid
- MissionOptions
{}
Refer to the Mission object
Mission
for the possible values
Only the items to be updated need to be added as 'item = value'.

### Returns


Mission
The
                    mission
                    object
                    if
                    the
                    mission
                    exists
                    or
nil
otherwise.

`nil`
`local
mission = ScenEdit_SetMission(
'USA'
,
'CV CAP Left'
,{TankerUsage=
1
,OnStation=
2
})`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
