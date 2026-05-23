# ScenEdit_UpdateUnit

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_UpdateUnit.html](https://commandlua.github.io/assets/Function_ScenEdit_UpdateUnit.html)  
> 爬取时间: 2026-05-23 10:33:49  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_UpdateUnit
                    ( table )


This function Updates the components
                    of
                    an
                    unit.
As this function also calls
ScenEdit_SetUnit()
, additional parameters for that function may also be passed to this function.


### Parameters

- table
{
                            }
guid =
string
The GUID of the unit
mode =
value
'add_sensor', 'remove_sensor', 'update_sensor_arc',
'add_mount', 'remove_mount', 'update_mount_arc',
'add_weapon', 'remove_weapon',
'add_comms', 'remove_comms',
'add_fuel', 'remove_fuel',
'add_magazine', 'add_magazine_only', 'remove_magazine',
'add_dock_facility', 'remove_dock_facility',
'add_air_facility', 'remove_air_facility',
'delta'
The action mode to perform
dbid =
number
Component DBID to affect
file =
string
The filename to upload update from (Applies to 'mode = delta' only)
arc_detect =
{
                                    }

                                    of multiple
detection arcs
arc
Arc code string (applies to 'mode = ...sensor...')
arc_track =
{
                                    }

                                    of multiple
illumination arcs
arc
Arc code string (applies to 'mode = ...sensor...')
arc_mount =
{
                                    }

                                    of multiple
mount arcs
arc
Arc code string (applies to 'mode = ...mount...')
sensorid =
string
A specific sensor GUID to operate on (not applicable to adding sensor)
mountid =
string
A specific mount GUID to operate on (not applicable to adding mount)
weaponid =
string
A specific weapon GUID to operate on (not applicable to adding weapon)
commsid =
string
A specific communication GUID to operate on (not applicable to adding comms)
magid =
string
A specific magazine GUID to operate on (not applicable to adding magazine)
airfacid =
string
A specific air facility GUID to operate on (not applicable to adding air facility)
dockfacid =
string
A specific docking facility GUID to operate on (not applicable to adding docking facility)
fuel =
{
                                    }

                                    of multiple
Fuel to perform action on
string
fuel type
number
quantity
- guid =
string
The GUID of the unit
- mode =
value
'add_sensor', 'remove_sensor', 'update_sensor_arc',
'add_mount', 'remove_mount', 'update_mount_arc',
'add_weapon', 'remove_weapon',
'add_comms', 'remove_comms',
'add_fuel', 'remove_fuel',
'add_magazine', 'add_magazine_only', 'remove_magazine',
'add_dock_facility', 'remove_dock_facility',
'add_air_facility', 'remove_air_facility',
'delta'
The action mode to perform
- dbid =
number
Component DBID to affect
- file =
string
The filename to upload update from (Applies to 'mode = delta' only)
- arc_detect =
{
                                    }

                                    of multiple
detection arcs
arc
Arc code string (applies to 'mode = ...sensor...')
- arc_track =
{
                                    }

                                    of multiple
illumination arcs
arc
Arc code string (applies to 'mode = ...sensor...')
- arc_mount =
{
                                    }

                                    of multiple
mount arcs
arc
Arc code string (applies to 'mode = ...mount...')
- sensorid =
string
A specific sensor GUID to operate on (not applicable to adding sensor)
- mountid =
string
A specific mount GUID to operate on (not applicable to adding mount)
- weaponid =
string
A specific weapon GUID to operate on (not applicable to adding weapon)
- commsid =
string
A specific communication GUID to operate on (not applicable to adding comms)
- magid =
string
A specific magazine GUID to operate on (not applicable to adding magazine)
- airfacid =
string
A specific air facility GUID to operate on (not applicable to adding air facility)
- dockfacid =
string
A specific docking facility GUID to operate on (not applicable to adding docking facility)
- fuel =
{
                                    }

                                    of multiple
Fuel to perform action on
string
fuel type
number
quantity
- arc
Arc code string (applies to 'mode = ...sensor...')
- arc
Arc code string (applies to 'mode = ...sensor...')
- arc
Arc code string (applies to 'mode = ...mount...')
- string
fuel type
- number
quantity

### Returns


Unit
The
                    updated unit
                    object

`ScenEdit_UpdateUnit( { guid='2cd64757-1b66-4609-ad56-df41bee652e5',mode='add_sensor',dbid=3352 } )`
`ScenEdit_UpdateUnit( { 
					guid='2cd64757-1b66-4609-ad56-df41bee652e5',mode='remove_sensor',
dbid=3352,sensorId='871aea14-d963-4052-a7fc-ed36e97bb732'} )`
`ScenEdit_UpdateUnit( { guid='2cd64757-1b66-4609-ad56-df41bee652e5',mode='delta',file='new.ini' } )`
`local u = ScenEdit_UpdateUnit( { 
					guid='CY41MA-0HN9IIDE9MCFT', 
					mode='add_dock_facility', 
					dbid=19})
--local u = ScenEdit_UpdateUnit( { guid='CY41MA-0HN9IIDE9MCFT', 
					mode='remove_dock_facility', 
					dbid=19, 
					dockfacid='CY41MA-0HN9IIDE9MDV6'} )
print(u.components)`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
