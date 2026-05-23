# Command_SaveScen

> 官方文档来源: [https://commandlua.github.io/assets/Function_Command_SaveScen.html](https://commandlua.github.io/assets/Function_Command_SaveScen.html)  
> 爬取时间: 2026-05-23 10:37:37  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### Command_SaveScen( saveFile )


This function creates an instant save file.
This could be triggered to be run at specific times after certain events as a checkpoint for recovery or an AAR,


### Parameters

- saveFile
string
The
full path
to the location to create the save file.

### Returns

- None

### Example

`Command_SaveScen("C:/temp/mysave.save")`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
