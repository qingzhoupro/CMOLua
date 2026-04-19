# Lua API 参考文档索引

> AI 调用资料的索引 - 帮助 AI 找到正确的函数参考资料

## 快速导航

| 任务需求 | 参考文档 |
|---------|----------|
| 添加/删除单位 | `unit-functions.md` |
| 创建/管理任务 | `mission-functions.md` |
| 设置阵营关系 | `side-functions.md` |
| 事件响应/触发 | `event-functions.md` |
| 攻击/接触处理 | `contact-functions.md` |
| 参考点/区域/工具 | `reference-functions.md` |
| 场景/天气/UI | `tool-functions.md` |

## 函数分类

### 单位操作 (unit-functions.md)

**添加单位**
```lua
ScenEdit_AddUnit({...})
```

**获取/设置单位**
```lua
ScenEdit_GetUnit({...})
ScenEdit_SetUnit({...})
```

**武器/弹药**
```lua
ScenEdit_SetLoadout({...})
ScenEdit_FillMagsForLoadout({...})
ScenEdit_AddReloadsToUnit({...})
ScenEdit_AddWeaponToUnitMagazine({...})
ScenEdit_UpdateUnit({...})  -- 传感器/挂载/组件/燃料
ScenEdit_ClearAllAircraft({...})
```

**单位转移 / 损伤**
```lua
ScenEdit_SetUnitSide({...})  -- 单位转阵营（心理战/接管）
ScenEdit_SetUnitDamage({...}) -- 设置损伤状态
ScenEdit_KillUnit({...})     -- 摧毁单位（触发事件）
ScenEdit_DeleteUnit({...})   -- 删除单位（不触发事件）
```

**EMCON / Doctrine**
```lua
ScenEdit_SetEMCON(...)
ScenEdit_SetDoctrine({...}, {...})
```

---

### 任务操作 (mission-functions.md)

**创建任务**
```lua
ScenEdit_AddMission(side, name, type, {...})
-- type: Strike, Patrol, Mining, Cargo
```

**分配单位**
```lua
ScenEdit_AssignUnitToMission(unit, mission)
```

**巡逻区域**
```lua
ScenEdit_SetMission(side, name, {zone={...}})
```

---

### 阵营操作 (side-functions.md)

**创建阵营**
```lua
ScenEdit_AddSide({name="Blue"})
```

**设置态度**
```lua
ScenEdit_SetSidePosture(sideA, sideB, "H")
-- H=敌对, F=友好, N=中立, U=不友好
```

---

### 事件系统 (event-functions.md)

**创建事件**
```lua
ScenEdit_SetEvent(name, {mode="add"})
ScenEdit_SetTrigger({mode="add", type="UnitDestroyed", ...})
ScenEdit_SetAction({mode="add", type="LuaScript", ScriptText="..."})
```

**事件信息获取**
```lua
ScenEdit_UnitX()  -- 触发事件的单位
ScenEdit_UnitC()  -- 检测到的接触
```

---

### 接触处理 (contact-functions.md)

**获取接触**
```lua
ScenEdit_GetContact({side="Blue", guid="..."})
ScenEdit_GetContacts("Blue")
```

**攻击接触**
```lua
ScenEdit_AttackContact(attacker, contactId, {...})
```

---

### 参考点和区域 (reference-functions.md)

**参考点**
```lua
ScenEdit_AddReferencePoint({...})
```

**工具函数**
```lua
Tool_Range(unitA, unitB, "nm")
Tool_Bearing(unitA, unitB)
World_GetPointFromBearing({...})
```

---

### 工具函数 (tool-functions.md)

**场景信息**
```lua
GetScenarioTitle()
ScenEdit_CurrentTime()
ScenEdit_GetScore(side)
```

**UI**
```lua
ScenEdit_MsgBox(msg, buttons)
ScenEdit_SpecialMessage(side, msg)
ScenEdit_InputBox(prompt, default)
```

**存储**
```lua
ScenEdit_SetKeyValue(key, value)
ScenEdit_GetKeyValue(key)
```

---

## AI 提示词模板

### 添加飞机
```
请参考:
- unit-functions.md → ScenEdit_AddUnit
- templates/basic/add-aircraft.lua
- 使用 query_dbid("F-16") 查询 DBID
```

### 创建巡逻任务
```
请参考:
- mission-functions.md → ScenEdit_AddMission
- templates/advanced/patrol-mission.lua
```

### 事件触发
```
请参考:
- event-functions.md → ScenEdit_SetTrigger
- event-functions.md → ScenEdit_UnitX/UnitC
```