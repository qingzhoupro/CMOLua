# CMO Lua API 渐进披露加载规则

## 核心理念

**按需加载，而非全量加载。** 避免一次性把整个函数文档塞进上下文，导致模型产生幻觉。

---

## 分层结构

```
Layer 0: official-api-index.md  (~250行，总是加载)
    │
    ├── Layer 1a: unit-functions.md      (Unit 操作)
    ├── Layer 1b: mission-functions.md    (Mission 操作)
    ├── Layer 1c: side-functions.md       (Side/阵营操作)
    ├── Layer 1d: event-functions.md     (事件系统)
    ├── Layer 1e: contact-functions.md    (接触处理)
    ├── Layer 1f: reference-functions.md (参考点/区域)
    └── Layer 1g: tool-functions.md       (工具函数)
            │
            └── Layer 2: generated/{函数名}.md  (逐函数文档)
```

---

## Layer 0: 轻量索引（总是加载）

**文件**: `references/lua-api/official-api-index.md`

**何时加载**: 每个 CMO Lua 对话开始时自动加载。

**内容**: 所有函数的名称、参数形式、返回值类型、官方 URL。约 ~250 行。

**作用**: 防止编造函数名。任何使用的函数必须先在本索引中确认存在。

---

## Layer 1: 分类文档（按需加载）

**何时加载**: 用户请求涉及该类操作时。

### Layer 1a: Unit 操作
**文件**: `references/lua-api/unit-functions.md`
**触发条件**: 用户请求添加/获取/设置/删除/更新单位时
**覆盖函数**: `ScenEdit_AddUnit`, `ScenEdit_GetUnit`, `ScenEdit_SetUnit`, `ScenEdit_UpdateUnit`, `ScenEdit_DeleteUnit`, `ScenEdit_KillUnit`, `ScenEdit_SetLoadout`, `ScenEdit_GetLoadout`, `ScenEdit_SetEMCON`, `ScenEdit_SetDoctrine`, `ScenEdit_RefuelUnit`, `ScenEdit_AddReloadsToUnit`, `ScenEdit_AddWeaponToUnitMagazine`, `ScenEdit_FillMagsForLoadout`, `ScenEdit_SetUnitSide`, `ScenEdit_SetUnitDamage`, `ScenEdit_ClearAllAircraft`, `ScenEdit_DistributeWeaponAtAirbase`

### Layer 1b: Mission 操作
**文件**: `references/lua-api/mission-functions.md`
**触发条件**: 用户请求创建/获取/设置/删除任务，分配单位到任务时
**覆盖函数**: `ScenEdit_AddMission`, `ScenEdit_GetMission`, `ScenEdit_SetMission`, `ScenEdit_DeleteMission`, `ScenEdit_GetMissions`, `ScenEdit_AssignUnitToMission`, `ScenEdit_RemoveUnitAsTarget`, `ScenEdit_AssignUnitAsTarget`, `ScenEdit_CreateMissionFlightPlan`, `ScenEdit_ExportMission`, `ScenEdit_ImportMission`

### Layer 1c: Side/阵营操作
**文件**: `references/lua-api/side-functions.md`
**触发条件**: 用户请求创建阵营、设置阵营关系时
**覆盖函数**: `ScenEdit_AddSide`, `ScenEdit_RemoveSide`, `ScenEdit_SetSidePosture`, `ScenEdit_GetSidePosture`, `ScenEdit_SetSideOptions`, `ScenEdit_GetSideOptions`, `ScenEdit_GetSideIsHuman`, `VP_GetSides`, `VP_GetSide`, `VP_GetScenario`, `VP_GetUnit`, `VP_GetContact`, `ScenEdit_PlayerSide`

### Layer 1d: Event/事件系统
**文件**: `references/lua-api/event-functions.md`
**触发条件**: 用户请求创建事件、触发器、条件、动作时
**覆盖函数**: `ScenEdit_SetEvent`, `ScenEdit_GetEvent`, `ScenEdit_GetEvents`, `ScenEdit_SetTrigger`, `ScenEdit_SetCondition`, `ScenEdit_SetAction`, `ScenEdit_SetEventTrigger`, `ScenEdit_SetEventCondition`, `ScenEdit_SetEventAction`, `ScenEdit_AddSpecialAction`, `ScenEdit_GetSpecialAction`, `ScenEdit_ExecuteSpecialAction`, `ScenEdit_ExecuteEventAction`, `ScenEdit_UnitX`, `ScenEdit_UnitC`, `ScenEdit_UnitY`, `ScenEdit_EventX`

### Layer 1e: Contact/接触处理
**文件**: `references/lua-api/contact-functions.md`
**触发条件**: 用户请求获取接触、攻击接触时
**覆盖函数**: `ScenEdit_GetContact`, `ScenEdit_GetContacts`, `ScenEdit_AttackContact`

