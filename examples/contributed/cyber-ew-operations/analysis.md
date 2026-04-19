# 网电作战案例 - 代码解析

## 核心概念：outOfComms

`outOfComms` 参数模拟网络中断效果：
- `"True"` = 单位断网，失去指挥控制
- `"False"` = 恢复正常通信

**注意**：CMO 中 `outOfComms` 是字符串类型，必须用引号。

## 场景 1 解析

```lua
ScenEdit_SetUnit({side = "{{SIDE}}", name = "{{UNIT_NAME}}", outOfComms = "True"})
```
- 遍历多个目标单位逐一断网
- 适用于破坏通信网络的电子战场景

## 场景 2 解析

```lua
ScenEdit_SetUnit({side = "{{SIDE}}", name = "{{RADAR_UNIT}}", outOfComms = "True"})
```
- 针对特定雷达系统的定向攻击
- 配合事件系统实现定时效果

## 事件触发恢复机制

```lua
ScenEdit_SetEvent("{{RECOVERY_EVENT_NAME}}", {IsActive = "True"})
```
- 事件激活后等待定时器触发
- 触发后执行恢复脚本并关闭事件

## 参数化版本优点

1. 代码复用性强
2. 易于修改目标列表
3. 适合作为通用工具函数
