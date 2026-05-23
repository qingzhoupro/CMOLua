# ScenEdit_AddUnit

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_AddUnit.html](https://commandlua.github.io/assets/Function_ScenEdit_AddUnit.html)  
> 爬取时间: 2026-05-23 10:33:43  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_AddUnit (table)


This function adds a new unit to a side based on the supplied table.
As the function
ScenEdit_SetUnit()
is called at the end of this function, any options not listed below will be passed into the next function.
There should be no need to call
ScenEdit_SetUnit()
seperately.


### Parameters

- table
{}
The unit details to add.
Note that some settings will depend on the type of unit specified, eg aircraft generally need loadouts and altitude whereas neither is needed by a ship.
type =
UnitType
The description of the type of unit to add ( eg Ship, Sub, ...)
unitname =
string
The name of the unit
side =
string
The side name/GUID to add the unit to
dbid =
number
The database id of the unit
base =
string
Unit base name/GUID where the unit will be 'hosted' (applies to types AIR, SHIP, SUB)
latitude =
Latitude
Not required if a
base
is defined as unit adopts that location
longitude =
Longitude
Not required if a
base
is defined as adopts that location
altitude =
Altitude
The Unit altitude (applies to AIR). If a
base
is defined, it will adopt it's altitude
loadoutid =
number
Aircraft database loadout id (applies to type AIR)
orbit =
number
Orbit index (applies to type SATELLITE)
guid =
string
Optional custom GUID to override the auto generated one
- type =
UnitType
The description of the type of unit to add ( eg Ship, Sub, ...)
- unitname =
string
The name of the unit
- side =
string
The side name/GUID to add the unit to
- dbid =
number
The database id of the unit
- base =
string
Unit base name/GUID where the unit will be 'hosted' (applies to types AIR, SHIP, SUB)
- latitude =
Latitude
Not required if a
base
is defined as unit adopts that location
- longitude =
Longitude
Not required if a
base
is defined as adopts that location
- altitude =
Altitude
The Unit altitude (applies to AIR). If a
base
is defined, it will adopt it's altitude
- loadoutid =
number
Aircraft database loadout id (applies to type AIR)
- orbit =
number
Orbit index (applies to type SATELLITE)
- guid =
string
Optional custom GUID to override the auto generated one
`base`
`base`
`base`

### Returns


Unit
A wrapper defining the added unit. This will be nil if the function failed to add the unit.


### Example

`Show an example of how to use the function. Explain it or add multiple examples to expand it`
`ScenEdit_AddUnit({
type
=
'Air'
, unitname =
'F-15C Eagle'
, loadoutid =
16934
, dbid =
3500
, side =
'NATO'
, Lat=
"5.123"
,Lon=
"-12.51"
,alt=
5000
})`
`ScenEdit_AddUnit( {
type
=
'Ship'
, unitname =
'GOE II Det C'
, dbid =
3127
, side =
'USN'
, latitude=
"5.123"
,longitude=
"-12.51"
,proficiency='Veteran'} )`
`ScenEdit_AddUnit({
type
=
'Air'
, unitname =
'F-15C Eagle'
, loadoutid =
16934
, dbid =
3500
, side =
'NATO'
, Lat=
"5.123"
,Lon=
"-12.51"
,alt=
5000
})`
`ScenEdit_AddUnit( {
type
=
'Ship'
, unitname =
'GOE II Det C'
, dbid =
3127
, side =
'USN'
, latitude=
"5.123"
,longitude=
"-12.51"
,proficiency='Veteran'} )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
