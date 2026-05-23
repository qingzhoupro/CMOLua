# ScenEdit_CurrentTime

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_CurrentTime.html](https://commandlua.github.io/assets/Function_ScenEdit_CurrentTime.html)  
> 爬取时间: 2026-05-23 10:36:34  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_CurrentTime ()


This function returns the current scenario date/time.
This can then be customised to show in various ways for the in-game messages


### Parameters

- None

### Returns


TimeStamp
The UTC Unix timestamp of the current time in-game.

`local now = ScenEdit_CurrentTime()
local elapsed = now - timeFromLastTiggered
if elapsed > 60*5 then
-- been more than 5 minutes, set the lastTriggered time to now
timeFromLastTiggered = now
end`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
