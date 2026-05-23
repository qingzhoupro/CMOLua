# ScenEdit_AttackContact

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_AttackContact.html](https://commandlua.github.io/assets/Function_ScenEdit_AttackContact.html)  
> 爬取时间: 2026-05-23 10:35:57  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_AttackContact (attackerID, contactId, options)


This function causes an attack on a contact as an auto-target or manual target, with weapon allocation.


For a BOL attack, use "BOL" as the contactId.


Note:
The function will use the
weapon
from the aircraft loadout if applicable when no
mount
is supplied.
If no 'mount' is supplied, the first available one with the 'weapon' will be used.


### Parameters

- attackerID
string
The attacking unit name/guid
- contactId
string
The contact being attacked as a name/guid (GUID is better as the name can change as its classification changes)
- options
{}
mode =
TargetingMode
0 = AutoTargeted, 1 = ManualWeaponAlloc, 2 = ManualTargeted
The attack behaviour. 'ManualWeaponAlloc' requires supplying the weapon information to fire with.
mount =
number
The mount dbid to fire from [Applies to manual weapon launch ]
weapon =
number
The weapon dbid on the mount to fire [Applies to manual weapon launch ]
qty =
number
The number of weapons to fire in this salvo [Applies to manual weapon launch ]
If the contactId is 'BOL', then the following applies.
latitude =
latitude
The latitude of the aimpoint
longitude =
longitude
The longitude of the aimpoint
If the mode is '1' (ManualWeaponAlloc), then the following apply.
course =
{} of multiple
The course of the weapon(s) launched to the aimpoint/contact, otherwise direct to aimpoint. There is no check that the weapon can still hit the target after applying the 'course'.
latitude =
latitude
The latitude of the waypoint
longitude =
longitude
The longitude of the waypoint
- mode =
TargetingMode
0 = AutoTargeted, 1 = ManualWeaponAlloc, 2 = ManualTargeted
The attack behaviour. 'ManualWeaponAlloc' requires supplying the weapon information to fire with.
- mount =
number
The mount dbid to fire from [Applies to manual weapon launch ]
- weapon =
number
The weapon dbid on the mount to fire [Applies to manual weapon launch ]
- qty =
number
The number of weapons to fire in this salvo [Applies to manual weapon launch ]
- latitude =
latitude
The latitude of the aimpoint
- longitude =
longitude
The longitude of the aimpoint
- course =
{} of multiple
The course of the weapon(s) launched to the aimpoint/contact, otherwise direct to aimpoint. There is no check that the weapon can still hit the target after applying the 'course'.
latitude =
latitude
The latitude of the waypoint
longitude =
longitude
The longitude of the waypoint
- latitude =
latitude
The latitude of the waypoint
- longitude =
longitude
The longitude of the waypoint

### Returns


True/False
True if attack successfully assigned

`ScenEdit_AttackContact( 'Phantom #1', 'SKUNK #12', { mode='1', mount=438, weapon=1413, qty=10 } )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
