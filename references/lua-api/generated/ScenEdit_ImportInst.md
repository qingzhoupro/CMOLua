# ScenEdit_ImportInst

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_ImportInst.html](https://commandlua.github.io/assets/Function_ScenEdit_ImportInst.html)  
> 爬取时间: 2026-05-23 10:37:45  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_ImportInst
                    (side,filename)


This function imports unit(s) in XML format from an INST file in the folder 'ImportExport'.


### Parameters

- side
string
The
                        side
                        to
                        import
                        the
                        inst
                        file
                        as
- filename
string
The
                        filename
                        of
                        the
                        inst
                        file

### Returns


number
Number of units imported

`local a = ScenEdit_ImportInst( "USN","NAF Midway-Henderson Airport 2010.inst" )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
