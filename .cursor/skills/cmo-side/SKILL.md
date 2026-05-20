---
doc_id: CMO-SKILL-SIDE-001
title: Side 阵营技能
description: 阵营创建和管理，基于官方 CMO Lua API
references:
  - references/lua-api/Functions.md
  - references/lua-api/常用函数总结.md
---

# Side 阵营技能

> **重要：所有 API 用法必须以官方文档为准，不得编造函数名或参数格式。**
>
> 官方参考: `Functions.md` → `ScenEdit_AddSide` / `ScenEdit_SetSidePosture`

## Step 0.5: 经验教训查询（按需）

根据场景状态加载对应教训。

### 查询逻辑

1. 检查场景是否为空（无阵营）
2. 从 `memory/cold/lesson-index.md` 匹配教训 ID
3. 从 `memory/cold/lesson-root-causes.md` 加载相关教训
4. 注入到 `memory/hot/session.md`

### 场景状态 → 教训映射

| 场景状态 | 需加载的教训 ID |
|---------|----------------|
| 空白场景 | SIDE-NOT-EXIST, SIDE-API |
| 有场景上下文 | 跳过 Step 0.5（已有经验） |

### 空白场景必读教训

- **SIDE-NOT-EXIST**: 空白场景必须先创建阵营，再添加单元
- **SIDE-API**: `ScenEdit_AddSide` 仅支持 `{side="xxx"}` 参数

---

## 创建阵营

```lua
-- 官方 API: ScenEdit_AddSide({side = "阵营名"})
-- 参数: 仅支持 side (name/posture/orientation 不存在!)
ScenEdit_AddSide({side = "Red"})
ScenEdit_AddSide({side = "Blue"})
```

### 官方示例 (Functions.md)

```lua
ScenEdit_AddSide({side='OPFOR'})
```

## 设置阵营姿态

```lua
-- 官方 API: ScenEdit_SetSidePosture(sideA, sideB, posture)
-- 参数: 位置参数, 非表!
-- posture 值: 'F'=友方, 'H'=敌对, 'N'=中立, 'U'=不友好
ScenEdit_SetSidePosture("Red", "Blue", "H")
ScenEdit_SetSidePosture("Blue", "Red", "H")
```

### 官方示例 (常用函数总结.md)

```lua
ScenEdit_SetSidePosture("Red","Blue","H")
ScenEdit_SetSidePosture("Blue","Red","H")
ScenEdit_SetSidePosture("Green","Red","N")
ScenEdit_SetSidePosture("Green","Blue","N")
```

### 完整示例 (基于官方文档)

```lua
-- 创建红色阵营
ScenEdit_AddSide({side="Red"})
-- 创建绿色阵营
ScenEdit_AddSide({side="Green"})
-- 创建蓝色阵营
ScenEdit_AddSide({side="Blue"})

-- 设置红色阵营与蓝色阵营互为敌对关系
ScenEdit_SetSidePosture("Red","Blue","H")
ScenEdit_SetSidePosture("Blue","Red","H")

-- 设置绿色阵营与另两个阵营均互为中立关系
ScenEdit_SetSidePosture("Green","Red","N")
ScenEdit_SetSidePosture("Green","Blue","N")

print("The code is running successfully!")
```

## 检查 Side 是否存在

场景中的 side 可通过 `VP_GetSides()` 获取:

```lua
local sides = VP_GetSides()
for _, side in ipairs(sides) do
    print(side.name)
end
```

## 常见错误

| 错误写法 | 正确写法 |
|---------|---------|
| `ScenEdit_AddSide({name="Red", orientation="hostile"})` | `ScenEdit_AddSide({side="Red"})` |
| `ScenEdit_AddSide({name="Red", posture="H"})` | `ScenEdit_AddSide({side="Red"})` |
| `ScenEdit_SetSideRelations({side_a="Red", side_b="Blue", relation="H"})` | `ScenEdit_SetSidePosture("Red","Blue","H")` |
| `ScenEdit_AddSide({posture="H"})` (缺少 side) | `ScenEdit_AddSide({side="Red"})` |
