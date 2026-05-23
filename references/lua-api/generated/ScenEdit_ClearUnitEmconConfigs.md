# ScenEdit_ClearUnitEmconConfigs

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_ClearUnitEmconConfigs.html](https://commandlua.github.io/assets/Function_ScenEdit_ClearUnitEmconConfigs.html)  
> 爬取时间: 2026-05-23 10:38:14  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_ClearUnitEmconConfigs( AUNameOrID )


The function's purpose is to clear any Intermittent Emission configuration for the unit.


### Parameters

- AUNameOrID
string
The name or GUID of the unit. As no Side is supplied, the unit name would need to be unique across the scenario.

### Returns

- True/False
True if successful

### Example

`ScenEdit_ClearUnitEmconConfigs ( 'USS Ulysess' )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
