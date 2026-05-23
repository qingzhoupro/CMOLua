# ScenEdit_DuplicateEmconConfigToSide

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_DuplicateEmconConfigToSide.html](https://commandlua.github.io/assets/Function_ScenEdit_DuplicateEmconConfigToSide.html)  
> 爬取时间: 2026-05-23 10:38:16  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_DuplicateEmconConfigToSide (  PresetAlertID, SourceSideNameOrID, TargetSideNameOrID )


The function's purpose is to duplicate an Alert setting from one side to another side.


### Parameters

- SourceSideNameOrID
string
The name or GUID of the side to copy Alert configuration from.
- TargetSideNameOrID
string
The name or GUID of the side to copy Alert configuration to.
- PresetAlertID
value
"GREEN"
"BLUE"
"YELLOW"
"ORANGE"
"RED"
"CUSTOM"
"ALL"
The Alert level

### Returns

- True/False
True if successful

### Example

`ScenEdit_DuplicateEmconConfigToUnit('green', 'canada', 'USA')`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
