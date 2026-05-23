---
doc_id: CMO-SESSION-HOT-001
title: Hot Session State
description: 当前会话的运行时状态，包含防错提醒和上下文
created: 2026-05-23
---

# Hot Session State

## 本次防错提醒

- GroundUnit type 必须为 `"GROUND UNIT"`（全大写+空格），禁止 `GroundUnit`/`GROUNDUNIT`
- DBID 已通过 MCP 验证（202, 2434, 3240）
- ScenEdit_AddUnit 坐标参数使用 `latitude`/`longitude`（非 lat/lon）
- 空白场景先 `ScenEdit_AddSide` 再 `ScenEdit_AddUnit`
- ScenEdit_SetSidePosture 使用位置参数：`("SideA", "SideB", "H")`

## 会话信息

- 用户请求：从朝鲜半岛远程火箭炮打击陆上目标场景
- 场景类型：空白场景
- 涉及单位：GROUND UNIT（火箭炮）、Facility/Marker（目标）
