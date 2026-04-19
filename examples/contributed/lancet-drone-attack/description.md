# Lancet 巡飞弹攻击模拟

## 场景描述

模拟自杀式巡飞弹（Loitering Munition）对敌方高价值目标的攻击行为：
1. 检测敌方接触
2. 按名称关键词筛选目标
3. 接近后移动攻击弹并摧毁目标

## 适用场景

- 巡飞弹攻击演练
- 反炮兵作战
- 精确打击演示
- 无人系统作战

## 前置条件

- 攻击方拥有巡飞弹单位（Lancet、Hero 等）
- 目标方存在高价值目标
- 攻击方能探测到目标（己方接触列表中有目标）

## ⚠️ 重要限制

**GUID 必须从实际场景中获取**，每个想定中单位的 GUID 都不同。

### 如何获取单位 GUID

```lua
-- 方法 1：在 Lua 控制台查询单位
local u = ScenEdit_GetUnit({name = "{{UNIT_NAME}}"})
print("GUID: " .. u.guid)

-- 方法 2：获取所有单位列表
local units = VP_GetSide({Side = "{{SIDE}}"}).units
for i, v in ipairs(units) do
    local u = ScenEdit_GetUnit({guid = v.guid})
    print(v.guid .. " | " .. u.name .. " | " .. u.type)
end
```

## 核心函数

| 函数 | 说明 |
|------|------|
| `ScenEdit_GetContacts("Side")` | 获取敌方接触列表 |
| `Tool_Range(guid1, guid2)` | 计算两单位间距离（海里） |
| `ScenEdit_SetUnit({...})` | 移动单位到指定位置 |
| `ScenEdit_KillUnit({guid=})` | 摧毁单位 |
