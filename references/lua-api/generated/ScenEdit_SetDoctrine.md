# ScenEdit_SetDoctrine

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_SetDoctrine.html](https://commandlua.github.io/assets/Function_ScenEdit_SetDoctrine.html)  
> 爬取时间: 2026-05-23 10:34:01  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_SetDoctrine
                    (table, doctrine)


This function Sets
                    the
                    doctrine
                    of
                    the
                    designated
                    object


It modifies
                    the
                    doctrine
                    of
                    that
                    object
                    at
                    the Side,Unit/Group or Mission level


The doctrine level to be affected is determined by the parameters passed:
side only -> side level
guid, unitname -> unit/group level
mission -> mission level
In order to reset a doctrine back to 'inherit', pass a empty 'doctrine' to the function.

- side only -> side level
- guid, unitname -> unit/group level
- mission -> mission level

### Parameters

- table
{}
side =
string
The side name/GUID of the unit
unitname =
string
The name of unit
guid =
string
The GUID of the unit
mission =
string
The mission guid/name
escort =
True/False
If a mission, apply changes to Escort of Strike mission
- doctrine
{}
Refer to the Doctrine object
Doctrine
for the possible values
Only the items to be updated need to be added as 'doctrine_item = value'.
The value of 'inherit' will reset that doctrine_item to inherit from its parent doctrine, otherwise the value is validated against its acceptable values.
- side =
string
The side name/GUID of the unit
- unitname =
string
The name of unit
- guid =
string
The GUID of the unit
- mission =
string
The mission guid/name
- escort =
True/False
If a mission, apply changes to Escort of Strike mission

### Returns


Doctrine
Returns the
                    updated doctrine object

`ScenEdit_SetDoctrine({side=
"Soviet Union"
}, {kinematic_range_for_torpedoes =
"AutomaticAndManualFire"
,use_nuclear_weapons=
"yes"
})`
`ScenEdit_SetDoctrine({side=
"Soviet Union"
, mission=
"ASW PATROL"
}, {kinematic_range_for_torpedoes =
"AutomaticAndManualFire"
,use_nuclear_weapons=
"yes"
})`
`ScenEdit_SetDoctrine({side=
"Soviet Union"
, unitname=
"Bear #2"
}, {use_nuclear_weapons=
"yes"
})`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