### Layer 1f: 参考点/区域
**文件**: `references/lua-api/reference-functions.md`
**触发条件**: 用户请求添加参考点、设置巡逻区域时
**覆盖函数**: `ScenEdit_AddReferencePoint`, `ScenEdit_GetReferencePoint`, `ScenEdit_GetReferencePoints`, `ScenEdit_SetReferencePoint`, `ScenEdit_DeleteReferencePoint`, `ScenEdit_AddZone`, `ScenEdit_SetZone`, `ScenEdit_RemoveZone`, `ScenEdit_TransformZone`, `Tool_Range`, `Tool_Bearing`, `Tool_LOS`, `World_GetPointFromBearing`, `World_GetLocation`, `World_GetElevation`, `World_GetCircleFromPoint`

### Layer 1g: 工具函数
**文件**: `references/lua-api/tool-functions.md`
**触发条件**: 用户请求天气、分数、保存、UI 消息时
**覆盖函数**: `GetScenarioTitle`, `ScenEdit_CurrentTime`, `ScenEdit_CurrentLocalTime`, `ScenEdit_EndScenario`, `ScenEdit_GetScenHasStarted`, `ScenEdit_GetWeather`, `ScenEdit_SetWeather`, `ScenEdit_GetScore`, `ScenEdit_SetScore`, `ScenEdit_GetTimeOfDay`, `ScenEdit_SetStartTime`, `ScenEdit_SetTime`, `ScenEdit_MsgBox`, `ScenEdit_InputBox`, `ScenEdit_SpecialMessage`, `ScenEdit_SetKeyValue`, `ScenEdit_GetKeyValue`, `ScenEdit_ClearKeyValue`, `Command_SaveScen`, `ScenEdit_RunScript`, `ScenEdit_SelectedUnits`

---

## Layer 2: 逐函数文档（精确到单个函数）

**文件**: `references/lua-api/generated/{函数名}.md`
**何时加载**: 涉及到具体函数的参数细节时（参数名、类型、示例代码）
**覆盖范围**: 单个函数，包含官方文档原文（参数说明、返回值、示例代码）
**爬取工具**: `scripts/scrape_cmo_api.py`

### 高频函数优先爬取（第一批次）

| 优先级 | 函数 | 对应分类文档 |
|-------|------|------------|
| P0 | `ScenEdit_AddUnit` | unit-functions.md |
| P0 | `ScenEdit_GetUnit` | unit-functions.md |
| P0 | `ScenEdit_SetUnit` | unit-functions.md |
| P0 | `ScenEdit_AddMission` | mission-functions.md |
| P0 | `ScenEdit_AssignUnitToMission` | mission-functions.md |
| P0 | `ScenEdit_AddSide` | side-functions.md |
| P0 | `ScenEdit_SetSidePosture` | side-functions.md |
| P0 | `VP_GetSides` | side-functions.md |
| P0 | `VP_GetSide` | side-functions.md |
| P1 | `ScenEdit_SetTrigger` | event-functions.md |
| P1 | `ScenEdit_SetAction` | event-functions.md |
| P1 | `ScenEdit_GetEvent` | event-functions.md |
| P1 | `ScenEdit_AddReferencePoint` | reference-functions.md |
| P1 | `ScenEdit_GetContact` | contact-functions.md |
| P1 | `ScenEdit_GetContacts` | contact-functions.md |
| P2 | 其余所有函数 | 对应分类文档 |

---

## 触发规则（按关键词匹配）

| 用户关键词 | 加载分类文档 |
|-----------|------------|
| 添加单位 / addUnit / AddUnit / Aircraft / Ship / Submarine | unit-functions.md |
| 创建任务 / addMission / 巡逻 / 攻击 | mission-functions.md |
| 阵营 / side / 敌对 / 友好 | side-functions.md |
| 事件 / 触发器 / 触发 / condition / action | event-functions.md |
| 接触 / contact / 攻击 / AttackContact | contact-functions.md |
| 参考点 / reference point / 巡逻区域 / zone | reference-functions.md |
| 天气 / 分数 / 保存 / 消息 / score / weather | tool-functions.md |

---

## 禁止行为

1. **禁止跳过 Layer 0 直接生成代码** — 必须先确认函数存在于 `official-api-index.md`
2. **禁止跳过 Layer 1 直接用 Layer 2** — 先加载分类文档，再深入单个函数
3. **禁止凭记忆添加函数** — 所有函数必须在本规则的 URL 中可查
4. **禁止凭记忆描述参数** — 必须从 `generated/{函数名}.md` 或分类文档中引用
5. **禁止混用参数形式** — 确认函数是表参数还是位置参数，严格遵守

---

## 验证流程

生成代码前的最小验证链：

```
用户请求
    │
    ▼
确认 official-api-index.md 中存在该函数名
    │
    ▼
确认参数形式（表参数 vs 位置参数）
    │
    ▼
加载对应分类文档（Layer 1）
    │
    ▼
如需精确参数 → 加载 generated/{函数名}.md（Layer 2）
    │
    ▼
生成代码
```
