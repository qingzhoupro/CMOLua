# CMO Lua API 轻量官方索引

> 本文件是日常工作的"默认加载索引"，仅包含每个函数的名称、参数形式和官方 URL。
> 详细参数说明请查阅 `generated/{函数名}.md`（按需加载）。

## Unit 操作
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `ScenEdit_AddUnit` | `表参数` | Unit wrapper / nil | [link](https://commandlua.github.io/assets/Function_ScenEdit_AddUnit.html) |
| `ScenEdit_GetUnit` | `表参数` 或 `位置参数` | Unit wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetUnit.html) |
| `ScenEdit_SetUnit` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetUnit.html) |
| `ScenEdit_UpdateUnit` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_UpdateUnit.html) |
| `ScenEdit_DeleteUnit` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_DeleteUnit.html) |
| `ScenEdit_KillUnit` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_KillUnit.html) |
| `ScenEdit_SetLoadout` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetLoadout.html) |
| `ScenEdit_GetLoadout` | `表参数` | Loadout wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetLoadout.html) |
| `ScenEdit_SetEMCON` | `混合` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetEMCON.html) |
| `ScenEdit_SetDoctrine` | `混合` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetDoctrine.html) |
| `ScenEdit_GetDoctrine` | `表参数` | Doctrine wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetDoctrine.html) |
| `ScenEdit_RefuelUnit` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_RefuelUnit.html) |
| `ScenEdit_AddReloadsToUnit` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_AddReloadsToUnit.html) |
| `ScenEdit_AddWeaponToUnitMagazine` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_AddWeaponToUnitMagazine.html) |
| `ScenEdit_FillMagsForLoadout` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_FillMagsForLoadout.html) |
| `ScenEdit_MergeUnits` | `位置参数` | Unit wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_MergeUnits.html) |
| `ScenEdit_SplitUnit` | `表参数` | table | [link](https://commandlua.github.io/assets/Function_ScenEdit_SplitUnit.html) |
| `ScenEdit_SetUnitSide` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetUnitSide.html) |
| `ScenEdit_SetUnitDamage` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetUnitDamage.html) |
| `ScenEdit_ClearAllAircraft` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_ClearAllAircraft.html) |
| `ScenEdit_ClearAllMagazines` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_ClearAllMagazines.html) |
| `ScenEdit_TransferCargo` | `混合` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_TransferCargo.html) |
| `ScenEdit_UnloadCargo` | `混合` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_UnloadCargo.html) |
| `ScenEdit_UpdateUnitCargo` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_UpdateUnitCargo.html) |
| `ScenEdit_HostUnitToParent` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_HostUnitToParent.html) |
| `ScenEdit_DistributeWeaponAtAirbase` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_DistributeWeaponAtAirbase.html) |

## Mission 操作
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `ScenEdit_AddMission` | `位置参数` | Mission wrapper / nil | [link](https://commandlua.github.io/assets/Function_ScenEdit_AddMission.html) |
| `ScenEdit_GetMission` | `表参数` | Mission wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetMission.html) |
| `ScenEdit_SetMission` | `混合` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetMission.html) |
| `ScenEdit_DeleteMission` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_DeleteMission.html) |
| `ScenEdit_GetMissions` | `位置参数` | table | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetMissions.html) |
| `ScenEdit_AssignUnitToMission` | `混合` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_AssignUnitToMission.html) |
| `ScenEdit_RemoveUnitAsTarget` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_RemoveUnitAsTarget.html) |
| `ScenEdit_AssignUnitAsTarget` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_AssignUnitAsTarget.html) |
| `ScenEdit_CreateMissionFlightPlan` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_CreateMissionFlightPlan.html) |
| `ScenEdit_ExportMission` | `表参数` | string (XML) | [link](https://commandlua.github.io/assets/Function_ScenEdit_ExportMission.html) |
| `ScenEdit_ImportMission` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_ImportMission.html) |

