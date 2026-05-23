# VP_SetTimeCompression

> 官方文档来源: [https://commandlua.github.io/assets/Function_VP_SetTimeCompression.html](https://commandlua.github.io/assets/Function_VP_SetTimeCompression.html)  
> 爬取时间: 2026-05-23 10:37:58  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### VP_SetTimeCompression ( number )


The function changes the current time compression ( the 'x#' on the UI).


### Parameters

- number
value
0 = One Second
1 = Two Seconds
2 = Five Seconds
3 = Fifteen Seconds
4 = Coarse One Sec Slice
5 = Coarse Five Sec Slice

### Returns

- None

### Example

`VP_SetTimeCompression( 2 )  -- change to 5 seconds`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
