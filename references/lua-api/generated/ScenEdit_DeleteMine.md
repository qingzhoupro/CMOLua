# ScenEdit_DeleteMine

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_DeleteMine.html](https://commandlua.github.io/assets/Function_ScenEdit_DeleteMine.html)  
> 爬取时间: 2026-05-23 10:37:35  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_DeleteMine (side, guid)


This function deletes a specific mine from a side's minefield


### Parameters

- side
string
Side name/guid
- guid
string
Mine guid

### Returns


True/False
True if successful

`local a = ScenEdit_DeleteMine( { side='Blue', guid='cccccccc'} )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
