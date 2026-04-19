# 贡献指南

感谢您对本项目的关注！欢迎提交贡献。

---

## 贡献方式

### 方式一：提交案例

在 `examples/contributed/` 目录下创建新的案例文件夹：

```
examples/contributed/<案例名称>/
├── description.md    # 场景描述
├── lua-script.lua   # Lua 代码
└── analysis.md       # 代码解析（可选）
```

### 方式二：改进现有案例

- 修正代码错误
- 添加更详细的注释
- 补充分析文档
- 更新占位符为更通用的写法

### 方式三：反馈问题

通过 GitHub Issues 反馈：
- 代码在特定 CMO 版本下不兼容
- 文档描述不清
- 功能缺失

---

## 代码规范

### 文件头部

每个 `lua-script.lua` 文件顶部必须包含许可证头：

```lua
--[[
  File: examples/contributed/<案例名>/lua-script.lua
  License: CC BY-NC-ND 4.0
  Copyright (c) 2019-2026海空兵棋与AI
  
  Third-Party Acknowledgments:
  - [如有参考，注明来源和链接]
  
  Disclaimer:
  - CMO and its database are copyrighted by Matrix Games Ltd.
  - This project uses CMO's public Lua scripting API only.
--]]
```

### 硬编码要求

- **禁止**在代码中硬编码：
  - 具体的单位名称（Ukraine、Red、Blue 等真实地名/阵营名）
  - 具体的 DBID 数字
  - 具体的 GUID
  - 具体的经纬度
- **必须**使用 `{{PLACEHOLDER}}` 格式占位，并在文件顶部注释说明

### 示例

```lua
-- ✅ 正确：使用占位符
ScenEdit_SetUnit({side = "{{SIDE}}", name = "{{UNIT_NAME}}", outOfComms = "True"})

-- ❌ 错误：硬编码真实地名
ScenEdit_SetUnit({side = "Ukraine", name = "Radar #1", outOfComms = "True"})
```

---

## 提交流程

1. **Fork** 本仓库
2. 创建您的分支（`git checkout -b contrib/<案例名>`）
3. 提交代码（确保包含许可证头）
4. 提交 Pull Request
5. 等待维护者审核

---

## 内容要求

贡献的内容应满足以下条件：

1. **原创性**：代码为原创，或已注明参考来源
2. **可运行**：代码逻辑正确，占位符仅需替换即可运行
3. **有说明**：`description.md` 包含足够的上下文说明
4. **无隐私**：不包含任何个人联系信息（微信号、邮箱等）
5. **合规性**：不包含 CMO 官方数据库的版权内容

---

## 案例命名规范

- 使用英文或拼音（避免中文目录名兼容问题）
- 使用小写字母和连字符
- 示例：`auto-track-zone`、`psyop-defection`

---

## 许可证说明

提交贡献即表示您同意：
- 您的代码遵循 **CC BY-NC-ND 4.0** 许可证
- 项目维护者可在必要时调整许可证条款
- 您的贡献可用于海空兵棋与AI 的知识星球等付费内容

---

## 联系我们

- 公众号：**海空兵棋与AI**
- 知识星球：**兵推圈**（通过公众号获取加入方式）
- GitHub Issues：报告问题或提出建议

> 注意：请勿在 GitHub 上提交包含个人联系方式的内容。
