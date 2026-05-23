# Tool_QueryRCS

> 官方文档来源: [https://commandlua.github.io/assets/Function_Tool_QueryRCS.html](https://commandlua.github.io/assets/Function_Tool_QueryRCS.html)  
> 爬取时间: 2026-05-23 10:38:06  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### Tool_QueryRCS ( table)


This function calculates and returns a numerical value representing the signature strength of a specified
					targetunitname from the perspective of a designated sensorunitname. The type of signature being queried is
					determined by the SIGNATURETYPE parameter. A higher returned value signifies a more easily detectable target
					in the specified signature spectrum


### Parameters

- table
{
							}
- sensorunitname
string
The guid/name of the unit that is sensing the target.
- targetunitname
string
The name of the unit whose signature is being measured.
- SIGNATURETYPE =
SIGNATURETYPE
HullSonar_PassiveOnly_VLF,
										HullSonar_PassiveOnly_LF
										HullSonar_PassiveOnly_MF
										HullSonar_PassiveOnly_HF
										ActiveSonar
										Visual_Detect
										Visual_ID
										IR_Detect
										IR_ID
										Radar_A_D
										Radar_E_M
A string specifying the type of signature to be queried.

### Returns


number
Returns a numerical value representing the calculated signature strength


### SIGNATURETYPE Values

- HullSonar_PassiveOnly_VLF
- HullSonar_PassiveOnly_LF
- HullSonar_PassiveOnly_MF
- HullSonar_PassiveOnly_HF
- ActiveSonar
- Visual_Detect
- Visual_ID
- IR_Detect
- IR_ID
- Radar_A_D
- Radar_E_M
`local RCS = Tool_QueryRCS({sensorunitname="WT2BOY-0HNG7PDJTMU9E", targetunitname="WT2BOY-0HNG7PDJTMU5P", SIGNATURETYPE="Radar_E_M"})
print(RCS)
22.5134506225586`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
