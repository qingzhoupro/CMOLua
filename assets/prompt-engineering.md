# Prompt 工程指南

## 概述

本指南帮助 AI 助手更好地理解用户意图并生成正确的 CMO Lua 代码。

## 常见查询模式

### 1. 添加单位

```
用户：添加一架 F-16 到 Blue 阵营
AI 应：
1. 调用 query_dbid("F-16") 获取 DBID
2. 参考 add-aircraft.lua 模板
3. 生成代码
```

### 2. 创建任务

```
用户：创建一个海上巡逻任务
AI 应：
1. 参考 create-mission.lua 模板
2. 设置 type="Patrol", subtype="NAVAL"
3. 提示设置巡逻区域
```

### 3. 设置阵营关系

```
用户：设置 Red 和 Blue 敌对
AI 应：
1. 调用 ScenEdit_SetSidePosture("Red", "Blue", "H")
2. 同时设置反向 ScenEdit_SetSidePosture("Blue", "Red", "H")
```

## 常见错误

### 1. 参数名错误

错误：`ScenEdit_AddUnit({Lat=24.5, Lon=118.0})`
正确：`ScenEdit_AddUnit({latitude="24.5", longitude="118.0"})`

### 2. DBID 错误

错误：使用猜测的 DBID
正确：通过 MCP `query_dbid()` 查询

### 3. 单位类型错误

错误：`type="Plane"`
正确：`type="Aircraft"`

### 4. 字符串引号

错误：`latitude='24.5'` (单引号可能有问题)
正确：`latitude="24.5"` 或 `latitude='24.5'`

## 调试技巧

### 1. 输出日志
```lua
print("Debug: " .. unit.name)
```

### 2. 检查单位存在
```lua
local u = ScenEdit_GetUnit({name="Unit Name"})
if u == nil then
    print("Unit not found")
end
```

### 3. 检查返回值
```lua
local result = ScenEdit_AddUnit({...})
print(result)
```

## 参考资料

- 函数参考：`references/lua-api/`
- 数据类型：`references/data-types/`
- 模板库：`templates/`