# Tool_LOS

> 官方文档来源: [https://commandlua.github.io/assets/Function_Tool_LOS.html](https://commandlua.github.io/assets/Function_Tool_LOS.html)  
> 爬取时间: 2026-05-23 10:36:21  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### Tool_LOS ( table)


This function can return
(a) the distance to the radar horizon between mix of units and altitudes, or
(b) a true/false if a LOS exists between a unit and a contact


### Parameters

- table
{
                            }
mode =
number
Distance to horizon (0) or LOS is clear (1)
horizon =
number
Radar (0),  Visual (1) or ESM (2)
useRangeLimits =
True/False
If using a unit as the 'observer', use the min/max ranges of the sensor(s) in the unit to get the 'horizon'
observer =
{
                            }
altitude =
number
or
string
Altitude of the observer.
guid =
number
Observer unit GUID. The altitude of the unit and any mast height will be calculated.
If performing a LOS check, then this must be supplied
The 'altitude' and 'guid' are mutally exclusive; either use a Unit or Altitude. The Altitude is in meters; however you use a string to put this in as feet ('10000 ft') and it will be converted.
location =
{
								}
latitude =
number
or
string
Latitude of the from location
longitude =
number
or
string
Longitude of the from location
target =
{
                            }
altitude =
number
or
string
Altitude of the target
guid =
number
Target contact GUID. The altitude of the actual unit will be calculated.
If performing a LOS check, then this must be supplied
The 'altitude' and 'guid' are mutally exclusive; either use a Unit or Altitude. The Altitude is in meters; however you use a string to put this in as feet ('10000 ft') and it will be converted.
location =
{
								}
latitude =
number
or
string
Latitude of the to location
longitude =
number
or
string
Longitude of the to location
Returns
number
The
                    horizontal
                    distance
                    in
                    NM,
					or
True/False
Is the line of sight clear
Example
local los = Tool_LOS( {observer = {alt=10}, target ={alt=10972}} )
print(string.format('Distance to horizon = %.2f NM', los) )
Distance to horizon = 239.63 NM
local los = Tool_LOS( {observer = {guid='GNRIJH-0HMJFCEE2I3U8'}, target ={alt=10972}, useRangeLimits=true} )
print(string.format('Distance to horizon = %.2f NM', los) )
Distance to horizon = 230.00 NM
local los = Tool_LOS( {observer = {guid='GNRIJH-0HMJFCEE2I3U8'}, target ={guid='GNRIJH-0HMJFCEE2I9AN'}, mode = 1, horizon = 0} )
if type(los) == 'boolean' then
print(string.format('Line of sight to target = %s', los) )
else
print(string.format('Distance to horizon = %.2f NM', los) )
end
Line of sight to target = true
- mode =
number
Distance to horizon (0) or LOS is clear (1)
- horizon =
number
Radar (0),  Visual (1) or ESM (2)
- useRangeLimits =
True/False
If using a unit as the 'observer', use the min/max ranges of the sensor(s) in the unit to get the 'horizon'
- observer =
{
                            }
altitude =
number
or
string
Altitude of the observer.
guid =
number
Observer unit GUID. The altitude of the unit and any mast height will be calculated.
If performing a LOS check, then this must be supplied
The 'altitude' and 'guid' are mutally exclusive; either use a Unit or Altitude. The Altitude is in meters; however you use a string to put this in as feet ('10000 ft') and it will be converted.
location =
{
								}
latitude =
number
or
string
Latitude of the from location
longitude =
number
or
string
Longitude of the from location
- target =
{
                            }
altitude =
number
or
string
Altitude of the target
guid =
number
Target contact GUID. The altitude of the actual unit will be calculated.
If performing a LOS check, then this must be supplied
The 'altitude' and 'guid' are mutally exclusive; either use a Unit or Altitude. The Altitude is in meters; however you use a string to put this in as feet ('10000 ft') and it will be converted.
location =
{
								}
latitude =
number
or
string
Latitude of the to location
longitude =
number
or
string
Longitude of the to location
- altitude =
number
or
string
Altitude of the observer.
- guid =
number
Observer unit GUID. The altitude of the unit and any mast height will be calculated.
If performing a LOS check, then this must be supplied
- location =
{
								}
latitude =
number
or
string
Latitude of the from location
longitude =
number
or
string
Longitude of the from location
- latitude =
number
or
string
Latitude of the from location
- longitude =
number
or
string
Longitude of the from location
- altitude =
number
or
string
Altitude of the target
- guid =
number
Target contact GUID. The altitude of the actual unit will be calculated.
If performing a LOS check, then this must be supplied
- location =
{
								}
latitude =
number
or
string
Latitude of the to location
longitude =
number
or
string
Longitude of the to location
- latitude =
number
or
string
Latitude of the to location
- longitude =
number
or
string
Longitude of the to location

### Returns


number
The
                    horizontal
                    distance
                    in
                    NM,
					or
True/False
Is the line of sight clear

`local los = Tool_LOS( {observer = {alt=10}, target ={alt=10972}} )
print(string.format('Distance to horizon = %.2f NM', los) )
Distance to horizon = 239.63 NM`
`local los = Tool_LOS( {observer = {guid='GNRIJH-0HMJFCEE2I3U8'}, target ={alt=10972}, useRangeLimits=true} )
print(string.format('Distance to horizon = %.2f NM', los) )
Distance to horizon = 230.00 NM`
`local los = Tool_LOS( {observer = {guid='GNRIJH-0HMJFCEE2I3U8'}, target ={guid='GNRIJH-0HMJFCEE2I9AN'}, mode = 1, horizon = 0} )
if type(los) == 'boolean' then
print(string.format('Line of sight to target = %s', los) )
else
print(string.format('Distance to horizon = %.2f NM', los) )
end
Line of sight to target = true`

---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
