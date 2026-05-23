# ScenEdit_SpecialMessage

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SpecialMessage.html](https://commandlua.github.io/assets/Function_ScenEdit_SpecialMessage.html)  
> 爬取时间: 2026-05-23 10:37:01  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SpecialMessage
                    (side, message, [location, forceMapRecenter])


This function will Display a special message consisting of the HTML text
message
to the side specified by
side
.
Optional parameters
location
allows the player to jump to the specified map position by clicking a button in a pop-up window.
The optional parameter
forceMapRecenter
will center the map on specified location.


### Parameters

- side
string
The side name/guid to display the message to, or
'playerside'
(see Note below)
- message
string
The HTML text to display to the player. Plain text is also accepted.
- location [optional]
{
                            }

                            of
latitude =
latitude
longitude =
longitude
The position that the 'Jump to Location' button takes the player to if clicked.
- forceMapRecenter [optional]
True/False
The map will be centered on location if present.
`'playerside'`
- latitude =
latitude
- longitude =
longitude

### Returns


number
1 if successful, raises an error if unsuccessful.

`ScenEdit_SpecialMessage( 'playerside', 'Here\'s a message!', { latitude = 1.2, longitude = 3.4 } )`

Note:
The string
'playerside'
is a special name that refers to whichever side is currently under player control and can be used to ensure that a special message is visible regardless of the player switching sides during the session or choosing a different side at scenario start.

`'playerside'`

Caution:
Players can disable pop-ups for special messages in the game options. Ensure that players are aware of the need to turn this feature on if special messages are essential to scenario function.


---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
