---
doc_id: CMO-SKILL-AUTO-001
title: CMO 自动生成工作流
description: 完整的 CMO Lua 代码生成工作流，支持场景上下文感知
references:
  - references/lua-api/Functions.md
  - references/lua-api/常用函数总结.md
  - references/lua-api/CMO_Lua函数_Unit.md
  - references/lua-api/CMO_Lua函数_Mission.md
---
# CMO 自动生成工作流

> **重要：所有函数必须基于官方文档，不允许编造函数名或参数格式。**
> 代码生成前必须查阅 references 中列出的官方文档。

## 流程概览

```
用户请求 → 场景上下文检测 → 【Step 0.5】经验教训查询 → MCP验证 → 数据查询 → 代码生成 → 自检 → 输出
```

---

## Step 0: 场景上下文检测

**重要：生成代码前，必须先了解当前场景的状态。**

### 检测逻辑

1. 检查用户是否提供了场景侦察输出
2. 检查 `memory/skill/scenario-context.md` 是否有内容
3. 根据情况决定下一步：

```
场景侦察输出
  → 有：读取场景信息，基于真实数据生成代码（无占位符）
  → 无：询问用户场景状态，或提供 scene-scout.lua

空白场景（用户明确说明）
  → 直接生成代码，可使用示例占位符

新对话/无上下文
  → 提供 scene-scout.lua 让用户获取场景信息
```

### 场景侦察脚本

当需要获取场景信息时，提供以下脚本让用户执行：

将以下代码复制到 CMO Lua 控制台执行，将完整输出粘贴回给我：

```lua
-- 用法：复制到 CMO Lua 控制台执行
-- by HKBQ 202603


print("=== CMO 场景全局侦察报告 ===")

-- 1. 获取场景基础状态
print("场景标题: " .. tostring(GetScenarioTitle()))
print("场景是否已开始: " .. tostring(ScenEdit_GetScenHasStarted()))

-- 2. 获取当前天气快照
local weather = ScenEdit_GetWeather()
if weather then
    print(string.format("环境天气: 温度 %s°C | 云量 %d%% | 海况 %s 级", 
        tostring(weather.temp), math.floor((weather.undercloud or 0) * 100), tostring(weather.seastate)))
end
print("")

-- 3. 获取所有阵营及其得分、控制权状态
local sides = VP_GetSides()
print("【阵营积分与控制概况】")
for _, side in ipairs(sides) do
    local is_human = false
    pcall(function() is_human = ScenEdit_GetSideIsHuman(side.name) end)
    local score = 0
    pcall(function() score = ScenEdit_GetScore(side.name) end)
    print(string.format("  - [%s] 阵营得分: %s | 控制方: %s", side.name, tostring(score), is_human and "人类玩家" or "AI 电脑"))
end
print("")

-- 4. 各阵营任务清册 (安全过滤)
print("【各阵营任务清册】")
for _, side in ipairs(sides) do
    local success, missions = pcall(ScenEdit_GetMissions, side.name)
    if success and missions and #missions > 0 then
        print("  - 阵营 [" .. side.name .. "] 当前编组任务:")
        for _, m in ipairs(missions) do
            print("    * 任务名: " .. tostring(m.name) .. " | GUID: " .. tostring(m.guid or m.objectid))
        end
    else
        print("  - 阵营 [" .. side.name .. "] 无可用或可读任务。")
    end
end
print("")

-- 5. 获取各阵营己方真实单元 (Units) - 引入真实 Wrapper 转换
print("【各阵营真实单元 (Units) 扫描】")
for _, side in ipairs(sides) do
    local units = side.units
    if units and #units > 0 then
        print("  - 阵营 [" .. side.name .. "] 实际拥有单元数: " .. #units)
  
        -- 限制展示前 5 个进行结构示例
        local max_unit_dump = math.min(#units, 5)
        for i = 1, max_unit_dump do
            local raw_u = units[i]
            local u_guid = raw_u.guid or raw_u.objectid
  
            -- 通过全局 ScenEdit_GetUnit 将轻量指针显式转换为功能完整的真实的 Unit 包装器对象
            local get_u_success, real_unit = pcall(ScenEdit_GetUnit, { guid = u_guid })
  
            local u_name = raw_u.name or "未命名实体"
            local u_type = "未知大类"
            local u_class = "未知型号"
  
            if get_u_success and real_unit then
                -- 成功解包，提取官方合规的类目和大类属性
                u_type = real_unit.category or "未知大类"
                u_class = real_unit.classname or "未知型号"
            end
  
            print(string.format("    * [己方单位] %s | 大类: %s | 级别型号: %s | GUID: %s", 
                tostring(u_name), tostring(u_type), tostring(u_class), tostring(u_guid)))
        end
  
        if #units > 5 then
            print("    * ... 其余 " .. (#units - 5) .. " 个己方单元已省略。")
        end
    else
        print("  - 阵营 [" .. side.name .. "] 视点下无直接控制的单元。")
    end
end
print("")

-- 6. 安全扫描已知接触情报 (Contacts) - 防御 nil 拼接与视点隔离
print("【各阵营已知接触情报 (Contacts)】")
for _, side in ipairs(sides) do
    local contacts = side.contacts 
    if contacts and #contacts > 0 then
        print("  - 阵营 [" .. side.name .. "] 总计探测到目标数: " .. #contacts)
  
        local max_dump = math.min(#contacts, 5)
        for i = 1, max_dump do
            local target = contacts[i]
            local con_guid = target.guid or target.objectid or target.ObjectID
            local safe_guid_str = tostring(con_guid)
  
            if con_guid then
                local get_success, a_contact = pcall(VP_GetContact, { guid = safe_guid_str })
                if get_success and a_contact then
                    local name = a_contact.name or "未知接触"
                    local contact_type_desc = a_contact.type_description or "未分类接触"
                    print(string.format("    * [探测解析成功] 目标: %s | 情报分类: %s | GUID: %s", 
                        tostring(name), tostring(contact_type_desc), safe_guid_str))
                else
                    print("    * [视点隔离/仅知实体] 接触 GUID: " .. safe_guid_str)
                end
            else
                print("    * [警告] 该接触快照中未包含有效的 ID 字段")
            end
        end
  
        if #contacts > 5 then
            print("    * ... 阵营 [" .. side.name .. "] 其余 " .. (#contacts - 5) .. " 个已知接触目标已省略。")
        end
    else
        print("  - 阵营 [" .. side.name .. "] 当前没有已建立的敌情接触。")
    end
end
print("")

print("=== 侦察报告执行完毕 ===")
```

