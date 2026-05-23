# ScenEdit_AddMission

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_AddMission.html](https://commandlua.github.io/assets/Function_ScenEdit_AddMission.html)  
> 爬取时间: 2026-05-23 10:34:34  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_AddMission (SideNameOrId, MissionNameOrId, MissionType, MissionOptions)


This function adds a new mission to the side based on the supplied options
It is suggested to make the mission name unique across the scenario to ensure there are no conflicts as to the side it is applicable to
Once the core mission is added, the mission can be adjusted through a wrapper or
ScenEdit_SetMission


### Parameters

- SideNameOrId
string
The mission side name/guid
- MissionNameOrId
string
The mission name as this is a new mission
- MissionType
MissionType
The type of mission which will control what is valid for the following options
- MissionOptions
{}
The mission specific options
category =
MissionCategory
Mission (0), Package (1), Taskpool (2)
The category of mission being added. The default is 'Mission'.
destination =
string
A mission destination location name/guid (This only applies to a 'Ferry' mission)
pool =
ParentTaskpool
The name or GUID of the task pool this package draws from. (This only applies to mission category 'package')
type =
MissionSubType
Mission sub-type (This only applies to mission types 'Patrol' and 'Strike')
zone =
{} of multiple
The area to operate in (This only applies to 'Patrol', 'Support', 'Mining', 'Cargo' missions)
string
The reference point guid/name
- category =
MissionCategory
Mission (0), Package (1), Taskpool (2)
The category of mission being added. The default is 'Mission'.
- destination =
string
A mission destination location name/guid (This only applies to a 'Ferry' mission)
- pool =
ParentTaskpool
The name or GUID of the task pool this package draws from. (This only applies to mission category 'package')
- type =
MissionSubType
Mission sub-type (This only applies to mission types 'Patrol' and 'Strike')
- zone =
{} of multiple
The area to operate in (This only applies to 'Patrol', 'Support', 'Mining', 'Cargo' missions)
string
The reference point guid/name
- string
The reference point guid/name

### Returns


Mission
A mission wrapper for the new mission or
nil
otherwise.
Retaining the mission guid for updating would be desirable rather than rely on the name itself.

`nil`
`local mission = ScenEdit_AddMission( 'USA', 'Marker strike', 'strike',{ type = 'land'} )`
`local missionReferencePoints={'rp-1','rp-2','rp-3'}
local mission = ScenEdit_AddMission (OPFORsideName, 'OPFOR Mission', 'Patrol', {type= 'AAW',zone= missionReferencePoints} )`
`-- create a task pool
local m = ScenEdit_AddMission('sidea', 'Strike Pool', 'Strike', {category='taskpool',type='land',pool='strike pool'})
-- create a package under the task pool
m = ScenEdit_AddMission('sidea', 'Package 1', 'Strike', {category='package',type='land',pool='strike pool'})
m = ScenEdit_AddMission('sidea', 'mission', 'Strike', {type='land',pool='strike pool'})
print(m)`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
