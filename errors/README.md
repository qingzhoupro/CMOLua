# Errors 目录

## 结构

| 文件 | 说明 |
|------|------|
| `index.md` | 错误总索引 |
| `missing-loadoutid.md` | Missing LoadoutID 错误 |
| `invalid-dbid.md` | Invalid DBID 错误 |
| `invalid-type.md` | Invalid unit type 错误 |
| `invalid-coords.md` | Invalid coordinates 错误 |
| `side-not-found.md` | Side not found 错误 |

## 使用流程

1. 遇到新错误 → 查找 `index.md`
2. 找到错误类型 → 查看对应文件
3. 找到解决方案 → 修复代码
4. 如果是新错误 → 追加到 `index.md`

## 更新规则

每次遇到 CMO Lua 错误：
1. 先查 `index.md` 是否已有
2. 如果没有，追加新错误到 `index.md`
3. 可选：创建独立文件详细记录
