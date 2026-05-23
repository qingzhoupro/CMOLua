# ScenEdit_GetMinefield

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetMinefield.html](https://commandlua.github.io/assets/Function_ScenEdit_GetMinefield.html)  
> 爬取时间: 2026-05-23 10:37:33  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetMinefield( table )


This function retrieves the mines in a minefield


The Reference Points are checked against the side's normal RPs, and then against the side's non-navigation/exclusion zone RPs.
Note that the 'area' supports two methods of supplying the RPs; one with just a list of name/guids (the preferred simplier way),
and the more complicated way with each one being another table.
The second method would be useful if passing a returned 'area' table from some other function call.
Both peform the same operation.


### Parameters

- table
{}
side =
string
Side name/guid
area =
{} of multiple
The area defining the minefield
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
- area =
{} of multiple
The area defining the minefield
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

- guid
string
Mine guid
- type
number
Mine database id
- delay
number
Time to fuze
- latitude
latitude
The latitude of the mine
- longitude
longitude
The longitude of the mine
- depth
number
Depth of mine
`local
a = ScenEdit_GetMinefield({side=
'Blue'
, area={
'rp-1'
,
'rp-2'
,
'rp-3'
,
'rp-4'
} } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
