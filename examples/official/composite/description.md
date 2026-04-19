# 合成作战案例

## 场景描述

蓝方执行两栖登陆作战，整合海军航母编队、鹞式攻击机、F-35B 战斗机、直升机和登陆部队。
红方部署防空导弹和岸防炮进行防御。

## 场景参数

| 参数 | 值 |
|------|-----|
| 蓝方编队位置 | (35.0, 140.0) |
| 登陆点 | (35.2, 140.3) |
| 红方防御区域 | (35.3, 140.4) |

## 涉及函数

- `ScenEdit_AddUnit()` - 添加海军、空军、陆军单位
- `ScenEdit_AddMission()` - 创建打击和支援任务
- `ScenEdit_AssignUnitToMission()` - 分配单位到任务
- `ScenEdit_SetDoctrine()` - 设置作战条令
- `ScenEdit_SetEvent()` - 创建损失报告事件

## Lua 语法要点

1. **Facility 作为地面单位**：地面单位使用 `type="Facility"`
2. **group 属性**：用于组织和管理
3. **多类型任务配合**：Strike + Support + Cargo
4. **事件系统**：追踪单位损失和分数变化