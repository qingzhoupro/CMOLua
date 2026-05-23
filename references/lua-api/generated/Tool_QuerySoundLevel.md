# Tool_QuerySoundLevel

> 官方文档来源: [https://commandlua.github.io/assets/Function_Tool_QuerySoundLevel.html](https://commandlua.github.io/assets/Function_Tool_QuerySoundLevel.html)  
> 爬取时间: 2026-05-23 10:38:08  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### Tool_QuerySoundLevel ( table)


Returns the sound SL of naval units


### Parameters

- table
{
							}
- targetunitname
string
The guid/name of the unit that is sensing the target.
- targetside
string
(Optional) name of unit side
- frequency =
Freq
'VLF','LF','MF','HF'
(Optional) sound band of interest; LF is default

### Returns


number
Returns a numerical value representing the SL in the given band

`print(Tool_QuerySoundLevel({targetunitname="SSN 768 Hartford"}))
56.4`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
