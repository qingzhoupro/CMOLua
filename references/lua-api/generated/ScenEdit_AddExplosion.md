# ScenEdit_AddExplosion

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_AddExplosion.html](https://commandlua.github.io/assets/Function_ScenEdit_AddExplosion.html)  
> 爬取时间: 2026-05-23 10:37:53  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_AddExplosion( table )


This function creates a detonation of a warhead at a specific location.
Useful for simulating explosions where no weapon is fired such as a bomb being detonated.
*** Does not currently support under surface explosions ****


### Parameters

- table
{}
altitude =
altitude
The altitude of the detonation. If no 'altitude' is passed, or the value of the parameter is 'surface', the explosion will occur at 'ground zero' at that location.
latitude =
latitude
The latitude of the detonation
longitude =
longitude
The longitude of the detonation
warheadid =
number
The database ID of the warhead to detonate
- altitude =
altitude
The altitude of the detonation. If no 'altitude' is passed, or the value of the parameter is 'surface', the explosion will occur at 'ground zero' at that location.
- latitude =
latitude
The latitude of the detonation
- longitude =
longitude
The longitude of the detonation
- warheadid =
number
The database ID of the warhead to detonate

### Returns

- True/False
True if function successful

Simulating an explosion of device '1.4kg HE' at the unit 'myUnit' location

`ScenEdit_AddExplosion({warheadid = 253, latitude = myUnit.latitude, longitude = myUnit.longitude, altitude = myUnit.altitude})`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
