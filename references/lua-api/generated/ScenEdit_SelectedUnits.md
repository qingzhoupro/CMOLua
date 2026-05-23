# ScenEdit_SelectedUnits

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SelectedUnits.html](https://commandlua.github.io/assets/Function_ScenEdit_SelectedUnits.html)  
> 爬取时间: 2026-05-23 10:38:35  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SelectedUnits
                    ()


This function returns a list (of name and guid)
                    of the units (actual or contact) currently selected


### Parameters

- None

### Returns


table {} of
units
{} of multiple
guid
string
name
string
contacts
{} of multiple
guid
string
name
string
A Table
                    of
                    ids
                    for selected
                    'units'and
                    'contacts'.

- units
{} of multiple
guid
string
name
string
- contacts
{} of multiple
guid
string
name
string
- guid
string
- name
string
- guid
string
- name
string
`local selected = ScenEdit_SelectedUnits( )
print(selected.units)  -- list of selected units`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
