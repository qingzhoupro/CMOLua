# ScenEdit_AddMinefield

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_AddMinefield.html](https://commandlua.github.io/assets/Function_ScenEdit_AddMinefield.html)  
> 爬取时间: 2026-05-23 10:37:29  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_AddMinefield( table )


This function will attempt to lay a minefield for a Side consisting of the mine type, a number to lay, an arming delay and the area of the field to sow them in.
Mines are laid within their depth settings, and there are proximity considerations. This is why the full number might not be laid in one execution of the command.
Normal RPs are checked first, and then the No-nav/Exclusion zone RPs for the area to lay the mines in.
If NO mines are being laid, check that the water depth is within the parameters of the mine being laid.


Normal RPs are checked first, and then the No-nav/Exclusion zone RPs for the area to lay the mines in.


### Parameters

- table
{}
area =
{} of multiple
The area to lay the mines in
string
The reference point guid/name
dbid =
number
The database id of the mine to use
delay =
number
The arming delay in seconds
number =
number
The number of mines to attempt to lay
side =
string
The Side name/guid that owns the mines
- area =
{} of multiple
The area to lay the mines in
string
The reference point guid/name
- dbid =
number
The database id of the mine to use
- delay =
number
The arming delay in seconds
- number =
number
The number of mines to attempt to lay
- side =
string
The Side name/guid that owns the mines
- string
The reference point guid/name

### Returns


number
number of mines actually laid

`local a = ScenEdit_AddMinefield( { side='Sidea', dbid=634, number=100, delay=60000, area={'rp-3136','rp-3137','rp-3138','rp-3139'} } )
print('Number laid ' .. a)
Number laid 51`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
