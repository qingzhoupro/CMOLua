# ScenEdit_SetSidePosture

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetSidePosture.html](https://commandlua.github.io/assets/Function_ScenEdit_SetSidePosture.html)  
> 爬取时间: 2026-05-23 10:34:59  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetSidePosture
                    (sideA, sideB, posture)


This function Sets
                    side
                    A's
                    posture
                    towards
                    side
                    B
                    to
                    the
                    specified
                    posture.This
                    is
                    the
                    same
                    as
Stance
,but
                    only
                    the
                    first
                    character
                    of
                    the
                    name
                    is


### Parameters

- sideA
string
Side
                        A's
                        name
                        or
                        GUID
- sideB
string
Side
                        B's
                        name
                        or
                        GUID
- posture
value
'F' = Friendly
'H' = Hostile
'N' = Neutral
'U' = Unfriendly
The
                        posture
                        of
                        side
                        A
                        towards
                        side
                        B

### Returns


boolean
True/False
                    for
                    Successful/Failure

`ScenEdit_SetSidePosture(
"LuaSideA"
,
"LuaSideB"
,
"H"
)`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
