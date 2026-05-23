# ScenEdit_UpdateUnitCargo

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_UpdateUnitCargo.html](https://commandlua.github.io/assets/Function_ScenEdit_UpdateUnitCargo.html)  
> 爬取时间: 2026-05-23 10:34:28  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_UpdateUnitCargo
                    ( table )


This function Updates the
                    cargo space
                    on
                    a
                    unit.
By default, this treats the cargo type as 'mount' as per the original cargo V1 specifications.
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
'add_cargo', 'remove_cargo'
The action mode to perform
cargo =
{
                                    }

                                    of multiple
cargo to affect
string
Unit/Container GUID - the specific unit/container to remove from cargo. This is not supported for ADD_CARGO.
or
{
                                            }

                                            of
number
Mount database id (DBID) and is treated as one mount to act on
or
{
                                            }

                                            of
number
Number to act on
number
Mount DBID to affect
Note the order of 'number to affect' and 'DBID'
or
{
                                            }

                                            of
number
Number to act on
number
Unit/Container DBID to affect
value
'1 = Mount', '2 = Ground', '3 = Facility', '4 = Container'
Type of cargo that DBID refers to
- guid =
string
The GUID of the unit
- mode =
value
'add_cargo', 'remove_cargo'
The action mode to perform
- cargo =
{
                                    }

                                    of multiple
cargo to affect
string
Unit/Container GUID - the specific unit/container to remove from cargo. This is not supported for ADD_CARGO.
or
{
                                            }

                                            of
number
Mount database id (DBID) and is treated as one mount to act on
or
{
                                            }

                                            of
number
Number to act on
number
Mount DBID to affect
Note the order of 'number to affect' and 'DBID'
or
{
                                            }

                                            of
number
Number to act on
number
Unit/Container DBID to affect
value
'1 = Mount', '2 = Ground', '3 = Facility', '4 = Container'
Type of cargo that DBID refers to
- string
Unit/Container GUID - the specific unit/container to remove from cargo. This is not supported for ADD_CARGO.
- {
                                            }

                                            of
number
Mount database id (DBID) and is treated as one mount to act on
- {
                                            }

                                            of
number
Number to act on
number
Mount DBID to affect
Note the order of 'number to affect' and 'DBID'
- {
                                            }

                                            of
number
Number to act on
number
Unit/Container DBID to affect
value
'1 = Mount', '2 = Ground', '3 = Facility', '4 = Container'
Type of cargo that DBID refers to
- number
Number to act on
- number
Mount DBID to affect
- number
Number to act on
- number
Unit/Container DBID to affect
- value
'1 = Mount', '2 = Ground', '3 = Facility', '4 = Container'
Type of cargo that DBID refers to

### Returns


Unit
The
                    updated unit
                    object

`ScenEdit_UpdateUnitCargo( { guid='2cd64757-1b66-4609-ad56-df41bee652e5', mode='add_cargo', cargo={ {5,752}, {700 } } } )`
`ScenEdit_UpdateUnitCargo( { guid='2cd64757-1b66-4609-ad56-df41bee652e5', mode='remove_cargo', cargo={'871aea14-d963-4052-a7fc-ed36e97bb732',{5,752} } } )`
`local u = ScenEdit_GetUnit({name='Yokosuka Building 14 (Large)', guid='29541903-93d0-436b-9f08-a4696f12a4fc'})
local a = ScenEdit_UpdateUnitCargo({guid='29541903-93d0-436b-9f08-a4696f12a4fc',mode='add_cargo',cargo={ {1,2541}, {3,361,3}, {4,7,4}, {2,246,2} } })
print(a.cargo)`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
