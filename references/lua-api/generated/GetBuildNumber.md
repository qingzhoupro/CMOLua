# GetBuildNumber

> 官方文档来源: [https://commandlua.github.io/assets/Function_GetBuildNumber.html](https://commandlua.github.io/assets/Function_GetBuildNumber.html)  
> 爬取时间: 2026-05-23 10:37:39  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### GetBuildNumber ()


This function returns the build number of the current game executable.
This is useful if you know that a certain function is not available or has changed from a certain build so the Lua scripts can be made flexible to handle the change.
For example, if the parameters to a certain function changed from a certain build number, then the script could check the executable build number, and call the function with the old parameters if the executable is before that build, and use new one parameters if after that build.


For example, if the parameters to a certain function changed from a certain build number, then the script could check the executable build number, and call the function with the old parameters if the executable is before that build, and use new one parameters if after that build.


### Parameters

- None

### Returns

- string
The build number
`(GetBuildNumber())
>>> 1134.3`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
