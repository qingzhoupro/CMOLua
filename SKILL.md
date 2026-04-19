# CMO-HKBQSKILL SKILL 文件

> AI 助手使用 CMO Lua 的行为规范

## 概述

CMO-HKBQSKILL 是 Command: Modern Operations (CMO) 海空兵棋的 AI 助手技能库。

**核心目标：** AI 生成的所有 Lua 代码，必须通过 MCP 连接真实 CMO 数据库，**禁止凭空编造 DBID、LoadoutID、GUID、阵营名等任何数据**。

---

## 行为红线（违反直接报错）

1. **严禁硬编码 DBID**——任何 `dbid = 数字` 必须先通过 MCP 查询
2. **严禁编造 LoadoutID**——飞机必须先查 `DataAircraftLoadouts` 表
3. **严禁编造 GUID**——GUID 必须是真实单位创建后返回的 UUID
4. **严禁用中文查询 MCP**——CMO 数据库字段是英文，必须翻译成英文再查

---

## MCP 调用时机（强制）

**只要代码中涉及以下任何一项，必须立即调用 MCP 查询：**

| 代码中出现的内容 | 必须调用的 MCP 工具 |
|---------------|-------------------|
| 装备名称（如 F-16、宙斯盾舰） | `query_dbid("F-16C")` |
| 阵营名称（如 蓝方、红方） | `read_query` 查 `sides` 表 |
| 基地 DBID（type="Facility"） | `query_dbid("runway")` |
| 飞机 DBID（type="Aircraft"） | `query_dbid("F-16")` |
| 舰艇 DBID（type="Ship"） | `query_dbid("Aegis destroyer")` |
| 潜艇 DBID（type="Submarine"） | `query_dbid("attack submarine")` |
| LoadoutID（飞机挂载） | `read_query` 查 `DataAircraftLoadouts` |
| 数据库表结构不确定时 | `describe_table()` 或 `list_tables()` |

**⚠ 查询内容必须翻译成英文！**

```
用户：在海参崴添加 F-16 战斗机
→ 调用 query_dbid("F-16C Fighting Falcon")
→ 调用 read_query("SELECT ID FROM DataAircraftLoadouts WHERE ComponentID = {{DBID}}")
→ 确认 DBID 和 LoadoutID 存在后，再生成代码
```

---

## 参数清单（严格区分大小写）

### 1. ScenEdit_AddUnit 参数

```lua
ScenEdit_AddUnit({
    side        = "Blue",           -- 阵营名称（字符串，首字母大写）
    type        = "Aircraft",       -- 单位类型（见下表）
    dbid        = {{DBID}},         -- 数据库 ID（数值，通过 MCP 查询）
    name        = "{{UNIT_NAME}}",  -- 单位名称（用户自定义）
    latitude    = 35.6762,          -- 纬度（数值，-90 ~ 90）
    longitude   = 139.6503,         -- 经度（数值，-180 ~ 180）
    -- 以下参数仅 Aircraft（飞机）需要：
    LoadoutID   = {{LOADOUT_ID}},   -- 载荷 ID（数值，非字符串；必须！）
    -- 以下参数可选：
    altitude    = 3000,             -- 高度（默认米；可用 "5000 FT" 指定英尺）
    heading     = 90,               -- 航向（度数）
    speed       = 450,             -- 速度（节）
    -- ⚠ Facility 类型不需要 LoadoutID
})
```

**type 合法值（严格区分大小写）：**

| type 值 | 适用单位 | 需要 LoadoutID |
|---------|---------|--------------|
| `Aircraft` | 固定翼飞机 | ✅ 必须 |
| `Ship` | 水面舰艇 | ❌ 不需要 |
| `Submarine` | 潜艇 | ❌ 不需要 |
| `Facility` | 地面设施（机场、雷达等） | ❌ 不需要 |

### 2. ScenEdit_AddSide 参数

```lua
ScenEdit_AddSide({
    name = "Blue",      -- 阵营名称（首字母大写）
    color = "128,128,255"  -- 可选，RGB 颜色
})
```

### 3. ScenEdit_SetRelationship 参数

```lua
ScenEdit_SetRelationship({
    sideOne = "Blue",
    sideTwo = "Red",
    relationship = "Hostile"  -- 或 "Neutral"、"Friendly"、"Allied"
})
```

### 4. ScenEdit_AddMission 参数

```lua
ScenEdit_AddMission({
    side = "Blue",
    name = "巡逻任务",
    type = "Patrol",   -- Patrol / Strike / Escort 等
    ...
})
```

---

## 常见错误速查

> 生成代码前必须检查：参考 `errors/index.md`

| 错误信息 | 最常见原因 |
|---------|----------|
| `Missing 'LoadoutID'` | Aircraft 未填 LoadoutID，或参数名拼错（`loadoutid`） |
| `The requested object has been deprecated` | DBID 不存在——必须用 MCP 重新查询 |
| `Invalid unit type 'xxx'` | type 拼写错误（如 `Air`、`Ground`、`ship`） |
| `Invalid latitude/longitude value` | 参数名拼错，或值超出范围（纬度 ±90 / 经度 ±180）；lat/lon 是官方别名，无需强制使用完整单词 |
| `side 'xxx' does not exist` | 阵营未创建，或名称大小写不一致 |

---

## 参考知识库（生成代码前必须查阅）

| 资料 | 位置 | 用途 |
|------|------|------|
| Lua 函数参考 | `references/lua-api/index.md` | API 参数详解 |
| 数据类型参考 | `references/data-types/index.md` | latitude/longitude/altitude 等 |
| 常见 DBID 速查 | `references/dbid/index.md` | ⚠ 仅最常用装备速查，**大多数场景仍需 MCP 查询** |
| 报错记录库 | `errors/index.md` | 常见错误及解决方案 |
| 基础模板 | `templates/basic/` | add-aircraft.lua / add-ship.lua 等 |
| 高级模板 | `templates/advanced/` | patrol-mission.lua 等 |
| 官方案例 | `examples/official/` | 完整场景参考 |

---

## 输出前自审（必须执行）

每次生成 Lua 代码后，输出前必须逐项检查：

- [ ] `latitude` / `longitude` / `altitude` 参数名**正确**（lat/lon/alt 是官方别名，同样有效）
- [ ] `LoadoutID` 参数**存在且大写 L/I**，类型为**数值**
- [ ] `latitude` / `longitude` / `altitude` 参数名**完全正确**（lat/lon/alt 是官方支持的别名）
- [ ] `type` 为 `Aircraft` / `Ship` / `Submarine` / `Facility`（**非** Air/Ground）
- [ ] `dbid` 为**数值**，且通过 MCP 查询得到（非编造）
- [ ] 阵营 `side` 已在代码中通过 `ScenEdit_AddSide` 创建
- [ ] `errors/index.md` 中没有匹配到本次代码的问题
- [ ] 查询 MCP 时使用**英文**关键词

发现问题：**立即修正后再输出**。

---

## 输出成果保存位置

用户通过 Skill 生成的 Lua 代码，**保存到 `outputs/` 目录**：

```
outputs/
├── lua/          # Lua 脚本（命名为 [场景名]_[日期].lua）
├── config/       # 配置文件
└── docs/         # 说明文档
```

- **不要**将生成代码保存到 `templates/` 或 `examples/contributed/`
- `examples/contributed/` 仅接受通过审核的正式贡献案例

---

## 参考链接

- 官方 Lua 文档：https://commandlua.github.io/assets/Functions.html
- 网友案例：https://commandops.github.io/
