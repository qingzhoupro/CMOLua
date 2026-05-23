# ScenEdit_TransferCargo

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_TransferCargo.html](https://commandlua.github.io/assets/Function_ScenEdit_TransferCargo.html)  
> 爬取时间: 2026-05-23 10:34:24  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_TransferCargo
                    (fromUnit, toUnit, cargoList)


This function Transfers a
                    cargo
                    list
                    from a
                    'parent' to a
                    'child' unit


### Parameters

- fromUnit
string
The
                        unit name/guid
                        with the
                        cargo
- toUnit
string
The
                        unit name/guid
                        get the
                        cargo
- cargoList
{
                            }

                            of multiple
cargo to affect
string
Cargo GUID - treated as one unit to act on
or
{
                                    }

                                    of
number
Cargo database id (DBID) and is treated as one unit to act on
or
{
                                    }

                                    of
number
Number to act on
number
Cargo DBID to affect
Note the order of 'number to affect' and 'DBID'
- string
Cargo GUID - treated as one unit to act on
- {
                                    }

                                    of
number
Cargo database id (DBID) and is treated as one unit to act on
- {
                                    }

                                    of
number
Number to act on
number
Cargo DBID to affect
Note the order of 'number to affect' and 'DBID'
- number
Number to act on
- number
Cargo DBID to affect

### Returns


True/False
Successful
                    or
                    not

`ScenEdit_TransferCargo( '2cd64757-1b66-4609-ad56-df41bee652e5','Perth RAN', { {5,752}, {700 } } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
