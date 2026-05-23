# ScenEdit_GetContacts

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetContacts.html](https://commandlua.github.io/assets/Function_ScenEdit_GetContacts.html)  
> 爬取时间: 2026-05-23 10:35:56  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetContacts (side)


This function is similar to
ScenEdit_GetContact()
but it returns a table of contacts on the side


### Parameters

- side
string
The side name/guid.

### Returns


Table {} of
Contact
A Table of contact wrappers for the side or
nil
if no side found.

`nil`
`local con = ScenEdit_GetContacts('south korea')`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
