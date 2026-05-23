# ScenEdit_GetWeather

> 官方文档来源: [https://commandlua.github.io/assets/Function_ScenEdit_GetWeather.html](https://commandlua.github.io/assets/Function_ScenEdit_GetWeather.html)  
> 爬取时间: 2026-05-23 10:36:41  
> **警告：以下内容完全来自官方文档，请勿凭记忆修改。**

---


### ScenEdit_GetWeather
                    ()


This function Gets
                    the
                    current
                    weather
                    conditions.


### Parameters


### Returns


Weather

`local a = ScenEdit_GetWeather()`

A more involved use of this for a weather report

`function DTG(TimeVar)
if TimeVar == nil then
TimeVar = ScenEdit_CurrentTime()
end
local msgtime = os.date("!%d%H%M" .. "Z" .. " " .. "%b %y", TimeVar)
local msgtime = string.upper(msgtime)
return msgtime
function Round(num, numDecimalPlaces)
local mult = 10^(numDecimalPlaces or 0)
return math.floor(num * mult + 0.5) / mult
end
function ACP126(rec_station,snd_station,precedence,from,to,classification,body)
--rec_station --4 letter code (e.g. YDCX)
--snd_station --4 letter code +/- NR 3 number (e.g. YBDN NR 270)
--precedence --Flash (Z), Immediate (O), Priority (P), Routine (R), Flash Override (Y)
local dtg = DTG()
--from --e.g. MET FLT OPS
--to --e.g. SSN 21 SEAWOLF
--classification --Unclass +/- SBU / FOUO / NOFORN (Restricted), Confidential, Secret, Top Secret
--body
_,gr = body:gsub("%S+","")
local sig_string = string.upper('
'..rec_station..'
'..
'DE '..snd_station..'
'..
precedence..' '..dtg..'
'..
'fm '..from..'
'..
'to '..to..'
'..
'wd gr'..gr..'
'..
'bt
'..
classification..'
'..
body..'
'..
'bt
'..
'nnnn
')
return sig_string
end
function WeatherReport(outlook)
if outlook == nil then outlook = 'next forecast at '..DTG(ScenEdit_CurrentTime()+21600) end
--Generate special message to player
local weather = ScenEdit_GetWeather() --Get new weather parameters
local temp, cloud, rain, sea = weather.temp, weather.undercloud, weather.rainfall, weather.seastate
local f_temp = Round((temp*1.8) + 32,0) --Convert to Fahrenheit
--create rain/precipitation descriptor (based on in-game descriptions)
if rain == 0 then precipdesc = 'nil'
elseif rain < 5 then precipdesc = 'very light'
elseif rain < 11 then precipdesc = 'light'
elseif rain < 20 then precipdesc = 'moderate'
elseif rain < 30 then precipdesc = 'heavy'
elseif rain < 40 then precipdesc = 'very heavy'
else precipdesc = 'extreme'
end
--create cloud descriptor (based on in-game descriptions)
if cloud == 0 then clouddesc = 'clear skies'
elseif cloud < 0.2 then clouddesc = 'light low clouds'
elseif cloud < 0.3 then clouddesc = 'light middle clouds'
elseif cloud < 0.4 then clouddesc = 'light high clouds'
elseif cloud < 0.5 then clouddesc = 'moderate low clouds'
elseif cloud < 0.6 then clouddesc = 'moderate middle clouds'
elseif cloud < 0.7 then clouddesc = 'moderate high clouds'
elseif cloud < 0.8 then clouddesc = 'moderate middle clouds & light high clouds'
elseif cloud < 0.9 then clouddesc = 'solid middle clouds & moderate high clouds'
elseif cloud < 1.0 then clouddesc = 'thin fog & solid cloud cover'
else clouddesc = 'thick fog & solid cloud cover'
end
--rec_station,snd_station,precedence,from,to,classification,body
local wx_time = DTG()
local wx_report = ACP126('NEWC','JOCMETOPS','r','HQJOC METEOROLOGICAL OFFICE','FFG 06 NEWCASTLE
INFO ALL STATIONS','unclass','WX REPORT ' .. wx_time .. ' - EAST COAST AND BASS STRAIT
AVERAGE TEMP '.. temp ..'°C / '..f_temp..'°F
SEA STATE '.. sea ..'
'..precipdesc..' PRECIPITATION
'..clouddesc..'
'..outlook)
ScenEdit_SpecialMessage('playerside',wx_report)
end
WeatherReport()`

'..rec_station..'
'..
'DE '..snd_station..'
'..
precedence..' '..dtg..'
'..
'fm '..from..'
'..
'to '..to..'
'..
'wd gr'..gr..'
'..
'bt
'..
classification..'
'..
body..'
'..
'bt
'..
'nnnn


---

*本文件由脚本自动生成，如需更新请运行 `python scripts/scrape_cmo_api.py`*
