# UI_OpenNewDatabaseWindow

> 官方文档来源: [https://commandlua.github.io/assets/Function_UI_OpenNewDatabaseWindow.html](https://commandlua.github.io/assets/Function_UI_OpenNewDatabaseWindow.html)  
> 爬取时间: 2026-05-23 10:37:18  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### UI_OpenNewDatabaseWindow
                    (SelectedObjectType, SelectedObjectID)


This function opens the database page for the specified unit type and dbid


### Parameters

- SelectedObjectType
type
Aircraft, Ship, Submarine, Facility, Ground Unit, Satellite, Weapon, Sensor
The unit type
- SelectedObjectID
number
The unit database ID

### Returns


None

- None
`UI_OpenNewDatabaseWindow("aircraft", 10)`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
