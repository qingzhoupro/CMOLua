# ScenEdit_TransformZone

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_TransformZone.html](https://commandlua.github.io/assets/Function_ScenEdit_TransformZone.html)  
> 爬取时间: 2026-05-23 10:36:15  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_TransformZone ( SideNameOrID, ZoneNameOrID, TargetType )


The function purpose is to convert a 'zone' from one type to another.
The types of 'zone' as non-navigation, exclusion and standard.
Once converted, some update may be required for any specifics related to the converted zone


### Parameters

- SideNameOrID
string
The side name/GUID containg the zone. Custom environment zones are always owned by the Nature side.
- ZoneNameOrID
string
The name/GUID of the zone
- TargetType
string
exclusion
nonav
standard
customenvironment
The type of zone to convert it to

### Returns

- An empty string "" on success else an error message.

### Example


Convert a non-navigation zone to an exclusion zone.
Note the zone under 'nonavzones' has been removed and a
new
one created under 'exclusionzones'.

`local a = VP_GetSide({side='sidea'})
print(a.nonavzones)
{ [1] = { description = 'no-go zone', guid = '3d339174-1264-4e29-8b5f-c11a3f6edee9' } }
print(a.exclusionzones)
{ }
print(a.standardzones)
{ }
ScenEdit_TransformZone ( 'sidea', 'no-go zone', 'exclusion' )
print(a.nonavzones)
{ }
print(a.exclusionzones)
{ [1] = { description = 'no-go zone', guid = 'GNRIJH-0HMJ351GVC5AI' } }
print(a.standardzones)
{ }`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
