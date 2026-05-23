# ScenEdit_GetSpecialAction

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetSpecialAction.html](https://commandlua.github.io/assets/Function_ScenEdit_GetSpecialAction.html)  
> 爬取时间: 2026-05-23 10:38:39  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetSpecialAction ( action_info )


This function retrieves the properties of special action


### Parameters

- table
{}
side =
string
Side name/guid
mode = 'list'
Extracts all special actions for all sides if 'side' not supplied, else filters just for 'side'
ActionNameOrID =
string
Specific Special action event name/guid
- side =
string
Side name/guid
- mode = 'list'
Extracts all special actions for all sides if 'side' not supplied, else filters just for 'side'
- ActionNameOrID =
string
Specific Special action event name/guid

### Returns

- guid
string
Event guid
- name
string
Event name
- description
string
Event description
- isActive
True/False
Event is active?
- IsRepeatable
True/False
Event is active?
- ScriptText
string
Event script
`ScenEdit_GetSpecialAction( { side='SideA', ActionNameOrID='Perform SAR' } )`
`ScenEdit_GetSpecialAction( { side='SideA', mode='list' } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
