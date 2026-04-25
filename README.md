# CMO-HKBQSKILL

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

文件名保持不变（如 `DB3K_514.db3`），无需重命名。

### 第三步：在终端运行安装向导

打开终端（PowerShell / CMD / Windows Terminal），cd 到项目目录，然后运行：

```powershell
python .\scripts\install.py
```

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
- **MCP 实时查 DBID**：连接真实 CMO 数据库，彻底告别硬编码 ID
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
├── SKILL.md                  # AI 行为规范（核心入口，IDE 加载此文件）
├── mcp/
│   ├── server.py             # MCP 服务端（6 个工具）
│   ├── requirements.txt
│   └── db/                  # 放入你的 DB3K_*.db3 文件
├── references/               # 知识库
│   ├── lua-api/             # Lua API 参考
│   ├── data-types/          # 数据类型参考（经纬度/高度等）
│   └── dbid/                # 常用 DBID 速查（仅辅助，不可替代 MCP）
├── templates/                # Lua 模板（basic/advanced/event/utility）
├── examples/                 # 完整场景案例
├── errors/                   # 常见错误及解决方案
└── scripts/
    ├── install.bat           # 一键安装向导（双击即可）
    └── start-mcp.ps1         # 启动 MCP 服务
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
