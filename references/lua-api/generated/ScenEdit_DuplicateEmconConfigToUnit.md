# ScenEdit_DuplicateEmconConfigToUnit

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_DuplicateEmconConfigToUnit.html](https://commandlua.github.io/assets/Function_ScenEdit_DuplicateEmconConfigToUnit.html)  
> 爬取时间: 2026-05-23 10:38:18  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_DuplicateEmconConfigToUnit ( PresetAlertID, SourceAUNameOrID, TargetAUNameOrID )


The function's purpose is to copy a unit's Alert configuration to another unit.


### Parameters

- SourceAUNameOrID
string
The name or GUID of the unit to copy Alert configuration from. As no Side is supplied, the unit name would need to be unique across the scenario.
- TargetAUNameOrID
string
The name or GUID of the unit to copy Alert configuration to. As no Side is supplied, the unit name would need to be unique across the scenario.
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

`ScenEdit_DuplicateEmconConfigToUnit('green', 'USS Ulysess', 'USS Troy')`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
