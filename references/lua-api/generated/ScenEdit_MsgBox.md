# ScenEdit_MsgBox

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_MsgBox.html](https://commandlua.github.io/assets/Function_ScenEdit_MsgBox.html)  
> 爬取时间: 2026-05-23 10:36:57  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_MsgBox
                    (string, style)


This function displays a message box with the passed string. The buttons to show are controlled by the 'style'.


### Parameters

- string
string
The
                        string
                        to
                        display
                        to
                        the
                        user
- style
value
0 = OK
1 = OK and Cancel buttons
2 = Abort, Retry and Ignore buttons
3 = Yes, No and Cancel buttons
4 = Yes and No buttons
5 = Retry and Cancel buttons.
The
                        style
                        of
                        the
                        message
                        box

### Returns


number
The button
                    number
                    pressed.
                    None = 0,
                    OK = 1,
                    Cancel = 2,
                    Abort = 3,
                    Retry = 4,
                    Ignore = 5,
                    Yes = 6,
                    No = 7

`local a = ScenEdit_MsgBox('Select both a downed pilot to rescue and a nearby friendly unit to perform this special action.',0)`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
