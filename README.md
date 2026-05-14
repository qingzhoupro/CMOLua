---
doc_id: CMO-README-001
title: CMO-HKBQSKILL 项目说明
description: CMO 兵棋 Lua 代码生成的 AI 助手项目
version: 1.0.0
updated: 2026-05-14
tags:
  - CMO
  - Lua
  - MCP
  - 兵棋
---

# CMO-HKBQSKILL

> [English](README_en.md) | 中文

> **第一次用？只需要 3 步，3 分钟搞定。**

支持 Cursor / Trae / VSCode + Continue / Claude Desktop 等所有实现了 MCP 协议的 IDE。

---

## 第一次使用（3 步）

### 第一步：克隆项目

```powershell
git clone https://github.com/qingzhoupro/CMOLua.git
cd CMOLua
```

### 第二步：放入数据库文件

从你的 CMO 游戏目录复制数据库文件到本项目：

```
<CMO游戏目录>/DB/DB3K_*.db3
        复制到
本项目/mcp/db/DB3K_*.db3
```

文件名保持不变（如 `DB3K_499.db3`），无需重命名。

### 第三步：在终端运行安装向导

打开终端（PowerShell / CMD / Windows Terminal），cd 到项目目录，然后运行：

```powershell
python .\scripts\install.py
```

> ⚠️ **重要**：确保在 IDE 中打开的文件夹是项目的**根目录**。打开后 IDE 文件列表应该**直接看到** `assets`、`database_schema`、`scripts` 等子文件夹才对。

> 不要双击 py 文件，双击会闪退。在终端里输入命令才能看到交互反馈。

安装成功后显示：

```
 +------------------------------------------------------+
 |                                                      |
 |   C M O - H K B Q S K I L L                        |
 |   ===================================                |
 |                                                      |
 |   ALL SYSTEM STATUS : NOMINAL                        |
 |   MCP SERVER         : READY                         |
 |   DATABASE           : CONNECTED                     |
 |                                                      |
 |   Next: Restart IDE, load SKILL.md                  |
 |                                                      |
 +------------------------------------------------------+
```

然后重启 IDE，开始对话即可。

---

## 功能

- **自然语言 → Lua**：描述场景，生成可运行的脚本
- **MCP 实时查 DBID**：连接真实 CMO 数据库，如“用MCP查询伊朗革命卫队最新导弹快艇，返回快艇DBID和反舰武器型号”
- **模板库**：基础到高级，复制即用
- **报错速查**：常见错误 + 解决方案

---

## 兼容 IDE

| IDE                | 支持情况     | 说明                                     |
| ------------------ | ------------ | ---------------------------------------- |
| Cursor             | MCP 自动连接 | 首次打开项目后自动加载                   |
| Trae               | MCP 兼容     | 需确认 Python 环境一致                   |
| VS Code + Continue | MCP 兼容     | 在 Continue 插件中配置                   |
| Claude Desktop     | MCP 兼容     | 在 `claude_desktop_config.json` 中配置 |

---

## MCP 手动配置（可选）

如果 IDE 没有自动检测到 MCP，在对应配置文件中添加：

```json
{
  "mcpServers": {
    "CMO_DBID_Lookup": {
      "command": "python",
      "args": ["-m", "fastmcp", "run", "mcp/server.py"]
    }
  }
}
```

配置文件位置：

- **Cursor**: `%APPDATA%\Cursor\User\mcp.json`
- **Trae**: `%APPDATA%\Trae\mcp.json`
- **VS Code**: `.vscode/settings.json`（在 `"mcpServers"` 下）
- **Claude Desktop**: `%APPDATA%\Claude\claude_desktop_config.json`

---

## 项目结构

```
CMO-HKBQSKILL/
├── SKILL.md                  # AI 行为规范（核心入口）
├── .cursor/
│   ├── commands/             # 命令入口
│   │   ├── cmo.md          # /cmo 主命令
│   │   ├── cmo-unit.md     # /cmo-unit 快速添加单位
│   │   ├── cmo-query.md    # /cmo-query 数据库查询
│   │   ├── cmo-mission.md  # /cmo-mission 任务生成
│   │   └── cmo-check.md    # /cmo-check 代码自检
│   ├── skills/              # 技能包
│   │   ├── cmo-auto/       # 完整工作流
│   │   ├── cmo-query/     # DBID 查询
│   │   ├── cmo-unit/      # Unit 操作
│   │   ├── cmo-side/      # Side 阵营
│   │   ├── cmo-mission/   # Mission 任务
│   │   ├── cmo-debug/     # Debug 调试
│   │   └── cmo-faq/       # 常见问题
│   └── mcp.json           # MCP 配置
├── mcp/
│   ├── server.py            # MCP 服务端
│   ├── requirements.txt
│   └── db/                  # DB3K_*.db3 文件
├── memory/                  # 三层记忆体系
│   ├── hot/                # 当前会话
│   ├── warm/               # 跨会话
│   └── cold/               # 长期知识
├── references/              # 知识库
│   ├── lua-api/            # Lua API 参考
│   ├── data-types/         # 数据类型参考
│   └── dbid/               # DBID 速查
├── templates/               # Lua 模板
├── examples/               # 完整场景案例
├── errors/                  # 错误教训库
└── scripts/
    └── install.py          # 安装向导
```

---

## 数据库版本说明

CMO 数据库文件名中的版本号（如 `DB3K_489`、`DB3K_514`）对应游戏版本。只要是 `DB3K_*.db3` 格式，任意版本均可使用。放入哪个版本就用哪个。

---

## 常见问题

**报错 "No module named fastmcp"**
请确认 `pip install -r mcp/requirements.txt` 安装到了 IDE 使用的 Python 环境。Windows Cursor 通常在 `C:\Program Files\Python313\python.exe`。

**MCP 服务无法启动**

1. 确认 `mcp/db/` 目录下有 `.db3` 文件
2. 确认 `pip install fastmcp` 成功
3. 重启 IDE

---

## 资料来源

- 官方 Lua 文档：https://commandlua.github.io/assets/Functions.html
- 网友案例：https://commandops.github.io/