### 场景上下文填充

收到用户粘贴的侦察输出后，读取并填充 `memory/skill/scenario-context.md`，记录：

- 场景名称
- 所有阵营名称和人类控制状态
- 所有单元的名称、类型、阵营、GUID、位置
- 所有任务的名称、类型、子类型、巡逻区
- 所有参考点的名称和坐标

---

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

---

## Step 2: 解析需求

根据场景上下文检测结果：

**有场景上下文时：**

- 单位类型：从上下文确认 `Aircraft` / `Ship` / `Submarine` / `Facility` / `GROUND UNIT`
- 阵营：从上下文中读取真实阵营名称，不使用占位符
- 位置：从上下文推断已有单元位置，或询问用户指定
- 检查是否有同名单元存在，避免冲突

**空白场景时：**

- **必须先创建阵营**：调用 `ScenEdit_AddSide()` 创建所有需要的阵营
- **再设置阵营关系**：调用 `ScenEdit_SetSidePosture()` 设置敌对/友好关系
- 单位类型：`Aircraft` / `Ship` / `Submarine` / `Facility` / `GROUND UNIT`
- 位置：手动指定或从需求推断

### 空白场景阵营创建模板（基于官方 API）

```lua
-- 官方 API: ScenEdit_AddSide({side = "阵营名"})
-- 仅支持 side 参数，name/posture/orientation 不存在！
ScenEdit_AddSide({side="Red"})
ScenEdit_AddSide({side="Blue"})

-- 官方 API: ScenEdit_SetSidePosture(sideA, sideB, posture)
-- 位置参数，非表！posture: 'H'=敌对, 'F'=友方, 'N'=中立, 'U'=不友好
ScenEdit_SetSidePosture("Red", "Blue", "H")
ScenEdit_SetSidePosture("Blue", "Red", "H")
```

---

## Step 3: 数据查询

```python
# 获取 DBID
cmo_nl_query("F-16C 战斗机的 DBID")

# 获取 LoadoutID（仅 Aircraft）
cmo_get_loadouts("F-16C")
```

---

## Step 4: 生成代码

**空白场景必须先创建阵营，再添加单元：**

