# ScenEdit_GetReferencePoint

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetReferencePoint.html](https://commandlua.github.io/assets/Function_ScenEdit_GetReferencePoint.html)  
> 爬取时间: 2026-05-23 10:36:01  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetReferencePoint ( table)


This function will return details for a specific reference point.
The RP will be checked against normal side RPs and then against the non-navigation and exclusion zone RPs for a match.


### Parameters

- table
{}
side =
string
Side name/guid
name =
or
guid =
string
The name/guid of the reference point
- side =
string
Side name/guid
- name =
or
guid =
string
The name/guid of the reference point

### Returns


ReferencePoint
Reference point wrapper

`local points = ScenEdit_GetReferencePoint( { side="United States", name="rp-100"} )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
