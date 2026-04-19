# Lua 模板索引

## 概述

本目录包含 CMO Lua 代码模板，使用 `{{变量名}}` 格式标记可替换内容。

## 模板分类

### 基础模板 (basic/)

基础单位创建和操作模板：
- `create-side.lua` - 创建阵营
- `add-unit.lua` - 添加单位（通用）
- `add-aircraft.lua` - 添加飞机
- `add-ship.lua` - 添加舰艇
- `add-submarine.lua` - 添加潜艇
- `add-facility.lua` - 添加设施
- `create-mission.lua` - 创建任务
- `reference-point.lua` - 创建参考点

### 高级模板 (advanced/)

复杂任务模板：
- `patrol-mission.lua` - 巡逻任务
- `strike-mission.lua` - 打击任务
- `escort-mission.lua` - 护航任务
- `cargo-mission.lua` - 运输任务
- `minefield.lua` - 布雷任务
- `submarine-patrol.lua` - 潜艇巡逻
- `airbase.lua` - 完整空军基地

### 事件模板 (event/)

事件响应模板：
- `time-trigger.lua` - 时间触发器
- `unit-destroyed.lua` - 单位被摧毁
- `contact-detected.lua` - 发现目标
- `special-action.lua` - 特殊动作
- `condition-action.lua` - 条件-动作对

### 工具模板 (utility/)

常用工具函数：
- `remove-sensor.lua` - 移除传感器
- `set-emcon.lua` - 设置电磁管控
- `set-doctrine.lua` - 设置条令
- `unit-loop.lua` - 单位遍历
- `get-unit-info.lua` - 获取单位信息
- `message-box.lua` - 消息框

## 使用方法

### 1. 选择模板

根据需求选择合适的模板文件。

### 2. 替换变量

将 `{{变量名}}` 替换为实际值：
- `{{SIDE}}` → "Blue"
- `{{UNIT_NAME}}` → "F-16 #1"
- `{{DBID}}` → 1234

### 3. 添加 DBID

使用 MCP 工具查询正确的 DBID：
```
用户：查询 F-16 的 DBID
AI：调用 query_dbid("F-16") 返回结果
```

### 4. 测试代码

在 CMO Lua Console 中测试生成的代码。

## 示例

原始模板：
```lua
ScenEdit_AddUnit({
    side = '{{SIDE}}',
    type = 'Aircraft',
    name = '{{UNIT_NAME}}',
    dbid = {{DBID}},
    LoadoutID = {{LOADOUT_ID}},
    latitude = '{{LATITUDE}}',
    longitude = '{{LONGITUDE}}',
    altitude = '{{ALTITUDE}}'
})
```

替换后：
```lua
ScenEdit_AddUnit({
    side = 'Blue',
    type = 'Aircraft',
    name = 'F-16 #1',
    dbid = 3785,
    LoadoutID = 332,
    latitude = '24.587',
    longitude = '118.021',
    altitude = '5000'
})
```

## 贡献指南

用户可贡献新模板：
1. 编写可运行的 Lua 代码
2. 提取可变量替换为 `{{变量名}}` 格式
3. 添加说明注释
4. 保存到 `templates/basic/` 或适当分类