```lua
-- Step 1: 创建阵营 (官方 API)
ScenEdit_AddSide({side="Red"})
ScenEdit_AddSide({side="Blue"})

-- Step 2: 设置敌对关系 (官方 API: 位置参数)
ScenEdit_SetSidePosture("Red", "Blue", "H")
ScenEdit_SetSidePosture("Blue", "Red", "H")

-- Step 3: 添加单元 (官方 API: ScenEdit_AddUnit)
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

**基于场景上下文生成真实代码（无占位符）：**

> **注意**：以下示例中的 DBID（如 F-16C 的 `1719`）和 LoadoutID（如 `2230`）为静态参考值，可能因数据库版本不同而失效。**实际生成代码时，必须通过 MCP 动态查询获取最新的 DBID 和 LoadoutID。**

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

**空白场景时可使用示例占位符，但需注明用户需要替换的内容。**

---

## Step 5: 自检

### 空白场景额外检查

- [ ] 所有阵营已通过 `ScenEdit_AddSide({side="xxx"})` 创建
- [ ] 阵营关系已通过 `ScenEdit_SetSidePosture("A","B","H")` 设置

### 单元自检

- [ ] DBID 验证（通过 MCP 确认存在）
- [ ] LoadoutID 存在（Aircraft 类型必须）
- [ ] type 正确（参考 cmo-unit 有效值列表）
- [ ] 坐标参数正确（latitude / longitude，非 lat / lon）
- [ ] altitude 单位为米
- [ ] 阵营名称与场景上下文一致
- [ ] 单位名称不与现有单元冲突

### API 语法自检（防止编造）

- [ ] `ScenEdit_AddSide` 使用 `{side="xxx"}` 格式
- [ ] `ScenEdit_SetSidePosture` 使用 `(A, B, posture)` 位置参数格式
- [ ] `ScenEdit_AddMission` 使用 `(Side, Name, Type, {options})` 位置参数格式

---

## Step 6: 错误处理

错误 → `errors/index.md` 查找解决方案。

### 常见错误速查

| 错误信息                       | 原因                                                        | 解决方案                                                                                                                       |
| ------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `Side 'xxx' doesn't exist`   | 在创建阵营之前就添加了单元                                  | 先调用 `ScenEdit_AddSide({side="xxx"})` 创建阵营，再添加单元                                                                 |
| `DBID not found`             | 通过 MCP 查询的 DBID 不存在于当前数据库                     | 重新通过 `cmo_nl_query()` 验证 DBID 是否正确                                                                                 |
| `Missing LoadoutID`          | Aircraft 类型未指定 LoadoutID                               | 通过 `cmo_get_loadouts()` 查询并添加 LoadoutID 参数                                                                          |
| `Invalid unit type`          | 使用了错误的 type 值（如 `Air`、`Sub`、`GroundUnit`） | 改用正确值：`Aircraft` / `Ship` / `Submarine` / `Facility` / `GROUND UNIT`（**GROUND UNIT 必须全大写加空格**） |
| `Invalid latitude/longitude` | 使用了 lat/lon 而非 latitude/longitude                      | 修正参数名称：`latitude`、`longitude`                                                                                      |

---

## API 正确语法参考（官方文档索引）

> **所有函数必须查阅官方文档，不允许编造。**

| 功能     | 错误写法                                                              | 正确写法                                                | 参考文档                       |
| -------- | --------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------ |
| 创建阵营 | `ScenEdit_AddSide({name="R", orientation="H"})`                     | `ScenEdit_AddSide({side="Red"})`                      | lua-api/Functions.md           |
| 设置关系 | `ScenEdit_SetSideRelations({side_a="R", side_b="B", relation="H"})` | `ScenEdit_SetSidePosture("Red","Blue","H")`           | lua-api/常用函数总结.md        |
| 场景标题 | `ScenEdit_GetScenario().name`                                       | `GetScenarioTitle()`                                  | lua-api/Functions.md           |
| 阵营列表 | `ScenEdit_GetSides()`                                               | `VP_GetSides()`                                       | lua-api/Functions.md           |
| 阵营单元 | `ScenEdit_GetUnits({side=...})`                                     | `VP_GetSide({side="xxx"}).units`                      | lua-api/Functions.md           |
| 任务列表 | `ScenEdit_GetMissions()`                                            | `ScenEdit_GetMissions("阵营名")`                      | lua-api/CMO_Lua函数_Mission.md |
| 添加任务 | `ScenEdit_AddMission({side="R", name="N", type="P"})`               | `ScenEdit_AddMission("Side","Name","Type",{options})` | lua-api/CMO_Lua函数_Mission.md |
| 参考点   | `ScenEdit_ReferencePoints(side)`                                    | `ScenEdit_GetReferencePoints({side="xxx"})`           | lua-api/Functions.md           |

### posture 参数值

| 值    | 含义                 |
| ----- | -------------------- |
| `H` | Hostile（敌对）      |
| `F` | Friendly（友方）     |
| `N` | Neutral（中立）      |
| `U` | Unfriendly（不友好） |
