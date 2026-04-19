# CMO Lua 函数总览

## 概述

本文档列出 CMO 中可用的所有 Lua 函数，按功能分类。

## 函数列表

### 单位操作 (Unit)
| 函数 | 说明 |
|------|------|
| `ScenEdit_AddUnit()` | 添加单位 |
| `ScenEdit_GetUnit()` | 获取单位 |
| `ScenEdit_SetUnit()` | 设置单位属性 |
| `ScenEdit_UpdateUnit()` | 更新单位 |
| `ScenEdit_DeleteUnit()` | 删除单位 |
| `ScenEdit_KillUnit()` | 摧毁单位 |
| `ScenEdit_SetLoadout()` | 设置挂载 |
| `ScenEdit_GetLoadout()` | 获取挂载 |
| `ScenEdit_SetEMCON()` | 设置电磁管控 |
| `ScenEdit_SetDoctrine()` | 设置条令 |
| `ScenEdit_GetDoctrine()` | 获取条令 |
| `ScenEdit_RefuelUnit()` | 加油 |
| `ScenEdit_AddWeaponToUnitMagazine()` | 添加武器到弹药库 |
| `ScenEdit_AddReloadsToUnit()` | 添加补给 |

### 任务操作 (Mission)
| 函数 | 说明 |
|------|------|
| `ScenEdit_AddMission()` | 创建任务 |
| `ScenEdit_GetMission()` | 获取任务 |
| `ScenEdit_SetMission()` | 设置任务属性 |
| `ScenEdit_DeleteMission()` | 删除任务 |
| `ScenEdit_AssignUnitToMission()` | 分配单位到任务 |
| `ScenEdit_RemoveUnitAsTarget()` | 移除目标 |
| `ScenEdit_AssignUnitAsTarget()` | 分配目标 |
| `ScenEdit_GetMissions()` | 获取所有任务 |
| `ScenEdit_CreateMissionFlightPlan()` | 创建飞行计划 |

### 阵营操作 (Side)
| 函数 | 说明 |
|------|------|
| `ScenEdit_AddSide()` | 添加阵营 |
| `ScenEdit_RemoveSide()` | 移除阵营 |
| `ScenEdit_SetSidePosture()` | 设置态度 |
| `ScenEdit_GetSidePosture()` | 获取态度 |
| `ScenEdit_SetSideOptions()` | 设置阵营选项 |
| `ScenEdit_GetSideOptions()` | 获取阵营选项 |
| `ScenEdit_GetSideIsHuman()` | 是否是人类玩家 |

### 事件操作 (Event)
| 函数 | 说明 |
|------|------|
| `ScenEdit_SetEvent()` | 创建/更新事件 |
| `ScenEdit_GetEvent()` | 获取事件 |
| `ScenEdit_GetEvents()` | 获取所有事件 |
| `ScenEdit_SetTrigger()` | 设置触发器 |
| `ScenEdit_SetCondition()` | 设置条件 |
| `ScenEdit_SetAction()` | 设置动作 |
| `ScenEdit_SetEventTrigger()` | 事件+触发器 |
| `ScenEdit_SetEventCondition()` | 事件+条件 |
| `ScenEdit_SetEventAction()` | 事件+动作 |
| `ScenEdit_AddSpecialAction()` | 添加特殊动作 |
| `ScenEdit_ExecuteSpecialAction()` | 执行特殊动作 |
| `ScenEdit_ExecuteEventAction()` | 执行事件动作 |
| `ScenEdit_UnitX()` | 获取触发事件的单位 |
| `ScenEdit_UnitC()` | 获取触发事件的接触 |
| `ScenEdit_UnitY()` | 获取另一个相关单位 |

### 接触/目标 (Contact)
| 函数 | 说明 |
|------|------|
| `ScenEdit_GetContact()` | 获取接触 |
| `ScenEdit_GetContacts()` | 获取所有接触 |
| `ScenEdit_AttackContact()` | 攻击接触 |

