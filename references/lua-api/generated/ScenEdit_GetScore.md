# ScenEdit_GetScore

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetScore.html](https://commandlua.github.io/assets/Function_ScenEdit_GetScore.html)  
> 爬取时间: 2026-05-23 10:36:45  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetScore( side )


This function retrieves the current score on a side.
'PlayerSide' can be used for the
side
to access the current playing side.

`side`

### Parameters

- side
string
The side name/guid

### Returns


number
The side's score

`local a = ScenEdit_GetScore("PlayerSide")`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
