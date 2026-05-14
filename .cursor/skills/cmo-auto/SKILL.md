---
doc_id: CMO-SKILL-AUTO-001
title: CMO 自动生成工作流
description: 完整的 CMO Lua 代码生成工作流
---

# CMO 自动生成工作流

## 流程概览

```
用户请求 → MCP验证 → 数据查询 → 代码生成 → 自检 → 输出
```

## Step 0: MCP 验证

```python
cmo_intelligent_query("测试查询")
```
失败则终止。

## Step 1: 解析需求

- 单位类型： Aircraft / Ship / Submarine / Facility / GroundUnit
- 阵营： Blue / Red / Green / Neutral
- 位置： 手动指定或从需求推断

## Step 2: 数据查询

```python
# 获取 DBID
cmo_intelligent_query("F-16C 战斗机的 DBID")

# 获取 LoadoutID（仅 Aircraft）
cmo_query("F-16C 的默认挂载")
```

## Step 3: 生成代码

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

## Step 4: 自检

- [ ] DBID 验证
- [ ] LoadoutID 存在
- [ ] type 正确
- [ ] 坐标参数
- [ ] altitude 单位

## Step 5: 错误处理

错误 → `errors/index.md` 查找解决方案
