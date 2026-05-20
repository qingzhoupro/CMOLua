---
doc_id: CMO-SKILL-FAQ-001
title: FAQ 常见问题
description: 常见问题速查
---

# FAQ 常见问题

## Step 0.5: 教训速查入口

本文件是错误教训的快速查询入口。遇到具体问题时，直接查阅对应章节。

### 常见错误速查

| 错误现象 | 对应教训 | 快速链接 |
|---------|---------|---------|
| Aircraft 报错 Missing LoadoutID | LOADOUTID | → `.cursor/skills/cmo-unit/SKILL.md` |
| type="GroundUnit" 报错 | GROUND-UNIT-TYPE | → `.cursor/skills/cmo-unit/SKILL.md` |
| 坐标参数名报错 | LATITUDE-PARAM | → `.cursor/skills/cmo-unit/SKILL.md` |
| 飞机飞不起来 | ALTITUDE-UNIT | → `.cursor/skills/cmo-unit/SKILL.md` |
| Facility 放水里报错 | FACILITY-TERRAIN | → `.cursor/skills/cmo-unit/SKILL.md` |
| 空白场景添加单元报错 | SIDE-NOT-EXIST | → `.cursor/skills/cmo-side/SKILL.md` |
| 巡逻区引用错误 | MISSION-REF-POINT | → `.cursor/skills/cmo-mission/SKILL.md` |

详细教训 → `memory/cold/lesson-root-causes.md`

---

## 常见问题

### Q: MCP 工具不可用？

1. 检查 `.cursor/mcp.json` 存在
2. 重启 Cursor IDE
3. 确认 `mcp/intelligent_explorer.py` 可运行

### Q: DBID 查询返回空？

1. 确认拼写正确
2. 尝试自然语言查询
3. 检查是否为虚构单位

### Q: LoadoutID 查询失败？

```sql
SELECT ID FROM DataAircraftLoadouts WHERE ComponentID = {{DBID}};
```

### Q: NATO 查询返回空？

NATO (ID=2060) 是聚合组织标记，不是具体国家。
查询 NATO 装备 → 查询各成员国装备。

### Q: altitude 单位？

CMO 中 altitude 默认单位是**米**。
如果数据是英尺，需转换：英尺 ÷ 3.281 = 米

### Q: 如何添加阵营？

```lua
-- 官方 API: ScenEdit_AddSide({side = "阵营名"})
-- 仅支持 side 参数，name/posture 不存在!
ScenEdit_AddSide({side = "Blue Force"})
```

详细 → `.cursor/skills/cmo-side/SKILL.md`
