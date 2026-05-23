# ScenEdit_SetAction

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetAction.html](https://commandlua.github.io/assets/Function_ScenEdit_SetAction.html)  
> 爬取时间: 2026-05-23 10:35:30  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetAction
                    (table)


This function Sets
                    the
                    attributes
                    of
                    an
                    Event action.


The available operation/modes available are:
'list'   : dumps the Action currently installed
'add'    : adds a new Action
'remove' : deletes the Action. The Action won't be deleted if it is in an Event.
'update' : modifies the Action

- 'list'   : dumps the Action currently installed
- 'add'    : adds a new Action
- 'remove' : deletes the Action. The Action won't be deleted if it is in an Event.
- 'update' : modifies the Action

### Parameters

- table
{}
description =
string
Action GUID or Description
mode =
string
"add", "remove", "update", "list"
Type of action to take on details
rename =
or
newname =
string
New Description for the Action. Applicable to mode 'update' only
type =
string
Type of Action. Applicable to mode 'add' only
scripttext =
string
Script to be executed for a Lua Action
scriptfor =
number
0: EventAction, 1: WaypointAction
Script for action or for waypoints selector
- description =
string
Action GUID or Description
- mode =
string
"add", "remove", "update", "list"
Type of action to take on details
- rename =
or
newname =
string
New Description for the Action. Applicable to mode 'update' only
- type =
string
Type of Action. Applicable to mode 'add' only
- scripttext =
string
Script to be executed for a Lua Action
- scriptfor =
number
0: EventAction, 1: WaypointAction
Script for action or for waypoints selector

### Returns


table {}
Table
                    of
                    action values (needs to be expanded )

`local action = ScenEdit_SetAction( { description='my action', mode = 'list' } )
print(action)  -- list of action settings`
`local action = ScenEdit_SetAction( { description='my action', mode = 'remove' } )
print(action)  -- list of the removed action settings`
`local myscript = "ScenEdit_SpecialMessage('Blue','Starting data tx')"
                        ScenEdit_SetAction( {name='ELF transmission2', description="action for waypoints", type="luascript", mode='add', scripttext = myscript, scriptfor=1})`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
