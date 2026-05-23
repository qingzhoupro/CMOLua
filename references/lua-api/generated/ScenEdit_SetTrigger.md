# ScenEdit_SetTrigger

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetTrigger.html](https://commandlua.github.io/assets/Function_ScenEdit_SetTrigger.html)  
> 爬取时间: 2026-05-23 10:35:26  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetTrigger
                    ( table )


This function Sets
                    the
                    attributes
                    of
                    a
                    trigger.


### Parameters

- table
{
                            }
description =
string
Trigger GUID or Description
mode =
string
"add", "remove", "update", "list"
Type of action to take on details
rename =
or
newname =
string
New Description for the Trigger. Applicable to mode 'update' only
type =
string
Type of Trigger. Applicable to mode 'add' only
- description =
string
Trigger GUID or Description
- mode =
string
"add", "remove", "update", "list"
Type of action to take on details
- rename =
or
newname =
string
New Description for the Trigger. Applicable to mode 'update' only
- type =
string
Type of Trigger. Applicable to mode 'add' only

### Returns


table {
                        }
Table
                    of
                    trigger values (needs to be expanded )

`local action = ScenEdit_SetTrigger( { description='my trigger', mode = 'list' } )
print(action) -- list of trigger settings`
`local action = ScenEdit_SetTrigger( { description='my trigger', mode = 'remove' } )
print(action) -- list of the removed trigger settings`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
