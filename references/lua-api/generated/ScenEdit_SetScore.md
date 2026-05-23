# ScenEdit_SetScore

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetScore.html](https://commandlua.github.io/assets/Function_ScenEdit_SetScore.html)  
> 爬取时间: 2026-05-23 10:36:47  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetScore
                    (side, score, reason)


This function updates
                    a
                    given
                    side's
                    score.


### Parameters

- side
string
The
                        name/GUID
                        of
                        the
                        side
- score
number
The
                        new
                        score
                        for
                        the
                        side
- reason
string
The
                        reason
                        for
                        the
                        score
                        change

### Returns


number
The
                    new
                    score
                    for
                    the
                    side

`ScenEdit_SetScore(
"PlayerSide"
,
20
,
"Reset score"
)`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
