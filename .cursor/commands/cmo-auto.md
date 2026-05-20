---
doc_id: CMO-CMD-AUTO-001
trigger: /cmo-auto
title: 完整工作流
description: 完整的 CMO Lua 代码生成工作流，支持场景上下文感知
---
# /cmo-auto - 完整工作流

执行完整的 CMO Lua 代码生成工作流。

## 官方文档索引

> **所有函数必须基于官方文档，不允许编造。**
> 参考: `.cursor/skills/cmo-auto/SKILL.md` (含完整 references 列表)

## 流程概览

```
场景上下文检测 → 【Step 0.5】经验教训查询 → MCP验证 → 数据查询 → 代码生成 → 自检 → 输出
```

## Step 0: 场景上下文检测

**重要：生成代码前，必须先了解当前场景状态。**

### 检测逻辑

```
有场景上下文 → 基于真实数据生成代码（无占位符）
无场景上下文 → 询问用户场景状态，或引导执行 /cmo-scene
空白场景     → 直接生成
```

### 无场景信息时的引导

```
我需要了解你的场景才能生成精准代码。

请选择：
1. 执行 /cmo-scene 获取场景信息（推荐）
2. 告诉我当前场景的基本信息（阵营、已有的单元、部署经纬度等）
3. 这是空白场景，直接生成示例代码
```

## Step 0.5: 经验教训查询（按需）

**规则：只读与本次需求相关的教训，不要全量加载。**

### 触发条件

- 用户明确要求生成代码时 → 执行 Step 0.5
- 用户说「直接生成」时 → 跳过 Step 0.5
- 用户粘贴报错信息时 → 触发错误收集（见 `/cmo-errors`）

### 查询逻辑

1. 扫描用户需求关键词（飞机/舰艇/巡逻/阵营等）
2. 读取 `memory/cold/lesson-index.md`（约 20 行索引）
3. 根据关键词匹配教训 ID
4. 从 `memory/cold/lesson-root-causes.md` 只加载对应段落（约 3-5 行）
5. 将匹配到的教训要点追加到 `memory/hot/session.md` 的「本次防错提醒」区
6. 后续流程中引用这些提醒

### 关键词映射

| 用户需求 | 需加载的教训 ID |
|---------|----------------|
| 飞机/Aircraft/F-16 | LOADOUTID, ALTITUDE-UNIT, DEPRECATED-DBID |
| 舰艇/Ship | DEPRECATED-DBID |
| 地面/GROUND UNIT | GROUND-UNIT-TYPE, FACILITY-TERRAIN |
| 机场/Facility | FACILITY-TERRAIN |
| 坐标/经纬度 | LATITUDE-PARAM |
| 空白场景添加单元 | SIDE-NOT-EXIST, SIDE-API |
| 创建阵营 | SIDE-API |
| 巡逻/任务 | MISSION-REF-POINT |

### 禁止行为

- 不要将整个 lesson 文件加载到上下文
- 不要在 Step 0.5 做代码生成或 MCP 调用
- 不要输出与本次需求无关的教训

### 输出到 hot/session.md

```markdown
## 本次防错提醒

<!-- 注入本次相关的教训要点，例如： -->
- Aircraft 必须有 LoadoutID（MCP 查询）
- altitude 默认单位是米
- DBID 必须通过 MCP 查询，不编造
```

---

## Step 1: MCP 验证

```python
cmo_nl_query("测试查询")
```

失败则终止。

## Step 2: 解析需求

**有场景上下文时：**

- 单位类型：从上下文确认 Aircraft / Ship / Submarine / Facility / GroundUnit
- 阵营：从上下文中读取真实阵营名称
- 位置：从上下文推断已有单元位置
- 检查是否有同名单元存在

**空白场景时：**

- **必须先创建阵营**，再添加单元！直接 `ScenEdit_AddUnit` 会报错 `Side 'xxx' doesn't exist`
- 单位类型：Aircraft / Ship / Submarine / Facility / GroundUnit
- 位置：手动指定

## Step 3: 数据查询

