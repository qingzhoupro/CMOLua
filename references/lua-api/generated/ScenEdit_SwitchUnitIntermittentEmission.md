# ScenEdit_SwitchUnitIntermittentEmission

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SwitchUnitIntermittentEmission.html](https://commandlua.github.io/assets/Function_ScenEdit_SwitchUnitIntermittentEmission.html)  
> 爬取时间: 2026-05-23 10:38:26  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SwitchUnitIntermittentEmission( AUNameOrID,PresetAlertID,Switch )


The function's purpose is to turn off/on the Intermittent Emission for the specified Alert Level


### Parameters

- AUNameOrID
string
The name or GUID of the unit. As no Side is supplied, the unit name would need to be unique across the scenario.
PresetAlertID
value
"GREEN"
"BLUE"
"YELLOW"
"ORANGE"
"RED"
"CUSTOM"
"ALL"
The Alert level
Switch
number
Use 0 to turn off the Emission interval, 1 to turn on the Emission interval (USEEMISSIONINTERVAL)

### Returns

- True/False
True if successful

### Example

`ScenEdit_SwitchUnitIntermittentEmission ( 'USS Ulysess', 'Green', 1 )  -- turn on interval for Alert level Green for the unit`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
