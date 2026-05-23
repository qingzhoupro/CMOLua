# VP_GetContact

> 官方文档来源: [https://commandlua.github.io/assets/Function_VP_GetContact.html](https://commandlua.github.io/assets/Function_VP_GetContact.html)  
> 爬取时间: 2026-05-23 10:35:15  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### VP_GetContact
                    ( table )


This function returns
                    details
                    about
                    a
                    contact
                    unit


### Parameters

- table
{
                            }
guid =
string
The GUID of the contact
- guid =
string
The GUID of the contact

### Returns


Contact
Contact object

`local side = VP_GetSide( { name ="NATO" } )
local contacts = side.contacts
--List Of contacts
local con_guid = contacts[12].objectid
-- GUID of a specific contact
local a_contact = VP_GetContact( { guid = con_guid } )
-- details of contact as distinct to unit details`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