## Side / 阵营操作
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `ScenEdit_AddSide` | `表参数` | Side wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_AddSide.html) |
| `ScenEdit_RemoveSide` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_RemoveSide.html) |
| `ScenEdit_SetSidePosture` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetSidePosture.html) |
| `ScenEdit_GetSidePosture` | `位置参数` | string | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetSidePosture.html) |
| `ScenEdit_SetSideOptions` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetSideOptions.html) |
| `ScenEdit_GetSideOptions` | `位置参数` | table | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetSideOptions.html) |
| `ScenEdit_GetSideIsHuman` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetSideIsHuman.html) |
| `VP_GetSides` | `位置参数` | table | [link](https://commandlua.github.io/assets/Function_VP_GetSides.html) |
| `VP_GetSide` | `表参数` | Side wrapper | [link](https://commandlua.github.io/assets/Function_VP_GetSide.html) |
| `VP_GetUnit` | `表参数` | Contact wrapper | [link](https://commandlua.github.io/assets/Function_VP_GetUnit.html) |
| `VP_GetContact` | `表参数` | Contact wrapper | [link](https://commandlua.github.io/assets/Function_VP_GetContact.html) |
| `VP_GetScenario` | `位置参数` | Scenario wrapper | [link](https://commandlua.github.io/assets/Function_VP_GetScenario.html) |
| `ScenEdit_PlayerSide` | `位置参数` | string | [link](https://commandlua.github.io/assets/Function_ScenEdit_PlayerSide.html) |

## Event / 事件系统
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `ScenEdit_SetEvent` | `混合` | Event wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetEvent.html) |
| `ScenEdit_GetEvent` | `混合` | Event wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetEvent.html) |
| `ScenEdit_GetEvents` | `位置参数` | table | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetEvents.html) |
| `ScenEdit_SetTrigger` | `表参数` | Trigger wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetTrigger.html) |
| `ScenEdit_SetCondition` | `表参数` | Condition wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetCondition.html) |
| `ScenEdit_SetAction` | `表参数` | Action wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetAction.html) |
| `ScenEdit_SetEventTrigger` | `混合` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetEventTrigger.html) |
| `ScenEdit_SetEventCondition` | `混合` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetEventCondition.html) |
| `ScenEdit_SetEventAction` | `混合` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetEventAction.html) |
| `ScenEdit_AddSpecialAction` | `表参数` | SpecialAction wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_AddSpecialAction.html) |
| `ScenEdit_GetSpecialAction` | `混合` | SpecialAction wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetSpecialAction.html) |
| `ScenEdit_ExecuteSpecialAction` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_ExecuteSpecialAction.html) |
| `ScenEdit_ExecuteEventAction` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_ExecuteEventAction.html) |
| `ScenEdit_UnitX` | `位置参数` | Unit wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_UnitX.html) |
| `ScenEdit_UnitC` | `位置参数` | Contact wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_UnitC.html) |
| `ScenEdit_UnitY` | `位置参数` | table | [link](https://commandlua.github.io/assets/Function_ScenEdit_UnitY.html) |
| `ScenEdit_EventX` | `位置参数` | Event wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_EventX.html) |

## Contact / 接触处理
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `ScenEdit_GetContact` | `表参数` | Contact wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetContact.html) |
| `ScenEdit_GetContacts` | `位置参数` | table | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetContacts.html) |
| `ScenEdit_AttackContact` | `混合` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_AttackContact.html) |

## 参考点 / 区域
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `ScenEdit_AddReferencePoint` | `表参数` | ReferencePoint wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_AddReferencePoint.html) |
| `ScenEdit_GetReferencePoint` | `表参数` | ReferencePoint wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetReferencePoint.html) |
| `ScenEdit_GetReferencePoints` | `位置参数` | table | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetReferencePoints.html) |
| `ScenEdit_SetReferencePoint` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetReferencePoint.html) |
| `ScenEdit_DeleteReferencePoint` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_DeleteReferencePoint.html) |
| `ScenEdit_AddZone` | `表参数` | Zone wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_AddZone.html) |
| `ScenEdit_SetZone` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetZone.html) |
| `ScenEdit_RemoveZone` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_RemoveZone.html) |
| `ScenEdit_TransformZone` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_TransformZone.html) |

