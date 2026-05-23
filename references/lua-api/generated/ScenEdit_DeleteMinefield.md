# ScenEdit_DeleteMinefield

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_DeleteMinefield.html](https://commandlua.github.io/assets/Function_ScenEdit_DeleteMinefield.html)  
> 爬取时间: 2026-05-23 10:37:31  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_DeleteMinefield (side, area)


This function will delete all the mines owned by the side in the minefield as defined by 'area'.
The Reference Points are checked against the side's normal RPs, and then against the side's non-navigation/exclusion zone RPs.
Note that the 'area' supports two methods of supplying the RPs; one with just a list of name/guids (the preferred simplier way),
and the more complicated way with each one being another table.
The second method would be useful if passing a returned 'area' table from some other function call.
Both peform the same operation.


### Parameters

- side
string
Side name/guid
- area =
{} of multiple
The area defining minefield to remove
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


number
Number of mines removed

`local a = ScenEdit_DeleteMinefield( { side='Blue', area={ 'rp-1', 'rp-2', 'rp-3', 'rp-4' } } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
