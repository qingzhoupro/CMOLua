# CMO-HKBQSKILL

> [English](README_en.md) | [中文](README.md)

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

> ⚠️ **Important**: Make sure the folder you open in your IDE is the **root directory**. You should **directly see** subfolders like `assets`, `database_schema`, `scripts` in the file list.

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
- **MCP live DBID lookup**: Connect to the live CMO database
- **Command + Skill dual-layer**: Compact entry + detailed skill packages
- **Three-tier memory**: HOT(session) / WARM(project) / COLD(knowledge)
- **Template library**: Basic to advanced, copy and run
- **Error lessons**: Common errors with solutions

---

## Experience-Based Teaching System

CMO-HKBQSKILL supports user-contributed experience teaching through a three-tier architecture for progressive error prevention:

### Three-Tier Architecture

| Tier | Directory | Description |
|------|----------|-------------|
| HOT | `memory/hot/` | Active lessons for current session (transient context) |
| WARM | `memory/warm/` | Recent high-frequency lessons (cross-session) |
| COLD | `memory/cold/` | Long-term lesson library (organized by root cause) |

### Lesson Library

Core files:

- `memory/cold/lesson-root-causes.md` — Lesson body (categorized by 3 root causes)
- `memory/cold/lesson-index.md` — Lesson index (quick lookup)

Three root cause categories:

| Category | Description |
|----------|-------------|
| Lua Hallucination | AI fabricated non-existent APIs/parameters |
| Geo Coordinates | Latitude/longitude or altitude values or parameter names are wrong |
| Intent Misunderstanding | AI misunderstood user requirements leading to wrong direction |

### User Contributions

| Directory | Description |
|----------|-------------|
| `memory/user/01_个人经验/` | Personal original experience |
| `memory/user/02_成功案例/` | Verified successful cases |
| `memory/user/03_踩坑记录/` | Error lesson records |

Templates → `memory/TEMPLATES/`

### Error Collection Command

Use `/cmo-errors` command to collect error lessons:

```
/cmo-errors         # Interactive collection
/cmo-errors add     # Quick add
/cmo-errors list    # View lesson list
/cmo-errors review  # Review recent lessons
```

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
├── .cursor/
│   ├── commands/             # Command entry points
│   │   ├── cmo.md          # /cmo main command
│   │   ├── cmo-unit.md     # /cmo-unit quick add unit
│   │   ├── cmo-query.md    # /cmo-query database query
│   │   ├── cmo-mission.md  # /cmo-mission mission generation
│   │   ├── cmo-check.md    # /cmo-check code self-check
│   │   └── cmo-errors.md   # /cmo-errors error collection
│   ├── skills/              # Skill packages
│   │   ├── cmo-auto/       # Complete workflow
│   │   ├── cmo-query/     # DBID query
│   │   ├── cmo-unit/       # Unit operations
│   │   ├── cmo-side/       # Side/forces
│   │   ├── cmo-mission/    # Mission creation
│   │   ├── cmo-debug/      # Debug & troubleshooting
│   │   └── cmo-faq/        # FAQ
│   └── mcp.json            # MCP configuration
├── mcp/
│   ├── server.py            # MCP server
│   ├── requirements.txt
│   └── db/                  # ← place your DB3K_*.db3 here
├── memory/                 # Three-tier memory system
│   ├── hot/                # Current session
│   ├── warm/               # Cross-session
│   ├── cold/               # Long-term (lesson library)
│   │   ├── lesson-root-causes.md  # Lesson body
│   │   └── lesson-index.md        # Lesson index
│   ├── TEMPLATES/         # User contribution templates
│   ├── skill/              # Skill optimization tracking
│   └── user/               # User manual addition area
│       ├── 01_个人经验/
│       ├── 02_成功案例/
│       └── 03_踩坑记录/
├── references/              # Knowledge base
│   ├── lua-api/            # Lua API reference
│   ├── data-types/         # Data type reference
│   └── dbid/               # DBID quick reference
├── templates/               # Lua templates
├── examples/                # Complete scenario examples
├── errors/                  # Error lessons library
└── scripts/
    └── install.py          # Installation wizard
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

## Changelog

> Only functional changes and known limitations that affect users are recorded. Internal debugging notes are excluded.

### Recent Optimizations (2026)

- [x] Removed all absolute path references from skill files, replaced with relative paths
- [x] Enhanced error handling: added quick-reference table with causes and solutions
- [x] Added disclaimer for DBID example expiry in sample code
- [x] Improved scenario scout flow guidance
- [x] New experience-based teaching system: three-tier architecture + lesson library + Step 0.5 progressive embedding
- [x] New `/cmo-errors` command: interactive error lesson collection
- [ ] Planned: auto-detect database version and adapt DBID offsets
- [ ] Planned: expand template library with more mission types (patrol, attack, escort)

---

## Resources

- Official Lua docs: https://commandlua.github.io/assets/Functions.html
- Community cases: https://commandops.github.io/
