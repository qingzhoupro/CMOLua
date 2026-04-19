# CmoSkill

**CMO Lua programming plugin for Cursor / Trae / VSCode / Claude AI assistants**

Generate runnable [Command: Modern Operations](https://www.matrixgames.com/game/command-modern-operations) Lua scripts from natural language descriptions.

---

## ✨ Features

- 🗣️ **Natural language → Lua**: Describe a scenario, get production-ready code
- 🔍 **MCP DBID lookup**: Connect to live CMO database, no hardcoded IDs
- 📦 **Template library**: From basic to advanced, copy and run
- 🐛 **Error reference**: Common errors with solutions

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/your-username/CmoSkill.git
cd CmoSkill

# 2. Install dependencies
pip install -r mcp/requirements.txt

# 3. Copy database (first time only)
# Copy CMO database file to mcp/db/DB3K_514.db3

# 4. Start MCP server
python mcp/server.py

# 5. Load SKILL.md into your IDE, start chatting
```

## 💡 Example

```
You: Add a Blue MQ-9 drone tracking a Red destroyer in the Sea of Japan
AI: [query DBID → query LoadoutID → generate Lua code]
```

## 🔧 Compatible IDEs

| IDE | Support |
|-----|---------|
| Cursor | ✅ Full (Skill entry) |
| Trae | ✅ MCP compatible |
| VS Code + Continue | ✅ MCP compatible |
| Claude Desktop | ✅ MCP compatible |
| Other Claude family | ✅ MCP compatible |

## 📁 Project Structure

```
CmoSkill/
├── SKILL.md              # AI assistant behavior spec (core entry)
├── mcp/
│   ├── server.py         # MCP server
│   ├── requirements.txt
│   └── db/DB3K_514.db3  # (user copies CMO database here)
├── references/           # Knowledge base
│   ├── lua-api/
│   └── dbid/             # Common DBID quick reference
├── templates/           # Lua code templates
├── examples/            # Case library
└── errors/             # Error reference
```

## 📚 Case Library

Cases sourced from the WeChat public account **海空兵棋与AI** Lua programming series. See [`examples/`](examples/).

---

[📖 Documentation](README.md) · [🌐 中文](README.md) · [📺 Command Reference](https://commandlua.github.io/assets/Functions.html)
