# ScenEdit_UseAttachmentOnSide

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_UseAttachmentOnSide.html](https://commandlua.github.io/assets/Function_ScenEdit_UseAttachmentOnSide.html)  
> 爬取时间: 2026-05-23 10:37:51  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_UseAttachmentOnSide
                    (attachment, sidename)


This function uses
                    an
                    attachment
                    on
                    a
                    side
                    (used
                    for
                    .inst
                    files
                    as
                    attachments).


### Parameters

- attachment
string
Name
                        of
                        the
                        attachment
                        (as shown
                        in the
                        properties
                        section
                        when
                        created/added)
or more accurately
                        the
                        GUID
                        of
                        the
                        attachment (as found in AttachmentRepo folders)
- sidename
string
The
                        name
                        of
                        the
                        side
                        to
                        import
                        the
                        attachment
                        into

### Returns


True/False
True if successful, or
nil
otherwise

`nil`
`local b = ScenEdit_UseAttachmentOnSide('8269b881-20ce-4f2e-baa0-6823e46d55a4', 'sidea' )`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
