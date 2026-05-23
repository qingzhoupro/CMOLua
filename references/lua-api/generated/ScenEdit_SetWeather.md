# ScenEdit_SetWeather

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetWeather.html](https://commandlua.github.io/assets/Function_ScenEdit_SetWeather.html)  
> 爬取时间: 2026-05-23 10:36:43  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetWeather
                    (temperature, rainfall, undercloud, seastate)


This function Sets
                    the
                    current
                    weather
                    conditions.
It
                    takes
                    four
                    numbers
                    that
                    describe
                    the
                    desired
                    weather
                    conditions.These
                    conditions
                    are
                    applied
                    globally.


### Parameters

- temperature
number
The
                        current
                        baseline
                        temperature
                        (in
                        deg
                        C). Varies
                        by
                        latitude.
- rainfall
number
The
                        rainfall
                        rate, 0-50.
- undercloud
number
The
                        amount
                        of
                        sky
                        that
                        is
                        covered
                        in
                        cloud, 0.0-1.0
- seastate
number
The
                        current
                        sea
                        state
                        0-9.

### Returns


boolean
True/False
                    for
                    Successful/Failure

`ScenEdit_SetWeather(math.random(0,25), math.random(0,50), math.random(0,10)/10.0, math.random(0,9) )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
