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
- **MCP 实时查 DBID**：连接真实 CMO 数据库
- **Command + Skill 双层架构**：精简入口 + 详细技能包
- **三层记忆体系**：HOT(会话) / WARM(项目) / COLD(知识)
- **模板库**：基础到高级，复制即用
- **错误教训库**：常见错误 + 解决方案

---

## 经验教学体系

CMO-HKBQSKILL 支持用户手动添加经验教学，通过三层架构实现渐进式防错：

### 三层架构

| 层级 | 目录 | 说明 |
|------|------|------|
| HOT | `memory/hot/` | 本会话激活的教训要点（临驻上下文） |
| WARM | `memory/warm/` | 近期高频教训记录（跨会话） |
| COLD | `memory/cold/` | 长期教训库（按根因归类） |

### 教训库

核心文件：

- `memory/cold/lesson-root-causes.md` — 教训本体（按 3 大根因分类）
- `memory/cold/lesson-index.md` — 教训索引（快速定位）

三大根因分类：

| 分类 | 说明 |
|------|------|
| Lua 幻觉 | AI 编造了不存在的 API/参数 |
| 地理坐标 | 经纬度/altitude 值或参数名错误 |
| 意图理解 | 未正确理解用户需求导致方向错 |

### 用户贡献

| 目录 | 说明 |
|------|------|
| `memory/user/01_个人经验/` | 个人原创经验 |
| `memory/user/02_成功案例/` | 验证通过的成功案例 |
| `memory/user/03_踩坑记录/` | 错误教训记录 |

使用模板 → `memory/TEMPLATES/`

### 错误收集命令

使用 `/cmo-errors` 命令收集错误教训：

```
/cmo-errors        # 交互式收集
/cmo-errors add    # 快速添加
/cmo-errors list   # 查看教训列表
/cmo-errors review # 复习近期教训
```

---

## 兼容 IDE


| IDE                | 支持情况     | 说明                                 |
| ------------------ | -------- | ---------------------------------- |
| Cursor             | MCP 自动连接 | 首次打开项目后自动加载                        |
| Trae               | MCP 兼容   | 需确认 Python 环境一致                    |
| VS Code + Continue | MCP 兼容   | 在 Continue 插件中配置                   |
| Claude Desktop     | MCP 兼容   | 在 `claude_desktop_config.json` 中配置 |


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
│   │   ├── cmo-check.md    # /cmo-check 代码自检
│   │   └── cmo-errors.md   # /cmo-errors 错误收集
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
├── references/              # 知识库
│   ├── lua-api/            # Lua API 参考
│   ├── data-types/         # 数据类型参考
│   └── dbid/               # DBID 速查
├── templates/               # Lua 模板
├── examples/               # 完整场景案例
├── errors/                  # 错误教训库
├── memory/                  # 三层记忆体系
│   ├── hot/                # 当前会话
│   ├── warm/               # 跨会话
│   ├── cold/               # 长期知识 (教训库)
│   │   ├── lesson-root-causes.md  # 教训本体
│   │   └── lesson-index.md        # 教训索引
│   ├── TEMPLATES/          # 用户贡献模板
│   ├── skill/              # Skill 优化追踪
│   └── user/                # 用户手动添加区
│       ├── 01_个人经验/
│       ├── 02_成功案例/
│       └── 03_踩坑记录/
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

## 更新日志

> 仅记录对用户有意义的功能性变更和已知限制。内部调试信息不予记录。

### 近期优化 (2026)

- 移除技能文件中所有绝对路径引用，改用相对路径
- 增强错误处理：增加常见报错速查表（含原因与解决方案）
- 示例代码增加 DBID 有效期免责声明
- 完善场景侦察流程引导
- 新增经验教学体系：三层架构 + 教训库 + Step 0.5 渐进嵌入
- 新增 `/cmo-errors` 命令：错误教训交互式收集
- 下一步计划：支持自动检测数据库版本并适配 DBID 偏移
- 下一步计划：增加更多任务类型（巡逻、攻击、护航）的模板

---

## 资料来源

- 官方 Lua 文档：[https://commandlua.github.io/assets/Functions.html](https://commandlua.github.io/assets/Functions.html)
- 网友案例：[https://commandops.github.io/](https://commandops.github.io/)

