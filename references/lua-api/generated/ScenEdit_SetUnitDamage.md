# ScenEdit_SetUnitDamage

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetUnitDamage.html](https://commandlua.github.io/assets/Function_ScenEdit_SetUnitDamage.html)  
> 爬取时间: 2026-05-23 10:34:18  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetUnitDamage
                    ( table )


This function Sets the
                    unit
                    damage for
                    components


### Parameters

- table
{
                            }
side =
string
The side name/GUID of the unit
unitname =
string
The name of unit
guid =
string
The GUID of the unit
fires =
Fire_level?
Fire level
flood =
Flood_level?
Flooding level
dp =
number
Damage points left
components =
{
                                    }

                                    of multiple
value
'rudder', 'cargo', 'cic', 'pressurehull'
Standard component to damage
string
Damage level ('none', 'destroyed', or damage_severity_setting)
or
string
Specific component GUID to damage
string
Damage level ('none', 'destroyed', or damage_severity_setting)
or
'type'
Fixed value to indicate a random component damage
type =
'sensor', etc
Random component type to damage
string
Damage level ('none', 'destroyed', or damage_severity_setting)
- side =
string
The side name/GUID of the unit
- unitname =
string
The name of unit
- guid =
string
The GUID of the unit
- fires =
Fire_level?
Fire level
- flood =
Flood_level?
Flooding level
- dp =
number
Damage points left
- components =
{
                                    }

                                    of multiple
value
'rudder', 'cargo', 'cic', 'pressurehull'
Standard component to damage
string
Damage level ('none', 'destroyed', or damage_severity_setting)
or
string
Specific component GUID to damage
string
Damage level ('none', 'destroyed', or damage_severity_setting)
or
'type'
Fixed value to indicate a random component damage
type =
'sensor', etc
Random component type to damage
string
Damage level ('none', 'destroyed', or damage_severity_setting)
- value
'rudder', 'cargo', 'cic', 'pressurehull'
Standard component to damage
- string
Damage level ('none', 'destroyed', or damage_severity_setting)
- string
Specific component GUID to damage
- string
Damage level ('none', 'destroyed', or damage_severity_setting)
- 'type'
Fixed value to indicate a random component damage
- type =
'sensor', etc
Random component type to damage
- string
Damage level ('none', 'destroyed', or damage_severity_setting)

### Returns


Component
The
                    unit's
                    components
                    object

`ScenEdit_SetUnitDamage({ side='SideA', unitname='TheShip', fires=1, components={ {'rudder','Medium'}, {'type',type='sensor',1} } })`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
