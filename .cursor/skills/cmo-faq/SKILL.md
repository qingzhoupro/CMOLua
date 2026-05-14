---
doc_id: CMO-SKILL-FAQ-001
title: FAQ 常见问题
description: 常见问题速查
---

# FAQ 常见问题

## Q: MCP 工具不可用？

1. 检查 `.cursor/mcp.json` 存在
2. 重启 Cursor IDE
3. 确认 `mcp/intelligent_explorer.py` 可运行

## Q: DBID 查询返回空？

1. 确认拼写正确
2. 尝试自然语言查询
3. 检查是否为虚构单位

## Q: LoadoutID 查询失败？

```sql
SELECT ID FROM DataAircraftLoadouts WHERE ComponentID = {{DBID}};
```

## Q: NATO 查询返回空？

NATO (ID=2060) 是聚合组织标记，不是具体国家。
查询 NATO 装备 → 查询各成员国装备。

## Q: altitude 单位？

CMO 中 altitude 默认单位是**米**。
如果数据是英尺，需转换：英尺 ÷ 3.281 = 米

## Q: 如何添加阵营？

```lua
ScenEdit_AddSide({name = "Blue", side = "Blue Force"})
```

详细 → `.cursor/skills/cmo-side/SKILL.md`
