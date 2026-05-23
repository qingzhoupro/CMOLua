# ScenEdit_SetCondition

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetCondition.html](https://commandlua.github.io/assets/Function_ScenEdit_SetCondition.html)  
> 爬取时间: 2026-05-23 10:35:28  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetCondition
                    ( table )


This function Sets
                    the
                    attributes
                    of
                    an Event
                    Condition.


### Parameters

- table
{}
description =
string
Condition GUID or Description
mode =
string
"add", "remove", "update", "list"
Type of action to take on details
rename =
or
newname =
string
New Description for the Condition. Applicable to mode 'update' only
type =
string
Type of Condition. Applicable to mode 'add' only
- description =
string
Condition GUID or Description
- mode =
string
"add", "remove", "update", "list"
Type of action to take on details
- rename =
or
newname =
string
New Description for the Condition. Applicable to mode 'update' only
- type =
string
Type of Condition. Applicable to mode 'add' only

### Returns


table {}
Table
                    of
                    condition values (needs to be expanded )

`local action = ScenEdit_SetContion( { description='my condition', mode = 'list' } )
print(action)  -- list of condition settings`
`local action = ScenEdit_SetContion( { description='my condition', mode = 'remove' } )
print(action)  -- list of the removed condition settings`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
