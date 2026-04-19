# 航母打击群案例 - 代码解析

## World_GetPointFromBearing 原理

```lua
World_GetPointFromBearing({
    LATITUDE  = lat,      -- 起点纬度
    LONGITUDE = lon,      -- 起点经度
    DISTANCE  = dist,     -- 距离（海里）
    BEARING   = angle     -- 方位角（度，从正北顺时针）
})
```

返回值：`{latitude = lat, longitude = lon}`

### 示例

```lua
-- 航母航向 0°（正北）
-- 在航母前方 40 海里处创建一个点
local pos = World_GetPointFromBearing({
    LATITUDE = CV.latitude,
    LONGITUDE = CV.longitude,
    DISTANCE = 40,
    BEARING = (CV_HEADING + 0) % 360
})
```

### 方位角换算

| 相对位置 | 方位角公式 |
|---------|-----------|
| 正前方 | `(heading + 0) % 360` |
| 右前方 30° | `(heading + 30) % 360` |
| 左前方 30° | `(heading + 330) % 360` |
| 正后方 | `(heading + 180) % 360` |

## 编队部署逻辑

1. **先创建航母**，获取其 `latitude`、`longitude`、`heading`
2. **计算属舰方位**：以航母为圆心，按战术距离和角度计算目标经纬度
3. **创建属舰**：传入计算后的经纬度，航向与航母一致

## group 属性

使用 `unit.group = name` 可将所有机场设施归组，同理可用于编队舰艇的分组管理。
