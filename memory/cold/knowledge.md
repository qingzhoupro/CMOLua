# COLD - 长期知识沉淀

> 成功案例、错误教训、最佳实践（永不删除）

## 成功案例

### 案例 1: F-16C 中队创建
```lua
ScenEdit_AddUnit({
  side = "Blue",
  type = "Aircraft",
  name = "F-16C #1",
  dbid = 1719,
  LoadoutID = 2230,
  latitude = 35.6762,
  longitude = 139.6503,
  altitude = 9144,
  heading = 0,
  speed = 500
})
```
**要点**: 必须有 LoadoutID，altitude 用米

### 案例 2: 舰艇创建
```lua
ScenEdit_AddUnit({
  side = "Blue",
  type = "Ship",
  name = "Arleigh Burke #1",
  dbid = 2275,
  latitude = 35.0,
  longitude = 140.0,
  heading = 90,
  speed = 20
})
```
**要点**: Ship 不需要 LoadoutID

## 错误教训

### 教训 1: Missing LoadoutID
**错误**: Aircraft 忘记加 LoadoutID
**解决**: Aircraft 总是需要 LoadoutID
**防止**: 自检清单第2项

### 教训 2: 硬编码 DBID
**错误**: 猜测 DBID 导致报错
**解决**: 总是通过 MCP 查询
**防止**: 自检清单第1项

### 教训 3: type 拼写
**错误**: type = "Air" 而非 type = "Aircraft"
**解决**: 记住5种有效 type 值
**防止**: 记住有效值列表

## 最佳实践

1. **MCP 优先**: 任何数据先查 MCP
2. **自检在后**: 输出前逐项检查
3. **错误归档**: 新错误立即记录
4. **模板复用**: 参考 templates/

## 数据库知识

### 枚举值速查
- NATO = 2060
- USA = 2
- China = 77
- Russia = 74

### 现役判断
```sql
WHERE YearDecommissioned = 0 AND Hypothetical = 'False'
```

### 非虚构判断
```sql
WHERE Hypothetical = 'False'
```
