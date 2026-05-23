# ScenEdit_ClearKeyValue

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_ClearKeyValue.html](https://commandlua.github.io/assets/Function_ScenEdit_ClearKeyValue.html)  
> 爬取时间: 2026-05-23 10:37:27  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_ClearKeyValue (key, forCampaign)


This function removes a key (and its value) from the persistent keystore.
To clear the full keystore, use "" as the 'key'.


### Parameters

- key
string
The key to clear or empty for all
- forCampaign
True/False
Use key store for passing data to next scenario in a campaign. [Experimental] [Optional, default = false]

### Returns


True/False
True if Successful

`ScenEdit_ClearKeyValue("A")`

### ScenEdit_CurrentLocalTime ()


Ths function returns the scenario local time.


### Parameters

- None

### Returns


string
The local time as HH:MM:SS.

`local myTime = ScenEdit_CurrentLocalTime()`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
