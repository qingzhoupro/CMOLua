# ScenEdit_MergeUnits

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_MergeUnits.html](https://commandlua.github.io/assets/Function_ScenEdit_MergeUnits.html)  
> 爬取时间: 2026-05-23 10:34:12  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### Function ScenEdit_MergeUnits( )


Merge the selected units in to the first one on the list


### Parameters

- List the parameters as in the Syntax line

### Returns

- Unit wrapper of the merged unit

### Example

`local a = ScenEdit_MergeUnits()
print(a)
unit {
 type = 'Facility', 
 subtype = '5001', 
 name = 'Mech Inf', 
 side = 'SideA', 
 guid = 'ff0ef686-bf03-4228-af7c-a726f8c178cf', 
 class = 'Mech Inf Plt (Type 96 APC x 4)', 
 proficiency = 'Regular', 
 latitude = '34.7079918909088', 
 longitude = '136.197564336924', 
 altitude = '243', 
 heading = '0', 
 speed = '0', 
 throttle = 'FullStop', 
 autodetectable = 'False', 
 mounts = '4', 
 magazines = '4', 
 unitstate = 'Unassigned', 
 fuelstate = 'None', 
 weaponstate = 'None', 
 AllowMultiMission = 'False', 
 AssignedMissionsQueue = 'table', 
}`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
