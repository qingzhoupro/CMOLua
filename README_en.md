# CMO-HKBQSKILL

> **First time? Just 3 steps, 3 minutes to get started.**

Supports any IDE that implements the MCP protocol: Cursor, Trae, VS Code + Continue, Claude Desktop, and more.

---

## First-Time Setup (3 Steps)

### Step 1: Clone the Project

```powershell
git clone https://github.com/qingzhoupro/CMOLua.git
cd CMOLua
```

### Step 2: Add the Database File

Copy your CMO database file to the project:

```
<CMO game folder>/DB/DB3K_*.db3
        ↓  paste into ↓
this-project/mcp/db/DB3K_*.db3
```

Keep the original filename (e.g., `DB3K_499.db3`). No renaming needed.

### Step 3: Run the Installation Wizard

Open a terminal (PowerShell / CMD / Windows Terminal), navigate to the project directory, and run:

```powershell
python .\scripts\install.py
```

> Do not double-click the .py file — it will exit immediately. Run it from the terminal to see interactive feedback.

After successful installation, you will see:

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

Then restart your IDE and start chatting.

---

## Features

- **Natural language → Lua**: Describe a scenario, get production-ready scripts
- **MCP live DBID lookup**: Connect to the live CMO database — query "Iranian Revolutionary Guard latest missile boat, return its DBID and anti-ship weapon type"
- **Template library**: Basic to advanced, copy and run
- **Error reference**: Common errors with solutions

---

## Compatible IDEs

| IDE | Support | Notes |
|-----|---------|-------|
| Cursor | MCP auto-connects | Loads automatically after first project open |
| Trae | MCP compatible | Confirm Python environment matches |
| VS Code + Continue | MCP compatible | Configure in Continue extension |
| Claude Desktop | MCP compatible | Configure in `claude_desktop_config.json` |

---

## Manual MCP Configuration (Optional)

If your IDE does not auto-detect the MCP server, add this to its config file:

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
- **VS Code**: `.vscode/settings.json` (under `"mcpServers"`)
- **Claude Desktop**: `%APPDATA%\Claude\claude_desktop_config.json`

---

## Project Structure

```
CMO-HKBQSKILL/
├── SKILL.md                  # AI behavior spec (core entry point)
├── mcp/
│   ├── server.py             # MCP server (6 tools)
│   ├── requirements.txt
│   └── db/                   # ← place your DB3K_*.db3 here
├── references/               # Knowledge base
│   ├── lua-api/              # Lua API reference
│   ├── data-types/           # Data type reference (lat/lon/altitude)
│   └── dbid/                 # Common DBID quick ref (auxiliary, not a substitute for MCP)
├── templates/                # Lua templates (basic/advanced/event/utility)
├── examples/                 # Complete scenario examples
├── errors/                   # Common errors and solutions
└── scripts/
    ├── install.py           # Installation wizard (main entry point)
    ├── config.py            # Database configuration utility
    ├── check-deps.ps1       # Dependency checker
    ├── scan_database.py     # Database scanner
    ├── export_table_schemas.py # Schema exporter
    ├── uninstall.ps1        # Uninstaller
    └── validate-structure.ps1 # Structure validator
```

---

## Database Version

The version number in the filename (`DB3K_489`, `DB3K_514`, etc.) corresponds to the game build. Any `DB3K_*.db3` file works — just put whichever version you have in the `mcp/db/` folder.

---

## FAQ

**"No module named fastmcp"**
Make sure `pip install -r mcp/requirements.txt` was installed to the Python environment your IDE uses. Windows Cursor typically uses `C:\Program Files\Python313\python.exe`.

**MCP won't start**

1. Confirm a `.db3` file exists in `mcp/db/`
2. Confirm `pip install fastmcp` succeeded
3. Restart the IDE

---

## Resources

- Official Lua docs: https://commandlua.github.io/assets/Functions.html
- Community cases: https://commandops.github.io/
