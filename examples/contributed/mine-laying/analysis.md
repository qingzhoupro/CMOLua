# 布雷案例 - 代码解析

## ScenEdit_AddMinefield() 参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `side` | string | 布雷方阵营 |
| `dbid` | number | 水雷数据库 ID |
| `number` | number | 布雷数量 |
| `delay` | number | 布雷延迟（毫秒） |
| `area` | table | 参考点名称数组（4个点） |

## 返回值

布雷函数返回实际布雷数量（数字），可用于验证布雷是否成功。

## 水雷 DBID 查询

```lua
-- 使用 MCP 查询水雷 DBID
-- query_dbid("水雷") 或 query_dbid("mine")
```

## 布雷延迟 delay

- `delay = 60000` = 60秒延迟布雷
- 延迟布雷适合模拟布雷载机飞行到目标区域所需时间
