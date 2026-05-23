# ScenEdit_SetKeyValue

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetKeyValue.html](https://commandlua.github.io/assets/Function_ScenEdit_SetKeyValue.html)  
> 爬取时间: 2026-05-23 10:37:23  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetKeyValue
                    (key, value, forCampaign)


This function Sets
                    the
                    value
                    for
                    a
                    key
                    in
                    the
                    persistent
                    key
                    store.


This
                    function
                    allows
                    you
                    to
                    add
                    values,associated
                    with
                    keys,to
                    a
                    persistent
                    store
KeyStore
that
                    is
                    retained
                    when
                    the
                    game
                    is
                    saved
                    and
                    resumed.Keys
                    and
                    values
                    are
                    both
                    represented
                    as
                    non-
nil
strings.The
                    value
                    is
                    retrieved
                    by
ScenEdit_GetKeyValue
.

`nil`

### Parameters

- key
string
The
                        key
                        to
                        associate
                        with
- value
string
The
                        value
                        to
                        associate
- forCampaign
boolean
Pass
                        the
                        store
                        to
                        next
                        scenario
                        in
                        campaign. Optional, default
                        = false
`ScenEdit_SetKeyValue(
"A"
,
"B"
)
                        ScenEdit_GetKeyValue(
"A"
)
-- returns "B"`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
