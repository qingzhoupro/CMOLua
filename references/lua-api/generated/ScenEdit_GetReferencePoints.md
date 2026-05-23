# ScenEdit_GetReferencePoints

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetReferencePoints.html](https://commandlua.github.io/assets/Function_ScenEdit_GetReferencePoints.html)  
> 爬取时间: 2026-05-23 10:36:03  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetReferencePoints ( table)


This function will return the details for a range of reference point.
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
The name/guid of the reference point (for a single point)
area =
{} of multiple
For multiple RPs
name =
or
guid =
string
The name/guid of the reference point
or
string
The name/guid of the reference point
- side =
string
Side name/guid
- name =
or
guid =
string
The name/guid of the reference point (for a single point)
- area =
{} of multiple
For multiple RPs
name =
or
guid =
string
The name/guid of the reference point
or
string
The name/guid of the reference point
- name =
or
guid =
string
The name/guid of the reference point
- string
The name/guid of the reference point

### Returns


table {} of multiple
ReferencePoint
Reference point wrappers

`local points = ScenEdit_GetReferencePoints( { side="United States", area={ "rp-100", "rp-101", "rp-102", "rp-103", "rp-104"} } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
