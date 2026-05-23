# Tool_EmulateNoConsole

> 官方文档来源: [https://commandlua.github.io/assets/Function_Tool_EmulateNoConsole.html](https://commandlua.github.io/assets/Function_Tool_EmulateNoConsole.html)  
> 爬取时间: 2026-05-23 10:38:04  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### Tool_EmulateNoConsole
                    ( mode )


This function allows other functions to behave as if there is no console attached by executing in the Lua console.
This is useful examining how functions behave when running within Command as in Events by running the script in the console first.
Some functions will 'die' if running in interactive mode.


### Parameters

- mode
True/False
'True' (which is the default mode if no parameter supplied) turns on the emulation mode, 'False' will turn it off.

### Returns


True/False
Current interactive mode

`local d = Tool_EmulateNoConsole( )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
