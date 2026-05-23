# ScenEdit_GetSideOptions

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetSideOptions.html](https://commandlua.github.io/assets/Function_ScenEdit_GetSideOptions.html)  
> 爬取时间: 2026-05-23 10:35:05  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetSideOptions (options)


This function retrieves the side attributes ( guid, awareness, proficiency)


### Parameters

- table
{}
side =
string
Side name/guid
- side =
string
Side name/guid

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
`local a = ScenEdit_GetSideOptions( { side='SideA' } )
print(a)
if a.awareness == 'Normal' then print('awareness is normal') end
if a.proficiency == 'Regular' then print('proficiency is regular') end
Output
{ awareness = 'Normal', side = 'SideA', guid = '387dfb31-e553-412a-8258-9b959aa00aed', proficiency = 'Regular' }
awareness is normal
proficiency is regular`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
