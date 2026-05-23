# ScenEdit_WeaponAllocation

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_WeaponAllocation.html](https://commandlua.github.io/assets/Function_ScenEdit_WeaponAllocation.html)  
> 爬取时间: 2026-05-23 10:38:33  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_WeaponAllocation (attackerID, contactId, attackingSideID)


This function returns the type and number of weapons allocated by a unit or side


### Parameters

- attackerID
string
The attacking unit guid
- contactId
string
The contact guid being attacked
- attackingSideID
string
The attacking side guid

### Returns

- shooter
string
Shooter GUID
- qtyAssigned
number
Quantity of weapons allocated
- weapon
string
Weapon DBID
- weaponName
string
Weapon name
- target
string
Target GUID
- qtyFired
number
Quantity of weapons fired
`local weaponsAllocation = ScenEdit_WeaponAllocation( 'TTZL89-0HNB700MD8D73', 'TTZL89-0HNB700MD8A4G' )
print(weaponsAllocation)
Output
{ [1] = { shooter = 'TTZL89-0HNB700MD8D73', qtyAssigned = 1, weapon = 779, weaponName = 'MGM-140B ATACMS Blk IA [275 x M74 Dual Purpose]', target = 'TTZL89-0HNB700MD8A4G', qtyFired = 1 } }`
`local weaponsAllocation = ScenEdit_WeaponAllocation( nil, 'TTZL89-0HNB700MD8A4G', 'TTZL89-0HNB700MD8A45' )
print(weaponsAllocation)
Output
{
[1] = { shooter = 'TTZL89-0HNB700MD8D73', qtyAssigned = 1, weapon = 779, weaponName = 'MGM-140B ATACMS Blk IA [275 x M74 Dual Purpose]', target = 'TTZL89-0HNB700MD8A4G', qtyFired = 1 },
[2] = { shooter = 'TTZL89-0HNB700MD8AE5', qtyAssigned = 2, weapon = 11, weaponName = 'AGM-158B JASSM-ER', target = 'TTZL89-0HNB700MD8A4G', qtyFired = 2 }
}`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
