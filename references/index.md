# AI 参考索引 - 完整导航

> 本文件是 CMO-HKBQSKILL 的主索引，帮助 AI 快速找到所需资料。

## 一、索引结构

```
references/
├── lua-api/              # Lua 函数参考
│   ├── index.md          # ← 主索引（本文件）
│   ├── functions.md      # 函数总览
│   ├── unit-functions.md    # 单位操作
│   ├── mission-functions.md  # 任务操作
│   ├── side-functions.md    # 阵营操作
│   ├── event-functions.md   # 事件系统
│   ├── contact-functions.md # 接触处理
│   ├── reference-functions.md # 参考点/工具
│   └── tool-functions.md    # 工具函数
└── data-types/           # 数据类型参考
    ├── index.md          # ← 数据类型索引
    ├── overview.md       # 数据类型总览
    ├── altitude.md       # 高度格式
    ├── latlon.md         # 经纬度格式
    └── doctrine.md       # 作战条令
```

## 二、AI 工作流程

### 场景 1：添加飞机单位

**1. 确定需求**
- 添加什么类型的单位？→ Aircraft
- 在哪个位置？→ 需要 latitude, longitude, altitude

**2. 查找函数**
- 参考：`lua-api/unit-functions.md` → `ScenEdit_AddUnit`
- 参考：`references/data-types/altitude.md` → 高度格式
- 参考：`references/data-types/latlon.md` → 经纬度格式

**3. 查询 DBID**
- 调用 MCP：`query_dbid("F-16")` → 获取 DBID

**4. 生成代码**
```lua
ScenEdit_AddUnit({
    side = "Blue",
    type = "Aircraft",
    name = "F-16 #1",
    dbid = 3785,
    latitude = "35.0",
    longitude = "127.0",
    altitude = "5000"
})
```

---

### 场景 2：创建巡逻任务

**1. 确定需求**
- 什么类型的巡逻？→ NAVAL（海上巡逻）
- 巡逻区域？→ 需要参考点

**2. 查找函数**
- 参考：`lua-api/mission-functions.md` → `ScenEdit_AddMission`
- 参考：`lua-api/reference-functions.md` → `ScenEdit_AddReferencePoint`
- 参考：`templates/advanced/patrol-mission.lua`

**3. 生成代码**
```lua
-- 创建参考点
ScenEdit_AddReferencePoint({side="Blue", name="RP-1", lat="35.0", lon="127.0"})
ScenEdit_AddReferencePoint({side="Blue", name="RP-2", lat="35.1", lon="128.0"})

-- 创建任务
ScenEdit_AddMission("Blue", "Sea Patrol", "Patrol", {type="NAVAL"})
ScenEdit_SetMission("Blue", "Sea Patrol", {zone={"RP-1", "RP-2"}})
```

---

### 场景 3：事件响应

**1. 确定需求**
- 什么触发条件？→ 单位被摧毁
- 触发后做什么？→ 发送消息

**2. 查找函数**
- 参考：`lua-api/event-functions.md` → `ScenEdit_SetEvent`, `ScenEdit_SetTrigger`, `ScenEdit_SetAction`
- 参考：`lua-api/event-functions.md` → `ScenEdit_UnitX()`

**3. 生成代码**
```lua
ScenEdit_SetEvent("单位损失", {mode="add", IsRepeatable=1})
ScenEdit_SetTrigger({mode="add", type="UnitDestroyed", side="Blue"})
ScenEdit_SetAction({
    mode="add",
    type="LuaScript",
    ScriptText='local u=ScenEdit_UnitX();ScenEdit_SpecialMessage(u.side,"单位损失:"..u.name)'
})
```

---

## 三、快速参考表

### 函数分类

| 功能 | 函数 | 参考文档 |
|------|------|----------|
| 添加单位 | `ScenEdit_AddUnit()` | unit-functions.md |
| 获取单位 | `ScenEdit_GetUnit()` | unit-functions.md |
| 删除单位 | `ScenEdit_DeleteUnit()` | unit-functions.md |
| 创建任务 | `ScenEdit_AddMission()` | mission-functions.md |
| 分配单位 | `ScenEdit_AssignUnitToMission()` | mission-functions.md |
| 创建阵营 | `ScenEdit_AddSide()` | side-functions.md |
| 设置态度 | `ScenEdit_SetSidePosture()` | side-functions.md |
| 创建事件 | `ScenEdit_SetEvent()` | event-functions.md |
| 设置触发器 | `ScenEdit_SetTrigger()` | event-functions.md |
| 设置动作 | `ScenEdit_SetAction()` | event-functions.md |
| 获取接触 | `ScenEdit_GetContact()` | contact-functions.md |
| 添加参考点 | `ScenEdit_AddReferencePoint()` | reference-functions.md |
| 距离计算 | `Tool_Range()` | reference-functions.md |
| 发送消息 | `ScenEdit_SpecialMessage()` | tool-functions.md |

### 数据类型

| 类型 | 格式 | 参考 |
|------|------|------|
| 高度 | `"5000"` 或 `"15000 FT"` | altitude.md |
| 纬度 | `"35.0"` 或 `"N 35.0"` | latlon.md |
| 经度 | `"127.0"` 或 `"E 127.0"` | latlon.md |
| 态度 | `"H"`, `"F"`, `"N"`, `"U"` | doctrine.md |
| 熟练度 | `"Regular"`, `"Veteran"` | doctrine.md |

### 任务类型

| 类型 | 子类型 | 说明 |
|------|--------|------|
| Strike | AIR, LAND, SEA, SUB | 打击任务 |
| Patrol | ASW, NAVAL, AAW, LAND, MIXED | 巡逻任务 |
| Mining | NAVAL | 布雷任务 |
| Cargo | - | 运输任务 |

---

## 四、MCP 工具（DBID 查询）

> 注意：DBID 查询走 MCP，不是这里的内容！
> **⚠ 查询内容必须使用英文！**

**MCP 工具**：
- `query_dbid("F-16")` - 自然语言查询
- `get_dbid_by_name("F-22")` - 按名称查询
- `get_dbid_by_country("United States", "aircraft")` - 按国家查询

---

## 五、模板库

| 模板 | 用途 | 路径 |
|------|------|------|
| add-aircraft.lua | 添加飞机 | templates/basic/ |
| add-ship.lua | 添加舰艇 | templates/basic/ |
| create-mission.lua | 创建任务 | templates/basic/ |
| patrol-mission.lua | 巡逻任务 | templates/advanced/ |
| strike-mission.lua | 打击任务 | templates/advanced/ |
| set-emcon.lua | EMCON 设置 | templates/utility/ |
| unit-loop.lua | 单位遍历 | templates/utility/ |

---

## 六、资料来源

1. **本地文档**：F:\codeAi\AIassistant\03_Archive\900_系统管理\CMO语法资料\
2. **官方文档**：https://commandlua.github.io/assets/Functions.html
3. **网友案例**：https://commandops.github.io/