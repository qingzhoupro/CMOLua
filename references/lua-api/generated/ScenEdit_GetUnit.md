# ScenEdit_GetUnit

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetUnit.html](https://commandlua.github.io/assets/Function_ScenEdit_GetUnit.html)  
> 爬取时间: 2026-05-23 10:33:45  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetUnit (table)


This function gets the properties of the Unit.


### Parameters

- table
{}
side =
string
The side name/GUID of the unit
unitname =
string
The name of unit
guid =
string
The GUID of the unit
- side =
string
The side name/GUID of the unit
- unitname =
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


local myUnit = 
                            ScenEdit_GetUnit( { guid=
                            'f4f9e0af-15c2-4582-8e80-b827c2ec2f56'} )
print( myUnit)
unit {
type = 'Ship',
subtype = '3106',
name = 'CG 56 San Jacinto',
side = 'United States',
guid = 'f4f9e0af-15c2-4582-8e80-b827c2ec2f56',
class = 'CG 56 San Jacinto [Ticonderoga Baseline 3, VLS]',
proficiency = 'Regular',
latitude = '22.3252605703301',
longitude = '62.1828983227462',
altitude = '0',
heading = '0',
speed = '10',
throttle = 'FullStop',
autodetectable = 'False',
group = 'Bush CSG',
mounts = '25',
magazines = '32',
unitstate = 'Unassigned',
fuelstate = 'None',
weaponstate = 'None',
}

`local myUnit = 
                            ScenEdit_GetUnit( { guid=
                            'f4f9e0af-15c2-4582-8e80-b827c2ec2f56'} )
print( myUnit)
unit {
type = 'Ship',
subtype = '3106',
name = 'CG 56 San Jacinto',
side = 'United States',
guid = 'f4f9e0af-15c2-4582-8e80-b827c2ec2f56',
class = 'CG 56 San Jacinto [Ticonderoga Baseline 3, VLS]',
proficiency = 'Regular',
latitude = '22.3252605703301',
longitude = '62.1828983227462',
altitude = '0',
heading = '0',
speed = '10',
throttle = 'FullStop',
autodetectable = 'False',
group = 'Bush CSG',
mounts = '25',
magazines = '32',
unitstate = 'Unassigned',
fuelstate = 'None',
weaponstate = 'None',
}`

local myUnit = 
                            ScenEdit_GetUnit( { side='United States', unitname='CG 56 San Jacinto'} )
print( myUnit)
unit {
type = 'Ship',
subtype = '3106',
name = 'CG 56 San Jacinto',
side = 'United States',
guid = 'f4f9e0af-15c2-4582-8e80-b827c2ec2f56',
class = 'CG 56 San Jacinto [Ticonderoga Baseline 3, VLS]',
proficiency = 'Regular',
latitude = '22.3252605703301',
longitude = '62.1828983227462',
altitude = '0',
heading = '0',
speed = '10',
throttle = 'FullStop',
autodetectable = 'False',
group = 'Bush CSG',
mounts = '25',
magazines = '32',
unitstate = 'Unassigned',
fuelstate = 'None',
weaponstate = 'None',
}

`local myUnit = 
                            ScenEdit_GetUnit( { side='United States', unitname='CG 56 San Jacinto'} )
print( myUnit)
unit {
type = 'Ship',
subtype = '3106',
name = 'CG 56 San Jacinto',
side = 'United States',
guid = 'f4f9e0af-15c2-4582-8e80-b827c2ec2f56',
class = 'CG 56 San Jacinto [Ticonderoga Baseline 3, VLS]',
proficiency = 'Regular',
latitude = '22.3252605703301',
longitude = '62.1828983227462',
altitude = '0',
heading = '0',
speed = '10',
throttle = 'FullStop',
autodetectable = 'False',
group = 'Bush CSG',
mounts = '25',
magazines = '32',
unitstate = 'Unassigned',
fuelstate = 'None',
weaponstate = 'None',
}`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
