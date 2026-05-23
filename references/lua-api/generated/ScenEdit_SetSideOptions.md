# ScenEdit_SetSideOptions

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetSideOptions.html](https://commandlua.github.io/assets/Function_ScenEdit_SetSideOptions.html)  
> 爬取时间: 2026-05-23 10:35:03  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetSideOptions
                    (table)


This function updates the
                    side
                    options


### Parameters

- table
{}
side =
string
The side guid/name
awareness =
Awareness
The side awareness
AutoTrackCivillians =
True/False
The side sbility to track civilians
collectiveResponsibility =
True/False
The side collective resposibility
computerControlledOnly =
True/False
The side is controlled by AI
proficiency =
Proficiency
The side proficiency
switchto =
True/False
[optional] Switch the current side to the 'side' parameter.
- side =
string
The side guid/name
- awareness =
Awareness
The side awareness
- AutoTrackCivillians =
True/False
The side sbility to track civilians
- collectiveResponsibility =
True/False
The side collective resposibility
- computerControlledOnly =
True/False
The side is controlled by AI
- proficiency =
Proficiency
The side proficiency
- switchto =
True/False
[optional] Switch the current side to the 'side' parameter.

### Returns

- side
string
Side name
- guid
string
Side guid
- awareness
string
Side awareness
- proficiency
string
Side proficiency
`local a = ScenEdit_SetSideOptions({side='sidea', awareness = 'blind', PROFICIENCY= 2})
print(a)
if a.awareness == 'Normal' then print('awareness is normal') end
if a.proficiency == 'Regular' then print('proficiency is regular') end
Output
{ awareness = 'Blind', side = 'SideA', guid = '387dfb31-e553-412a-8258-9b959aa00aed', proficiency = 'Regular' }
proficiency is regular`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