### 参考点和区域
| 函数 | 说明 |
|------|------|
| `ScenEdit_AddReferencePoint()` | 添加参考点 |
| `ScenEdit_GetReferencePoint()` | 获取参考点 |
| `ScenEdit_GetReferencePoints()` | 获取所有参考点 |
| `ScenEdit_SetReferencePoint()` | 设置参考点 |
| `ScenEdit_DeleteReferencePoint()` | 删除参考点 |
| `ScenEdit_AddZone()` | 添加区域 |
| `ScenEdit_RemoveZone()` | 移除区域 |
| `ScenEdit_SetZone()` | 设置区域 |
| `ScenEdit_TransformZone()` | 变换区域 |

### 工具函数 (Tool)
| 函数 | 说明 |
|------|------|
| `Tool_Range()` | 计算单位间距离 |
| `Tool_Bearing()` | 计算方位 |
| `Tool_LOS()` | 视线检测 |
| `Tool_LOS_Points()` | 点对点视线 |
| `World_GetPointFromBearing()` | 从方位获取点 |
| `World_GetElevation()` | 获取海拔 |
| `World_GetLocation()` | 获取位置 |
| `World_GetCircleFromPoint()` | 获取圆形点集 |
| `ScenEdit_GetWeather()` | 获取天气 |
| `ScenEdit_SetWeather()` | 设置天气 |
| `ScenEdit_CurrentTime()` | 当前时间 |
| `ScenEdit_MsgBox()` | 消息框 |
| `ScenEdit_SpecialMessage()` | 特殊消息 |
| `ScenEdit_InputBox()` | 输入框 |
| `ScenEdit_GetKeyValue()` | 获取存储值 |
| `ScenEdit_SetKeyValue()` | 设置存储值 |
| `ScenEdit_ClearKeyValue()` | 清除存储值 |
| `Command_SaveScen()` | 保存场景 |
| `Tool_EmulateNoConsole()` | 模拟无控制台 |

### 场景操作
| 函数 | 说明 |
|------|------|
| `GetScenarioTitle()` | 获取场景标题 |
| `ScenEdit_EndScenario()` | 结束场景 |
| `ScenEdit_GetScore()` | 获取分数 |
| `ScenEdit_SetScore()` | 设置分数 |
| `ScenEdit_GetScenHasStarted()` | 场景是否已开始 |
| `VP_GetScenario()` | 获取场景 |
| `VP_GetSide()` | 获取阵营 |
| `VP_GetSides()` | 获取所有阵营 |
| `VP_GetUnit()` | 获取单位（视图） |
| `VP_GetContact()` | 获取接触（视图） |

### 货物和运输
| 函数 | 说明 |
|------|------|
| `ScenEdit_UnloadCargo()` | 卸载货物 |
| `ScenEdit_TransferCargo()` | 转移货物 |
| `ScenEdit_HostUnitToParent()` | 装载单位 |
| `ScenEdit_UpdateUnitCargo()` | 更新货物 |

### 布雷和扫雷
| 函数 | 说明 |
|------|------|
| `ScenEdit_AddMinefield()` | 添加雷区 |
| `ScenEdit_DeleteMinefield()` | 删除雷区 |
| `ScenEdit_GetMinefield()` | 获取雷区 |
| `ScenEdit_DeleteMine()` | 删除水雷 |

### 水雷类型
| 函数 | 说明 |
|------|------|
| `ScenEdit_DistributeWeaponAtAirbase()` | 分配武器到机场 |

### 其他
| 函数 | 说明 |
|------|------|
| `ScenEdit_AddExplosion()` | 添加爆炸 |
| `ScenEdit_AddCustomLoss()` | 添加自定义损失 |
| `ScenEdit_AddMinefield()` | 添加雷场 |
| `ScenEdit_SplitUnit()` | 分离单位 |
| `ScenEdit_MergeUnits()` | 合并单位 |

## 详细信息

详见各分类文档：
- `unit-functions.md` - 单位函数详解
- `mission-functions.md` - 任务函数详解
- `side-functions.md` - 阵营函数详解
- `event-functions.md` - 事件函数详解
- `contact-functions.md` - 接触函数详解
- `reference-functions.md` - 参考点函数详解
- `tool-functions.md` - 工具函数详解
- `tables.md` - 数据表结构