## Tool / 工具函数
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `Tool_Range` | `位置参数` | number | [link](https://commandlua.github.io/assets/Function_Tool_Range.html) |
| `Tool_Bearing` | `位置参数` | number | [link](https://commandlua.github.io/assets/Function_Tool_Bearing.html) |
| `Tool_LOS` | `混合` | boolean / string | [link](https://commandlua.github.io/assets/Function_Tool_LOS.html) |
| `Tool_LOS_Points` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_Tool_LOS_Points.html) |
| `World_GetPointFromBearing` | `表参数` | table | [link](https://commandlua.github.io/assets/Function_World_GetPointFromBearing.html) |
| `World_GetElevation` | `表参数` | number | [link](https://commandlua.github.io/assets/Function_World_GetElevation.html) |
| `World_GetLocation` | `位置参数` | table | [link](https://commandlua.github.io/assets/Function_World_GetLocation.html) |
| `World_GetCircleFromPoint` | `表参数` | table | [link](https://commandlua.github.io/assets/Function_World_GetCircleFromPoint.html) |

## Scenario / 场景操作
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `GetScenarioTitle` | `位置参数` | string | [link](https://commandlua.github.io/assets/Function_GetScenarioTitle.html) |
| `ScenEdit_CurrentTime` | `位置参数` | string | [link](https://commandlua.github.io/assets/Function_ScenEdit_CurrentTime.html) |
| `ScenEdit_CurrentLocalTime` | `位置参数` | string | [link](https://commandlua.github.io/assets/Function_ScenEdit_CurrentLocalTime.html) |
| `ScenEdit_EndScenario` | `位置参数` | void | [link](https://commandlua.github.io/assets/Function_ScenEdit_EndScenario.html) |
| `ScenEdit_GetScenHasStarted` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetScenHasStarted.html) |
| `ScenEdit_GetWeather` | `位置参数` | table | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetWeather.html) |
| `ScenEdit_SetWeather` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetWeather.html) |
| `ScenEdit_GetScore` | `位置参数` | number | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetScore.html) |
| `ScenEdit_SetScore` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetScore.html) |
| `ScenEdit_GetTimeOfDay` | `位置参数` | string | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetTimeOfDay.html) |
| `ScenEdit_SetStartTime` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetStartTime.html) |
| `ScenEdit_SetTime` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetTime.html) |
| `ScenEdit_GetDateTimeTicks` | `位置参数` | number | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetDateTimeTicks.html) |

## UI
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `ScenEdit_MsgBox` | `位置参数` | number | [link](https://commandlua.github.io/assets/Function_ScenEdit_MsgBox.html) |
| `ScenEdit_InputBox` | `位置参数` | string / nil | [link](https://commandlua.github.io/assets/Function_ScenEdit_InputBox.html) |
| `ScenEdit_SpecialMessage` | `混合` | void | [link](https://commandlua.github.io/assets/Function_ScenEdit_SpecialMessage.html) |
| `UI_SetCameraView` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_UI_SetCameraView.html) |
| `ScenEdit_SelectedUnits` | `位置参数` | table | [link](https://commandlua.github.io/assets/Function_ScenEdit_SelectedUnits.html) |

## Storage / 存储
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `ScenEdit_SetKeyValue` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetKeyValue.html) |
| `ScenEdit_GetKeyValue` | `位置参数` | string / nil | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetKeyValue.html) |
| `ScenEdit_ClearKeyValue` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_ClearKeyValue.html) |

## 水雷
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `ScenEdit_AddMinefield` | `表参数` | Minefield wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_AddMinefield.html) |
| `ScenEdit_DeleteMinefield` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_DeleteMinefield.html) |
| `ScenEdit_GetMinefield` | `表参数` | Minefield wrapper | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetMinefield.html) |
| `ScenEdit_DeleteMine` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_DeleteMine.html) |

## 其他
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `Command_SaveScen` | `位置参数` | string | [link](https://commandlua.github.io/assets/Function_Command_SaveScen.html) |
| `GetBuildNumber` | `位置参数` | number | [link](https://commandlua.github.io/assets/Function_GetBuildNumber.html) |
| `ScenEdit_RunScript` | `位置参数` | void | [link](https://commandlua.github.io/assets/Function_ScenEdit_RunScript.html) |
| `ScenEdit_AddExplosion` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_AddExplosion.html) |
| `ScenEdit_AddCustomLoss` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_AddCustomLoss.html) |
| `SetScenarioTitle` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_SetScenarioTitle.html) |
| `VP_SetTimeCompression` | `位置参数` | void | [link](https://commandlua.github.io/assets/Function_VP_SetTimeCompression.html) |
| `Tool_EmulateNoConsole` | `位置参数` | void | [link](https://commandlua.github.io/assets/Function_Tool_EmulateNoConsole.html) |

## EMCON
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `ScenEdit_ClearAllSideUnitsEmconConfigs` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_ClearAllSideUnitsEmconConfigs.html) |
| `ScenEdit_ClearUnitEmconConfigs` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_ClearUnitEmconConfigs.html) |
| `ScenEdit_GetUnitIntermittentEmissionConfig` | `表参数` | table | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetUnitIntermittentEmissionConfig.html) |
| `ScenEdit_SetSideEmconAlertness` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetSideEmconAlertness.html) |
| `ScenEdit_SetUnitIntermittentEmissionConfig` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetUnitIntermittentEmissionConfig.html) |
| `ScenEdit_SwitchUnitIntermittentEmission` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SwitchUnitIntermittentEmission.html) |
| `ScenEdit_DuplicateEmconConfigToSide` | `位置参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_DuplicateEmconConfigToSide.html) |
| `ScenEdit_DuplicateEmconConfigToUnit` | `混合` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_DuplicateEmconConfigToUnit.html) |

## Doctrine WRA
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `ScenEdit_GetDoctrineWRA` | `表参数` | table | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetDoctrineWRA.html) |
| `ScenEdit_SetDoctrineWRA` | `表参数` | boolean | [link](https://commandlua.github.io/assets/Function_ScenEdit_SetDoctrineWRA.html) |

## Formation
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `ScenEdit_GetFormation` | `混合` | table | [link](https://commandlua.github.io/assets/Function_ScenEdit_GetFormation.html) |

## Weapon Allocation
| 函数 | 参数形式 | 返回值 | 官方 URL |
|------|---------|-------|---------|
| `ScenEdit_WeaponAllocation` | `混合` | table | [link](https://commandlua.github.io/assets/Function_ScenEdit_WeaponAllocation.html) |
