# 自动搜索跟踪区域案例 - 代码解析

## autotrack() 函数原理

```
         name2 (lat2,lon2)
              ┌──────┐
              │      │
   name1 ────┤  ●   ├──── name4
(lat1,lon1)  │ target│  (lat4,lon4)
              │      │
              └──────┘
         name3 (lat3,lon3)
```

以目标位置为中心，计算正方形四个顶点：
- 顶点1：左上角（lat - range, lon - range）
- 顶点2：右上角（lat - range, lon + range）
- 顶点3：右下角（lat + range, lon + range）
- 顶点4：左下角（lat + range, lon - range）

## ScenEdit_SetReferencePoint vs ScenEdit_AddReferencePoint

- `AddReferencePoint` — 创建新的参考点
- `SetReferencePoint` — 更新已有参考点的坐标

本函数使用 `SetReferencePoint` 来实时更新位置，避免重复创建参考点。

## 事件触发建议

| 触发方式 | 适用场景 |
|---------|---------|
| 接触检测 | 发现新目标时立即调整 |
| 定期时间 | 持续跟踪移动目标 |
| 单位距离 | 目标进入某范围时触发 |
