# CMO 数据库结构文档

> 自动生成于 2026-04-25 09:17:59
> 
> 数据库: `F:\codeAi\AIassistant\03_Archive\CMO-HKBQSKILL\mcp\db\DB3K_514.db3`
> 
> 共 174 张表

---

## 目录


### 数据表 (Data*)

- [DataAircraft](#dataaircraft)  
- [DataAircraftCodes](#dataaircraftcodes)  
- [DataAircraftComms](#dataaircraftcomms)  
- [DataAircraftFacility](#dataaircraftfacility)  
- [DataAircraftFuel](#dataaircraftfuel)  
- [DataAircraftLoadouts](#dataaircraftloadouts)  
- [DataAircraftMounts](#dataaircraftmounts)  
- [DataAircraftPropulsion](#dataaircraftpropulsion)  
- [DataAircraftSensors](#dataaircraftsensors)  
- [DataAircraftSignatures](#dataaircraftsignatures)  
- [DataComm](#datacomm)  
- [DataCommCapabilities](#datacommcapabilities)  
- [DataCommDirectors](#datacommdirectors)  
- [DataCommType](#datacommtype)  
- [DataCommTypeCanTalkTo](#datacommtypecantalkto)  
- [DataContainer](#datacontainer)  
- [DataDockingFacility](#datadockingfacility)  
- [DataFacility](#datafacility)  
- [DataFacilityAircraftFacilities](#datafacilityaircraftfacilities)  
- [DataFacilityComms](#datafacilitycomms)  
- [DataFacilityDockingFacilities](#datafacilitydockingfacilities)  
- [DataFacilityFuel](#datafacilityfuel)  
- [DataFacilityMagazines](#datafacilitymagazines)  
- [DataFacilityMounts](#datafacilitymounts)  
- [DataFacilitySensors](#datafacilitysensors)  
- [DataFacilitySignatures](#datafacilitysignatures)  
- [DataFuel](#datafuel)  
- [DataGroundUnit](#datagroundunit)  
- [DataGroundUnitAircraftFacilities](#datagroundunitaircraftfacilities)  
- [DataGroundUnitCodes](#datagroundunitcodes)  
- [DataGroundUnitComms](#datagroundunitcomms)  
- [DataGroundUnitDockingFacilities](#datagroundunitdockingfacilities)  
- [DataGroundUnitFuel](#datagroundunitfuel)  
- [DataGroundUnitMagazines](#datagroundunitmagazines)  
- [DataGroundUnitMounts](#datagroundunitmounts)  
- [DataGroundUnitPropulsion](#datagroundunitpropulsion)  
- [DataGroundUnitSensors](#datagroundunitsensors)  
- [DataGroundUnitSignatures](#datagroundunitsignatures)  
- [DataLoadout](#dataloadout)  
- [DataLoadoutWeapons](#dataloadoutweapons)  
- [DataMagazine](#datamagazine)  
- [DataMagazineWeapons](#datamagazineweapons)  
- [DataMount](#datamount)  
- [DataMountComms](#datamountcomms)  
- [DataMountDirectors](#datamountdirectors)  
- [DataMountMagazineWeapons](#datamountmagazineweapons)  
- [DataMountSensors](#datamountsensors)  
- [DataMountWeapons](#datamountweapons)  
- [DataPropulsion](#datapropulsion)  
- [DataPropulsionPerformance](#datapropulsionperformance)  
- [DataSatellite](#datasatellite)  
- [DataSatelliteCodes](#datasatellitecodes)  
- [DataSatelliteComms](#datasatellitecomms)  
- [DataSatelliteMounts](#datasatellitemounts)  
- [DataSatelliteOrbits](#datasatelliteorbits)  
- [DataSatelliteSensors](#datasatellitesensors)  
- [DataSatelliteSignatures](#datasatellitesignatures)  
- [DataSensor](#datasensor)  
- [DataSensorCapabilities](#datasensorcapabilities)  
- [DataSensorCodes](#datasensorcodes)  
- [DataSensorFrequencyIlluminate](#datasensorfrequencyilluminate)  
- [DataSensorFrequencySearchAndTrack](#datasensorfrequencysearchandtrack)  
- [DataSensorSensorGroups](#datasensorsensorgroups)  
- [DataShip](#dataship)  
- [DataShipAircraftFacilities](#datashipaircraftfacilities)  
- [DataShipCodes](#datashipcodes)  
- [DataShipComms](#datashipcomms)  
- [DataShipDockingFacilities](#datashipdockingfacilities)  
- [DataShipFuel](#datashipfuel)  
- [DataShipMagazines](#datashipmagazines)  
- [DataShipMounts](#datashipmounts)  
- [DataShipPropulsion](#datashippropulsion)  
- [DataShipSensors](#datashipsensors)  
- [DataShipSignatures](#datashipsignatures)  
- [DataSubmarine](#datasubmarine)  
- [DataSubmarineAircraftFacilities](#datasubmarineaircraftfacilities)  
- [DataSubmarineCodes](#datasubmarinecodes)  
- [DataSubmarineComms](#datasubmarinecomms)  
- [DataSubmarineDockingFacilities](#datasubmarinedockingfacilities)  
- [DataSubmarineFuel](#datasubmarinefuel)  
- [DataSubmarineMagazines](#datasubmarinemagazines)  
- [DataSubmarineMounts](#datasubmarinemounts)  
- [DataSubmarinePropulsion](#datasubmarinepropulsion)  
- [DataSubmarineSensors](#datasubmarinesensors)  
- [DataSubmarineSignatures](#datasubmarinesignatures)  
- [DataWarhead](#datawarhead)  
- [DataWeapon](#dataweapon)  
- [DataWeaponCodes](#dataweaponcodes)  
- [DataWeaponComms](#dataweaponcomms)  
- [DataWeaponDirectors](#dataweapondirectors)  
- [DataWeaponFuel](#dataweaponfuel)  
- [DataWeaponPropulsion](#dataweaponpropulsion)  
- [DataWeaponRecord](#dataweaponrecord)  
- [DataWeaponSensors](#dataweaponsensors)  
- [DataWeaponSignatures](#dataweaponsignatures)  
- [DataWeaponTargets](#dataweapontargets)  
- [DataWeaponWRA](#dataweaponwra)  
- [DataWeaponWarheads](#dataweaponwarheads)  
- [DataWeaponWeapons](#dataweaponweapons)  

### 枚举表 (Enum*)

- [EnumAircraftAutonomousControlLevel](#enumaircraftautonomouscontrollevel)  
- [EnumAircraftCategory](#enumaircraftcategory)  
- [EnumAircraftCockpitGen](#enumaircraftcockpitgen)  
- [EnumAircraftCockpitVisibility](#enumaircraftcockpitvisibility)  
- [EnumAircraftCode](#enumaircraftcode)  
- [EnumAircraftFacilityType](#enumaircraftfacilitytype)  
- [EnumAircraftPhysicalSize](#enumaircraftphysicalsize)  
- [EnumAircraftType](#enumaircrafttype)  
- [EnumArcs](#enumarcs)  
- [EnumArmorType](#enumarmortype)  
- [EnumCargoType](#enumcargotype)  
- [EnumCommCapability](#enumcommcapability)  
- [EnumCommLatency](#enumcommlatency)  
- [EnumCommQuality](#enumcommquality)  
- [EnumCommType](#enumcommtype)  
- [EnumContainerType](#enumcontainertype)  
- [EnumDockingFacilityPhysicalSize](#enumdockingfacilityphysicalsize)  
- [EnumDockingFacilityType](#enumdockingfacilitytype)  
- [EnumErgonomics](#enumergonomics)  
- [EnumFacilityCSGen](#enumfacilitycsgen)  
- [EnumFacilityCategory](#enumfacilitycategory)  
- [EnumFacilityType](#enumfacilitytype)  
- [EnumFuelType](#enumfueltype)  
- [EnumGroundUnitCSGen](#enumgroundunitcsgen)  
- [EnumGroundUnitCategory](#enumgroundunitcategory)  
- [EnumGroundUnitCode](#enumgroundunitcode)  
- [EnumLoadoutMissionProfile](#enumloadoutmissionprofile)  
- [EnumLoadoutRole](#enumloadoutrole)  
- [EnumLoadoutTimeOfDay](#enumloadouttimeofday)  
- [EnumLoadoutWeather](#enumloadoutweather)  
- [EnumLoadoutWinchesterShotgun](#enumloadoutwinchestershotgun)  
- [EnumOperatorCountry](#enumoperatorcountry)  
- [EnumOperatorService](#enumoperatorservice)  
- [EnumPropulsionCombinedType](#enumpropulsioncombinedtype)  
- [EnumPropulsionType](#enumpropulsiontype)  
- [EnumRunwayLength](#enumrunwaylength)  
- [EnumSatelliteCSGen](#enumsatellitecsgen)  
- [EnumSatelliteCategory](#enumsatellitecategory)  
- [EnumSatelliteCode](#enumsatellitecode)  
- [EnumSatelliteOrbitPlane](#enumsatelliteorbitplane)  
- [EnumSatelliteType](#enumsatellitetype)  
- [EnumSensorCapability](#enumsensorcapability)  
- [EnumSensorCode](#enumsensorcode)  
- [EnumSensorFrequency](#enumsensorfrequency)  
- [EnumSensorGeneration](#enumsensorgeneration)  
- [EnumSensorRole](#enumsensorrole)  
- [EnumSensorType](#enumsensortype)  
- [EnumShipCSGen](#enumshipcsgen)  
- [EnumShipCategory](#enumshipcategory)  
- [EnumShipCode](#enumshipcode)  
- [EnumShipPhysicalSize](#enumshipphysicalsize)  
- [EnumShipType](#enumshiptype)  
- [EnumSignatureType](#enumsignaturetype)  
- [EnumSubmarineCSGen](#enumsubmarinecsgen)  
- [EnumSubmarineCategory](#enumsubmarinecategory)  
- [EnumSubmarineCode](#enumsubmarinecode)  
- [EnumSubmarinePhysicalSize](#enumsubmarinephysicalsize)  
- [EnumSubmarineType](#enumsubmarinetype)  
- [EnumWarheadCaliber](#enumwarheadcaliber)  
- [EnumWarheadExplosivesType](#enumwarheadexplosivestype)  
- [EnumWarheadType](#enumwarheadtype)  
- [EnumWeaponCode](#enumweaponcode)  
- [EnumWeaponGeneration](#enumweapongeneration)  
- [EnumWeaponImpactType](#enumweaponimpacttype)  
- [EnumWeaponProfileAttack](#enumweaponprofileattack)  
- [EnumWeaponProfileCruise](#enumweaponprofilecruise)  
- [EnumWeaponTarget](#enumweapontarget)  
- [EnumWeaponType](#enumweapontype)  
- [EnumWeaponWRA](#enumweaponwra)  
- [EnumWeaponWRAAutoFireRange](#enumweaponwraautofirerange)  
- [EnumWeaponWRASelfDefenceRange](#enumweaponwraselfdefencerange)  
- [EnumWeaponWRAShooterQty](#enumweaponwrashooterqty)  
- [EnumWeaponWRAWeaponQty](#enumweaponwraweaponqty)  

### 其他

- [Capabilities](#capabilities)  
- [ManagementDatabase](#managementdatabase)  


---

## 详细表结构


### Capabilities

**行数**: 7  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |
| Supported | BOOLEAN | 否 | 'False' | - |

### DataAircraft

**行数**: 7543  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Category | INTEGER | 是 | 1001 | - |
| Type | INTEGER | 是 | 1001 | - |
| Name | TEXT | 是 | - | - |
| Comments | TEXT | 是 | - | - |
| OperatorCountry | INTEGER | 是 | 0 | - |
| OperatorService | INTEGER | 是 | 0 | - |
| YearCommissioned | INTEGER | 是 | 0 | - |
| YearDecommissioned | INTEGER | 是 | 0 | - |
| Length | DOUBLE | 是 | 0 | - |
| Span | DOUBLE | 是 | 0 | - |
| Height | DOUBLE | 是 | 0 | - |
| WeightEmpty | INTEGER | 是 | 0 | - |
| WeightMax | INTEGER | 是 | 0 | - |
| WeightPayload | INTEGER | 是 | 0 | - |
| Crew | INTEGER | 是 | 1 | - |
| Agility | DOUBLE | 是 | 0 | - |
| ClimbRate | DOUBLE | 是 | 0 | - |
| AutonomousControlLevel | INTEGER | 是 | 0 | - |
| CockpitGen | INTEGER | 是 | 0 | - |
| Ergonomics | INTEGER | 是 | 3000 | - |
| OODADetectionCycle | INTEGER | 是 | 0 | - |
| OODATargetingCycle | INTEGER | 是 | 0 | - |
| OODAEvasiveCycle | INTEGER | 是 | 0 | - |
| TotalEndurance | INTEGER | 是 | 0 | - |
| PhysicalSizeCode | INTEGER | 是 | 1001 | - |
| RunwayLengthCode | INTEGER | 是 | 1001 | - |
| Hypothetical | BOOLEAN | 否 | 'False' | - |
| Cost | INTEGER | 是 | 0 | - |
| DamagePoints | DOUBLE | 是 | 0 | - |
| AircraftEngineArmor | INTEGER | 是 | 0 | - |
| AircraftFuselageArmor | INTEGER | 是 | 0 | - |
| AircraftCockpitArmor | INTEGER | 是 | 0 | - |
| Visibility | TEXT | 是 | - | - |
| FuelOffloadRate | INTEGER | 是 | 0 | - |
| FuelOnloadRate | INTEGER | 是 | 0 | - |
| Deprecated | BOOLEAN | 否 | 'No' | - |

### DataAircraftCodes

**行数**: 20267  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| CodeID | INTEGER | 否 | - | ✓ |

### DataAircraftComms

**行数**: 17076  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| ParentSpecific | BOOLEAN | 否 | 'True' | - |
| IsRelay | BOOLEAN | 否 | 'No' | - |

### DataAircraftFacility

**行数**: 149  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Type | INTEGER | 是 | 0 | - |
| PhysicalSize | INTEGER | 是 | 0 | - |
| Capacity | INTEGER | 是 | 0 | - |
| RunwayLength | INTEGER | 是 | 0 | - |

### DataAircraftFuel

**行数**: 7514  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataAircraftLoadouts

**行数**: 97280  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 否 | - | ✓ |

### DataAircraftMounts

**行数**: 7484  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| ComponentNumber | INTEGER | 是 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| SB1 | BOOLEAN | 否 | - | - |
| SB2 | BOOLEAN | 否 | - | - |
| SMF1 | BOOLEAN | 否 | - | - |
| SMF2 | BOOLEAN | 否 | - | - |
| SMA1 | BOOLEAN | 否 | - | - |
| SMA2 | BOOLEAN | 否 | - | - |
| SS1 | BOOLEAN | 否 | - | - |
| SS2 | BOOLEAN | 否 | - | - |
| PB1 | BOOLEAN | 否 | - | - |
| PB2 | BOOLEAN | 否 | - | - |
| PMF1 | BOOLEAN | 否 | - | - |
| PMF2 | BOOLEAN | 否 | - | - |
| PMA1 | BOOLEAN | 否 | - | - |
| PMA2 | BOOLEAN | 否 | - | - |
| PS1 | BOOLEAN | 否 | - | - |
| PS2 | BOOLEAN | 否 | - | - |

### DataAircraftPropulsion

**行数**: 7543  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataAircraftSensors

**行数**: 20370  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| DegOverride | INTEGER | 是 | 0 | - |
| SB1 | BOOLEAN | 否 | - | - |
| SB2 | BOOLEAN | 否 | - | - |
| SMF1 | BOOLEAN | 否 | - | - |
| SMF2 | BOOLEAN | 否 | - | - |
| SMA1 | BOOLEAN | 否 | - | - |
| SMA2 | BOOLEAN | 否 | - | - |
| SS1 | BOOLEAN | 否 | - | - |
| SS2 | BOOLEAN | 否 | - | - |
| PB1 | BOOLEAN | 否 | - | - |
| PB2 | BOOLEAN | 否 | - | - |
| PMF1 | BOOLEAN | 否 | - | - |
| PMF2 | BOOLEAN | 否 | - | - |
| PMA1 | BOOLEAN | 否 | - | - |
| PMA2 | BOOLEAN | 否 | - | - |
| PS1 | BOOLEAN | 否 | - | - |
| PS2 | BOOLEAN | 否 | - | - |
| DegOverrideMax | INTEGER | 是 | 0 | - |
| SB1Max | BOOLEAN | 否 | - | - |
| SB2Max | BOOLEAN | 否 | - | - |
| SMF1Max | BOOLEAN | 否 | - | - |
| SMF2Max | BOOLEAN | 否 | - | - |
| SMA1Max | BOOLEAN | 否 | - | - |
| SMA2Max | BOOLEAN | 否 | - | - |
| SS1Max | BOOLEAN | 否 | - | - |
| SS2Max | BOOLEAN | 否 | - | - |
| PB1Max | BOOLEAN | 否 | - | - |
| PB2Max | BOOLEAN | 否 | - | - |
| PMF1Max | BOOLEAN | 否 | - | - |
| PMF2Max | BOOLEAN | 否 | - | - |
| PMA1Max | BOOLEAN | 否 | - | - |
| PMA2Max | BOOLEAN | 否 | - | - |
| PS1Max | BOOLEAN | 否 | - | - |
| PS2Max | BOOLEAN | 否 | - | - |
| VerticalDegMax | INTEGER | 是 | 0 | - |
| MastHeight | INTEGER | 是 | 0 | - |

### DataAircraftSignatures

**行数**: 45258  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Type | INTEGER | 否 | - | ✓ |
| Front | DOUBLE | 是 | 0 | - |
| Side | DOUBLE | 是 | 0 | - |
| Rear | DOUBLE | 是 | 0 | - |
| Top | DOUBLE | 是 | 0 | - |

### DataComm

**行数**: 503  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Name | TEXT | 是 | - | - |
| Comments | TEXT | 是 | - | - |
| Type | INTEGER | 是 | - | - |
| Range | INTEGER | 是 | 0 | - |
| Channels | INTEGER | 是 | 0 | - |
| IsOptional | BOOLEAN | 否 | 'False' | - |
| WeaponLinkRequiresSensor | BOOLEAN | 否 | 'False' | - |
| Hypothetical | BOOLEAN | 否 | 'False' | - |
| Deprecated | BOOLEAN | 否 | 'No' | - |
| QualityGrade | INTEGER | 是 | 0 | - |
| RefreshRateGrade | INTEGER | 是 | 0 | - |
| RefreshRate | INTEGER | 是 | 0 | - |

### DataCommCapabilities

**行数**: 1737  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| CodeID | INTEGER | 是 | - | ✓ |

### DataCommDirectors

**行数**: 708  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| ComponentNumber | INTEGER | 是 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataCommType

**行数**: 177  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Name | TEXT | 是 | - | - |
| Comments | TEXT | 是 | '"-"' | - |
| IsWireless | BOOLEAN | 否 | 'Yes' | - |

### DataCommTypeCanTalkTo

**行数**: 2  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataContainer

**行数**: 14  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | 0 | ✓ |
| Name | TEXT | 是 | - | - |
| Comments | TEXT | 是 | - | - |
| Type | INTEGER | 是 | 0 | - |
| Length | DOUBLE | 是 | 0 | - |
| Width | DOUBLE | 是 | 0 | - |
| Height | DOUBLE | 是 | 0 | - |
| IsHold | BOOLEAN | 否 | 'No' | - |
| Container_ParadropCapable | BOOLEAN | 否 | 'No' | - |
| Weight | INTEGER | 是 | 0 | - |
| PayloadCapacity | INTEGER | 是 | 0 | - |
| CubicCapacity | INTEGER | 是 | 0 | - |

### DataDockingFacility

**行数**: 58  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Type | INTEGER | 是 | 1001 | - |
| PhysicalSize | INTEGER | 是 | 1001 | - |
| Capacity | INTEGER | 是 | 1 | - |

### DataFacility

**行数**: 4613  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Name | TEXT | 是 | - | - |
| Comments | TEXT | 是 | - | - |
| Category | INTEGER | 是 | 1001 | - |
| Type | INTEGER | 是 | 1001 | - |
| OperatorCountry | INTEGER | 是 | 0 | - |
| OperatorService | INTEGER | 是 | 0 | - |
| YearCommissioned | INTEGER | 是 | 0 | - |
| YearDecommissioned | INTEGER | 是 | 0 | - |
| Area | INTEGER | 是 | 0 | - |
| Length | INTEGER | 是 | 0 | - |
| Width | INTEGER | 是 | 0 | - |
| Crew | INTEGER | 是 | 0 | - |
| ArmorGeneral | INTEGER | 是 | 0 | - |
| DamagePoints | INTEGER | 是 | 0 | - |
| MastHeight | INTEGER | 是 | 0 | - |
| MissileDefense | INTEGER | 是 | 0 | - |
| CSGen | INTEGER | 是 | 0 | - |
| Ergonomics | INTEGER | 是 | 3000 | - |
| OODADetectionCycle | INTEGER | 是 | 0 | - |
| OODATargetingCycle | INTEGER | 是 | 0 | - |
| OODAEvasiveCycle | INTEGER | 是 | 0 | - |
| MountsAreAimpoints | BOOLEAN | 否 | 'False' | - |
| Radius | INTEGER | 是 | 0 | - |
| Hypothetical | BOOLEAN | 否 | 'False' | - |
| Cost | INTEGER | 是 | 0 | - |
| Deprecated | BOOLEAN | 否 | 'No' | - |

### DataFacilityAircraftFacilities

**行数**: 788  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataFacilityComms

**行数**: 188  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| ParentSpecific | BOOLEAN | 否 | 'True' | - |
| IsRelay | BOOLEAN | 否 | 'No' | - |

### DataFacilityDockingFacilities

**行数**: 63  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataFacilityFuel

**行数**: 39  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataFacilityMagazines

**行数**: 1214  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataFacilityMounts

**行数**: 15007  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| SB1 | BOOLEAN | 否 | - | - |
| SB2 | BOOLEAN | 否 | - | - |
| SMF1 | BOOLEAN | 否 | - | - |
| SMF2 | BOOLEAN | 否 | - | - |
| SMA1 | BOOLEAN | 否 | - | - |
| SMA2 | BOOLEAN | 否 | - | - |
| SS1 | BOOLEAN | 否 | - | - |
| SS2 | BOOLEAN | 否 | - | - |
| PB1 | BOOLEAN | 否 | - | - |
| PB2 | BOOLEAN | 否 | - | - |
| PMF1 | BOOLEAN | 否 | - | - |
| PMF2 | BOOLEAN | 否 | - | - |
| PMA1 | BOOLEAN | 否 | - | - |
| PMA2 | BOOLEAN | 否 | - | - |
| PS1 | BOOLEAN | 否 | - | - |
| PS2 | BOOLEAN | 否 | - | - |

### DataFacilitySensors

**行数**: 1254  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| SB1 | BOOLEAN | 否 | - | - |
| SB2 | BOOLEAN | 否 | - | - |
| SMF1 | BOOLEAN | 否 | - | - |
| SMF2 | BOOLEAN | 否 | - | - |
| SMA1 | BOOLEAN | 否 | - | - |
| SMA2 | BOOLEAN | 否 | - | - |
| SS1 | BOOLEAN | 否 | - | - |
| SS2 | BOOLEAN | 否 | - | - |
| PB1 | BOOLEAN | 否 | - | - |
| PB2 | BOOLEAN | 否 | - | - |
| PMF1 | BOOLEAN | 否 | - | - |
| PMF2 | BOOLEAN | 否 | - | - |
| PMA1 | BOOLEAN | 否 | - | - |
| PMA2 | BOOLEAN | 否 | - | - |
| PS1 | BOOLEAN | 否 | - | - |
| PS2 | BOOLEAN | 否 | - | - |
| SB1Max | BOOLEAN | 否 | - | - |
| SB2Max | BOOLEAN | 否 | - | - |
| SMF1Max | BOOLEAN | 否 | - | - |
| SMF2Max | BOOLEAN | 否 | - | - |
| SMA1Max | BOOLEAN | 否 | - | - |
| SMA2Max | BOOLEAN | 否 | - | - |
| SS1Max | BOOLEAN | 否 | - | - |
| SS2Max | BOOLEAN | 否 | - | - |
| PB1Max | BOOLEAN | 否 | - | - |
| PB2Max | BOOLEAN | 否 | - | - |
| PMF1Max | BOOLEAN | 否 | - | - |
| PMF2Max | BOOLEAN | 否 | - | - |
| PMA1Max | BOOLEAN | 否 | - | - |
| PMA2Max | BOOLEAN | 否 | - | - |
| PS1Max | BOOLEAN | 否 | - | - |
| PS2Max | BOOLEAN | 否 | - | - |
| MastHeight | DOUBLE | 是 | 0 | - |

### DataFacilitySignatures

**行数**: 27678  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Type | INTEGER | 否 | - | ✓ |
| Front | DOUBLE | 是 | 0 | - |
| Side | DOUBLE | 是 | 0 | - |
| Rear | DOUBLE | 是 | 0 | - |
| Top | DOUBLE | 是 | 0 | - |

### DataFuel

**行数**: 2173  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Type | INTEGER | 是 | 0 | - |
| Capacity | INTEGER | 是 | 0 | - |

### DataGroundUnit

**行数**: 467  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Name | TEXT | 是 | - | - |
| Comments | TEXT | 是 | - | - |
| Category | INTEGER | 是 | 1001 | - |
| OperatorCountry | INTEGER | 是 | 0 | - |
| OperatorService | INTEGER | 是 | 0 | - |
| YearCommissioned | INTEGER | 是 | 0 | - |
| YearDecommissioned | INTEGER | 是 | 0 | - |
| Area | DOUBLE | 是 | 0 | - |
| Length | DOUBLE | 是 | 0 | - |
| Width | DOUBLE | 是 | 0 | - |
| MastHeight | DOUBLE | 是 | 0 | - |
| Mass | DOUBLE | 是 | 0 | - |
| Crew | INTEGER | 是 | 0 | - |
| TroopCapacity | INTEGER | 是 | 0 | - |
| ArmorGeneral | INTEGER | 是 | 0 | - |
| DamagePoints | INTEGER | 是 | 0 | - |
| MissileDefense | INTEGER | 是 | 0 | - |
| CSGen | INTEGER | 是 | 0 | - |
| Ergonomics | INTEGER | 是 | 3000 | - |
| OODADetectionCycle | INTEGER | 是 | 0 | - |
| OODATargetingCycle | INTEGER | 是 | 0 | - |
| OODAEvasiveCycle | INTEGER | 是 | 0 | - |
| Hypothetical | BOOLEAN | 否 | 'False' | - |
| Cost | INTEGER | 是 | 0 | - |
| Deprecated | BOOLEAN | 否 | 'No' | - |
| MaxSeaState | INTEGER | 是 | 0 | - |
| Self_Cargo_Type | INTEGER | 是 | 0 | - |
| Self_Cargo_Mass | DOUBLE | 是 | 0 | - |
| Self_Cargo_Area | DOUBLE | 是 | 0 | - |
| Self_Cargo_Crew | INTEGER | 是 | 0 | - |
| Self_Cargo_Volume | DOUBLE | 是 | 0 | - |
| Self_Cargo_ParadropCapable | BOOLEAN | 否 | 'No' | - |
| Carry_Cargo_Type | INTEGER | 是 | 0 | - |
| Carry_Cargo_Mass | DOUBLE | 是 | 0 | - |
| Carry_Cargo_Area | DOUBLE | 是 | 0 | - |
| Carry_Cargo_Crew | INTEGER | 是 | 0 | - |
| Carry_Cargo_Volume | DOUBLE | 是 | 0 | - |
| Tow_Mass | DOUBLE | 是 | 0 | - |
| Setup | INTEGER | 是 | 0 | - |

### DataGroundUnitAircraftFacilities

**行数**: 0  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataGroundUnitCodes

**行数**: 900  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| CodeID | INTEGER | 否 | - | ✓ |

### DataGroundUnitComms

**行数**: 963  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| ParentSpecific | BOOLEAN | 否 | 'True' | - |
| IsRelay | BOOLEAN | 否 | 'No' | - |

### DataGroundUnitDockingFacilities

**行数**: 0  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataGroundUnitFuel

**行数**: 437  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataGroundUnitMagazines

**行数**: 402  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataGroundUnitMounts

**行数**: 821  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| SB1 | BOOLEAN | 否 | - | - |
| SB2 | BOOLEAN | 否 | - | - |
| SMF1 | BOOLEAN | 否 | - | - |
| SMF2 | BOOLEAN | 否 | - | - |
| SMA1 | BOOLEAN | 否 | - | - |
| SMA2 | BOOLEAN | 否 | - | - |
| SS1 | BOOLEAN | 否 | - | - |
| SS2 | BOOLEAN | 否 | - | - |
| PB1 | BOOLEAN | 否 | - | - |
| PB2 | BOOLEAN | 否 | - | - |
| PMF1 | BOOLEAN | 否 | - | - |
| PMF2 | BOOLEAN | 否 | - | - |
| PMA1 | BOOLEAN | 否 | - | - |
| PMA2 | BOOLEAN | 否 | - | - |
| PS1 | BOOLEAN | 否 | - | - |
| PS2 | BOOLEAN | 否 | - | - |

### DataGroundUnitPropulsion

**行数**: 448  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataGroundUnitSensors

**行数**: 355  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| SB1 | BOOLEAN | 否 | - | - |
| SB2 | BOOLEAN | 否 | - | - |
| SMF1 | BOOLEAN | 否 | - | - |
| SMF2 | BOOLEAN | 否 | - | - |
| SMA1 | BOOLEAN | 否 | - | - |
| SMA2 | BOOLEAN | 否 | - | - |
| SS1 | BOOLEAN | 否 | - | - |
| SS2 | BOOLEAN | 否 | - | - |
| PB1 | BOOLEAN | 否 | - | - |
| PB2 | BOOLEAN | 否 | - | - |
| PMF1 | BOOLEAN | 否 | - | - |
| PMF2 | BOOLEAN | 否 | - | - |
| PMA1 | BOOLEAN | 否 | - | - |
| PMA2 | BOOLEAN | 否 | - | - |
| PS1 | BOOLEAN | 否 | - | - |
| PS2 | BOOLEAN | 否 | - | - |
| SB1Max | BOOLEAN | 否 | - | - |
| SB2Max | BOOLEAN | 否 | - | - |
| SMF1Max | BOOLEAN | 否 | - | - |
| SMF2Max | BOOLEAN | 否 | - | - |
| SMA1Max | BOOLEAN | 否 | - | - |
| SMA2Max | BOOLEAN | 否 | - | - |
| SS1Max | BOOLEAN | 否 | - | - |
| SS2Max | BOOLEAN | 否 | - | - |
| PB1Max | BOOLEAN | 否 | - | - |
| PB2Max | BOOLEAN | 否 | - | - |
| PMF1Max | BOOLEAN | 否 | - | - |
| PMF2Max | BOOLEAN | 否 | - | - |
| PMA1Max | BOOLEAN | 否 | - | - |
| PMA2Max | BOOLEAN | 否 | - | - |
| PS1Max | BOOLEAN | 否 | - | - |
| PS2Max | BOOLEAN | 否 | - | - |
| MastHeight | DOUBLE | 是 | 0 | - |

### DataGroundUnitSignatures

**行数**: 2796  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Type | INTEGER | 否 | - | ✓ |
| Front | DOUBLE | 是 | 0 | - |
| Side | DOUBLE | 是 | 0 | - |
| Rear | DOUBLE | 是 | 0 | - |
| Top | DOUBLE | 是 | 0 | - |

### DataLoadout

**行数**: 33882  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Name | TEXT | 是 | - | - |
| Comments | TEXT | 是 | - | - |
| ROF | INTEGER | 是 | 0 | - |
| Capacity | INTEGER | 是 | 0 | - |
| ReadyTime | INTEGER | 是 | 0 | - |
| ReadyTime_Sustained | INTEGER | 是 | 0 | - |
| LoadoutRole | INTEGER | 是 | 0 | - |
| TimeofDay | INTEGER | 是 | 0 | - |
| Weather | INTEGER | 是 | 0 | - |
| PayloadWeightDragModifier | DOUBLE | 是 | 0 | - |
| DefaultCombatRadius | INTEGER | 是 | 0 | - |
| DefaultTimeOnStation | INTEGER | 是 | 0 | - |
| DefaultMissionProfile | INTEGER | 是 | 0 | - |
| RequiresBuddyIllumination | BOOLEAN | 否 | 'False' | - |
| Hypothetical | BOOLEAN | 否 | 'False' | - |
| QuickTurnaround | BOOLEAN | 否 | 'False' | - |
| QuickTurnaround_ReadyTime | INTEGER | 是 | 0 | - |
| QuickTurnaround_MaxSorties | INTEGER | 是 | 0 | - |
| QuickTurnaround_AdditionalTimePenalty | INTEGER | 是 | 0 | - |
| QuickTurnaround_AirborneTime | INTEGER | 是 | 0 | - |
| QuickTurnaround_TimeofDay | INTEGER | 是 | 0 | - |
| WinchesterShotgun | INTEGER | 是 | 0 | - |
| Cargo_Type | INTEGER | 否 | 0 | - |
| Cargo_Mass | DOUBLE | 否 | 0 | - |
| Cargo_Area | DOUBLE | 否 | 0 | - |
| Cargo_Crew | DOUBLE | 否 | 0 | - |
| Cargo_ParadropCapable | BOOLEAN | 否 | - | - |
| Cargo_Volume | INTEGER | 是 | 0 | - |
| Deprecated | BOOLEAN | 否 | 'False' | - |

### DataLoadoutWeapons

**行数**: 94143  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| Optional | BOOLEAN | 否 | - | - |
| Internal | BOOLEAN | 否 | - | - |

### DataMagazine

**行数**: 1732  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Name | TEXT | 是 | - | - |
| Comments | TEXT | 是 | - | - |
| ArmorGeneral | INTEGER | 是 | 0 | - |
| ROF | INTEGER | 是 | 0 | - |
| Capacity | INTEGER | 是 | 0 | - |
| AviationMagazine | BOOLEAN | 否 | 'False' | - |
| Hypothetical | BOOLEAN | 否 | 'False' | - |
| Deprecated | BOOLEAN | 否 | 'No' | - |

### DataMagazineWeapons

**行数**: 3784  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataMount

**行数**: 4154  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Name | TEXT | 是 | - | - |
| Comments | TEXT | 是 | - | - |
| ArmorGeneral | INTEGER | 是 | 0 | - |
| ROF | INTEGER | 是 | 0 | - |
| Capacity | INTEGER | 是 | 0 | - |
| MagazineROF | INTEGER | 是 | 0 | - |
| MagazineCapacity | INTEGER | 是 | 0 | - |
| DamagePoints | DOUBLE | 是 | 0 | - |
| Logistic | BOOLEAN | 否 | 'False' | - |
| ReserveTarget | BOOLEAN | 否 | 'False' | - |
| CanHotReload | BOOLEAN | 否 | 'False' | - |
| Availability | INTEGER | 是 | 0 | - |
| Trainable | BOOLEAN | 否 | 'False' | - |
| Autonomous | BOOLEAN | 否 | 'False' | - |
| LocalControl | BOOLEAN | 否 | 'False' | - |
| Hypothetical | BOOLEAN | 否 | 'False' | - |
| Cargo_Type | INTEGER | 否 | 0 | - |
| Cargo_Mass | DOUBLE | 否 | 0 | - |
| Cargo_Area | DOUBLE | 否 | 0 | - |
| Cargo_Crew | DOUBLE | 否 | 0 | - |
| Cargo_ParadropCapable | BOOLEAN | 否 | - | - |
| MobileUnitCategory | INTEGER | 是 | 0 | - |
| Deprecated | BOOLEAN | 否 | 'No' | - |

### DataMountComms

**行数**: 350  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| ParentSpecific | BOOLEAN | 否 | 'True' | - |
| IsRelay | BOOLEAN | 否 | 'No' | - |

### DataMountDirectors

**行数**: 5080  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| ComponentNumber | INTEGER | 是 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataMountMagazineWeapons

**行数**: 681  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataMountSensors

**行数**: 2135  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataMountWeapons

**行数**: 7425  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataPropulsion

**行数**: 4141  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Name | TEXT | 是 | - | - |
| Type | INTEGER | 是 | 0 | - |
| Comments | TEXT | 是 | - | - |
| Hypothetical | BOOLEAN | 否 | 'False' | - |
| NumberOfCompartments | DOUBLE | 是 | 0 | - |
| NumberOfEngines | DOUBLE | 是 | 0 | - |
| NumberOfShafts | DOUBLE | 是 | 0 | - |
| CombinedType | INTEGER | 是 | 0 | - |
| NumberOfEnginesPrim | DOUBLE | 是 | 0 | - |
| NumberOfEnginesScnd | DOUBLE | 是 | 0 | - |
| ThrustPerEngineMilitary | DOUBLE | 是 | 0 | - |
| ThrustPerEngineAfterburner | DOUBLE | 是 | 0 | - |
| SFCMilitary | DOUBLE | 是 | 0 | - |
| SFCAfterburner | DOUBLE | 是 | 0 | - |
| Deprecated | BOOLEAN | 否 | 'No' | - |

### DataPropulsionPerformance

**行数**: 23780  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| AltitudeBand | INTEGER | 是 | - | ✓ |
| Throttle | INTEGER | 是 | - | ✓ |
| Speed | INTEGER | 是 | 0 | - |
| AltitudeMin | DOUBLE | 是 | 0 | - |
| AltitudeMax | DOUBLE | 是 | 0 | - |
| Consumption | DOUBLE | 是 | 0 | - |

### DataSatellite

**行数**: 311  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Category | INTEGER | 是 | 1001 | - |
| Type | INTEGER | 是 | 1001 | - |
| Name | TEXT | 是 | - | - |
| Comments | TEXT | 是 | - | - |
| OperatorCountry | INTEGER | 是 | 0 | - |
| OperatorService | INTEGER | 是 | 0 | - |
| YearCommissioned | INTEGER | 是 | 0 | - |
| YearDecommissioned | INTEGER | 是 | 0 | - |
| Length | DOUBLE | 是 | 0 | - |
| Span | DOUBLE | 是 | 0 | - |
| Height | DOUBLE | 是 | 0 | - |
| WeightEmpty | INTEGER | 是 | 0 | - |
| WeightMax | INTEGER | 是 | 0 | - |
| WeightPayload | INTEGER | 是 | 0 | - |
| Armor | INTEGER | 是 | 0 | - |
| DamagePoints | INTEGER | 是 | 0 | - |
| MRVInclination | DOUBLE | 是 | 0 | - |
| MRVApogeePerigee | DOUBLE | 是 | 0 | - |
| CSGen | INTEGER | 是 | 0 | - |
| OODADetectionCycle | INTEGER | 是 | 0 | - |
| OODATargetingCycle | INTEGER | 是 | 0 | - |
| OODAEvasiveCycle | INTEGER | 是 | 0 | - |
| Hypothetical | BOOLEAN | 否 | 'False' | - |
| Cost | INTEGER | 是 | 0 | - |
| Deprecated | BOOLEAN | 否 | 'No' | - |

### DataSatelliteCodes

**行数**: 0  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| CodeID | INTEGER | 否 | - | ✓ |

### DataSatelliteComms

**行数**: 313  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| ParentSpecific | BOOLEAN | 否 | 'True' | - |
| IsRelay | BOOLEAN | 否 | 'No' | - |

### DataSatelliteMounts

**行数**: 1  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| SB1 | BOOLEAN | 否 | - | - |
| SB2 | BOOLEAN | 否 | - | - |
| SMF1 | BOOLEAN | 否 | - | - |
| SMF2 | BOOLEAN | 否 | - | - |
| SMA1 | BOOLEAN | 否 | - | - |
| SMA2 | BOOLEAN | 否 | - | - |
| SS1 | BOOLEAN | 否 | - | - |
| SS2 | BOOLEAN | 否 | - | - |
| PB1 | BOOLEAN | 否 | - | - |
| PB2 | BOOLEAN | 否 | - | - |
| PMF1 | BOOLEAN | 否 | - | - |
| PMF2 | BOOLEAN | 否 | - | - |
| PMA1 | BOOLEAN | 否 | - | - |
| PMA2 | BOOLEAN | 否 | - | - |
| PS1 | BOOLEAN | 否 | - | - |
| PS2 | BOOLEAN | 否 | - | - |

### DataSatelliteOrbits

**行数**: 1634  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| ComponentNumber | INTEGER | 是 | - | ✓ |
| MissonID | TEXT | 是 | '"-"' | - |
| MissonName | TEXT | 是 | '"-"' | - |
| OrbitNumber | INTEGER | 是 | 1 | - |
| LaunchDate | DATETIME | 是 | '#1/1/1900#' | - |
| CommissioningDate | DATETIME | 是 | '#1/1/1900#' | - |
| DecommissioningDate | DATETIME | 是 | '#1/1/1900#' | - |
| DeOrbitingDate | DATETIME | 是 | '#1/1/1900#' | - |
| SatelliteNumber | DOUBLE | 是 | 0 | - |
| InternationalDesignator1 | TEXT | 是 | '"-"' | - |
| InternationalDesignator2 | TEXT | 是 | '"-"' | - |
| InternationalDesignator3 | TEXT | 是 | '"-"' | - |
| EpochYear | DOUBLE | 是 | 0 | - |
| EpochDay | DOUBLE | 是 | 0 | - |
| FirstTimeDerivativeOfTheMeanMotionDividedByTwo | TEXT | 是 | '"-"' | - |
| SecondTimeDerivativeOfTheMeanMotionDividedBySix | TEXT | 是 | '"-"' | - |
| BSTAR | DOUBLE | 是 | 0 | - |
| ElementNumber | DOUBLE | 是 | 0 | - |
| Inclination | DOUBLE | 是 | 0 | - |
| RightAscensionOfTheAscendingNode | DOUBLE | 是 | 0 | - |
| Eccentricity | DOUBLE | 是 | 0 | - |
| ArgumentOfPerigee | DOUBLE | 是 | 0 | - |
| MeanAnomaly | DOUBLE | 是 | 0 | - |
| MeanMotion | DOUBLE | 是 | 0 | - |
| RevolutionNumberAtEpoch | DOUBLE | 是 | 0 | - |
| Comments | TEXT | 是 | '"-"' | - |
| Perigee | DOUBLE | 是 | 0 | - |
| Apogee | DOUBLE | 是 | 0 | - |
| OrbitalPeriod | DOUBLE | 是 | 0 | - |
| Plane | INTEGER | 是 | 0 | - |
| Operational | BOOLEAN | 否 | 'False' | - |
| TLE | TEXT | 是 | '"-"' | - |

### DataSatelliteSensors

**行数**: 251  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| SB1 | BOOLEAN | 否 | - | - |
| SB2 | BOOLEAN | 否 | - | - |
| SMF1 | BOOLEAN | 否 | - | - |
| SMF2 | BOOLEAN | 否 | - | - |
| SMA1 | BOOLEAN | 否 | - | - |
| SMA2 | BOOLEAN | 否 | - | - |
| SS1 | BOOLEAN | 否 | - | - |
| SS2 | BOOLEAN | 否 | - | - |
| PB1 | BOOLEAN | 否 | - | - |
| PB2 | BOOLEAN | 否 | - | - |
| PMF1 | BOOLEAN | 否 | - | - |
| PMF2 | BOOLEAN | 否 | - | - |
| PMA1 | BOOLEAN | 否 | - | - |
| PMA2 | BOOLEAN | 否 | - | - |
| PS1 | BOOLEAN | 否 | - | - |
| PS2 | BOOLEAN | 否 | - | - |
| SB1Max | BOOLEAN | 否 | - | - |
| SB2Max | BOOLEAN | 否 | - | - |
| SMF1Max | BOOLEAN | 否 | - | - |
| SMF2Max | BOOLEAN | 否 | - | - |
| SMA1Max | BOOLEAN | 否 | - | - |
| SMA2Max | BOOLEAN | 否 | - | - |
| SS1Max | BOOLEAN | 否 | - | - |
| SS2Max | BOOLEAN | 否 | - | - |
| PB1Max | BOOLEAN | 否 | - | - |
| PB2Max | BOOLEAN | 否 | - | - |
| PMF1Max | BOOLEAN | 否 | - | - |
| PMF2Max | BOOLEAN | 否 | - | - |
| PMA1Max | BOOLEAN | 否 | - | - |
| PMA2Max | BOOLEAN | 否 | - | - |
| PS1Max | BOOLEAN | 否 | - | - |
| PS2Max | BOOLEAN | 否 | - | - |

### DataSatelliteSignatures

**行数**: 1866  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Type | INTEGER | 否 | - | ✓ |
| Front | DOUBLE | 是 | 0 | - |
| Side | DOUBLE | 是 | 0 | - |
| Rear | DOUBLE | 是 | 0 | - |
| Top | DOUBLE | 是 | 0 | - |

### DataSensor

**行数**: 7251  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Name | TEXT | 是 | - | - |
| Comments | TEXT | 是 | - | - |
| Type | INTEGER | 是 | 1001 | - |
| Role | INTEGER | 是 | 1001 | - |
| Generation | INTEGER | 是 | 1001 | - |
| MasqueradeAs | INTEGER | 是 | 1001 | - |
| RangeMin | DOUBLE | 是 | 0 | - |
| RangeMax | DOUBLE | 是 | 0 | - |
| AltitudeMin | INTEGER | 是 | 0 | - |
| AltitudeMax | INTEGER | 是 | 0 | - |
| AltitudeMin_ASL | INTEGER | 是 | 0 | - |
| AltitudeMax_ASL | INTEGER | 是 | 0 | - |
| ScanInterval | INTEGER | 是 | 0 | - |
| ResolutionRange | DOUBLE | 是 | 0 | - |
| ResolutionHeight | INTEGER | 是 | 0 | - |
| ResolutionAngle | DOUBLE | 是 | 0 | - |
| DirectionFindingAccuracy | DOUBLE | 是 | 0 | - |
| MaxContactsAir | INTEGER | 是 | 0 | - |
| MaxContactsSurface | INTEGER | 是 | 0 | - |
| MaxContactsSubmarine | INTEGER | 是 | 0 | - |
| MaxContactsIlluminate | INTEGER | 是 | 0 | - |
| Availability | INTEGER | 是 | 0 | - |
| FrequencyUpper | DOUBLE | 是 | 0 | - |
| FrequencyLower | DOUBLE | 是 | 0 | - |
| FrequencyLowerIlluminate | DOUBLE | 是 | 0 | - |
| FrequencyUpperIlluminate | DOUBLE | 是 | 0 | - |
| RadarHorizontalBeamwidth | DOUBLE | 是 | 0 | - |
| RadarVerticalBeamwidth | DOUBLE | 是 | 0 | - |
| RadarSystemNoiseLevel | DOUBLE | 是 | 0 | - |
| RadarProcessingGainLoss | DOUBLE | 是 | 0 | - |
| RadarPeakPower | DOUBLE | 是 | 0 | - |
| RadarPulseWidth | DOUBLE | 是 | 0 | - |
| RadarBlindTime | DOUBLE | 是 | 0 | - |
| RadarPRF | INTEGER | 是 | 0 | - |
| RadarHorizontalBeamwidthIlluminate | DOUBLE | 是 | 0 | - |
| RadarVerticalBeamwidthIlluminate | DOUBLE | 是 | 0 | - |
| RadarSystemNoiseLevelIlluminate | DOUBLE | 是 | 0 | - |
| RadarProcessingGainLossIlluminate | DOUBLE | 是 | 0 | - |
| RadarPeakPowerIlluminate | DOUBLE | 是 | 0 | - |
| RadarPulseWidthIlluminate | DOUBLE | 是 | 0 | - |
| RadarBlindTimeIlluminate | DOUBLE | 是 | 0 | - |
| RadarPRFIlluminate | INTEGER | 是 | 0 | - |
| ESMSensitivity | DOUBLE | 是 | 0 | - |
| ESMSystemLoss | DOUBLE | 是 | 0 | - |
| ESMNumberOfChannels | DOUBLE | 是 | 0 | - |
| ESMPreciseEmitterID | BOOLEAN | 否 | 'False' | - |
| ECMGain | DOUBLE | 是 | 0 | - |
| ECMPeakPower | DOUBLE | 是 | 0 | - |
| ECMBandwidth | DOUBLE | 是 | 0 | - |
| ECMNumberOfTargets | INTEGER | 是 | 0 | - |
| ECMPoKReduction | DOUBLE | 是 | 0 | - |
| SonarSourceLevel | DOUBLE | 是 | 0 | - |
| SonarPulseLength | DOUBLE | 是 | 0 | - |
| SonarDirectivityIndex | DOUBLE | 是 | 0 | - |
| SonarRecognitionDifferentialActive | DOUBLE | 是 | 0 | - |
| SonarRecognitionDifferentialPassive | DOUBLE | 是 | 0 | - |
| SonarSensorToMachineryDistance | DOUBLE | 是 | 0 | - |
| SonarTowLength | DOUBLE | 是 | 0 | - |
| SonarMinimumDeploymentDepth | DOUBLE | 是 | 0 | - |
| SonarMaximumDeploymentDepth | DOUBLE | 是 | 0 | - |
| SonarCZNumber | INTEGER | 是 | 0 | - |
| VisualDetectionZoomLevel | DOUBLE | 是 | 0 | - |
| VisualClassificationZoomLevel | DOUBLE | 是 | 0 | - |
| IRDetectionZoomLevel | DOUBLE | 是 | 0 | - |
| IRClassificationZoomLevel | DOUBLE | 是 | 0 | - |
| MineSweepWidth | INTEGER | 是 | 0 | - |
| MineSweepMinimumDepth | INTEGER | 是 | 0 | - |
| MineSweepMaximumDepth | INTEGER | 是 | 0 | - |
| MineSweepMaximumSpeed | INTEGER | 是 | 0 | - |
| Hypothetical | BOOLEAN | 否 | 'False' | - |
| MinimumSignature_Radar | DOUBLE | 是 | 0 | - |
| MinimumSignature_Visual | DOUBLE | 是 | 0 | - |
| MinimumSignature_IR | DOUBLE | 是 | 0 | - |
| MinimumSignature_ESM | DOUBLE | 是 | 0 | - |
| MinimumSignature_ActiveSonar | DOUBLE | 是 | 0 | - |
| MinimumSignature_PassiveSonar | DOUBLE | 是 | 0 | - |
| Deprecated | BOOLEAN | 否 | 'No' | - |

### DataSensorCapabilities

**行数**: 24344  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| CodeID | INTEGER | 否 | - | ✓ |

### DataSensorCodes

**行数**: 9984  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| CodeID | INTEGER | 是 | - | ✓ |

### DataSensorFrequencyIlluminate

**行数**: 449  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Frequency | INTEGER | 否 | - | ✓ |

### DataSensorFrequencySearchAndTrack

**行数**: 14433  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Frequency | INTEGER | 否 | - | ✓ |

### DataSensorSensorGroups

**行数**: 1066  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| ComponentNumber | INTEGER | 是 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataShip

**行数**: 5046  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Category | INTEGER | 是 | 1001 | - |
| Type | INTEGER | 是 | 1001 | - |
| Name | TEXT | 是 | - | - |
| Comments | TEXT | 是 | - | - |
| OperatorCountry | INTEGER | 是 | 0 | - |
| OperatorService | INTEGER | 是 | 0 | - |
| YearCommissioned | INTEGER | 是 | 0 | - |
| YearDecommissioned | INTEGER | 是 | 0 | - |
| Length | DOUBLE | 是 | 0 | - |
| Beam | DOUBLE | 是 | 0 | - |
| Draft | DOUBLE | 是 | 0 | - |
| Height | DOUBLE | 是 | 0 | - |
| DisplacementEmpty | INTEGER | 是 | 0 | - |
| DisplacementStandard | INTEGER | 是 | 0 | - |
| DisplacementFull | INTEGER | 是 | 0 | - |
| Crew | INTEGER | 是 | 1 | - |
| ArmorBelt | INTEGER | 是 | 0 | - |
| ArmorBulkheads | INTEGER | 是 | 0 | - |
| ArmorDeck | INTEGER | 是 | 0 | - |
| ArmorBridge | INTEGER | 是 | 0 | - |
| ArmorCIC | INTEGER | 是 | 0 | - |
| ArmorEngineering | INTEGER | 是 | 0 | - |
| ArmorRudder | INTEGER | 是 | 0 | - |
| DamagePoints | INTEGER | 是 | 0 | - |
| FOCSeaState | INTEGER | 是 | 0 | - |
| MaxSeaState | INTEGER | 是 | 0 | - |
| RepairCapacity | INTEGER | 是 | 0 | - |
| TroopCapacity | INTEGER | 是 | 0 | - |
| CargoCapacity | INTEGER | 是 | 0 | - |
| MissileDefense | INTEGER | 是 | 0 | - |
| CSGen | INTEGER | 是 | 0 | - |
| Ergonomics | INTEGER | 是 | 3000 | - |
| OODADetectionCycle | INTEGER | 是 | 0 | - |
| OODATargetingCycle | INTEGER | 是 | 0 | - |
| OODAEvasiveCycle | INTEGER | 是 | 0 | - |
| PhysicalSizeCode | INTEGER | 是 | 1001 | - |
| Hypothetical | BOOLEAN | 否 | 'False' | - |
| Cargo_Type | INTEGER | 否 | 0 | - |
| Cargo_Mass | DOUBLE | 否 | 0 | - |
| Cargo_Area | DOUBLE | 否 | 0 | - |
| Cargo_Crew | DOUBLE | 否 | 0 | - |
| Cargo_Volume | INTEGER | 是 | 0 | - |
| Cost | INTEGER | 是 | 0 | - |
| Deprecated | BOOLEAN | 否 | 'No' | - |

### DataShipAircraftFacilities

**行数**: 7972  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataShipCodes

**行数**: 11508  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| CodeID | INTEGER | 否 | - | ✓ |

### DataShipComms

**行数**: 26259  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| ParentSpecific | BOOLEAN | 否 | 'True' | - |
| IsRelay | BOOLEAN | 否 | 'No' | - |

### DataShipDockingFacilities

**行数**: 2017  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataShipFuel

**行数**: 6787  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataShipMagazines

**行数**: 13420  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| ComponentNumber | INTEGER | 是 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataShipMounts

**行数**: 41841  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| ComponentNumber | INTEGER | 是 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| SB1 | BOOLEAN | 否 | - | - |
| SB2 | BOOLEAN | 否 | - | - |
| SMF1 | BOOLEAN | 否 | - | - |
| SMF2 | BOOLEAN | 否 | - | - |
| SMA1 | BOOLEAN | 否 | - | - |
| SMA2 | BOOLEAN | 否 | - | - |
| SS1 | BOOLEAN | 否 | - | - |
| SS2 | BOOLEAN | 否 | - | - |
| PB1 | BOOLEAN | 否 | - | - |
| PB2 | BOOLEAN | 否 | - | - |
| PMF1 | BOOLEAN | 否 | - | - |
| PMF2 | BOOLEAN | 否 | - | - |
| PMA1 | BOOLEAN | 否 | - | - |
| PMA2 | BOOLEAN | 否 | - | - |
| PS1 | BOOLEAN | 否 | - | - |
| PS2 | BOOLEAN | 否 | - | - |
| Offset | INTEGER | 是 | 0 | - |

### DataShipPropulsion

**行数**: 5046  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataShipSensors

**行数**: 33208  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| DegOverride | INTEGER | 是 | 0 | - |
| SB1 | BOOLEAN | 否 | - | - |
| SB2 | BOOLEAN | 否 | - | - |
| SMF1 | BOOLEAN | 否 | - | - |
| SMF2 | BOOLEAN | 否 | - | - |
| SMA1 | BOOLEAN | 否 | - | - |
| SMA2 | BOOLEAN | 否 | - | - |
| SS1 | BOOLEAN | 否 | - | - |
| SS2 | BOOLEAN | 否 | - | - |
| PB1 | BOOLEAN | 否 | - | - |
| PB2 | BOOLEAN | 否 | - | - |
| PMF1 | BOOLEAN | 否 | - | - |
| PMF2 | BOOLEAN | 否 | - | - |
| PMA1 | BOOLEAN | 否 | - | - |
| PMA2 | BOOLEAN | 否 | - | - |
| PS1 | BOOLEAN | 否 | - | - |
| PS2 | BOOLEAN | 否 | - | - |
| DegOverrideMax | INTEGER | 是 | 0 | - |
| SB1Max | BOOLEAN | 否 | - | - |
| SB2Max | BOOLEAN | 否 | - | - |
| SMF1Max | BOOLEAN | 否 | - | - |
| SMF2Max | BOOLEAN | 否 | - | - |
| SMA1Max | BOOLEAN | 否 | - | - |
| SMA2Max | BOOLEAN | 否 | - | - |
| SS1Max | BOOLEAN | 否 | - | - |
| SS2Max | BOOLEAN | 否 | - | - |
| PB1Max | BOOLEAN | 否 | - | - |
| PB2Max | BOOLEAN | 否 | - | - |
| PMF1Max | BOOLEAN | 否 | - | - |
| PMF2Max | BOOLEAN | 否 | - | - |
| PMA1Max | BOOLEAN | 否 | - | - |
| PMA2Max | BOOLEAN | 否 | - | - |
| PS1Max | BOOLEAN | 否 | - | - |
| PS2Max | BOOLEAN | 否 | - | - |
| VerticalDegMax | INTEGER | 是 | 0 | - |
| MastHeight | DOUBLE | 是 | 0 | - |

### DataShipSignatures

**行数**: 55506  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Type | INTEGER | 否 | - | ✓ |
| Front | DOUBLE | 是 | 0 | - |
| Side | DOUBLE | 是 | 0 | - |
| Rear | DOUBLE | 是 | 0 | - |
| Top | DOUBLE | 是 | 0 | - |

### DataSubmarine

**行数**: 746  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Category | INTEGER | 是 | 1001 | - |
| Type | INTEGER | 是 | 1001 | - |
| Name | TEXT | 是 | - | - |
| OperatorCountry | INTEGER | 是 | 0 | - |
| OperatorService | INTEGER | 是 | 0 | - |
| YearCommissioned | INTEGER | 是 | 0 | - |
| YearDecommissioned | INTEGER | 是 | 0 | - |
| Comments | TEXT | 是 | - | - |
| MaxDepth | INTEGER | 是 | 0 | - |
| DamagePoints | INTEGER | 是 | 0 | - |
| Length | DOUBLE | 是 | 0 | - |
| Beam | DOUBLE | 是 | 0 | - |
| Draft | DOUBLE | 是 | 0 | - |
| Height | DOUBLE | 是 | 0 | - |
| DisplacementEmpty | INTEGER | 是 | 0 | - |
| DisplacementStandard | INTEGER | 是 | 0 | - |
| DisplacementFull | INTEGER | 是 | 0 | - |
| Crew | INTEGER | 是 | 0 | - |
| CSGen | INTEGER | 是 | 0 | - |
| Ergonomics | INTEGER | 是 | 3000 | - |
| OODADetectionCycle | INTEGER | 是 | 0 | - |
| OODATargetingCycle | INTEGER | 是 | 0 | - |
| OODAEvasiveCycle | INTEGER | 是 | 0 | - |
| ROVRadius | DOUBLE | 是 | 0 | - |
| PhysicalSizeCode | INTEGER | 是 | 1001 | - |
| Hypothetical | BOOLEAN | 否 | 'False' | - |
| Cost | INTEGER | 是 | 0 | - |
| Cargo_Volume | INTEGER | 是 | 0 | - |
| Deprecated | BOOLEAN | 否 | 'No' | - |

### DataSubmarineAircraftFacilities

**行数**: 0  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| ComponentNumber | INTEGER | 是 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataSubmarineCodes

**行数**: 1081  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| CodeID | INTEGER | 否 | - | ✓ |

### DataSubmarineComms

**行数**: 3488  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| ParentSpecific | BOOLEAN | 否 | 'True' | - |
| IsRelay | BOOLEAN | 否 | 'No' | - |

### DataSubmarineDockingFacilities

**行数**: 47  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataSubmarineFuel

**行数**: 745  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataSubmarineMagazines

**行数**: 1118  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataSubmarineMounts

**行数**: 5285  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| ComponentNumber | INTEGER | 是 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| SB1 | BOOLEAN | 否 | - | - |
| SB2 | BOOLEAN | 否 | - | - |
| SMF1 | BOOLEAN | 否 | - | - |
| SMF2 | BOOLEAN | 否 | - | - |
| SMA1 | BOOLEAN | 否 | - | - |
| SMA2 | BOOLEAN | 否 | - | - |
| SS1 | BOOLEAN | 否 | - | - |
| SS2 | BOOLEAN | 否 | - | - |
| PB1 | BOOLEAN | 否 | - | - |
| PB2 | BOOLEAN | 否 | - | - |
| PMF1 | BOOLEAN | 否 | - | - |
| PMF2 | BOOLEAN | 否 | - | - |
| PMA1 | BOOLEAN | 否 | - | - |
| PMA2 | BOOLEAN | 否 | - | - |
| PS1 | BOOLEAN | 否 | - | - |
| PS2 | BOOLEAN | 否 | - | - |

### DataSubmarinePropulsion

**行数**: 1104  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataSubmarineSensors

**行数**: 5502  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| ComponentNumber | INTEGER | 是 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| SB1 | BOOLEAN | 否 | - | - |
| SB2 | BOOLEAN | 否 | - | - |
| SMF1 | BOOLEAN | 否 | - | - |
| SMF2 | BOOLEAN | 否 | - | - |
| SMA1 | BOOLEAN | 否 | - | - |
| SMA2 | BOOLEAN | 否 | - | - |
| SS1 | BOOLEAN | 否 | - | - |
| SS2 | BOOLEAN | 否 | - | - |
| PB1 | BOOLEAN | 否 | - | - |
| PB2 | BOOLEAN | 否 | - | - |
| PMF1 | BOOLEAN | 否 | - | - |
| PMF2 | BOOLEAN | 否 | - | - |
| PMA1 | BOOLEAN | 否 | - | - |
| PMA2 | BOOLEAN | 否 | - | - |
| PS1 | BOOLEAN | 否 | - | - |
| PS2 | BOOLEAN | 否 | - | - |
| SB1Max | BOOLEAN | 否 | - | - |
| SB2Max | BOOLEAN | 否 | - | - |
| SMF1Max | BOOLEAN | 否 | - | - |
| SMF2Max | BOOLEAN | 否 | - | - |
| SMA1Max | BOOLEAN | 否 | - | - |
| SMA2Max | BOOLEAN | 否 | - | - |
| SS1Max | BOOLEAN | 否 | - | - |
| SS2Max | BOOLEAN | 否 | - | - |
| PB1Max | BOOLEAN | 否 | - | - |
| PB2Max | BOOLEAN | 否 | - | - |
| PMF1Max | BOOLEAN | 否 | - | - |
| PMF2Max | BOOLEAN | 否 | - | - |
| PMA1Max | BOOLEAN | 否 | - | - |
| PMA2Max | BOOLEAN | 否 | - | - |
| PS1Max | BOOLEAN | 否 | - | - |
| PS2Max | BOOLEAN | 否 | - | - |

### DataSubmarineSignatures

**行数**: 8206  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Type | INTEGER | 否 | - | ✓ |
| Front | DOUBLE | 是 | 0 | - |
| Side | DOUBLE | 是 | 0 | - |
| Rear | DOUBLE | 是 | 0 | - |
| Top | DOUBLE | 是 | 0 | - |

### DataWarhead

**行数**: 1365  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Name | TEXT | 是 | - | - |
| Comments | TEXT | 是 | - | - |
| Type | INTEGER | 是 | 1001 | - |
| DamagePoints | DOUBLE | 是 | 0 | - |
| ProjectileCaliber | INTEGER | 是 | 1001 | - |
| ExplosivesType | INTEGER | 是 | 1001 | - |
| ExplosivesWeight | DOUBLE | 是 | 1001 | - |
| NumberOfWarheads | INTEGER | 是 | 1001 | - |
| ClusterBombDispersionAreaLength | INTEGER | 是 | 1001 | - |
| ClusterBombDispersionAreaWidth | INTEGER | 是 | 1001 | - |
| Hypothetical | BOOLEAN | 否 | 'False' | - |
| Deprecated | BOOLEAN | 否 | 'No' | - |

### DataWeapon

**行数**: 4449  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Name | TEXT | 是 | - | - |
| Comments | TEXT | 是 | - | - |
| Type | INTEGER | 是 | 1001 | - |
| Generation | INTEGER | 是 | 1001 | - |
| Length | DOUBLE | 是 | 0 | - |
| Span | DOUBLE | 是 | 0 | - |
| Diameter | DOUBLE | 是 | 0 | - |
| Weight | DOUBLE | 是 | 0 | - |
| BurnoutTime | DOUBLE | 是 | 0 | - |
| BurnoutWeight | DOUBLE | 是 | 0 | - |
| CruiseAltitude | DOUBLE | 是 | 0 | - |
| CruiseAltitude_ASL | DOUBLE | 是 | 0 | - |
| WaypointNumber | INTEGER | 是 | 0 | - |
| IlluminationTime | INTEGER | 是 | 0 | - |
| CEP | INTEGER | 是 | 0 | - |
| CEPSurface | INTEGER | 是 | 0 | - |
| AirPoK | DOUBLE | 是 | 0 | - |
| SurfacePoK | DOUBLE | 是 | 0 | - |
| LandPoK | DOUBLE | 是 | 0 | - |
| SubsurfacePoK | DOUBLE | 是 | 0 | - |
| ClimbRate | DOUBLE | 是 | 0 | - |
| AirRangeMax | DOUBLE | 是 | 0 | - |
| AirRangeMin | DOUBLE | 是 | 0 | - |
| SurfaceRangeMax | DOUBLE | 是 | 0 | - |
| SurfaceRangeMin | DOUBLE | 是 | 0 | - |
| LandRangeMax | DOUBLE | 是 | 0 | - |
| LandRangeMin | DOUBLE | 是 | 0 | - |
| SubsurfaceRangeMax | DOUBLE | 是 | 0 | - |
| SubsurfaceRangeMin | DOUBLE | 是 | 0 | - |
| LaunchSpeedMax | INTEGER | 是 | 0 | - |
| LaunchSpeedMin | INTEGER | 是 | 0 | - |
| LaunchAltitudeMax | DOUBLE | 是 | 0 | - |
| LaunchAltitudeMin | DOUBLE | 是 | 0 | - |
| LaunchAltitudeMax_ASL | DOUBLE | 是 | 0 | - |
| LaunchAltitudeMin_ASL | DOUBLE | 是 | 0 | - |
| TargetSpeedMax | INTEGER | 是 | 0 | - |
| TargetSpeedMin | INTEGER | 是 | 0 | - |
| TargetAltitudeMax | DOUBLE | 是 | 0 | - |
| TargetAltitudeMin | DOUBLE | 是 | 0 | - |
| TargetAltitudeMax_ASL | DOUBLE | 是 | 0 | - |
| TargetAltitudeMin_ASL | DOUBLE | 是 | 0 | - |
| SnapUpDownAltitude | DOUBLE | 是 | 0 | - |
| CanActAsSensor | BOOLEAN | 否 | 'False' | - |
| MaxFlightTime | INTEGER | 是 | 0 | - |
| DetonationDelay | INTEGER | 是 | 0 | - |
| TorpedoSpeedCruise | INTEGER | 是 | 0 | - |
| TorpedoRangeCruise | DOUBLE | 是 | 0 | - |
| TorpedoSpeedFull | INTEGER | 是 | 0 | - |
| TorpedoRangeFull | DOUBLE | 是 | 0 | - |
| Hypothetical | BOOLEAN | 否 | 'False' | - |
| BuddyIlluminationForCEC | BOOLEAN | 否 | 'False' | - |
| Cargo_Type | INTEGER | 是 | 0 | - |
| Cargo_Mass | DOUBLE | 是 | 0 | - |
| Cargo_Volume | DOUBLE | 是 | 0 | - |
| Cargo_Crew | DOUBLE | 是 | 0 | - |
| Cargo_ParadropCapable | BOOLEAN | 否 | 'No' | - |
| Cost | INTEGER | 是 | 0 | - |
| Deprecated | BOOLEAN | 否 | 'False' | - |

### DataWeaponCodes

**行数**: 9358  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| CodeID | INTEGER | 否 | - | ✓ |

### DataWeaponComms

**行数**: 768  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| ParentSpecific | BOOLEAN | 否 | 'True' | - |
| IsRelay | BOOLEAN | 否 | 'No' | - |

### DataWeaponDirectors

**行数**: 1167  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| ComponentNumber | INTEGER | 是 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataWeaponFuel

**行数**: 2724  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataWeaponPropulsion

**行数**: 2513  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataWeaponRecord

**行数**: 11406  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| DefaultLoad | INTEGER | 是 | 0 | - |
| MaxLoad | INTEGER | 是 | 0 | - |
| ROF | INTEGER | 是 | 0 | - |
| Multiple | INTEGER | 是 | 0 | - |
| Deprecated | BOOLEAN | 否 | 'No' | - |

### DataWeaponSensors

**行数**: 2332  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| ComponentNumber | INTEGER | 是 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |
| SB1 | BOOLEAN | 否 | - | - |
| SB2 | BOOLEAN | 否 | - | - |
| SMF1 | BOOLEAN | 否 | - | - |
| SMF2 | BOOLEAN | 否 | - | - |
| SMA1 | BOOLEAN | 否 | - | - |
| SMA2 | BOOLEAN | 否 | - | - |
| SS1 | BOOLEAN | 否 | - | - |
| SS2 | BOOLEAN | 否 | - | - |
| PB1 | BOOLEAN | 否 | - | - |
| PB2 | BOOLEAN | 否 | - | - |
| PMF1 | BOOLEAN | 否 | - | - |
| PMF2 | BOOLEAN | 否 | - | - |
| PMA1 | BOOLEAN | 否 | - | - |
| PMA2 | BOOLEAN | 否 | - | - |
| PS1 | BOOLEAN | 否 | - | - |
| PS2 | BOOLEAN | 否 | - | - |
| SB1Max | BOOLEAN | 否 | - | - |
| SB2Max | BOOLEAN | 否 | - | - |
| SMF1Max | BOOLEAN | 否 | - | - |
| SMF2Max | BOOLEAN | 否 | - | - |
| SMA1Max | BOOLEAN | 否 | - | - |
| SMA2Max | BOOLEAN | 否 | - | - |
| SS1Max | BOOLEAN | 否 | - | - |
| SS2Max | BOOLEAN | 否 | - | - |
| PB1Max | BOOLEAN | 否 | - | - |
| PB2Max | BOOLEAN | 否 | - | - |
| PMF1Max | BOOLEAN | 否 | - | - |
| PMF2Max | BOOLEAN | 否 | - | - |
| PMA1Max | BOOLEAN | 否 | - | - |
| PMA2Max | BOOLEAN | 否 | - | - |
| PS1Max | BOOLEAN | 否 | - | - |
| PS2Max | BOOLEAN | 否 | - | - |

### DataWeaponSignatures

**行数**: 48939  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Type | INTEGER | 否 | - | ✓ |
| Front | DOUBLE | 是 | 0 | - |
| Side | DOUBLE | 是 | 0 | - |
| Rear | DOUBLE | 是 | 0 | - |

### DataWeaponTargets

**行数**: 14013  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| CodeID | INTEGER | 否 | - | ✓ |

### DataWeaponWRA

**行数**: 25198  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| CodeID | INTEGER | 否 | - | ✓ |
| WeaponQty | INTEGER | 是 | 2 | - |
| ShooterQty | INTEGER | 是 | 1 | - |
| AutoFireRange | INTEGER | 是 | 5 | - |
| SelfDefenceRange | INTEGER | 是 | 5 | - |

### DataWeaponWarheads

**行数**: 3958  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| ComponentNumber | INTEGER | 否 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### DataWeaponWeapons

**行数**: 0  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| ComponentNumber | INTEGER | 是 | - | ✓ |
| ComponentID | INTEGER | 是 | 0 | - |

### EnumAircraftAutonomousControlLevel

**行数**: 8  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |
| OnSignalLoss | TEXT | 是 | - | - |

**枚举值** (8 个):

| ID | 描述 |
|-----|------|
| 0 | Undefined |
| 1000 | Remotely Piloted |
| 1500 | Self-Recovering |
| 2000 | Changeable Mission |
| 3000 | Fault/Event Adaptive |
| 4000 | Multi-Vehicle Coordination |
| 5000 | Battlespace Cognizant |
| 6000 | Fully Autonomous |

### EnumAircraftCategory

**行数**: 8  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (8 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Fixed Wing |
| 2002 | Fixed Wing, Carrier Capable |
| 2003 | Helicopter |
| 2004 | Tiltrotor |
| 2006 | Airship |
| 2007 | Seaplane |
| 2008 | Amphibian |

### EnumAircraftCockpitGen

**行数**: 7  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |
| Example | TEXT | 是 | - | - |
| OODADetectionCycle | INTEGER | 是 | 0 | - |
| OODATargetingCycle | INTEGER | 是 | 0 | - |
| OODAEvasiveCycle | INTEGER | 是 | 0 | - |

**枚举值** (7 个):

| ID | 描述 |
|-----|------|
| 0 | Undefined (Use Below) |
| 1000 | Basic Instruments Only |
| 1100 | Steam Gauges |
| 1150 | Steam Gauges (Complex) |
| 1200 | Glass Cockpit (Partial) |
| 1250 | Glass Cockpit |
| 1300 | Panoramic Cockpit Display |

### EnumAircraftCockpitVisibility

**行数**: 10  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | TEXT | 否 | '"A,A,A"' | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (10 个):

| ID | 描述 |
|-----|------|
| A,A,A | Observation Bubbles, 360-deg - Excellent visibility |
| A,A,B | Bubble Canopy, 4th Gen Fighters (F-14, F-15, F-16) - Excellent visibility |
| A,A,C | Forward Razorback Canopy (A-4, Su-25, Jaguar, helicopters) - Good front downward visibility |
| A,B,C | Glass Front, Fair Side Vision (helicopters) |
| A,C,C | Glass Front, Limited Side Vision (helicopters) |
| B,A,C | Aft Razorback Canopy - Limited front downward visibility (F-4, MiG-21, MiG-23, WW2 fighters) |
| B,B,B | Bombers /w Manned Gun Turrets |
| B,B,C | Bombers, Attack A/C - Sunk cockpit |
| B,C,C | Airliner - Very Limited Visibility |
| C,C,C | Unmanned |

### EnumAircraftCode

**行数**: 45  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (45 个):

| ID | 描述 |
|-----|------|
| 4001 | Supermanouverability (5th Gen Fighters) |
| 5002 | HIFR Capable |
| 5999 | Nap-of-the-Earth (NOE) |
| 6000 | Auto-GCAS (Ground Collision Avoidance System) |
| 6001 | Terrain Avoidance (Land: 300ft [91.4m], Sea: 100ft [30.5m]) |
| 6002 | Terrain Following (Land: 200ft [60.9m], Sea: 100ft [30.5m]) |
| 6003 | Fly-by-Wire |
| 6004 | Blip Enhance / Luneberg Reflectors |
| 6011 | Night Navigation (Ferry, Air-to-Air, Air-to-Surface Missiles) |
| 6012 | Night Navigation/Attack (Incl. Bomb, Rocket Delivery) |
| 7001 | Bombsight - Basic |
| 7002 | Bombsight - Ballistic Computing |
| 7003 | Bombsight - Advanced Computing |
| 7004 | Bombsight - Advanced Navigation (INS/GPS) |
| 7010 | Helmet Mounted Sight / Display (HMS/HMD) |
| 8001 | Probe Refueling |
| 8002 | Boom Refueling |
| 9001 | Centerline Drogue |
| 9002 | Wing Drogue |
| 9003 | Centerline Boom |
| 9101 | Fuselage Structure - Low Subsonic Fighter |
| 9102 | Fuselage Structure - High Subsonic Fighter |
| 9103 | Fuselage Structure - Low Supersonic Fighter |
| 9104 | Fuselage Structure - High Supersonic Fighter |
| 9111 | Fuselage Structure - Low Subsonic Attack Aircraft |
| 9112 | Fuselage Structure - High Subsonic Attack Aircraft |
| 9113 | Fuselage Structure - Low Supersonic Attack Aircraft |
| 9114 | Fuselage Structure - High Supersonic Attack Aircraft |
| 9121 | Fuselage Structure - Low Subsonic Bomber |
| 9122 | Fuselage Structure - High Subsonic Bomber |
| 9123 | Fuselage Structure - Low Supersonic Bomber |
| 9124 | Fuselage Structure - High Supersonic Bomber |
| 9185 | Fuselage Structure - High-Altitude Slow-Speed Recon |
| 9186 | Fuselage Structure - High-Altitude High-Speed Recon |
| 9191 | Fuselage Structure - Low Subsonic, Civilian Standards |
| 9192 | Fuselage Structure - High Subsonic, Civilian Standards |
| 9199 | Fuselage Structure - Airship |
| 10001 | RCSS - Active Cancellation |
| 10101 | RCSS - S-Shaped Intake(s) |
| 10102 | RCSS - Exposed Fan Blocker(s) |
| 10201 | RCSS - Stealth Pylons |
| 11101 | IRSS - Shielded Exhaust (Jet Deviation) |
| 11102 | IRSS - Masked Exhaust |
| 11103 | IRSS - Heavily Masked / Slit-Shaped Exhaust |
| 11201 | IRSS - Peak Temp Reduction (Cool-Air Mix) |

### EnumAircraftFacilityType

**行数**: 16  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (16 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Runway |
| 2002 | Runway w/ Arrest |
| 2003 | Runway-Grade Taxiway |
| 2004 | Runway Access Point |
| 2005 | Carrier Catapult |
| 2006 | Carrier Ski Jump |
| 2007 | Carrier Arresting Gear |
| 3001 | Pad |
| 3002 | Pad with Haul-Down |
| 4001 | Hangar |
| 4002 | Open Parking |
| 4003 | Elevator |
| 5001 | UAV Catapult |
| 6001 | Flat-Top Deck (Helo/STOL Only) |
| 6002 | Flat-Top Deck (VTOL Capable) |

### EnumAircraftPhysicalSize

**行数**: 9  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (9 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Small Aircraft (0-12m) |
| 2002 | Medium Aircraft (12.1-18m) |
| 2003 | Large Aircraft (18.1-26m) |
| 2004 | Very Large Aircraft (26.1-75m) |
| 3001 | UAS [NATO Class I, Micro] (0-2kg) |
| 3002 | UAS [NATO Class I, Mini] (2-20kg) |
| 3003 | UAS [NATO Class I, Small] (20-150kg) |
| 3004 | UAS [NATO Class II] (150-600kg) |

### EnumAircraftType

**行数**: 36  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (36 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Fighter |
| 2002 | Multirole (Fighter/Attack) |
| 2101 | Anti-Satellite Interceptor (ASAT) |
| 2102 | Airborne Laser Platform |
| 3001 | Attack |
| 3002 | Wild Weasel |
| 3101 | Bomber |
| 3401 | Battlefield Air Interdiction (BAI/CAS) |
| 4001 | Electronic Warfare |
| 4002 | Airborne Early Warning (AEW) |
| 4003 | Airborne Command Post (ACP) |
| 4101 | Search And Rescue (SAR) |
| 4201 | Mine Sweeper (MCM) |
| 6001 | Anti-Submarine Warfare (ASW) |
| 6002 | Maritime Patrol Aircraft (MPA) |
| 7001 | Forward Observer |
| 7002 | Area Surveillance |
| 7003 | Recon |
| 7004 | Electronic Intelligence (ELINT) |
| 7005 | Signals Intelligence (SIGINT) |
| 7101 | Transport |
| 7201 | Cargo |
| 7301 | Commercial |
| 7302 | Civilian |
| 7401 | Utility |
| 7402 | Naval Utility |
| 8001 | Tanker (Air Refueling) |
| 8101 | Trainer |
| 8102 | Target Towing |
| 8103 | Target Drone |
| 8201 | Unmanned Aerial Vehicle (UAV) |
| 8202 | Unmanned Combat Aerial Vehicle (UCAV) |
| 8901 | Rigid Airship |
| 8902 | Aerostat |
| 8903 | Blimp |

### EnumArcs

**行数**: 8  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (8 个):

| ID | 描述 |
|-----|------|
| 1001 | SB (000-045) |
| 1002 | SMF (045-090) |
| 1003 | SMA (090-135) |
| 1004 | SS (135-180) |
| 1005 | PB (315-360) |
| 1006 | PMF (270-315) |
| 1007 | PMA (225-270) |
| 1008 | PS (180-225) |

### EnumArmorType

**行数**: 12  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (12 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 1005 | Light (Handgun Resistant) |
| 1010 | Light (Assault Rifle Resistant) |
| 1015 | Light (HMG Resistant) |
| 1020 | Light (20-25mm RHA) |
| 1025 | Light (26-30mm RHA) |
| 1030 | Light (31-35mm RHA) |
| 1035 | Light (36-40mm RHA) |
| 2001 | Light (41-90mm RHA) |
| 2002 | Medium (91-140mm RHA) |
| 2003 | Heavy (141-200mm RHA) |
| 2004 | Special (201-500mm RHA) |

### EnumCargoType

**行数**: 6  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | 0 | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (6 个):

| ID | 描述 |
|-----|------|
| 0 | No Cargo |
| 1000 | Personnel (Squads, MANPADS, ATGM) |
| 2000 | Small Cargo (Car, AAA Guns, AMRAAM) |
| 3000 | Medium Cargo (APC, Towed Arty, Cruise Missiles) |
| 4000 | Large Cargo (Tank, TEL, Trailer) |
| 5000 | Very Large Cargo (IRBM / ICBM TEL) |

### EnumCommCapability

**行数**: 23  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (23 个):

| ID | 描述 |
|-----|------|
| 1200 | Send Only |
| 1201 | Receive Only |
| 1300 | LOS Limited |
| 1310 | Degrades With Range |
| 1401 | Secure |
| 1402 | Broadcast |
| 1450 | Low Probability of Intercept/Detection (LPI/LPD) |
| 1475 | Phased Array Antenna |
| 1500 | Jam Resistant |
| 3001 | ELF Radio (3-30 Hz) |
| 3002 | SLF Radio (30-300 Hz) |
| 3003 | ULF Radio (300-3000 Hz) |
| 3004 | VLF Radio (3-30 KHz) |
| 3005 | LF Radio (30-300 KHz) |
| 3006 | MF Radio (300-3000 KHz) |
| 3007 | HF Radio (3-30 MHz) |
| 3008 | VHF Radio (30-300 MHz) |
| 3009 | UHF Radio (300-3000 MHz) |
| 3010 | SHF Radio (3-30 GHz) |
| 3011 | EHF Radio (30-300 GHz) |
| 3100 | BLOS-LEO |
| 3110 | BLOS-MEO |
| 4000 | Daisy Chain Capability |

### EnumCommLatency

**行数**: 6  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |
| Capability | TEXT | 是 | - | - |
| Example | TEXT | 是 | - | - |

**枚举值** (6 个):

| ID | 描述 |
|-----|------|
| 0 | None |
| 1000 | Slow |
| 2000 | Norm |
| 3000 | Fast |
| 4000 | Instnt |
| 5000 | BMD |

### EnumCommQuality

**行数**: 6  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |
| Capability | TEXT | 是 | - | - |
| Example | TEXT | 是 | - | - |

**枚举值** (6 个):

| ID | 描述 |
|-----|------|
| 0 | None |
| 1000 | GLoc |
| 2000 | TacP |
| 3000 | AAW |
| 4000 | BMD |
| 5000 | FMV |

### EnumCommType

**行数**: 108  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (108 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Commercial SATCOM |
| 2002 | FLTSATCOM |
| 2003 | MILSTAR SATCOM |
| 2004 | AFSATCOM |
| 2005 | Skynet SATCOM |
| 2006 | Big Ball SATCOM |
| 2007 | Satellite Downlink |
| 2009 | Punch Bowl SATCOM |
| 2010 | SATCOM |
| 3001 | Visual Comm |
| 3002 | Laser Comm |
| 3003 | Land Line |
| 4001 | Link 4 |
| 4002 | Link 10 |
| 4003 | Link 11 |
| 4004 | Link 16 |
| 4005 | Link 14 |
| 4006 | Link 11B |
| 4007 | Link 22 |
| 4011 | CEC |
| 4021 | Link Y |
| 4022 | Link T |
| 5004 | LAMPS Datalink |
| 5006 | A346Z Datalink |
| 6001 | ELF Link (Submarine) |
| 7001 | Radio |
| 8002 | Two-Way Wire Guidance |
| 9001 | NATO Sonobuoy Link |
| 9002 | Generic Sonobuoy Link |
| 10001 | AEGIS Weapon Link |
| 10002 | Generic Weapon Link |
| 10003 | NTU Weapon Link |
| 10004 | NASAMS Weapon Link |
| 10005 | AGM-142 Weapon Link |
| 10006 | Patriot Weapon Link |
| 10008 | Rapier Weapon Link |
| 10009 | AIM-120 Weapon Link |
| 10010 | Roland Weapon Link |
| 10011 | AN/AAW-9/13 Weapon Link |
| 10012 | SA-12 Weapon Link |
| 10013 | AJ.168 Weapon Link |
| 10015 | AS.11/12 Weapon Wire |
| 10016 | SA-10/SA-N-6 Weapon Link |
| 10018 | HUMRAAM Weapon Link |
| 10019 | AS.30 Weapon Link |
| 10020 | HOT Weapon Link |
| 10021 | APK-8/9 Weapon Link |
| 10022 | IKARA Weapon Link |
| 10023 | AS-7 Weapon Link |

_... 共 108 个值_

### EnumContainerType

**行数**: 4  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | 0 | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (4 个):

| ID | 描述 |
|-----|------|
| 1001 | Standard |
| 1002 | Open Top |
| 2001 | Tank |
| 3001 | Pallet |

### EnumDockingFacilityPhysicalSize

**行数**: 13  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (13 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Very Small Pier (0-11m Long) |
| 2002 | Small Pier (11.1-17m Long) |
| 2003 | Medium Pier (17.1-25m Long) |
| 2004 | Large Pier (25.1-45m Long) |
| 2005 | Very Large Pier (45.1-200m) |
| 2006 | Extra Large Pier (200-500m) |
| 3001 | Very Small Dock/Ramp/Davit (0-11m Long) |
| 3002 | Small Dock/Ramp/Davit (LCVP, 11.1-17m Long) |
| 3003 | Medium Dock (LCM, 17.1-25m Long) |
| 3004 | Large Dock (LCU/LCAC, 25.1-45m Long) |
| 4001 | Dry-Deck Shelter (DDS) |
| 5001 | ROV/UUV |

### EnumDockingFacilityType

**行数**: 7  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (7 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Dock Well |
| 3001 | Davit |
| 3500 | Boat Ramp |
| 4001 | Dry-Deck Shelter (DDS) |
| 5001 | ROV/UUV Davit/Crane/Shelter |
| 9001 | Pier |

### EnumErgonomics

**行数**: 5  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |
| OODADetectionModPercent | INTEGER | 是 | 0 | - |
| OODATargetingModPercent | INTEGER | 是 | 0 | - |
| OODAEvasiveModPercent | INTEGER | 是 | 0 | - |

**枚举值** (5 个):

| ID | 描述 |
|-----|------|
| 1000 | Awful |
| 2000 | Poor |
| 3000 | Average |
| 4000 | Good |
| 5000 | Excellent |

### EnumFacilityCSGen

**行数**: 22  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |
| Example | TEXT | 是 | - | - |
| OODADetectionCycle | INTEGER | 是 | 0 | - |
| OODATargetingCycle | INTEGER | 是 | 0 | - |
| OODAEvasiveCycle | INTEGER | 是 | 0 | - |

**枚举值** (22 个):

| ID | 描述 |
|-----|------|
| 0 | Undefined (Use Below) |
| 1000 | None (Small) |
| 1001 | None (Large) |
| 2100 | Sensor (Fixed, Mechanical) |
| 2150 | Sensor (Fixed, Electronic) |
| 2200 | Sensor (Mobile, Mechanical) |
| 2250 | Sensor (Mobile, Electronic) |
| 3100 | SAM (Fixed, Analog) |
| 3150 | SAM (Fixed, Digital) |
| 3200 | SAM (TEL, Analog) |
| 3250 | SAM (TEL, Digital) |
| 3300 | SAM (SPAD, Analog) |
| 3350 | SAM (SPAD, Digital) |
| 4100 | AAA (Towed, Manual) |
| 4150 | AAA (Towed, Assisted) |
| 4200 | AAA (SPAAG, Manual) |
| 4250 | AAA (SPAAG, Assisted) |
| 5100 | Artillery (Towed) |
| 5200 | Artillery (SPG, Manual) |
| 5250 | Artillery (SPG, Digital FC) |
| 6100 | Mech/Armor (Analog) |
| 6200 | Mech/Armor (Digital) |

### EnumFacilityCategory

**行数**: 20  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (20 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Runway |
| 2002 | Runway-Grade Taxiway |
| 2003 | Runway Access Point |
| 3001 | Building (Surface) |
| 3002 | Building (Reveted) |
| 3003 | Building (Bunker) |
| 3004 | Building (Underground) |
| 3005 | Structure (Open) |
| 3006 | Structure (Reveted) |
| 3007 | Surface (Flat) & Underground |
| 4001 | Underwater |
| 4050 | Water (Surface) |
| 5001 | Mobile Vehicle(s) |
| 5002 | Mobile Personnel |
| 5003 | Mobile Vehicle(s) - Tracked |
| 5004 | Mobile Vehicle(s) - Half-Track |
| 5005 | Mobile Vehicle(s) - Wheeled |
| 6001 | Aerostat Mooring |
| 9001 | Air Base |

### EnumFacilityType

**行数**: 31  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (31 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Radar |
| 3001 | SAM |
| 4001 | AAA |
| 5001 | Artillery |
| 5011 | Towed Artillery |
| 5021 | Self Propelled Artillery |
| 5111 | Wheeled Rocket Artillery |
| 5121 | Tracked Rocket Artillery |
| 5201 | Mortar |
| 6001 | SSM |
| 7001 | Armored |
| 7500 | Combined Arms |
| 8001 | Infantry |
| 8011 | Marines |
| 8021 | Air Assault |
| 8031 | Mountain |
| 8041 | Airborne |
| 8101 | Special Forces |
| 9001 | Mechanized |
| 9041 | Mechanized Airborne |
| 9501 | Mechanized Wheeled |
| 10001 | Motorized |
| 11001 | Ammo |
| 12001 | Fuel |
| 13001 | Supply |
| 14001 | Recon |
| 14011 | Amphibious Recon |
| 16001 | Anti Tank |
| 17001 | Engineer |
| 18000 | Headquarters |

### EnumFuelType

**行数**: 12  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (12 个):

| ID | 描述 |
|-----|------|
| 1001 | No Fuel |
| 2001 | Aviation Fuel |
| 3001 | Diesel Fuel |
| 3002 | Oil Fuel |
| 3003 | Gas Fuel |
| 3006 | Gasoline |
| 4001 | Battery |
| 4002 | Air Independent |
| 4003 | Lithium-Ion Battery |
| 5001 | Rocket Fuel |
| 5002 | Torpedo Fuel |
| 5003 | Weapon Coast Time |

### EnumGroundUnitCSGen

**行数**: 13  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |
| Example | TEXT | 是 | - | - |
| OODADetectionCycle | INTEGER | 是 | 0 | - |
| OODATargetingCycle | INTEGER | 是 | 0 | - |
| OODAEvasiveCycle | INTEGER | 是 | 0 | - |

**枚举值** (13 个):

| ID | 描述 |
|-----|------|
| 0 | Undefined (Use Below) |
| 1000 | None |
| 2200 | Sensor (Mechanical) |
| 2250 | Sensor (Electronic) |
| 3300 | SAM (Analog) |
| 3350 | SAM (Digital) |
| 4100 | AAA (Manual) |
| 4150 | AAA (Assisted) |
| 5100 | Artillery (Towed) |
| 5200 | Artillery (SPG, Manual) |
| 5250 | Artillery (SPG, Digital FC) |
| 6100 | Mech/Armor (Analog) |
| 6200 | Mech/Armor (Digital) |

### EnumGroundUnitCategory

**行数**: 32  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | 0 | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (32 个):

| ID | 描述 |
|-----|------|
| 0 | None |
| 1000 | Infantry |
| 1010 | Marines |
| 1020 | Air Assault |
| 1030 | Mountain |
| 1040 | Airborne |
| 1100 | Special Forces |
| 1500 | Combined Arms |
| 2000 | Armor |
| 2500 | Armor Recon |
| 3000 | Artillery |
| 3010 | Towed Artillery |
| 3020 | Self-Propelled Artillery |
| 3110 | Wheeled Rocket Artillery |
| 3120 | Tracked Rocket Artillery |
| 3200 | Mortar |
| 4000 | SSM |
| 5000 | AAA |
| 6000 | SAM |
| 7000 | Engineer |
| 8000 | Supply |
| 9000 | Surveillance |
| 10000 | Recon |
| 10010 | Amphibious Recon |
| 11000 | Mech Infantry |
| 11010 | Mech Marines |
| 11040 | Mech Airborne |
| 11500 | Mech Wheeled |
| 12000 | Motorized Infantry |
| 13000 | Anti Tank |
| 14000 | Radar |
| 15000 | Headquarters |

### EnumGroundUnitCode

**行数**: 12  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (12 个):

| ID | 描述 |
|-----|------|
| 1001 | Troop Carrying |
| 1002 | Open Topped |
| 2001 | Amphibious |
| 2002 | Combat Swimmer |
| 3001 | Reactive Armor |
| 3002 | Mesh Skirting |
| 3003 | Depleted Uranium Armor (1st Gen) |
| 3004 | Depleted Uranium Armor (2nd Gen) |
| 3005 | Depleted Uranium Armor (3rd Gen) |
| 4001 | Wheeled Vehicle |
| 4002 | Half-Track Vehicle |
| 4003 | Tracked Vehicle |

### EnumLoadoutMissionProfile

**行数**: 174  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |
| FormUpTime | DOUBLE | 是 | - | - |
| FormUpAltitude | DOUBLE | 是 | - | - |
| CruiseAltitudeIngress | DOUBLE | 是 | - | - |
| CruiseAltitudeIngressTerrainFollowing | BOOLEAN | 否 | - | - |
| CruiseAltitudeEgress | DOUBLE | 是 | - | - |
| CruiseAltitudeEgressTerrainFollowing | BOOLEAN | 否 | - | - |
| CruiseThrottleSettingIngress | DOUBLE | 是 | - | - |
| CruiseThrottleSettingEgress | DOUBLE | 是 | - | - |
| CruiseOneWayOnly | BOOLEAN | 否 | - | - |
| CruiseAtOptimumAltitude | BOOLEAN | 否 | - | - |
| AttackAltitudeEgress | DOUBLE | 是 | - | - |
| AttackAltitudeEgressTerrainFollowing | BOOLEAN | 否 | - | - |
| AttackAltitudeIngress | DOUBLE | 是 | - | - |
| AttackAltitudeIngressTerrainFollowing | BOOLEAN | 否 | - | - |
| AttackThrottleSetting | DOUBLE | 是 | - | - |
| AttackDistanceIngress | DOUBLE | 是 | - | - |
| AttackDistanceEgress | DOUBLE | 是 | - | - |
| DropBombsAtMaxRange | BOOLEAN | 否 | - | - |
| StationAltitude | DOUBLE | 是 | - | - |
| StationAltitudeTerrainFollowing | BOOLEAN | 否 | - | - |
| StationThrottleSetting | DOUBLE | 是 | - | - |
| CombatAltitude | DOUBLE | 是 | - | - |
| CombatThrottleSetting | DOUBLE | 是 | - | - |
| CombatDuration | DOUBLE | 是 | - | - |
| ReservePercentage | DOUBLE | 是 | - | - |
| ReserveLoiterTime | DOUBLE | 是 | - | - |
| ReserveLoiterAltitude | DOUBLE | 是 | - | - |

**枚举值** (174 个):

| ID | 描述 |
|-----|------|
| 1001 | n/a |
| 2011 | CAP. Transit at 25k ft, on-station loiter, 2 minutes combat in Mil. Form-up 2 min at 2k ft. 10% reserves. |
| 2012 | CAP. Transit at 25k ft, on-station loiter, 2 minutes combat in Mil. Form-up 2 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |
| 2014 | CAP. Transit at 25k ft, on-station loiter, 2 minutes combat in Mil. Form-up 2 min at 2k ft. 5% reserves and 10 minute loiter at 2k ft |
| 2016 | CAP. Transit at 36k ft, on-station loiter, 2 minutes combat in AB. Form-up 2 min at 2k ft. 10% reserves. |
| 2017 | CAP. Transit at 36k ft, on-station loiter, 2 minutes combat in AB. Form-up 2 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |
| 2019 | CAP. Transit at 36k ft, on-station loiter, 2 minutes combat in AB. Form-up 2 min at 2k ft. 5% reserves and 10 minute loiter at 2k ft |
| 2021 | CAP. Transit at 36k ft, on-station loiter, 2 minutes combat in Mil. Form-up 2 min at 2k ft. 10% reserves. |
| 2022 | CAP. Transit at 36k ft, on-station loiter, 2 minutes combat in Mil. Form-up 2 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |
| 2024 | CAP. Transit at 36k ft, on-station loiter, 2 minutes combat in Mil. Form-up 2 min at 2k ft. 5% reserves and 10 minute loiter at 2k ft |
| 2025 | CAP. Transit at 50k ft, on-station loiter, 2 minutes combat in Mil. Form-up 2 min at 2k ft. 10% reserves. |
| 2026 | CAP. Transit at 50k ft, on-station loiter, 2 minutes combat in Mil. Form-up 2 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |
| 2027 | CAP. Transit at 50k ft, on-station loiter, 2 minutes combat in Mil. Form-up 2 min at 2k ft. 5% reserves and 10 minute loiter at 2k ft |
| 2028 | CAP. Transit at 55k ft, on-station loiter, 2 minutes combat in Mil. Form-up 2 min at 2k ft. 10% reserves. |
| 2029 | CAP. Transit at 55k ft, on-station loiter, 2 minutes combat in Mil. Form-up 2 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |
| 2030 | CAP. Transit at 55k ft, on-station loiter, 2 minutes combat in Mil. Form-up 2 min at 2k ft. 5% reserves and 10 minute loiter at 2k ft |
| 2031 | Intercept radius. Outbound at 36k ft and AB, return at 36k ft and cruise. No form-up time. 10% reserves. |
| 2032 | Intercept radius. Outbound at 36k ft and AB, return at 36k ft and cruise. No form-up time. 5% reserves and 20 minute loiter at 2k ft |
| 2036 | Intercept radius. Outbound at 36k ft and Mil, return at 36k ft and cruise. No form-up time. 10% reserves. |
| 2037 | Intercept radius. Outbound at 36k ft and Mil, return at 36k ft and cruise. No form-up time. 5% reserves and 20 minute loiter at 2k ft |
| 2038 | Intercept radius. Outbound at 15k ft and Mil, return at 15k ft and cruise. No form-up time. 10% reserves. |
| 2039 | Intercept radius. Outbound at 15k ft and Mil, return at 15k ft and cruise. No form-up time. 5% reserves and 20 minute loiter at 2k ft |
| 2041 | Intercept radius. Outbound at 40k ft and AB, return at 40k ft and cruise. No form-up time. 10% reserves. |
| 2042 | Intercept radius. Outbound at 40k ft and AB, return at 40k ft and cruise. No form-up time. 5% reserves and 20 minute loiter at 2k ft |
| 2051 | Fighter Sweep radius. Cruise at 36k ft. Form-up 2 min at 2k ft. 10% reserves. |
| 2052 | Fighter Sweep radius. Cruise at 36k ft. Form-up 2 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |
| 3001 | Strike radius, Lo-Lo-Lo profile. Cruise at SL. Weapon release at max range. No form-up time. 10% reserves. |
| 3002 | Strike radius, Lo-Lo-Lo profile. Cruise at SL. Weapon release at max range. No form-up time. 5% reserves and 20 minute loiter at 2k ft |
| 3006 | Strike radius, Lo-Lo-Lo profile. Cruise at SL. Weapon release at max range. Form-up 10 min at 2k ft. 10% reserves. |
| 3007 | Strike radius, Lo-Lo-Lo profile. Cruise at SL. Weapon release at max range. Form-up 10 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |
| 3011 | Strike radius, Lo-Lo-Lo profile. Cruise at SL. 100nm (50nm+50nm) dash on target at SL and Mil. Weapon release at max range. Form-up 10 min at 2k ft. 10% reserves. |
| 3012 | Strike radius, Lo-Lo-Lo profile. Cruise at SL. 100nm (50nm+50nm) dash on target at SL and Mil. Weapon release at max range. Form-up 10 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |
| 3014 | Strike radius, Lo-Lo-Lo profile. Cruise at SL. 60nm (30nm+30nm) dash on target at SL and Mil. Weapon release at max range. Form-up 10 min at 2k ft. 10% reserves. |
| 3015 | Strike radius, Lo-Lo-Lo profile. Cruise at SL. 60nm (30nm+30nm) dash on target at SL and Mil. Weapon release at max range. Form-up 10 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |
| 3017 | Strike radius, Lo-Lo-Hi profile. Ingress Cruise at SL. 30nm (15nm+15nm) dash on target at SL and AB. Egress Cruise at 36k ft. Weapon release at max range. Form-up 10 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft. (F-111A profile) |
| 3101 | Strike radius, Med-Med-Med profile. Cruise at 12k ft. Weapon release at max range. Form-up 10 min at 2k ft. 10% reserves. |
| 3102 | Strike radius, Med-Med-Med profile. Cruise at 12k ft. Weapon release at max range. Form-up 10 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |
| 3106 | Strike radius, Med-Med-Med profile. Cruise at 12k ft. 100nm (50nm+50nm) dash on target at 12k ft and Mil. Weapon release at max range. Form-up 10 min at 2k ft. 10% reserves. |
| 3107 | Strike radius, Med-Med-Med profile. Cruise at 12k ft. 100nm (50nm+50nm) dash on target at 12k ft and Mil. Weapon release at max range. Form-up 10 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |
| 3201 | Strike radius, Hi-Lo-Hi profile. Cruise at 25k ft. 100nm (50nm+50nm) dash on target at SL and Cruise. Weapon release at max range. Form-up 10 min at 2k ft. 10% reserves. |
| 3202 | Strike radius, Hi-Lo-Hi profile. Cruise at 25k ft. 100nm (50nm+50nm) dash on target at SL and Cruise. Weapon release at max range. Form-up 10 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |
| 3203 | Strike radius, Hi-Lo-Hi profile. Cruise at 25k ft. 100nm (50nm+50nm) dash on target at SL and Cruise. Weapon release at max range. Form-up 10 min at 2k ft. 5% reserves and 30 minute loiter at 2k ft |
| 3206 | Strike radius, Hi-Lo-Hi profile. Cruise at 25k ft. 100nm (50nm+50nm) dash on target at SL and Mil. Weapon release at max range. Form-up 10 min at 2k ft. 10% reserves. |
| 3207 | Strike radius, Hi-Lo-Hi profile. Cruise at 25k ft. 100nm (50nm+50nm) dash on target at SL and Mil. Weapon release at max range. Form-up 10 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |
| 3208 | Strike radius, Hi-Lo-Hi profile. Cruise at 25k ft. 100nm (50nm+50nm) dash on target at SL and Mil. Weapon release at max range. Form-up 10 min at 2k ft. 5% reserves and 30 minute loiter at 2k ft |
| 3211 | Strike radius, Hi-Lo-Hi profile. Cruise at 36k ft. 100nm (50nm+50nm) dash on target at SL and Cruise. Weapon release at max range. Form-up 10 min at 2k ft. 10% reserves. |
| 3212 | Strike radius, Hi-Lo-Hi profile. Cruise at 36k ft. 100nm (50nm+50nm) dash on target at SL and Cruise. Weapon release at max range. Form-up 10 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |
| 3213 | Strike radius, Hi-Lo-Hi profile. Cruise at 36k ft. 100nm (50nm+50nm) dash on target at SL and Cruise. Weapon release at max range. Form-up 10 min at 2k ft. 5% reserves and 30 minute loiter at 2k ft |
| 3216 | Strike radius, Hi-Lo-Hi profile. Cruise at 36k ft. 100nm (50nm+50nm) dash on target at SL and Mil. Weapon release at max range. Form-up 10 min at 2k ft. 10% reserves. |
| 3217 | Strike radius, Hi-Lo-Hi profile. Cruise at 36k ft. 100nm (50nm+50nm) dash on target at SL and Mil. Weapon release at max range. Form-up 10 min at 2k ft. 5% reserves and 20 minute loiter at 2k ft |

_... 共 174 个值_

### EnumLoadoutRole

**行数**: 55  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (55 个):

| ID | 描述 |
|-----|------|
| 1001 | n/a |
| 2001 | Intercept, BVR AAMs |
| 2002 | Intercept, WVR AAMs |
| 2003 | Air Superiority, BVR AAMs |
| 2004 | Air Superiority, WVR AAMs |
| 2005 | Point-defence, BVR AAMs |
| 2006 | Point-defence, WVR AAMs |
| 2007 | Guns Only |
| 2101 | Anti-Satellite Intercept (ASAT) |
| 2102 | Airborne Laser (ABM) |
| 3001 | Strike, Land/Naval |
| 3002 | Standoff Strike, Land/Naval |
| 3003 | SEAD, ARM, Land/Naval |
| 3004 | SEAD, TALD, Land/Naval |
| 3005 | DEAD, Land/Naval |
| 3101 | Strike, Land-only |
| 3102 | Standoff Strike, Land |
| 3103 | SEAD, ARM, Land |
| 3104 | SEAD, TALD, Land |
| 3105 | DEAD, Land |
| 3201 | Strike, Naval |
| 3202 | Standoff Strike, Naval |
| 3203 | SEAD, ARM, Naval |
| 3204 | SEAD, TALD, Naval |
| 3205 | DEAD, Naval |
| 3401 | BAI/CAS |
| 3501 | Buddy Illumination |
| 4001 | Offensive ECM |
| 4002 | Airborne Early Warning (AEW) |
| 4003 | Airborne Command Post (ACP) |
| 4004 | Chaff Dispenser |
| 4005 | Drone Deployment |
| 4101 | Search And Rescue (SAR) |
| 4102 | Combat Search And Rescue (CSAR) |
| 4201 | Mine Sweep (MCM) |
| 4202 | Mine Reconnaissance |
| 4301 | Naval Mine Laying |
| 6001 | ASW Patrol |
| 6002 | ASW Attack |
| 7001 | Forward Observer |
| 7002 | Area Surveillance |
| 7003 | Armed Recon |
| 7004 | Unarmed Recon |
| 7005 | Maritime Surveillance |
| 7101 | Paratroops |
| 7102 | Troop Transport |
| 7201 | Cargo Transport |
| 8001 | Air Refueling |
| 8101 | Training |
| 8102 | Target Tow |

_... 共 55 个值_

### EnumLoadoutTimeOfDay

**行数**: 4  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (4 个):

| ID | 描述 |
|-----|------|
| 1001 | n/a |
| 2001 | Day and night |
| 2002 | Night-only |
| 2003 | Day-only |

### EnumLoadoutWeather

**行数**: 4  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (4 个):

| ID | 描述 |
|-----|------|
| 1001 | n/a |
| 2001 | All-weather |
| 2002 | Limited all-weather |
| 2003 | Clear weather |

### EnumLoadoutWinchesterShotgun

**行数**: 20  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (20 个):

| ID | 描述 |
|-----|------|
| 1001 | n/a |
| 2001 | Winchester: Mission-specific weapons have been expended. Disengage immediately. |
| 2002 | Winchester: Mission-specific weapons have been expended. Allow targets of opportunity with air-to-air guns. PREFERRED! |
| 3001 | Shotgun: All BVR or Stand-Off weapons have been expended. Disengage immediately. |
| 3002 | Shotgun: All BVR or Stand-Off weapons have been expended. Allow easy targets of opportunity with WVR or Strike weapons. No air-to-air guns. |
| 3003 | Shotgun: All BVR or Stand-Off weapons have been expended. Allow easy targets of opportunity with WVR or Strike weapons, and air-to-air guns. |
| 4001 | Shotgun: 25% of relevant weapons have been expended. Disengage immediately. |
| 4002 | Shotgun: 25% of relevant weapons have been expended. Allow targets of opportunity, including air-to-air guns. |
| 4011 | Shotgun: 50% of relevant weapons have been expended. Disengage immediately. |
| 4012 | Shotgun: 50% of relevant weapons have been expended. Allow targets of opportunity, including air-to-air guns. |
| 4021 | Shotgun: 75% of relevant weapons have been expended. Disengage immediately. |
| 4022 | Shotgun: 75% of relevant weapons have been expended. Allow targets of opportunity, including air-to-air guns. |
| 5001 | Shotgun: One engagement with BVR or Stand-Off weapons. Disengage immediately. |
| 5002 | Shotgun: One engagement with BVR or Stand-Off weapons. Allow easy targets of opportunity with WVR or Strike weapons. No air-to-air guns. PREFERRED! |
| 5003 | Shotgun: One engagement with BVR or Stand-Off weapons. Allow easy targets of opportunity with WVR or Strike weapons, and air-to-air guns. |
| 5005 | Shotgun: One engagement with both BVR and WVR or Stand-Off and Strike weapons. No air-to-air guns. |
| 5006 | Shotgun: One engagement with both BVR and WVR or Stand-Off and Strike weapons. Allow easy targets of opportunity with air-to-air guns. PREFERRED! |
| 5011 | Shotgun: One engagement with WVR or Strike weapons. Disengage immediately. |
| 5012 | Shotgun: One engagement with WVR or Strike weapons. Allow targets of opportunity with air-to-air guns. PREFERRED! |
| 5021 | Shotgun: One engagement with guns. |

### EnumOperatorCountry

**行数**: 186  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |
| YearStart | INTEGER | 是 | - | - |
| YearEnd | INTEGER | 是 | - | - |

**枚举值** (186 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 1002 | Unknown |
| 1003 | Generic |
| 1101 | Civilian |
| 1102 | Commercial |
| 1201 | Pirates |
| 1202 | Rebels |
| 1203 | Terrorists |
| 2001 | Abu Dhabi |
| 2002 | Albania |
| 2003 | Algeria |
| 2004 | Angola |
| 2005 | Argentina |
| 2006 | Australia |
| 2007 | Austria |
| 2008 | Bahrain |
| 2009 | Bangladesh |
| 2010 | Belarus [1992-] |
| 2011 | Belgium |
| 2012 | Botswana |
| 2013 | Brazil |
| 2014 | Brunei |
| 2015 | Bulgaria |
| 2016 | Canada |
| 2017 | Chile |
| 2018 | China |
| 2019 | Colombia |
| 2020 | Croatia [1992-] |
| 2021 | Cuba |
| 2022 | Cyprus |
| 2023 | Czech Republic [1993-] |
| 2024 | Czechoslovakia  [-1992] |
| 2025 | Denmark |
| 2026 | Dominican Republic |
| 2027 | Ecuador |
| 2028 | Egypt |
| 2029 | El Salvador |
| 2030 | Estonia [1992-] |
| 2031 | Finland |
| 2032 | France |
| 2033 | Gabon |
| 2034 | Germany [DDR, -1990] |
| 2035 | Germany [FRG/Reunified] |
| 2036 | Greece |
| 2037 | Guatemala |
| 2038 | Honduras |
| 2039 | Hong Kong |
| 2040 | Hungary |
| 2041 | India |
| 2042 | Indonesia |

_... 共 186 个值_

### EnumOperatorService

**行数**: 59  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (59 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 1002 | Unknown |
| 1003 | Generic |
| 2001 | Air Force |
| 2002 | Navy |
| 2003 | Army |
| 2004 | Marines |
| 2005 | Coast Guard |
| 2006 | National Guard |
| 2007 | Home Guard |
| 2008 | Coastal Artillery |
| 2009 | Marine Corps |
| 2010 | Customs |
| 2011 | Civil Air Patrol |
| 2012 | Air National Guard |
| 2013 | Border Guard |
| 2014 | Police |
| 2015 | Space Force |
| 2101 | Royal Air Force |
| 2102 | Royal Navy |
| 2103 | Royal Army |
| 2104 | Royal Marines |
| 2201 | Frontal Aviation [VVS] |
| 2202 | Air Defence Troops [PVO] |
| 2203 | Naval Fleet [V-MF] |
| 2204 | Naval Aviation [AV-MF] |
| 2205 | Red Army |
| 2206 | Naval Infantry |
| 2207 | Strategic Rocket Forces |
| 2208 | Long Range Aviation [DA] |
| 2209 | Military Transport Aviation (VTA) |
| 2210 | PLAAF |
| 2211 | PLANAF |
| 2212 | PLAN |
| 2213 | PAFMM |
| 2214 | Maritime Safety Administration |
| 2215 | PAP |
| 2220 | PLAGF |
| 2221 | PLANMC |
| 2300 | PLAASF / PLASSF |
| 2301 | PLARF / Second Artillery Corps |
| 2302 | Surface-to-Air Missile Corps |
| 2401 | Air Corps |
| 2402 | Army Air Forces |
| 2501 | Military |
| 2601 | IRGC Navy |
| 2602 | IRGC Ground Forces |
| 2603 | Republican Guard |
| 2604 | Air Self-Defense Force |
| 2605 | Maritime Self-Defense Force |

_... 共 59 个值_

### EnumPropulsionCombinedType

**行数**: 14  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (14 个):

| ID | 描述 |
|-----|------|
| 1001 | N/A |
| 2000 | CODOG |
| 2050 | CODLOG |
| 2100 | CODAG |
| 2150 | CODLAG |
| 2200 | CODAD |
| 2250 | CODLAD |
| 2300 | COGOG |
| 2400 | COGAG |
| 2450 | COGLAG |
| 2500 | COGAS |
| 2550 | COSAG |
| 2600 | CONAS |
| 2700 | IEP/FEP |

### EnumPropulsionType

**行数**: 24  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (24 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Turbojet |
| 2002 | Turbofan |
| 2003 | Turboprop |
| 2004 | Piston |
| 2005 | Helo Turboshaft |
| 3001 | Diesel |
| 3002 | Steam |
| 3003 | Gas Turbine |
| 3004 | Nuclear |
| 3005 | Pump Jet Propulsor |
| 3006 | Gasoline |
| 3007 | Personnel |
| 4001 | Electric |
| 4002 | Air Independent |
| 5001 | Rocket [Boost & Coast] |
| 5002 | Torpedo Engine |
| 5003 | Weapon Coast |
| 5004 | Rocket [Long Burn] |
| 5005 | Ramjet |
| 6001 | Torpedo Thermal Combustion |
| 6002 | Torpedo Thermal Closed Cycle |
| 6003 | Torpedo Electric |
| 9001 | Static |

### EnumRunwayLength

**行数**: 13  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (13 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 1002 | Manual Launch |
| 1101 | Catapult Launcher |
| 2001 | 0m (VTOL) TOD/LAD |
| 2002 | 250-450m (STOL) TOD/LAD |
| 2003 | 451-900m TOD/LAD |
| 2004 | 901-1400m TOD/LAD |
| 2005 | 1401-2000m TOD/LAD |
| 2006 | 2001-2600m TOD/LAD |
| 2007 | 2601-3200m TOD/LAD |
| 2008 | 3201-4000m TOD/LAD |
| 2009 | 4001-5600m TOD/LAD |
| 3005 | 1-250m (LHA/LHD) TOD/LAD |

### EnumSatelliteCSGen

**行数**: 9  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |
| Example | TEXT | 是 | - | - |
| YearStart | INTEGER | 是 | - | - |
| YearEnd | INTEGER | 是 | - | - |
| OODADetectionCycle | INTEGER | 是 | 0 | - |
| OODATargetingCycle | INTEGER | 是 | 0 | - |
| OODAEvasiveCycle | INTEGER | 是 | 0 | - |

**枚举值** (9 个):

| ID | 描述 |
|-----|------|
| 0 | Undefined (Use Below) |
| 1100 | Visual (Gen 1) |
| 1200 | Visual (Gen 2) |
| 1300 | Visual (Gen 3) |
| 1400 | Visual (Gen 4) |
| 1500 | Visual (Gen 5) |
| 2100 | Non-Visual (Gen 1) |
| 2200 | Non-Visual (Gen 2) |
| 2300 | Non-Visual (Gen 3) |

### EnumSatelliteCategory

**行数**: 4  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (4 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Geo-Stationary |
| 2002 | Something Else |
| 2003 | Unmanned Test Vehicle |

### EnumSatelliteCode

**行数**: 0  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

### EnumSatelliteOrbitPlane

**行数**: 4  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (4 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | East |
| 2002 | West |
| 9001 | N/A |

### EnumSatelliteType

**行数**: 10  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (10 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | IMGSAT |
| 2002 | RORSAT |
| 2003 | EORSAT |
| 2004 | SIGINT |
| 2005 | ELINT |
| 2006 | NOSS |
| 2007 | MASINT |
| 2008 | Reusable Test Vehicle |
| 2009 | Communications |

### EnumSensorCapability

**行数**: 24  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (24 个):

| ID | 描述 |
|-----|------|
| 1001 | Air Search |
| 1002 | Surface Search |
| 1003 | Submarine Search |
| 1004 | Land Search - Fixed Facility |
| 1005 | Land Search - Mobile Unit |
| 1006 | Periscope Search |
| 1007 | C-RAM (Counter-Rocket, Artillery and Mortar) |
| 1011 | Space Search (ABM) |
| 1021 | Mine & Obstacle Search |
| 1022 | Torpedo Warning |
| 1023 | Missile Approach Warning |
| 2001 | Range Information |
| 2002 | Altitude Information |
| 2003 | Speed Information |
| 2004 | Heading Information |
| 4001 | Navigation Only |
| 4002 | Ground Mapping Only |
| 4003 | Terrain Avoidance / Following Only |
| 4004 | Weather Only |
| 4005 | Weather and Navigation Only |
| 9001 | OTH-B (Backscatter) |
| 9002 | OTH-SW (Surface Wave) |
| 10001 | TDOA (Time Difference of Arrivals) |
| 10002 | DF (Direction Finding) |

### EnumSensorCode

**行数**: 28  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (28 个):

| ID | 描述 |
|-----|------|
| 1001 | Identification Friend or Foe (IFF) [Side Info] |
| 1002 | Classification [Class Info] / Brilliant Weapon [Automatic Target Aquisition] |
| 1003 | Non-Cooperative Target Recognition (NCTR)  - Jet Engine Modulation [Class Info] |
| 1004 | Non-Cooperative Target Recognition (NCTR)  - Narrow Beam Interleaved Search and Track [Class Info] |
| 1011 | Continuous Tracking Capability |
| 1012 | Continuous Tracking Capability [Target Tracking Radar] |
| 1021 | Continuous Tracking Capability [Visual] |
| 1031 | Periscope Search - Basic Capability |
| 1032 | Periscope/Surface Search - Fine Range Resolution + Rapid Scan [1980+] |
| 1033 | Periscope/Surface Search - Advanced Processing [2000+] |
| 2001 | Track While Scan (TWS) |
| 2002 | Moving Target Indicator (MTI) |
| 2011 | Low Probability of Intercept (LPI) |
| 2701 | LLTV / NVG / CCD (Night-Capable) / Searchlight [Visual Night-Capable] |
| 3001 | Pulse-Only Radar |
| 3002 | Pulse Doppler Radar (Full LDSD Capability) |
| 3003 | Pulse Doppler Radar (Limited LDSD Capability) |
| 3011 | Passive Electronically Scanned Array (PESA) |
| 3012 | Active Electronically Scanned Array (AESA) |
| 3013 | Can Classify Ground Targets (SAR) |
| 4001 | Continuous Wave Illumination |
| 4002 | Interrupted Continuous Wave Illumination |
| 4003 | Weapon FCR (No CW Illumination) |
| 5001 | Frequency Agile |
| 5002 | Cognitive EW |
| 6001 | Generates AAW Fire-Control Data |
| 9101 | Shallow Water Capable (Partial) |
| 9102 | Shallow Water Capable (Full) [Classification Flag Required] |

### EnumSensorFrequency

**行数**: 36  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (36 个):

| ID | 描述 |
|-----|------|
| 1001 | A Band (30-250 MHz) [Old P Band (HF)] 100-300 cm |
| 1002 | B Band (250-500 MHz) [Old P Band (VHF)] 60-100 cm |
| 1003 | C Band (500-1000 MHz) [Old L Band (UHF)] 60-30cm |
| 1004 | D Band (1-2 GHz) [Old L Band] 15-30 cm |
| 1005 | E Band (2-3 GHz) [Old S Band] 10-15 cm |
| 1006 | F Band (3-4 GHz) [Old S Band] 7.5-10 cm |
| 1007 | G Band (4-6 GHz) [Old C Band] 5-7.5 cm |
| 1008 | H Band (6-8 GHz) [Old C Band] 3.75-5 cm |
| 1009 | I Band (8-10 GHz) [Old X Band] 3-3.75 cm |
| 1010 | J Band (10-20 GHz) [Old X Band] 1.5-3 cm |
| 1011 | K Band (20-40 GHz) [Old Ku Band] 0.75-1.5 cm |
| 1012 | L Band (40-60 GHz) [Old Ka Band] 5-7.5 mm |
| 1013 | M Band (60-100 GHz) [Old V/W Band] 3-5 mm |
| 2001 | Visual Light |
| 2002 | Near IR (0.75-8 µm) |
| 2003 | Far IR (8-1000 µm) |
| 2004 | Laser |
| 3001 | ELF Radio (3-30 Hz) |
| 3002 | SLF Radio (30-300 Hz) |
| 3003 | ULF Radio (300-3000 Hz) |
| 3004 | VLF Radio (3-30 KHz) |
| 3005 | LF Radio (30-300 KHz) |
| 3006 | MF Radio (300-3000 KHz) |
| 3007 | HF Radio (3-30 MHz) |
| 3008 | VHF Radio (30-300 MHz) |
| 3009 | UHF Radio (300-3000 MHz) |
| 3010 | SHF Radio (3-30 GHz) |
| 3011 | EHF Radio (30-300 GHz) |
| 4001 | LF Sonar (1-5 KHz, 3 KHz Center Frequency) |
| 4002 | MF Sonar (5-10 KHz, 7.5 KHz Center Frequency) |
| 4003 | HF Sonar (10-500 KHz, 20 KHz Center Frequency) |
| 4004 | VLF Sonar (0-1000 Hz, 200 Hz Center Frequency) |
| 5001 | GPS (GNSS) |
| 5002 | GLONASS (GNSS) |
| 5003 | BeiDou/COMPASS (GNSS) |
| 5004 | NavIC/IRNSS (GNSS) |

### EnumSensorGeneration

**行数**: 32  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (32 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 1002 | Not Applicable (N/A) |
| 2001 | Early 1950s |
| 2002 | Late 1950s |
| 2003 | Early 1960s |
| 2004 | Late 1960s |
| 2005 | Early 1970s |
| 2006 | Late 1970s |
| 2007 | Early 1980s |
| 2008 | Late 1980s |
| 2009 | Early 1990s |
| 2010 | Late 1990s |
| 2011 | Early 2000s |
| 2012 | Late 2000s |
| 2013 | Early 2010s |
| 2014 | Late 2010s |
| 2015 | Early 2020s |
| 2016 | Late 2020s |
| 2501 | Visual |
| 2601 | Visual, 1st Generation TV Camera (1960s/1970s, TISEO) |
| 2602 | Visual, 2nd Generation TV Camera (1980s/1990s, AXX-1 TCS) |
| 2603 | Visual, 3rd Generation TV Camera (2000s/2010s, CCD) |
| 2701 | LLTV, 1st Generation (1970s) |
| 2702 | LLTV, 2nd Generation (1980s/1990s) |
| 2703 | LLTV, 3rd Generation (2000s/2010s) |
| 2801 | Infrared, Non-Imaging |
| 2802 | Infrared, 1st Generation Imaging (1970s) |
| 2803 | Infrared, 2nd Generation Imaging (1980s/1990s, LANTIRN, Litening)
) |
| 2804 | Infrared, 3rd Generation Imaging (2000s/2010s, Impr LANTIRN, Litening II/III, ATFLIR) |
| 3001 | Seeker, Single Spectral IR |
| 3002 | Seeker, Dual Spectral IR |
| 3003 | Seeker, Imaging IR (IIR) / Focal Plane Array Seeker |

### EnumSensorRole

**行数**: 302  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |
| Comment | TEXT | 是 | - | - |

**枚举值** (302 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Radar, Air Search, 2D Long-Range |
| 2002 | Radar, Air Search, 3D Long-Range |
| 2003 | Radar, Air Search, 2D Medium-Range |
| 2004 | Radar, Air Search, 3D Medium-Range |
| 2005 | Radar, Air Search, 2D Short-Range |
| 2006 | Radar, Air Search, 3D Short-Range |
| 2011 | Radar, Air & Surface Search, 2D Long-Range |
| 2012 | Radar, Air & Surface Search, 3D Long-Range |
| 2013 | Radar, Air & Surface Search, 2D Medium-Range |
| 2014 | Radar, Air & Surface Search, 3D Medium-Range |
| 2015 | Radar, Air & Surface Search, 2D Short-Range |
| 2016 | Radar, Air & Surface Search, 3D Short-Range |
| 2017 | Radar, Height-Finder, Long-Range |
| 2018 | Radar, Height-Finder, Medium-Range |
| 2019 | Radar, Height-Finder, Short-Range |
| 2021 | Radar, Surface Search, Long-Range |
| 2022 | Radar, Surface Search, Medium-Range |
| 2023 | Radar, Surface Search, Short-Range |
| 2027 | Radar, Surface Search w/ OTH |
| 2028 | Radar, Surface Search & Navigation |
| 2029 | Radar, Periscope Search |
| 2031 | Radar, Navigation |
| 2032 | Radar, Ground Mapping |
| 2033 | TFR, Terrain Following Radar |
| 2034 | Radar, Weather |
| 2035 | Radar, Weather and Navigation |
| 2036 | Radar, Terrain Avoidance |
| 2039 | Radar, Bomb Scoring Radar |
| 2041 | TWR, Tail Warning Radar & Tail Gun Director |
| 2042 | TWR, Tail Warning Radar |
| 2049 | Radar, Missile Approach Warning System (MAWS) |
| 2051 | SLAR, Side-Looking Airborne Radar |
| 2101 | Radar, Target Indicator, 2D Surface-to-Air |
| 2102 | Radar, Target Indicator, 3D Surface-to-Air |
| 2103 | Radar, Target Indicator, 2D Surface-to-Air & Surface-to-Surface |
| 2104 | Radar, Target Indicator, 3D Surface-to-Air & Surface-to-Surface |
| 2105 | Radar, Target Indicator, Surf-to-Surf |
| 2109 | Radar, Counter-Battery |
| 2111 | Radar, FCR, Air-to-Air, Long-Range |
| 2112 | Radar, FCR, Air-to-Air, Medium-Range |
| 2113 | Radar, FCR, Air-to-Air, Short-Range |
| 2121 | Radar, FCR, Air-to-Air & Air-to-Surface, Long-Range |
| 2122 | Radar, FCR, Air-to-Air & Air-to-Surface, Medium-Range |
| 2123 | Radar, FCR, Air-to-Air & Air-to-Surface, Short-Range |
| 2124 | Radar, FCR, Air-to-Surface, Long-Range |
| 2125 | Radar, FCR, Air-to-Surface, Medium-Range |
| 2126 | Radar, FCR, Air-to-Surface, Short-Range |
| 2131 | Radar, FCR, Surface-to-Air, Long-Range |
| 2132 | Radar, FCR, Surface-to-Air, Medium-Range |

_... 共 302 个值_

### EnumSensorType

**行数**: 43  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (43 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Radar |
| 2002 | Semi-Active |
| 2003 | Visual |
| 2004 | Infrared |
| 2005 | Track-Via-Missile (TVM) |
| 2006 | Terminal Semi-Active |
| 3001 | ESM |
| 3002 | ECM |
| 3003 | EMP Projector |
| 3004 | Passive Coherent Location System |
| 4001 | Laser Designator |
| 4002 | Laser Spot Tracker (LST) |
| 4003 | Laser Rangefinder |
| 4101 | LIDAR |
| 5001 | Hull Sonar, Passive-Only |
| 5002 | Hull Sonar, Active/Passive |
| 5003 | Hull Sonar, Active-Only |
| 5004 | Bow Sonar, Active/Passive |
| 5011 | TASS, Passive-Only Towed Array Sonar System |
| 5012 | TASS, Active/Passive Towed Array Sonar System |
| 5013 | TASS, Active Towed Array Sonar System |
| 5021 | VDS, Passive Only Sonar |
| 5022 | VDS, Active/Passive Sonar |
| 5023 | VDS, Active Only Sonar |
| 5031 | Dipping Sonar, Passive-Only |
| 5032 | Dipping Sonar, Active/Passive |
| 5033 | Dipping Sonar, Active-Only |
| 5041 | Bottom Fixed Sonar, Passive-Only |
| 5101 | MAD |
| 5601 | Wake Detector |
| 5901 | Acoustic Intercept (Active Sonar Warning) |
| 6001 | Mine Sweep, Mechanical Cable Cutter |
| 6002 | Mine Sweep, Magnetic Influence |
| 6003 | Mine Sweep, Acoustic Influence |
| 6004 | Mine Sweep, Magnetic & Acoustic Multi-Influence |
| 6011 | Mine Sweep, Two-Ship Magnetic Influence |
| 6021 | Mine Neutralization, Moored Mine Cable Cutter |
| 6022 | Mine Neutralization, Explosive Charge Mine Disposal |
| 6031 | Mine Neutralization, Diver-deployed Explosive Charge |
| 7001 | Microwave Emitter |
| 8001 | Non-Detecting Emitter |
| 9001 | Sensor Group |

### EnumShipCSGen

**行数**: 10  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |
| Example | TEXT | 是 | - | - |
| YearStart | INTEGER | 是 | - | - |
| YearEnd | INTEGER | 是 | - | - |
| Architecture | TEXT | 是 | - | - |
| OODADetectionCycle | INTEGER | 是 | 0 | - |
| OODATargetingCycle | INTEGER | 是 | 0 | - |
| OODAEvasiveCycle | INTEGER | 是 | 0 | - |
| TrackCap | INTEGER | 是 | 0 | - |

**枚举值** (10 个):

| ID | 描述 |
|-----|------|
| 0 | Undefined (Use Below) |
| 1000 | None (Small Craft) |
| 1001 | None (Large Vessel) |
| 1100 | CS Gen 1 (1945-1950) |
| 1200 | CS Gen 2 (1951-1960) |
| 1300 | CS Gen 3 (1961-1970) |
| 1400 | CS Gen 4 (1971-1985) |
| 1500 | CS Gen 5 (1986-2000) |
| 1600 | CS Gen 6 (2001-2029) |
| 1700 | CS Gen 7 (2030+) |

### EnumShipCategory

**行数**: 9  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (9 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Carrier (Aviation Ship) |
| 2002 | Surface Combatant |
| 2003 | Amphibious |
| 2004 | Auxiliary |
| 2005 | Merchant |
| 2006 | Civilian |
| 2007 | Surface Combatant (Aviation Capable) |
| 2008 | Mobile Offshore Base (Aviation Capable) |

### EnumShipCode

**行数**: 60  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (60 个):

| ID | 描述 |
|-----|------|
| 1002 | Nuclear Shock Resistant |
| 1011 | Prairie Masker |
| 1012 | Advanced Quieting |
| 1013 | Waterjet Propulsion |
| 2001 | Helo In-Flight Refuel Capable (HIFR) |
| 2101 | Can Deploy Amphibious Vehicles From Cargo |
| 3001 | Passive or Single Stabilizers |
| 3002 | Dual or Triple Stabilizers |
| 3003 | Has Lateral Thrusters |
| 4001 | Low Construction Standards (-40% DP Penalty) |
| 4002 | All Aluminum Construction (-30% DP Penalty) |
| 4003 | Aluminum Superstructure Only (-20% DP Penalty) |
| 4006 | Wooden Hull Construction (-30% DP Penalty) |
| 4007 | Glass Reinforced Polyester (GRP) Construction (-20% DP Penalty) |
| 4011 | Hovercraft/SES (-40% DP Penalty) |
| 4012 | Catamaran/Trimaran Multihull (-30% DP Penalty) |
| 4020 | Laid Down Before 1930 (-20% DP Penalty) |
| 4022 | Built to Mercantile Standards (-30% DP Penalty) |
| 6001 | Degaussed Steel Hull |
| 6002 | Onboard Degaussing Gear (Magnetometer) [Minesweeper] |
| 6003 | Wooden Hull [Minesweeper] |
| 6004 | Glass Reinforced Polyester (GRP) Hull [Minesweeper] |
| 8001 | Refuel to Port x 1 (Out) |
| 8002 | Refuel to Port x 2 (Out) |
| 8003 | Refuel to Port x 3 (Out) |
| 8004 | Refuel to Port x 4 (Out) |
| 8005 | Refuel to Starboard x 1 (Out) |
| 8006 | Refuel to Starboard x 2 (Out) |
| 8007 | Refuel to Starboard x 3 (Out) |
| 8008 | Refuel to Starboard x 4 (Out) |
| 8011 | Refuel to Astern x 1 (Out) |
| 8012 | Refuel to Astern x 2 (Out) |
| 8101 | Refuel from Port x 1 (In) |
| 8102 | Refuel from Port x 2 (In) |
| 8103 | Refuel from Port x 3 (In) |
| 8104 | Refuel from Port x 4 (In) |
| 8105 | Refuel from Port x 5 (In) |
| 8106 | Refuel from Starboard x 1 (In) |
| 8107 | Refuel from Starboard x 2 (In) |
| 8108 | Refuel from Starboard x 3 (In) |
| 8109 | Refuel from Starboard x 4 (In) |
| 8110 | Refuel from Starboard x 5 (In) |
| 8111 | Refuel from Astern x 1 (In) |
| 8112 | Refuel from Astern x 2 (In) |
| 9001 | Replenish to Port x 1 (Out) |
| 9002 | Replenish to Port x 2 (Out) |
| 9003 | Replenish to Port x 3 (Out) |
| 9004 | Replenish to Port x 4 (Out) |
| 9005 | Replenish to Starboard x 1 (Out) |
| 9006 | Replenish to Starboard x 2 (Out) |

_... 共 60 个值_

### EnumShipPhysicalSize

**行数**: 11  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (11 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Very Small Pier (0-11m Long) |
| 2002 | Small Pier (11.1-17m Long) |
| 2003 | Medium Pier (17.1-25m Long) |
| 2004 | Large Pier (25.1-45m Long) |
| 2005 | Very Large Pier (45.1-200m) |
| 2006 | Extra Large Pier (200.1m-500m) |
| 3001 | Very Small Dock/Davit (0-11m Long) |
| 3002 | Small Dock/Davit (LCVP, 11.1-17m Long) |
| 3003 | Medium Dock (LCM, 17.1-25m Long) |
| 3004 | Large Dock (LCU/LCAC, 25.1-45m Long) |

### EnumShipType

**行数**: 181  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |
| YearStart | INTEGER | 是 | - | - |
| YearEnd | INTEGER | 是 | - | - |

**枚举值** (181 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | CV - Aircraft Carrier |
| 2002 | CVA - Attack Carrier |
| 2003 | CVB - Large Aircraft Carrier |
| 2004 | CVE - Escort Aircraft Carrier |
| 2005 | CVGH - Guided Missile Helicopter Carrier |
| 2006 | CVH - Helicopter Carrier |
| 2007 | CVL - Light Aircraft Carrier |
| 2008 | CVN - Nuclear Powered Aircraft Carrier |
| 2009 | CVS - Seaplane Carrier |
| 2010 | CVS - Anti-Submarine Aircraft Carrier |
| 2011 | AVT - Training Carrier |
| 3001 | B - Battleship |
| 3002 | BB - Battleship |
| 3003 | BBC - Command Battleship |
| 3004 | BBG - Guided Missile Battleship  |
| 3005 | BBH - Helicopter Battleship |
| 3006 | BCGN - Nuclear Powered Guided Missile Battle Cruiser |
| 3007 | BM - Monitor |
| 3101 | C - Cruiser |
| 3102 | CA - Heavy Cruiser |
| 3103 | CAG - Heavy Guided Missile Cruiser |
| 3104 | CB - Large Cruiser |
| 3105 | CBG - Large Guided Missile Cruiser |
| 3106 | CG - Guided Missile Cruiser |
| 3107 | CGH - Guided Missile Helicopter Cruiser |
| 3108 | CGN - Nuclear Powered Guided Missile Cruiser |
| 3109 | CL - Light Cruiser |
| 3110 | CLAA - Light Anti-Aircraft Cruiser |
| 3111 | CLC - Light Command Cruiser |
| 3112 | CLG - Light Guided Missile Cruiser |
| 3113 | CLH - Light Helicopter Cruiser |
| 3114 | CS - Scout Cruiser |
| 3201 | D - Destroyer |
| 3202 | DD - Destroyer |
| 3203 | DDG - Guided Missile Destroyer |
| 3204 | DDH - Helicopter Destroyer |
| 3205 | DDK - ASW Submarine Killer Destroyer |
| 3206 | DDR - Radar Picket Destroyer |
| 3207 | DE - Destroyer Escort |
| 3208 | DEG - Guided Missile Destroyer Escort |
| 3209 | DER - Radar Picket Destroyer Escort |
| 3210 | DL - Destroyer |
| 3211 | DLG - Guided Missile Destroyer |
| 3212 | DM - Destroyer Minelayer (converted destroyer)  |
| 3301 | F - Frigate |
| 3302 | FF - Frigate |
| 3303 | FFG - Guided Missile Frigate |
| 3304 | FFL - Corvette |
| 3305 | PF - Patrol Frigate |

_... 共 181 个值_

### EnumSignatureType

**行数**: 11  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (11 个):

| ID | 描述 |
|-----|------|
| 1001 | Passive Sonar, VLF (0-1000 Hz, 200 Hz Center Frequency) |
| 1002 | Passive Sonar, LF (1-5 KHz, 3 KHz Center Frequency) |
| 1003 | Passive Sonar, MF (5-10 KHz, 7.5 KHz Center Frequency) |
| 1004 | Passive Sonar, HF (10-500 KHz, 20 KHz Center Frequency) |
| 2001 | Active Sonar, VLF-HF (0-500 KHz) |
| 3001 | Visual Detection Range |
| 3002 | Visual Classification Range |
| 4001 | Infrared Detection Range |
| 4002 | Infrared Classification Range |
| 5001 | Radar, A-D Band (30-2000 MHz) |
| 5002 | Radar, E-M Band (2-100 GHz) |

### EnumSubmarineCSGen

**行数**: 8  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |
| Example | TEXT | 是 | - | - |
| YearStart | INTEGER | 是 | - | - |
| YearEnd | INTEGER | 是 | - | - |
| OODADetectionCycle | INTEGER | 是 | 0 | - |
| OODATargetingCycle | INTEGER | 是 | 0 | - |
| OODAEvasiveCycle | INTEGER | 是 | 0 | - |
| Architecture | TEXT | 是 | - | - |

**枚举值** (8 个):

| ID | 描述 |
|-----|------|
| 0 | Undefined (Use Below) |
| 1000 | None |
| 1100 | CS Gen 1 (1940-1960) |
| 1200 | CS Gen 2 (1961-1965) |
| 1300 | CS Gen 3 (1966-1980) |
| 1400 | CS Gen 4 (1981-2000) |
| 1500 | CS Gen 5 (2001-2029) |
| 1600 | CS Gen 6 (2030+) |

### EnumSubmarineCategory

**行数**: 4  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (4 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Submarine |
| 2002 | Biologics |
| 2003 | False Target |

### EnumSubmarineCode

**行数**: 13  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (13 个):

| ID | 描述 |
|-----|------|
| 1002 | Nonmagnetic Hull |
| 1003 | No Launch Transient |
| 1004 | Shrouded Propulsor |
| 1005 | Advanced Propulsor |
| 2001 | Double Hull |
| 2002 | Shock Resistant |
| 3003 | Has Lateral Thrusters |
| 4001 | Low Construction Standards (-40% DP Penalty) |
| 4002 | Titanium Hull (+20% DP) |
| 4003 | Laid Down Before 1930 (-20% DP Penalty) |
| 4004 | Double Hull (+20% DP) |
| 5001 | Lithium-Ion Batteries |
| 9001 | Snorkel |

### EnumSubmarinePhysicalSize

**行数**: 9  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (9 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Very Small Pier (0-11m Long) |
| 2002 | Small Pier (11.1-17m Long) |
| 2003 | Medium Pier (17.1-25m Long) |
| 2004 | Large Pier (25.1-45m Long) |
| 2005 | Very Large Pier (45.1-200m) |
| 2006 | Extra Large Pier (200m-500m) |
| 4001 | Dry-Deck Shelter (DDS) |
| 5001 | ROV/UUV |

### EnumSubmarineType

**行数**: 21  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (21 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 1900 | SSQ - Auxillary Submarine, Communications |
| 2001 | AGSS - Auxilary/Experimental Submarine  |
| 2002 | APSS - Auxiliary Cargo Submarine |
| 2003 | SS - Attack/Fleet Submarine  |
| 2004 | SSB - Ballistic Missile Submarine |
| 2005 | SSBN - Nuclear Powered Ballistic Missile Submarine |
| 2006 | SSG - Guided Missile Attack Submarine |
| 2007 | SSGN - Nuclear Powered Guided Missile Attack Submarine |
| 2008 | SSK - Hunter-Killer Submarine  |
| 2009 | SSM - Midget Submarine  |
| 2010 | SSN - Nuclear Powered Attack Submarine |
| 2011 | SSP - Transport Submarine  |
| 2012 | SSR - Radar Picket Submarine  |
| 2013 | SSRN - Nuclear Powered Radar Picket Submarine |
| 3001 | SDV - Swimmer Delivery Vehicle |
| 4001 | ROV - Remotely Operated Vehicle |
| 4002 | UUV - Unmanned Underwater Vehicle |
| 4003 | Unmanned Underwater Glider |
| 9001 | Biologics |
| 9002 | False Target |

### EnumWarheadCaliber

**行数**: 17  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (17 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Gun 6-15mm |
| 2002 | Gun 16-24mm |
| 2003 | Gun 25-60mm |
| 2004 | Gun 61-80mm |
| 2005 | Gun 81-150mm |
| 2006 | Gun 151-200mm |
| 2007 | Gun 201-350mm |
| 2008 | Gun 351-450mm |
| 3001 | Rocket 6-15mm |
| 3002 | Rocket 16-24mm |
| 3003 | Rocket 25-60mm |
| 3004 | Rocket 61-80mm |
| 3005 | Rocket 81-150mm |
| 3006 | Rocket 151-200mm |
| 3007 | Rocket 201-350mm |
| 3008 | Rocket 351-450mm |

### EnumWarheadExplosivesType

**行数**: 62  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |
| TNTEquivalent | DOUBLE | 是 | 0 | - |
| Comment | TEXT | 是 | - | - |

**枚举值** (62 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | HE [kg], TNT (Trinitrotoluene) |
| 2002 | HE [kg], HMX |
| 2003 | HE [kg], PETN (Pentrite) |
| 2004 | HE [kg], RDX (Cyclonite / Hexogen / C4) |
| 2005 | HE [kg], C4 |
| 2006 | HE [kg], Tritonal |
| 2007 | HE [kg], Ammonium Nitrate (Ammonite) |
| 2008 | HE [kg], Picric Acid / Trinitrophenol / Type 97 (Pertit / Pikrinit / Melinit / Ekrasit / Shimose) |
| 2009 | HE [kg], Torpex |
| 2010 | HE [kg], Dynamite |
| 2011 | HE [kg], PBXN-1XX |
| 2012 | HE [kg], AFX-757 |
| 2013 | HE [kg], Minol-2 |
| 2014 | HE [kg], H-6 |
| 2015 | HE [kg], Destex |
| 2016 | HE [kg], Minol-1 |
| 2017 | HE [kg], HBX-1 |
| 2018 | HE [kg], HBX-3 |
| 2019 | HE [kg], Hexanite |
| 2020 | HE [kg], Dipicrylamine / Hexyl (Hexamine / Hexite / Hexanitrodiphenylamine) |
| 2021 | HE [kg], Minol-3 |
| 2022 | HE [kg], Minol-4 |
| 2023 | HE [kg], PBX |
| 2024 | HE [kg], Comp B |
| 2101 | Incendiary [kg], Napalm |
| 2102 | Incendiary [kg], WP |
| 2103 | Incendiary [kg], FAE |
| 2201 | HEAT Shaped Charge, Light Armor (41-90mm) |
| 2202 | HEAT Shaped Charge, Medium Armor (91-140mm) |
| 2203 | HEAT Shaped Charge, Heavy Armor (141-200mm) |
| 2204 | HEAT Shaped Charge, Special Armor (201-500mm) |
| 2301 | Fragmentation [kg], Prefragmented |
| 2311 | Enhanced Armor-Piercing Fragmentation [kg], Light Armor (41-90mm) |
| 2312 | Enhanced Armor-Piercing Fragmentation [kg], Medium Armor (91-140mm) |
| 2313 | Enhanced Armor-Piercing Fragmentation [kg], Heavy Armor (141-200mm) |
| 2314 | Enhanced Armor-Piercing Fragmentation [kg], Special Armor (201-500mm) |
| 2401 | Continuous Rod [kg] |
| 4001 | Nuclear [kT] |
| 4011 | Chemical [kg] |
| 4012 | Bacteriological [kg] |
| 6001 | Submunitions [kg], Anti-Personnel (Fragmentation) |
| 6002 | Submunitions [kg], Anti-Tank, Light Armor (41-90mm) |
| 6003 | Submunitions [kg], Anti-Tank, Medium Armor (91-140mm) |
| 6004 | Submunitions [kg], Anti-Tank, Heavy Armor (141-200mm) |
| 6005 | Submunitions [kg], Anti-Tank, Special Armor (201-500mm) |
| 6011 | Submunitions [kg], Anti-Runway (Penetrator) |
| 7011 | Mine [kg], Anti-Personnel (Fragmentation) |
| 7012 | Mine [kg], Anti-Tank, Light Armor (41-90mm) |
| 7013 | Mine [kg], Anti-Tank, Medium Armor (91-140mm) |

_... 共 62 个值_

### EnumWarheadType

**行数**: 41  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (41 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | High Explosive (HE) Blast / Frag |
| 2002 | Armor-Piercing (AP) |
| 2003 | High Explosive Anti-Tank (HEAT) Shaped Charge |
| 2004 | Incendiary (Napalm, WP) |
| 2005 | Fragmentation |
| 2006 | Semi Armor-Piercing (SAP) |
| 2007 | High Explosive Splash Head (HESH) |
| 2008 | Continuous Rod |
| 2009 | Hard Target Penetrator (HTP) |
| 2010 | Fuel-Air Explosive (FAE / Thermobaric) |
| 2011 | Enhanced Armor-Piercing Fragmentation |
| 2012 | Fragmentation - ABM-Optimized |
| 3001 | Torpedo |
| 3002 | Depth Charge |
| 3003 | Torpedo, ASW Optimized |
| 4001 | Nuclear |
| 4011 | Chemical |
| 4021 | Bacteriological |
| 4031 | Microwave |
| 5002 | Weapon (DP=Weapon ID) |
| 5003 | Aircraft (DP=Aircraft ID) |
| 5004 | Ship (DP=Ship DBID) |
| 5005 | Submarine (DP=Submarine DBID) |
| 5006 | Ground Unit (DP=Unit DBID) |
| 5007 | Satellite (DP=Satellite DBID) |
| 6001 | Cluster Bomb, Anti-Personnel (Fragmentation) |
| 6002 | Cluster Bomb, Anti-Tank (Shaped Charge) |
| 6003 | Cluster Bomb, Anti-Runway (Penetrator) |
| 6012 | Cluster Bomb, Guided Submunitions, Anti-Tank (Shaped Charge) |
| 7001 | Mine, Anti-Personnel (Fragmentation) |
| 7002 | Mine, Anti-Tank (Shaped Charge) |
| 8001 | Long Rod Penetrator (APDS / APFSDS) |
| 9001 | Anti-Electrical |
| 9002 | Leaflet Dispensing |
| 9101 | COIL Laser |
| 9102 | Carbon Dioxide Laser |
| 9103 | Deuterium Fluoride Laser |
| 9104 | Solid-State Laser (Fiber) |
| 9201 | EMP - Directed |
| 9202 | EMP - Omnidirectional |

### EnumWeaponCode

**行数**: 80  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (80 个):

| ID | 描述 |
|-----|------|
| 1001 | Illuminate at Launch |
| 1002 | Terminal Illumination |
| 1003 | Supports Buddy Illumination |
| 1101 | Home On Jam (HOJ) |
| 2001 | Anti-Air Stern Chase |
| 2002 | Anti-Air Rear-Aspect |
| 2003 | Anti-Air All-Aspect |
| 2004 | Anti-Air Dogfight (High Off-Boresight) |
| 2005 | No Diving Target Mod |
| 2006 | Capable vs Seaskimmer |
| 2007 | ARH AAW - No HQ Track Required |
| 2009 | Counter- Rocket, Arty, Mortar (C-RAM) Capable |
| 2010 | Lock-On After Launch (LOAL) - CEC-Capable |
| 2011 | Flight Profile - Terrain Following |
| 2012 | Lock-On After Launch (LOAL) |
| 2025 | Launcher occupied during guidance |
| 3001 | ARM Target Memory |
| 3003 | Loiter Capability |
| 3004 | Loiter Capability (Parachute) |
| 4001 | Search Pattern |
| 4002 | Drive-Through Logic |
| 4003 | Bearing-Only Launch (BOL) |
| 4008 | Depressed Ballistic Trajectory (Iskander, ATACMS, etc.) |
| 4010 | Ballistic Trajectory (Ballistic Missile, GMLRS, etc.) |
| 4012 | Multi-Stage Missile |
| 6001 | Pod - Terrain Avoidance (Land: 300ft [91.4m], Sea: 200ft [60.9m]) |
| 6002 | Pod - Terrain Following (Land: 200ft [60.9m], Sea: 100ft [30.5m]) |
| 6009 | Pod - Day-Only Navigation |
| 6010 | Pod - Day-Only Navigation/Attack |
| 6011 | Pod - Night Navigation (Ferry, Air-to-Air, Air-to-Surface Missiles) |
| 6012 | Pod - Night Navigation/Attack (Incl. Bomb, Rocket Delivery) |
| 6021 | Pod - Recon, Day-Only |
| 6022 | Pod - Recon, Night Capable |
| 6101 | Weapon - INS Navigation |
| 6102 | Weapon - INS w/ GNSS Navigation |
| 6103 | Weapon - TERCOM Navigation |
| 6111 | Weapon - Pre-Briefed Target Only |
| 6112 | Weapon - Can Target Specific Subsystems |
| 6121 | Terminal Maneuver - Pop-Up |
| 6122 | Terminal Maneuver - Zig-Zag |
| 6123 | Terminal Maneuver - Random (Advanced) |
| 6129 | Re-Attack Capability |
| 6130 | Weapon Altitude Control Possible |
| 6131 | Attitude Control - Aerodynamic Only |
| 6132 | Attitude Control - Non-Aerodynamic Only |
| 6133 | Attitude Control - Combined |
| 6140 | Uses GPS |
| 6141 | Uses GLONASS |
| 6142 | Uses BeiDou/COMPASS |
| 6143 | Uses NavIC/IRNSS |

_... 共 80 个值_

### EnumWeaponGeneration

**行数**: 19  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (19 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 1002 | Not Applicable (N/A) |
| 2001 | Early 1950s |
| 2002 | Late 1950s |
| 2003 | Early 1960s |
| 2004 | Late 1960s |
| 2005 | Early 1970s |
| 2006 | Late 1970s |
| 2007 | Early 1980s |
| 2008 | Late 1980s |
| 2009 | Early 1990s |
| 2010 | Late 1990s |
| 2011 | Early 2000s |
| 2012 | Late 2000s |
| 2013 | Early 2010s |
| 2014 | Late 2010s |
| 2015 | Early 2020s |
| 3001 | Single Spectral IR Decoy |
| 3002 | Dual Spectral IR Decoy |

### EnumWeaponImpactType

**行数**: 4  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (4 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Airburst |
| 2002 | Contact |
| 2003 | Penetrator |

### EnumWeaponProfileAttack

**行数**: 2  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (2 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 9999 | *DO NOT USE YET* |

### EnumWeaponProfileCruise

**行数**: 2  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (2 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 9999 | *DO NOT USE YET* |

### EnumWeaponTarget

**行数**: 18  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (18 个):

| ID | 描述 |
|-----|------|
| 1001 | Aircraft |
| 1002 | Helicopter |
| 1003 | Missile |
| 1004 | Satellite |
| 1005 | C-RAM (Counter Rocket, Artillery and Mortar) |
| 2001 | Surface Vessel |
| 2002 | Submarine |
| 2003 | Mine |
| 2004 | Torpedo |
| 3001 | Land Structure - Soft |
| 3002 | Land Structure - Hardened |
| 3003 | Runway |
| 3004 | Radar |
| 4001 | Mobile Target - Soft |
| 4002 | Mobile Target - Hardened |
| 4003 | Mobile Target - Personnel |
| 5001 | Underwater Structure |
| 9001 | Air Base |

### EnumWeaponType

**行数**: 48  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (48 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 2001 | Guided Weapon |
| 2002 | Rocket |
| 2003 | Bomb |
| 2004 | Gun |
| 2005 | Decoy (Expendable) |
| 2006 | Decoy (Towed) |
| 2007 | Decoy (Vehicle) |
| 2008 | Training Round |
| 2009 | Dispenser |
| 2010 | Contact Bomb - Suicide |
| 2011 | Contact Bomb - Sabotage |
| 2012 | Guided Projectile |
| 2013 | Small Arms |
| 2014 | UAV (Expendable) |
| 3001 | Sensor Pod |
| 3002 | Drop Tank |
| 3003 | Buddy Store |
| 3004 | Ferry Tank |
| 4001 | Torpedo |
| 4002 | Depth Charge |
| 4003 | Sonobuoy |
| 4004 | Bottom Mine |
| 4005 | Moored Mine |
| 4006 | Floating Mine |
| 4007 | Moving Mine |
| 4008 | Rising Mine |
| 4009 | Drifting Mine |
| 4010 | Attached Mine |
| 4011 | Dummy Mine |
| 4012 | Guided Depth Charge |
| 4101 | Helicopter-Towed Package |
| 4102 | Aircraft |
| 4103 | Ship |
| 4104 | Submarine |
| 4105 | Satellite |
| 4106 | Ground Unit |
| 5001 | RV / MRV/ MIRV |
| 5002 | Pallet Munition |
| 6001 | Laser |
| 6002 | Microwave |
| 6003 | Laser Dazzler |
| 8001 | Hypersonic Glide Vehicle |
| 8002 | Glide Vehicle |
| 8003 | Hypersonic Cruise Missile |
| 9001 | Cargo |
| 9002 | Troops |
| 9003 | Paratroops |

### EnumWeaponWRA

**行数**: 93  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (93 个):

| ID | 描述 |
|-----|------|
| 1001 | None |
| 1999 | Air Contact Unknown |
| 2000 | Aircraft - Unspecified |
| 2001 | Aircraft - 5th Generation Fighter/Attack [Agility/Gen: 5.0+] (F-22, Eurofighter, Rafale) |
| 2002 | Aircraft - 4th Generation Fighter/Attack [Agility/Gen: 4.0-4.9] (F-14, F-15, F-16, MiG-29, Su-27) |
| 2003 | Aircraft - 3rd Generation Fighter/Attack [Agility/Gen: 3.0-3.9] (F-4, F-5, MiG-21, MiG-23) |
| 2004 | Aircraft - Less Capable Fighter/Attack [Agility: 2.0-2.9] (F-111, Lightning, Su-7, MiG-17) |
| 2011 | Aircraft - High-performance Bombers [Agility: 2.0+] (B-1B, B-2A, Tu-22M |
| 2012 | Aircraft - Medium-performance Bombers [Agility: 1.5-1.9] (B-52, Vulcan, Tu-16) |
| 2013 | Aircraft - Low-performance Bombers [Agility: 1.0-1.4] (B-24, Canberra, Tu-95, Bison) |
| 2021 | Aircraft - High-Performance Reconnaissance and Electronic Warfare [Agility: 4.0+] |
| 2022 | Aircraft - Medium-Performance Reconnaissance and Electronic Warfare [Agility: 3.0-3.9] |
| 2023 | Aircraft - Low-Performance Reconnaissance and Electronic Warfare [Agility: 2.0-2.9] |
| 2031 | Aircraft - Airborne Early Warning and Control |
| 2032 | Aircraft - Micro-UAV |
| 2100 | Helicopter - Unspecified |
| 2200 | Guided Weapon - Unspecified |
| 2201 | Guided Weapon - Supersonic Sea-Skimming |
| 2202 | Guided Weapon - Subsonic Sea-Skimming |
| 2203 | Guided Weapon - Supersonic |
| 2204 | Guided Weapon - Subsonic |
| 2211 | Guided Weapon - Ballistic |
| 2300 | Satellite - Unspecified |
| 2400 | C-RAM (Counter Rocket, Artillery and Mortar) |
| 2999 | Surface Contact - Unknown Type |
| 3000 | Ship - Unspecified |
| 3001 | Ship - Carrier, 0-25000 tons |
| 3002 | Ship - Carrier, 25001-45000 tons |
| 3003 | Ship - Carrier, 45001-95000 tons |
| 3004 | Ship - Carrier, 95000+ tons |
| 3101 | Ship - Surface Combatant, 0-500 tons |
| 3102 | Ship - Surface Combatant, 501-1500 tons, plus Missile Boats with smaller displacement |
| 3103 | Ship - Surface Combatant, 1501-5000 tons, plus Frigates and Corvettes with smaller displacement |
| 3104 | Ship - Surface Combatant, 5001-10000 tons, plus Destroyers with smaller displacement |
| 3105 | Ship - Surface Combatant, 10001-25000 tons, plus Cruisers with smaller displacement |
| 3106 | Ship - Surface Combatant, 25001-45000 tons |
| 3107 | Ship - Surface Combatant, 45001-95000 tons |
| 3108 | Ship - Surface Combatant, 95000+ tons |
| 3201 | Ship - Amphibious, 0-500 tons |
| 3202 | Ship - Amphibious, 501-1500 tons |
| 3203 | Ship - Amphibious, 1501-5000 tons |
| 3204 | Ship - Amphibious, 5001-10000 tons |
| 3205 | Ship - Amphibious, 10001-25000 tons |
| 3206 | Ship - Amphibious, 25001-45000 tons |
| 3207 | Ship - Amphibious, 45001-95000 tons |
| 3208 | Ship - Amphibious, 95000+ tons |
| 3301 | Ship - Auxiliary, 0-500 tons |
| 3302 | Ship - Auxiliary, 501-1500 tons |
| 3303 | Ship - Auxiliary, 1501-5000 tons |
| 3304 | Ship - Auxiliary, 5001-10000 tons |

_... 共 93 个值_

### EnumWeaponWRAAutoFireRange

**行数**: 5  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 否 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (5 个):

| ID | 描述 |
|-----|------|
| -99 | Max range |
| 0 | No automatic fire |
| 25 | 25% |
| 50 | 50% |
| 75 | 75% |

### EnumWeaponWRASelfDefenceRange

**行数**: 13  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (13 个):

| ID | 描述 |
|-----|------|
| -99 | Maximum range |
| 0 | Do not use weapon in self defence |
| 1 | 1 nm |
| 2 | 2 nm |
| 3 | 3 nm |
| 4 | 4 nm |
| 5 | 5 nm |
| 6 | 6 nm |
| 7 | 7 nm |
| 8 | 8 nm |
| 9 | 9 nm |
| 10 | 10 nm |
| 15 | 15 nm |

### EnumWeaponWRAShooterQty

**行数**: 4  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (4 个):

| ID | 描述 |
|-----|------|
| -99 | Any number of units, enough to fill weapon qty requirement |
| 1 | 1 unit |
| 2 | 2 units |
| 4 | 4 units |

### EnumWeaponWRAWeaponQty

**行数**: 15  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | - | ✓ |
| Description | TEXT | 是 | - | - |

**枚举值** (15 个):

| ID | 描述 |
|-----|------|
| -99 | Use all weapons against target |
| -6 | Use 1/4 the target's Missile Defence value (typical for heavy supersonic weapons like AS-4, SS-N-19) |
| -5 | Use 1/2 the target's Missile Defence value (typical for smaller supersonic weapons like SS-N-26) |
| -4 | Use four times the target's Missile Defence value |
| -3 | Use twice as many weapons as the target's Missile Defence value |
| -2 | Use target's Missile Defence value |
| 0 | Do not use weapon against this target type |
| 1 | 1 rnd |
| 2 | 2 rnds |
| 3 | 3 rnds |
| 4 | 4 rnds |
| 5 | 5 rnds |
| 6 | 6 rnds |
| 7 | 7 rnds |
| 8 | 8 rnds |

### ManagementDatabase

**行数**: 3  
**主键**: ID

| 列名 | 类型 | 可为空 | 默认值 | 主键 |
|------|------|--------|--------|------|
| ID | INTEGER | 是 | 0 | ✓ |
| Description | TEXT | 是 | - | - |
