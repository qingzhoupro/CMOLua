# CmoSkill

**Cursor / Trae / VSCode / Claude 系列 AI 助手的 CMO Lua 编程插件**

通过自然语言描述场景，自动生成 [Command: Modern Operations](https://www.matrixgames.com/game/command-modern-operations) 可运行的 Lua 代码。

---

## ✨ 功能

- 🗣️ **自然语言 → Lua**：描述场景，自动生成代码
- 🔍 **MCP 查 DBID**：连接 CMO 数据库，告别硬编码
- 📦 **模板库**：基础到高级，复制即用
- 🐛 **报错速查**：常见错误+解决方案

## 🚀 快速开始

```powershell
# 1. 克隆项目
git clone https://github.com/你的用户名/CmoSkill.git
cd CmoSkill

# 2. 安装依赖
pip install -r mcp/requirements.txt

# 3. 复制数据库（首次）
# 将 CMO 数据库文件复制到 mcp/db/DB3K_514.db3

# 4. 启动 MCP 服务
python mcp/server.py

# 5. 在 IDE 中加载 SKILL.md，开始对话
```

## 💡 示例

```
你：在日本海添加一架蓝方 MQ-9 无人机跟踪红方驱逐舰
AI：[自动查 DBID → 查 LoadoutID → 生成 Lua 代码]
```

## 🔧 兼容 IDE

| IDE | 支持情况 |
|-----|---------|
| Cursor | ✅ 完全支持（Skill 入口） |
| Trae | ✅ MCP 兼容 |
| VS Code + Continue | ✅ MCP 兼容 |
| Claude Desktop | ✅ MCP 兼容 |
| 其他 Claude 系列 | ✅ MCP 兼容 |

## 📁 项目结构

```
CmoSkill/
├── SKILL.md              # AI 助手行为规范（核心入口）
├── mcp/
│   ├── server.py         # MCP 服务端
│   ├── requirements.txt
│   └── db/DB3K_514.db3  # （需用户复制 CMO 数据库）
├── references/           # 知识库
│   ├── lua-api/
│   └── dbid/             # 常用 DBID 速查
├── templates/            # Lua 代码模板
├── examples/             # 案例库
└── errors/              # 报错记录库
```

## 📚 案例来源

本项目大量案例来自公众号 **「海空兵棋与AI」** Lua 编程系列文章，详见 [`examples/`](examples/)。

---

[📖 详细文档](README.md) · [🌐 English](README_en.md) · [📺 命令参考](https://commandlua.github.io/assets/Functions.html)

> 公众号 **「海空兵棋与AI」** 版权所有。商业授权请联系公众号。