```python
# 获取 DBID
cmo_nl_query("F-16C 战斗机的 DBID")

# 获取 LoadoutID（仅 Aircraft）
cmo_get_loadouts("F-16C")
```

## Step 4: 生成代码

**空白场景必须先创建阵营，再添加单元：**

```lua
-- 官方 API: ScenEdit_AddSide({side = "阵营名"})
-- 仅支持 side 参数，name/posture/orientation 不存在！
ScenEdit_AddSide({side="Red"})
ScenEdit_AddSide({side="Blue"})

-- 官方 API: ScenEdit_SetSidePosture(sideA, sideB, posture)
-- 位置参数，非表！posture: 'H'=敌对, 'F'=友方, 'N'=中立, 'U'=不友好
ScenEdit_SetSidePosture("Red", "Blue", "H")
ScenEdit_SetSidePosture("Blue", "Red", "H")

-- 添加单元
ScenEdit_AddUnit({
  side = "Red",
  type = "Ship",
  name = "舰艇名称",
  dbid = 1234,
  latitude = 26.95,
  longitude = 56.45,
  heading = 135,
  speed = 28
})
```

**基于场景上下文生成真实代码：**

```lua
ScenEdit_AddUnit({
  side = "Blue",
  type = "Aircraft",
  name = "F-16C #1",
  dbid = 1719,
  LoadoutID = 2230,
  latitude = 35.6762,
  longitude = 139.6503,
  altitude = 9144,
  heading = 0,
  speed = 500
})
```

## Step 5: 自检

### 空白场景额外检查

- [ ] 所有阵营已通过 `ScenEdit_AddSide({side="xxx"})` 创建
- [ ] 阵营关系已通过 `ScenEdit_SetSidePosture("A","B","H")` 设置

### 单元自检

- [ ] DBID 验证（通过 MCP 确认存在）
- [ ] LoadoutID 存在（Aircraft 类型必须）
- [ ] type 正确（Aircraft/Ship/Submarine/Facility/GroundUnit）
- [ ] 坐标参数正确（latitude / longitude，非 lat / lon）
- [ ] altitude 单位为米
- [ ] 阵营名称与场景一致
- [ ] 单位名称不与现有单元冲突

### API 语法自检（防止编造）

- [ ] `ScenEdit_AddSide` 使用 `{side="xxx"}` 格式
- [ ] `ScenEdit_SetSidePosture` 使用 `(A, B, posture)` 位置参数格式
- [ ] `ScenEdit_AddMission` 使用 `(Side, Name, Type, {options})` 位置参数格式

## Step 6: 错误处理

错误 → 查 `memory/cold/lesson-root-causes.md` 或使用 `/cmo-errors` 收集

## API 正确语法参考（防编造检查表）

| 功能     | 错误写法                                                              | 正确写法                                                |
| -------- | --------------------------------------------------------------------- | ------------------------------------------------------- |
| 创建阵营 | `ScenEdit_AddSide({name="R", orientation="H"})`                     | `ScenEdit_AddSide({side="Red"})`                      |
| 设置关系 | `ScenEdit_SetSideRelations({side_a="R", side_b="B", relation="H"})` | `ScenEdit_SetSidePosture("Red","Blue","H")`           |
| 场景标题 | `ScenEdit_GetScenario().name`                                       | `GetScenarioTitle()`                                  |
| 阵营列表 | `ScenEdit_GetSides()`                                               | `VP_GetSides()`                                       |
| 阵营单元 | `ScenEdit_GetUnits({side=...})`                                     | `VP_GetSide({side="xxx"}).units`                      |
| 任务列表 | `ScenEdit_GetMissions()`                                            | `ScenEdit_GetMissions("阵营名")`                      |
| 添加任务 | `ScenEdit_AddMission({side="R", name="N", type="P"})`               | `ScenEdit_AddMission("Side","Name","Type",{options})` |
| 参考点   | `ScenEdit_ReferencePoints(side)`                                    | `ScenEdit_GetReferencePoints({side="xxx"})`           |

参考 → `.cursor/skills/cmo-auto/SKILL.md`
