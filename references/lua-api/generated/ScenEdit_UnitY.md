# ScenEdit_UnitY

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_UnitY.html](https://commandlua.github.io/assets/Function_ScenEdit_UnitY.html)  
> 爬取时间: 2026-05-23 10:35:50  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_UnitY
                    ( )


(a) the Detecting Unit from
                    a
                    Unit
                    Detected
                    event
                    trigger, or
(b) the Damaging causing unit from a damage/destroyed event. The unit is the last one to actually cause damage during the event.


A table of details will be returned.
                    Otherwise, a
nil
is
                    returned.
Note
                    that
                    UnitY() can
                    also
                    be
                    used
                    as
                    a
                    shortcut
                    for
                    ScenEdit_UnitY().

`nil`

### Parameters

- None

### Returns


{
                        }

                        of
unit
Unit
The unit object
sensor
{
                                }

                                of multiple
sensors making contact
name
string
Sensor name
type
string
Sensor type

- unit
Unit
The unit object
- sensor
{
                                }

                                of multiple
sensors making contact
name
string
Sensor name
type
string
Sensor type
- name
string
Sensor name
- type
string
Sensor type
`local by = ScenEdit_UnitY()
                        print('Y:'); print( by)
print('Detected by: '); print( by.unit.name ..' of type ' .. by.unit.type ..' from ' .. by.unit.side)
print('Sensor: '); print( by.sensor[1].name .. ' of type ' .. by.sensor[1].type);`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
