# Lancet 无人机攻击案例 - 代码解析

## 核心逻辑流程

```
定期事件触发（1-5秒）
    │
    ▼
获取 Lancet 位置
    │
    ▼
获取所有敌方接触
    │
    ▼
遍历接触 → 名称匹配？
    │ 否
    └─── 继续遍历
    │ 是
    ▼
计算距离 ≤ 攻击范围？
    │ 否 → 提示距离太远
    │ 是
    ▼
移动 Lancet 到目标位置
    │
    ▼
摧毁 Lancet + 目标
```

## 关键函数

| 函数 | 作用 |
|------|------|
| `ScenEdit_GetUnit({guid=})` | 获取单位信息 |
| `ScenEdit_GetContacts("Side")` | 获取敌方接触列表 |
| `Tool_Range(guid1, guid2)` | 计算两单位间距离（海里） |
| `ScenEdit_SetUnit({...})` | 移动单位到指定位置 |
| `ScenEdit_KillUnit({guid=})` | 摧毁单位 |

## 参数化说明

| 参数 | 说明 |
|------|------|
| `{{ATTACKER_GUID}}` | 巡飞弹无人机唯一标识 |
| `{{TARGET_PATTERN}}` | 目标名称关键词（支持模糊匹配） |
| `{{ATTACK_RANGE}}` | 攻击距离（海里） |

## 事件设置建议

```
触发类型：定期时间
触发间隔：1-5 秒（根据场景调整）
动作：Lua 脚本 → LancetsAttack()
```
