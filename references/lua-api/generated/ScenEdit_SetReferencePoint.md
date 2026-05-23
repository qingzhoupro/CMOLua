# ScenEdit_SetReferencePoint

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetReferencePoint.html](https://commandlua.github.io/assets/Function_ScenEdit_SetReferencePoint.html)  
> 爬取时间: 2026-05-23 10:36:05  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetReferencePoint
                    (table)


This function Updates
                    the
                    values
                    contained
                    in
                    the
                    table. Values
                    may
                    be
                    omitted
                    if
                    they
                    are
                    intended
                    to
                    remain
                    unmodified.
The
                    'area' parameter
                    is
                    useful
                    for
                    changing
                    some
                    common
                    attribute, like
                    locking
                    or
                    highlighting,in
                    bulk.
Don't include the 'area' parameter if only updating one RP.


### Parameters

- table
{}
guid =
string
The guid for the reference point
side =
string
The side the reference point is visible to
name =
string
The name of the reference point
newname =
string
The new name of the reference point
latitude =
latitude
The latitude of the reference point
longitude =
longitude
The longitude of the reference point
highlighted =
True/False
True if the point should be selected
locked =
True/False
True if the point is locked
bearing =
number (0-360)
Bearing from the 'relative' unit
bearingtype =
type
Fixed (0) or Rotating (1)
Type of bearing
relativeto =
string
The unit name/guid that all the RP(s) relate to, if required
relativeto_contact =
string
The contact name/guid that all the RP(s) relate to, if required
relativeto_rp =
string
The RP name/guid that all the RP(s) relate to, if required
clear =
True/False
Remove the 'relative to' associated with the reference point(s)
area =
{
                                    }

                                    of multiple
A set of RPs to perform action on
name =
string
The name of the reference point
latitude =
latitude
The latitude of the reference point
longitude =
longitude
The longitude of the reference point
highlighted =
True/False
True if the reference point should be selected
locked =
True/False
True if the reference point is locked
distance =
distance
Distance from the 'relative' unit
bearing =
number (0-360)
Bearing from the 'relative' unit
bearingtype =
type
Fixed (0) or Rotating (1)
Bearing aspect of the reference point
- guid =
string
The guid for the reference point
- side =
string
The side the reference point is visible to
- name =
string
The name of the reference point
- newname =
string
The new name of the reference point
- latitude =
latitude
The latitude of the reference point
- longitude =
longitude
The longitude of the reference point
- highlighted =
True/False
True if the point should be selected
- locked =
True/False
True if the point is locked
- bearing =
number (0-360)
Bearing from the 'relative' unit
- bearingtype =
type
Fixed (0) or Rotating (1)
Type of bearing
- relativeto =
string
The unit name/guid that all the RP(s) relate to, if required
- relativeto_contact =
string
The contact name/guid that all the RP(s) relate to, if required
- relativeto_rp =
string
The RP name/guid that all the RP(s) relate to, if required
- clear =
True/False
Remove the 'relative to' associated with the reference point(s)
- area =
{
                                    }

                                    of multiple
A set of RPs to perform action on
name =
string
The name of the reference point
latitude =
latitude
The latitude of the reference point
longitude =
longitude
The longitude of the reference point
highlighted =
True/False
True if the reference point should be selected
locked =
True/False
True if the reference point is locked
distance =
distance
Distance from the 'relative' unit
bearing =
number (0-360)
Bearing from the 'relative' unit
bearingtype =
type
Fixed (0) or Rotating (1)
Bearing aspect of the reference point
- name =
string
The name of the reference point
- latitude =
latitude
The latitude of the reference point
- longitude =
longitude
The longitude of the reference point
- highlighted =
True/False
True if the reference point should be selected
- locked =
True/False
True if the reference point is locked
- distance =
distance
Distance from the 'relative' unit
- bearing =
number (0-360)
Bearing from the 'relative' unit
- bearingtype =
type
Fixed (0) or Rotating (1)
Bearing aspect of the reference point

### Returns


ReferencePoint
The
                    reference
                    point
                    object
                    for
                    the
                    reference
                    point
                    or
                    first
                    one
                    from
                    the
                    area list.

`ScenEdit_SetReferencePoint({side=
"United States"
, name=
"Downed Pilot"
, lat=
0.5
})`
`ScenEdit_SetReferencePoint({side=
"United States"
, name=
"Downed Pilot"
, lat=
0.5
, lon=
"N50.50.50"
, highlighted =
true
})`
`ScenEdit_SetReferencePoint({side=
"United States"
, area={
"rp-100"
,
"rp-101"
,
"rp-102"
,
"rp-103"
,
"rp-104"
}, highlighted =
true
})`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
