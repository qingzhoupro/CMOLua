# ScenEdit_GetKeyValue

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetKeyValue.html](https://commandlua.github.io/assets/Function_ScenEdit_GetKeyValue.html)  
> 爬取时间: 2026-05-23 10:37:25  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetKeyValue (key, forCampaign)


This function retrieves a value put into the persistent key store by
ScenEdit_SetKeyValue
.The key name used must be identical.


### Parameters

- key
string
The key to fetch the value for
- forCampaign
True/False
Read from the key store being passed to the next scenario in campaign. Optional, default = false

### Returns


string
The value associated with the key. "" if none exists.

`ScenEdit_SetKeyValue( "A", "2" )
local u = ScenEdit_GetKeyValue( "A")`

The variable 'u' contains "2"


---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
