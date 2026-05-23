# ScenEdit_RemoveSide

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_RemoveSide.html](https://commandlua.github.io/assets/Function_ScenEdit_RemoveSide.html)  
> 爬取时间: 2026-05-23 10:34:57  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_RemoveSide
                    (table)


This function remove a
                    side
                    from
                    play. This
                    removes
ALL
units
                    and
                    contacts for the side.


### Parameters

- table
{}
side =
string
The side name/GUID to remove
- side =
string
The side name/GUID to remove

### Returns


Side
A wrapper for the side removed, or
nil
otherwise

`nil`
`local s = ScenEdit_RemoveSide( {side="United States" } )
print( s.name .. ' was removed')`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
