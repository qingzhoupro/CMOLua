# UI_CallAdvancedHTMLDialog

> 官方文档来源: [https://commandlua.github.io/assets/Function_UI_CallAdvancedHTMLDialog.html](https://commandlua.github.io/assets/Function_UI_CallAdvancedHTMLDialog.html)  
> 爬取时间: 2026-05-23 10:38:45  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### UI_CallAdvancedHTMLDialog 
				( title, form, interactions )


The function allows you to show a HTML form, from which variables will be returned to the Lua script.


### Parameters

- title
string
The title that shows on the top of the dialog box
- form
string
A HTML form from which data can be entered, The current input supported modes are text, select, and radio.
- interactions
{ 
                            }

                            of
string
One of more Button names

### Returns


Table {} of
Form_name
=
value
The variable name from the form and its value. The button pressed is returned in the table under ['pressed'].

`local msg = [[
Example
Logistics Table
Introduce the quantity you need for each missile type
Missile
Qty
AIM-120A:
16x
24x
32x
HARM-88C
GBU-10
16x
24x
32x
]]
local button = UI_CallAdvancedHTMLDialog("Logistics", msg, {"Submit","Cancel"})
for k,v in pairs(button) do
print(k .. ' = ' .. v)
end
if button['pressed'] == 'Cancel' then
print("Cancel logic")
else
print("Process logic")
end
HARM = ''
pressed = Cancel
AIM-120D = 16
Cancel logic`

Introduce the quantity you need for each missile type


| Missile | Qty |
| --- | --- |
| AIM-120A: | 16x24x32x |
| HARM-88C |  |
| GBU-10 | 16x24x32x |


---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
