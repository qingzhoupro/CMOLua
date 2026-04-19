# 空战拦截案例

## 场景描述

蓝方在朝鲜半岛部署空军基地，红方从北方入侵。
蓝方部署 F-15C 执行空中截击（CAP），F-16C 执行对地打击。

## 场景参数

| 参数 | 值 |
|------|-----|
| 蓝方基地 | Osan AB (37.5, 127.0) |
| 拦截区域 | 4 个参考点定义的区域 |
| 红方入侵方向 | 北方 (130.0 经度) |

## 涉及函数

- `ScenEdit_AddUnit()` - 添加飞机单位
- `ScenEdit_AddMission()` - 创建任务
- `ScenEdit_SetMission()` - 设置任务参数
- `ScenEdit_AssignUnitToMission()` - 分配单位
- `ScenEdit_AddReferencePoint()` - 创建参考点
- `ScenEdit_SetDoctrine()` - 设置作战条令

## Lua 语法要点

1. **飞机类型**：使用 `type="Aircraft"` 或 `type="Air"`
2. **基地部署**：使用 `base="基地名称"` 而非经纬度
3. **挂载 ID**：`loadoutid` 必须匹配飞机类型
4. **CAP 任务**：`type="Strike"`, `subtype="AIR"`