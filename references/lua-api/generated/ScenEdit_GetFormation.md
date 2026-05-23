# ScenEdit_GetFormation

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetFormation.html](https://commandlua.github.io/assets/Function_ScenEdit_GetFormation.html)  
> 爬取时间: 2026-05-23 10:38:32  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetFormation (table)


This function gets the properties of a groups formation.


### Parameters

- table
{}
side =
string
The side name of the unit
name =
string
The name of unit
guid =
string
The GUID of the unit
- side =
string
The side name of the unit
- name =
string
The name of unit
- guid =
string
The GUID of the unit

### Returns

`nil`

Note:
When run interactively (i.e. in the console) ScenEdit_GetUnit() will
                        raise an exception if the selected unit is not found. This can be prevented using
Tool_EmulateNoConsole()
.


local formation = ScenEdit_GetFormation({side='Blue', name='Group 16'})
                            print(formation)
{
spacing_unit = 1,
lead = 'TTZL89-0HNB8KFCH7IQ1',
name = 'Column',
spacing = 1,
1 = {
longitude = -125.982767420485,
sprint = 'False',
bearing = 180,
distance = 1,
guid = 'TTZL89-0HNB8KFCH7JFM',
type = 'Rotating', latitude = 36.7916933243477
},
2 = {
longitude = -125.982767420485,
sprint = 'False',
bearing = 180,
distance = 2,
guid = 'TTZL89-0HNB8KFCH7K61',
type = 'Rotating', latitude = 36.7750457370943
},
3 = {
longitude = -125.982767420485,
sprint = 'False',
bearing = 180,
distance = 3,
guid = 'TTZL89-0HNB8KFCH7KS4',
type = 'Rotating', latitude = 36.7583981481733
}

`local formation = ScenEdit_GetFormation({side='Blue', name='Group 16'})
                            print(formation)
{
spacing_unit = 1,
lead = 'TTZL89-0HNB8KFCH7IQ1',
name = 'Column',
spacing = 1,
1 = {
longitude = -125.982767420485,
sprint = 'False',
bearing = 180,
distance = 1,
guid = 'TTZL89-0HNB8KFCH7JFM',
type = 'Rotating', latitude = 36.7916933243477
},
2 = {
longitude = -125.982767420485,
sprint = 'False',
bearing = 180,
distance = 2,
guid = 'TTZL89-0HNB8KFCH7K61',
type = 'Rotating', latitude = 36.7750457370943
},
3 = {
longitude = -125.982767420485,
sprint = 'False',
bearing = 180,
distance = 3,
guid = 'TTZL89-0HNB8KFCH7KS4',
type = 'Rotating', latitude = 36.7583981481733
}`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
