# Tool_BuildBlankScenario

> 官方文档来源: [https://commandlua.github.io/assets/Function_Tool_BuildBlankScenario.html](https://commandlua.github.io/assets/Function_Tool_BuildBlankScenario.html)  
> 爬取时间: 2026-05-23 10:38:00  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### Tool_BuildBlankScenario ( useDBname )


The function purpose is to create a blank scenario based on the current DB or by supplying the DB file name a different DB.


### Parameters

- useDBname
string
(Optional) file name from the DB folder

### Returns


True/False
True if successful. If result is nil, then the method failed.


### Example


Use s specific DB

`print(Tool_BuildBlankScenario('DB3K_503.db3'))
'Yes'`

Use whatever is the current DB setting as shown in DB list under Editor

`print(Tool_BuildBlankScenario())`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
