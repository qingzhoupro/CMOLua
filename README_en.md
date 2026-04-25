# CMO-HKBQSKILL

**Natural-language Lua script generator for Command: Modern Operations.**

Supports any IDE that implements MCP: Cursor, Trae, VS Code + Continue, Claude Desktop, and more.

---

## Features

- **Natural language → Lua**: Describe a scenario, get production-ready scripts
- **MCP live DBID lookup**: Connect to the live CMO database — no hardcoded IDs
- **Template library**: Basic to advanced, copy and run
- **Error reference**: Common errors with solutions

---

## Quick Start

### 1. Clone and install

```powershell
git clone https://github.com/qingzhoupro/CMOLua.git
cd CMO-HKBQSKILL
pip install -r mcp/requirements.txt
```

### 2. Add the database file (first time)

Copy your CMO database file from the game install directory:

```
<CMO game folder>/DB/DB3K_*.db3
        ↓  paste into ↓
this-project/mcp/db/DB3K_*.db3
```

Keep the original filename. `server.py` auto-discovers it.

### 3. Run the installer (first time)

```powershell
python .\scripts\install.py
```

The wizard runs through each setup step and prints a success banner at the end:

```
 ╔══════════════════════════════════════════════════════════╗
 ║                                                          ║
 ║   C M O - H K B Q S K I L L                            ║
 ║   =====================================                  ║
 ║                                                          ║
 ║      ALL SYSTEM STATUS : NOMINAL                        ║
 ║      MCP SERVER         : READY                         ║
 ║      DATABASE           : CONNECTED                     ║
 ║                                                          ║
 ╚══════════════════════════════════════════════════════════╝
```

### 4. Restart your IDE

MCP connects automatically when the IDE starts.

### 5. Verify

Ask the AI to look up a DBID in English, e.g.:

> "Query the DBID for F-16 fighter"

- Returns real data → MCP is ready
- Error → go back to step 1 and confirm the `.db3` file is in `mcp/db/`

---

## Compatible IDEs

| IDE | Support |
|-----|---------|
| Cursor | MCP auto-connects |
| Trae | MCP compatible |
| VS Code + Continue | MCP compatible |
| Claude Desktop | MCP compatible |

---

## Manual MCP Configuration (optional)

If your IDE does not auto-detect the MCP server, add this to its MCP config:

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

Config file locations:
- **Cursor**: `%APPDATA%\Cursor\User\mcp.json`
- **Trae**: `%APPDATA%\Trae\mcp.json`
- **VS Code**: `.vscode/settings.json`
- **Claude Desktop**: `%APPDATA%\Claude\claude_desktop_config.json`

---

## Project Structure

```
CMO-HKBQSKILL/
├── SKILL.md                  # AI behavior spec (load this file in your IDE)
├── mcp/
│   ├── server.py             # MCP server (6 tools)
│   ├── requirements.txt
│   └── db/                   # ← place your DB3K_*.db3 here
│       └── *.db3
├── references/               # Knowledge base
│   ├── lua-api/              # Lua API reference
│   ├── data-types/           # Data type reference
│   └── dbid/                 # Common DBID quick ref (auxiliary)
├── templates/                # Lua templates (basic/advanced/event/utility)
├── examples/                 # Complete scenario examples
├── errors/                   # Common errors and solutions
└── scripts/
    ├── install.ps1            # First-run wizard
    └── start-mcp.ps1          # Start MCP server
```

---

## Database Version

The version number in the filename (`DB3K_489`, `DB3K_514`, etc.) corresponds to the game build. Any `DB3K_*.db3` works — just put whichever version you have in the `mcp/db/` folder.

---

## FAQ

**"No module named fastmcp"**
Run `pip install -r mcp/requirements.txt` using the Python environment your IDE actually uses.

**MCP won't start**
1. Confirm a `.db3` file exists in `mcp/db/`
2. Confirm `pip install fastmcp` succeeded
3. Restart the IDE

**Database fields are in English — what language do I search in?**
Always translate to English before querying. For example, "Chinese destroyer" → `query_dbid("China destroyer")`.

---

## Links

- Official Lua docs: https://commandlua.github.io/assets/Functions.html
- Community cases: https://commandops.github.io/
