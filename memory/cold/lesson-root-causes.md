# 教训库 - 按根因归类

> AI 生成 Lua 代码时常见错误，按根因分为三大类。
> 单个教训格式：
> **教训-NAME** | 触发条件 | 错误信息 | 正确做法 | 自检项

---

## [全局教训]（所有功能通用）

**教训-GROUND-UNIT-TYPE** | 使用 GroundUnit/Ground Unit/GROUNDUNIT | Invalid unit type | `type = "GROUND UNIT"`（全大写+空格） | type 参数全大写

**教训-LOADOUTID** | Aircraft 类型 | Missing LoadoutID | Aircraft 必须通过 MCP 查 LoadoutID | 检查 LoadoutID 存在且大写

**教训-LATITUDE-PARAM** | 坐标参数 | Invalid latitude/longitude | `latitude`/`longitude`（全小写）| 参数名检查

**教训-ALTITUDE-UNIT** | altitude 赋值 | 飞机飞不起来 | altitude 默认单位是米，不加后缀默认米 | altitude 值合理范围

**教训-DEPRECATED-DBID** | 硬编码 DBID | deprecated in the database | 必须通过 MCP 查询，不编造 | DBID MCP 验证

---

## [阵营创建] (cmo-side)

**教训-SIDE-NOT-EXIST** | 未建阵营就添加单元 | Side 'xxx' doesn't exist | 空白场景必须先 `ScenEdit_AddSide({side="xxx"})` 再 `ScenEdit_AddUnit` | 空白场景检查阵营顺序

**教训-SIDE-API** | 编造 AddSide 参数 | Side not created | 仅 `{side="xxx"}`，无 name/posture 参数 | API 格式检查

---

## [单元操作] (cmo-unit)

**教训-FACILITY-TERRAIN** | Facility 放在水中 | This point appears to be underwater | 改用 GROUND UNIT 或 Category 4050水中设施 | Facility 坐标地形检查

---

## [任务操作] (cmo-mission)

**教训-MISSION-REF-POINT** | 巡逻区引用错误 | 参考点不存在 | 先查场景已有参考点名称 | 参考点存在性检查

---

## 用户添加教训

> 格式：`**教训-ID** | 触发条件 | 错误信息 | 正确做法 | 自检项`

示例：

```markdown
**教训-MY-CUSTOM** | 使用自定义关键词 | 错误信息 | 正确做法 | 自检项
```

添加后需同步更新 `lesson-index.md` 索引。
