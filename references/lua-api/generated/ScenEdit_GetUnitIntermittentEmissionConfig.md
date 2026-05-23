# ScenEdit_GetUnitIntermittentEmissionConfig

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetUnitIntermittentEmissionConfig.html](https://commandlua.github.io/assets/Function_ScenEdit_GetUnitIntermittentEmissionConfig.html)  
> 爬取时间: 2026-05-23 10:38:20  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetUnitIntermittentEmissionConfig ( AUNameOrID,PresetAlertID )


The function's purpose is to recall the configuation of the unit at the specified Alert.


### Parameters

- AUNameOrID
string
The name or GUID of the unit. As no Side is supplied, the unit name would need to be unique across the scenario.
- PresetAlertID
value
"GREEN"
"BLUE"
"YELLOW"
"ORANGE"
"RED"
"CUSTOM"
"ALL"
The Alert level

### Returns

- ConfigurationTable
{
                            }
UseEmissionInterval
True/False
EmissionDuration
number
Emission duration in seconds
EmissionInterval
number
Emission interval in seconds
EmissionIntervalVariation
number
Emission variation in seconds
SleepModeDelay
number
Time to sleep in seconds
FollowWRAforWakeBehavior
True/False
WakeWhenDetectingThreat
True/False
WakeID_UNKNOWN
True/False
WwkeID_PRECISEID
True/False
WakeID_KNWONTYPE
True/False
WakeIDKNOWNDOMAIN
True/False
WakeIDKNOWNCLASS
True/False
WakeStance_FRIENDLY
True/False
WakeStance_HOSTILE
True/False
WakeStance_NEUTRAL
True/False
WakeStance_UNFRIENDLY
True/False
WakeStance_UNKNOWN
True/False
- UseEmissionInterval
True/False
- EmissionDuration
number
Emission duration in seconds
- EmissionInterval
number
Emission interval in seconds
- EmissionIntervalVariation
number
Emission variation in seconds
- SleepModeDelay
number
Time to sleep in seconds
- FollowWRAforWakeBehavior
True/False
- WakeWhenDetectingThreat
True/False
- WakeID_UNKNOWN
True/False
- WwkeID_PRECISEID
True/False
- WakeID_KNWONTYPE
True/False
- WakeIDKNOWNDOMAIN
True/False
- WakeIDKNOWNCLASS
True/False
- WakeStance_FRIENDLY
True/False
- WakeStance_HOSTILE
True/False
- WakeStance_NEUTRAL
True/False
- WakeStance_UNFRIENDLY
True/False
- WakeStance_UNKNOWN
True/False

### Example

`local conf = {};
conf = ScenEdit_GetUnitIntermittentEmissionConfig ( 'USS Ulysess', 'Green')`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
