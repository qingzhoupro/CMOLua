# UI_CallAdvancedDialog

> 官方文档来源: [https://commandlua.github.io/assets/Function_UI_CallAdvancedDialog.html](https://commandlua.github.io/assets/Function_UI_CallAdvancedDialog.html)  
> 爬取时间: 2026-05-23 10:38:43  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### UI_CallAdvancedDialog 
				( title, description, interactions )


The function allows you to create a dynamic dialog box from Lua script.


### Parameters

- title
string
The title that shows on the top of the dialog box
- description
string
The message to include in the dialog box
- interactions
{ 
                            }

                            of
string
One of more Button names

### Returns


string
The Button pressed

`local button = UI_CallAdvancedDialog("My title", "My description", {"Potato","Orange","Apple","Banana","Tomato","Any other option"})
if button == 'Potato' then
print('You pressed ' .. button )
else
print('You did not press Potato but ' .. button )
end`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
