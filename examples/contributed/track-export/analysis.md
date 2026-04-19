# 轨迹导出案例 - 代码解析

## 输出数据字段

| 字段 | 说明 |
|------|------|
| Name | 单位名称 |
| Latitude | 纬度 |
| Longitude | 经度 |
| Altitude | 高度（英尺） |
| Heading | 航向（度） |
| Speed | 速度（节） |
| Time | 时间戳 |

## CSV 导出步骤

1. **运行想定**，让轨迹记录器收集数据
2. **打开 Lua 控制台**
3. **执行** `PrintTrackDataAsCSV()`
4. **复制** 所有输出行
5. **粘贴** 到文本编辑器，保存为 `.csv`
6. **用 Excel 打开**

## 事件设置

```
事件类型：定期时间触发
间隔：30秒（或根据需要）
动作：RecordTrackData("{{AIRCRAFT_NAME}}")
```

## 数据管理

```lua
-- 查看已记录条数
print(#TrackData.records)

-- 清除数据（重新开始）
ClearTrackData()

-- 导出
PrintTrackDataAsCSV()
```
