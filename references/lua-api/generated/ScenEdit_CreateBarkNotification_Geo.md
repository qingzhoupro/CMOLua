# ScenEdit_CreateBarkNotification_Geo

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_CreateBarkNotification_Geo.html](https://commandlua.github.io/assets/Function_ScenEdit_CreateBarkNotification_Geo.html)  
> 爬取时间: 2026-05-23 10:37:03  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_CreateBarkNotification_Geo (longitude, latitude, text, R, G, B [, moveUpward, fade, lifeTime, fontSize ] )


The function's purpose is to show a 'bark' at a specific location.
Barks are short text notifications that can be set to appear, briefly, anywhere on the map.


### Parameters

- longitude
longitude
- latitude
latitude
- text
string
Text to show
- R
number
The 'Red' component of the color (0-255) to show the text in
- G
number
The 'Green' component of the color (0-255)
- B
number
The 'Blue' component of the color (0-255)
- moveUpward
True/False
[Optional] Default is True. This will move the text upwards
- fade
True/False
[Optional] Default is True. This controls the fading out of the text
- lifeTime
number
[Optional] Default is 1 second. This controls how long the text stays visible
- fontSize
number
[Optional] Default is 18. This controls the fonst size of the text

### Returns

- True/False

### Example

`ScenEdit_CreateBarkNotification_Geo (-119.1778, 46.62715, 'Prepare to be amazed', 255, 0, 0 , true, true, 10, 18)`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
