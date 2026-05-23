# Exporter_SetSetting

> 官方文档来源: [https://commandlua.github.io/assets/Function_Exporter_SetSetting.html](https://commandlua.github.io/assets/Function_Exporter_SetSetting.html)  
> 爬取时间: 2026-05-23 10:38:10  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### Exporter_SetSetting(Category, Setting, Value)


The function updates some of the settings used by the 'exporting' functions within Command.
ThIs is mainly used by the Professional versions, with the 'Tacview' category being available in the Public version.
The settings are stored in the configuration file 'Config\EventExport.ini'.
These settings should not be changed unless you have some knowledge of what they do.
Note that the parameters are
case sensitive
for accuracy in setting them.


The settings are stored in the configuration file 'Config\EventExport.ini'.
These settings should not be changed unless you have some knowledge of what they do.


### Parameters

- Category
string
The type of the 'exporter'
- Setting
string
The parameter that can be changed
- Value
string
The value of the parameter

### Returns

- None

### Example

`Exporter_SetSetting('Tacview Settings', 'UseCustomUnitExportFrequency', 'False')`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
