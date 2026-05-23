# ScenEdit_SplitUnit

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SplitUnit.html](https://commandlua.github.io/assets/Function_ScenEdit_SplitUnit.html)  
> 爬取时间: 2026-05-23 10:34:14  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### Function ScenEdit_SplitUnit ( table )


Split a unit in to units with each component mount


### Parameters

- List the parameters as in the Syntax line

### Returns

- Table of unit wrappers

### Example

`local a = ScenEdit_SplitUnit({name='Mech Inf', guid='ff0ef686-bf03-4228-af7c-a726f8c178cf'})
print(a)
{ [1] = Command_Core.Facility, [2] = Command_Core.Facility, [3] = Command_Core.Facility }`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
