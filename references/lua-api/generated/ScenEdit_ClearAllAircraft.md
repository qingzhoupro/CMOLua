# ScenEdit_ClearAllAircraft

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_ClearAllAircraft.html](https://commandlua.github.io/assets/Function_ScenEdit_ClearAllAircraft.html)  
> 爬取时间: 2026-05-23 10:34:20  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_ClearAllAircraft ( table )


The function removes ALL embarked aircraft from the unit. If the unit is a group, then all units in the group are also affected.


### Parameters

- side =
string
The side name/GUID of the unit
- unitname =
string
The name of unit
- guid =
string
The GUID of the unit

### Returns

- None

### Example

`ScenEdit_ClearAllAircraft ( {guid='8269b881-20ce-4f2e-baa0-6823e46d55a4'} )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
