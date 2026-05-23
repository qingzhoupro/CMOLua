# ScenEdit_SetUnit

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetUnit.html](https://commandlua.github.io/assets/Function_ScenEdit_SetUnit.html)  
> 爬取时间: 2026-05-23 10:33:47  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetUnit
                    ( table )


This function Sets the properties of an existing unit


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
newname =
string
Rename the unit
group =
string
Assign to a group name/guid
mission =
string
Assign to a mission name/guid
speed =
number
Set unit speed (mutally exclusive to 'throttle')
throttle =
string
Set unit throttle (mutally exclusive to 'speed')
forceSpeed =
True/False
Force speed (use an external throttle setting???)
launch =
True/False
Launch unit from base
rtb =
True/False
Return unit to base
jettison =
value
"HEAVYONLY" = drop tanks, Air2Ground weapons
"WEAPONSONLY" = AG and Air2Air weapons
"ALLEXTERNAL" = drop tanks, all AG/AA, pods
"ALL" = all external and internal loads
"STORE_dbid = specific weapon DBID"
Jettison stores
refuel =
True/False
Unit attempts to refuel as per ROE
unassign =
True/False
Unassign unit
moveto =
True/False
Moves to alt/depth rather than jump to it
altitude =
number
Altitude to set
depth =
number
Depth to set
heading =
number
Set to immediate heading
desiredHeading =
number
Set to desired heading so unit turns towards it
longitude =
number
Unit's location - longitude
latitude =
number
Unit's location - latitude
autoDetectable =
True/False
Unit is autodetectable
outOfComms =
True/False
Unit is out of communications
holdPosition =
True/False
Unit holds position
holdFire =
True/False
Unit holds fire
proficiency =
string
Unit proficiency
manualthrottle =
value
FullStop = 0
Loiter = 1
Cruise = 2
Full = 3
Flank = 4
Manaual setting
manualspeed =
string
Manaual setting
manualaltitude =
string
Manaual setting
fuel =
{
                                    }

                                    of multiple
Set the unit fuel type quantity (aircraft are assumed to only have one type when allocating quantity)
string
fuel type
number
quantity
base =
string
Base name/guid to assign unit to
sprintDrift =
True/False
Unit uses sprint and drift (ship, submarine)
avoidcavitation =
True/False
Unit avoids cavitation (ship, submarine)
csar =
True/False
The unit can be assigned as a target for SAR
timetoready_minutes =
number
Number of minutes to ready (ship, submarine, aircraft)
course =
{
                                    }

                                    of multiple
latitude =
latitude
The latitude of the new reference point
longitude =
longitude
The longitude of the new reference point
- side =
string
The side name/GUID of the unit
- unitname =
string
The name of unit
- guid =
string
The GUID of the unit
- newname =
string
Rename the unit
- group =
string
Assign to a group name/guid
- mission =
string
Assign to a mission name/guid
- speed =
number
Set unit speed (mutally exclusive to 'throttle')
- throttle =
string
Set unit throttle (mutally exclusive to 'speed')
- forceSpeed =
True/False
Force speed (use an external throttle setting???)
- launch =
True/False
Launch unit from base
- rtb =
True/False
Return unit to base
- jettison =
value
"HEAVYONLY" = drop tanks, Air2Ground weapons
"WEAPONSONLY" = AG and Air2Air weapons
"ALLEXTERNAL" = drop tanks, all AG/AA, pods
"ALL" = all external and internal loads
"STORE_dbid = specific weapon DBID"
Jettison stores
- refuel =
True/False
Unit attempts to refuel as per ROE
- unassign =
True/False
Unassign unit
- moveto =
True/False
Moves to alt/depth rather than jump to it
- altitude =
number
Altitude to set
- depth =
number
Depth to set
- heading =
number
Set to immediate heading
- desiredHeading =
number
Set to desired heading so unit turns towards it
- longitude =
number
Unit's location - longitude
- latitude =
number
Unit's location - latitude
- autoDetectable =
True/False
Unit is autodetectable
- outOfComms =
True/False
Unit is out of communications
- holdPosition =
True/False
Unit holds position
- holdFire =
True/False
Unit holds fire
- proficiency =
string
Unit proficiency
- manualthrottle =
value
FullStop = 0
Loiter = 1
Cruise = 2
Full = 3
Flank = 4
Manaual setting
- manualspeed =
string
Manaual setting
- manualaltitude =
string
Manaual setting
- fuel =
{
                                    }

                                    of multiple
Set the unit fuel type quantity (aircraft are assumed to only have one type when allocating quantity)
string
fuel type
number
quantity
- base =
string
Base name/guid to assign unit to
- sprintDrift =
True/False
Unit uses sprint and drift (ship, submarine)
- avoidcavitation =
True/False
Unit avoids cavitation (ship, submarine)
- csar =
True/False
The unit can be assigned as a target for SAR
- timetoready_minutes =
number
Number of minutes to ready (ship, submarine, aircraft)
- course =
{
                                    }

                                    of multiple
latitude =
latitude
The latitude of the new reference point
longitude =
longitude
The longitude of the new reference point
- string
fuel type
- number
quantity
- latitude =
latitude
The latitude of the new reference point
- longitude =
longitude
The longitude of the new reference point

### Returns


Unit
Update unit object

`ScenEdit_SetUnit({side=
"United States"
, unitname=
"USS Test"
, lat =
5
})`
`ScenEdit_SetUnit({side=
"United States"
, unitname=
"USS Test"
, lat =
5
})`
`ScenEdit_SetUnit({side=
"United States"
, unitname=
"USS Test"
, lat =
5
, lon =
"N50.20.10"
})`
`ScenEdit_SetUnit({side=
"United States"
, unitname=
"USS Test"
, newname=
"USS Barack Obama"
})`
`ScenEdit_SetUnit({side=
"United States"
, unitname=
"USS Test"
, heading=
0
, HoldPosition=
1
, HoldFire=
1
,Proficiency=
"Ace"
, Autodetectable=
"yes"
})`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
