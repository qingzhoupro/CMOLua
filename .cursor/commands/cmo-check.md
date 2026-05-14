---
doc_id: CMO-CMD-CHECK-001
trigger: /cmo-check
title: 代码自检
description: 检查生成的 Lua 代码是否符合规范
---

# /cmo-check - 代码自检

## 自检清单

- [ ] DBID 通过 MCP 验证
- [ ] Aircraft 有 LoadoutID
- [ ] type 参数正确
- [ ] 坐标参数名正确 (latitude/longitude)
- [ ] altitude 单位是米
- [ ] 阵营已创建

## 常见错误

| 错误 | 原因 |
|------|------|
| Missing 'LoadoutID' | Aircraft 缺少 LoadoutID |
| Invalid unit type | type 参数错误 |
| Invalid latitude/longitude | 坐标参数名错误 |

详细错误 → `errors/index.md`
