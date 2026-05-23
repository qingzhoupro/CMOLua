# ScenEdit_HostUnitToParent

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_HostUnitToParent.html](https://commandlua.github.io/assets/Function_ScenEdit_HostUnitToParent.html)  
> 爬取时间: 2026-05-23 10:34:30  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_HostUnitToParent
                    (table)


This function hosts (bases) a unit on another unit.
If 'SelectedHostNameOrID' is used, then the unit will be moved from any location, including flying, to the location of the 'host' unit.
If 'SelectedBaseNameOrID' is used, then the unit's base will be set to this location only.
The parameters 'SelectedHostNameOrID' and 'SelectedBaseNameOrID' are usually mutally exclusive, and only one would normally be used at a time. They do the same 'basing' but one is immeditate the other not.
You can use both if you want to home port a unit but have it return to a different base.

- If 'SelectedHostNameOrID' is used, then the unit will be moved from any location, including flying, to the location of the 'host' unit.
- If 'SelectedBaseNameOrID' is used, then the unit's base will be set to this location only.

### Parameters

- table
{}
HostedUnitNameOrID =
string
The name or GUID of the unit to update.
The alternate parameter
HostedUnitNameOrID
can be used instead.
SelectedHostNameOrID =
string
The name or GUID of the host to move the unit into.
The alternate parameter
HostBaseNameOrID
can be used instead.
SelectedBaseNameOrID =
string
The name or GUID of the host to be the unit's assigned base.
The alternate parameter
AssignedBaseNameOrID
can be used instead.
"UnitX" can be used as a value in the above parameters when in an event script.
- HostedUnitNameOrID =
string
The name or GUID of the unit to update.
The alternate parameter
HostedUnitNameOrID
can be used instead.
- SelectedHostNameOrID =
string
The name or GUID of the host to move the unit into.
The alternate parameter
HostBaseNameOrID
can be used instead.
- SelectedBaseNameOrID =
string
The name or GUID of the host to be the unit's assigned base.
The alternate parameter
AssignedBaseNameOrID
can be used instead.

### Returns


True/False
True if successful.
OR if supplying both base parameters in same method.
[0] = host base T/F, [1] = assigned base T/F
True if successful.

`local a = ScenEdit_HostUnitToParent( {HostedUnitNameOrID='f4f9e0af-15c2-4582-8e80-b827c2ec2f56',
                        SelectedBaseNameOrID = 'San Diego'
                        } )`
`local a = ScenEdit_HostUnitToParent( {HostedUnitNameOrID='f4f9e0af-15c2-4582-8e80-b827c2ec2f56',
                        SelectedHostNameOrID = 'San Diego'
                        } )`
`local unit_ship1 = ScenEdit_GetUnit({side = "Side A", name = "Ship 1"})
local base_portA = ScenEdit_GetUnit({side = "Side A", name = "Port A"})
local base_portB = ScenEdit_GetUnit({side = "Side A", name = "Port B"})
local rebase_Ship1 = ScenEdit_HostUnitToParent({UnitName = unit_ship1.guid,  AssignedBaseNameOrID = base_portA.guid})
if type(rebase_Ship1) == 'boolean' then
print(tostring(rebase_Ship1))
else
print(tostring(rebase_Ship1[0]) .. ' ' .. tostring(rebase_Ship1[1]))
end`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
