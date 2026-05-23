# ScenEdit_GetSidePosture

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetSidePosture.html](https://commandlua.github.io/assets/Function_ScenEdit_GetSidePosture.html)  
> 爬取时间: 2026-05-23 10:35:01  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetSidePosture ( sideA, sideB)


This function shows the posture of sideA towards sideB.


### Parameters

- sideA
string
The first side name/guid
- sideB
string
The second side name/guid

### Returns


string
The posture as 'N','F','H',or 'A'. If posture is unknown, then '' is returned.

`local u = ScenEdit_GetSidePosture( 'NATO', 'Russia' } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
