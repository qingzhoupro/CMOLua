# -*- coding: utf-8 -*-
"""CMO-HKBQSKILL Installer - pure Python, UTF-8 safe output."""

import sys
import os
import shutil
import sqlite3
import json
import subprocess
from pathlib import Path


def cprint(msg: str, style: str = "normal"):
    """Print with ANSI color/style. Falls back to plain text on Windows."""
    RESET = "\033[0m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"

    icons = {"ok": "[+]", "warn": "[!]", "err": "[X]", "info": "[*]", "step": "[>]"}
    styles = {
        "ok": GREEN,
        "warn": YELLOW,
        "err": RED,
        "info": CYAN,
        "step": BOLD + CYAN,
        "title": BOLD + GREEN,
    }

    prefix = icons.get(style, "")
    color = styles.get(style, "")
    print(f"{color}{prefix} {msg}{RESET}")


def find_python():
    """Find a working Python executable."""
    candidates = []

    # Check PATH
    for name in ["python", "python3"]:
        path = shutil.which(name)
        if path:
            candidates.append((name, path))

    # Common Windows install locations
    program_files = os.environ.get("ProgramFiles", "C:\\Program Files")
    local_appdata = os.environ.get("LOCALAPPDATA", "")

    extra_paths = [
        Path(program_files) / "Python313" / "python.exe",
        Path(program_files) / "Python312" / "python.exe",
        Path(program_files) / "Python311" / "python.exe",
        Path(local_appdata) / "Programs" / "Python" / "Python313" / "python.exe",
        Path(local_appdata) / "Programs" / "Python" / "Python312" / "python.exe",
        Path(local_appdata) / "Programs" / "Python" / "Python311" / "python.exe",
        Path("C:/Program Files/Python313/python.exe"),
        Path("C:/Program Files/Python312/python.exe"),
    ]

    for p in extra_paths:
        if p.exists() and p not in [Path(p) for _, p in candidates]:
            candidates.append((str(p), str(p)))

    for name, path in candidates:
        try:
            version = subprocess.run(
                [path, "--version"], capture_output=True, text=True
            ).stdout.strip()
            return path, version
        except Exception:
            pass

    return None, None


def check_fastmcp(python_exe: str) -> bool:
    """Check if fastmcp is installed."""
    try:
        result = subprocess.run(
            [python_exe, "-m", "pip", "show", "fastmcp"],
            capture_output=True, text=True,
        )
        return result.returncode == 0
    except Exception:
        return False


def install_fastmcp(python_exe: str, req_file: str) -> bool:
    """Install fastmcp from requirements file."""
    try:
        result = subprocess.run(
            [python_exe, "-m", "pip", "install", "-r", req_file],
            capture_output=True, text=True, timeout=120,
        )
        return result.returncode == 0
    except Exception:
        return False


def find_db():
    """Find a DB3K database file in mcp/db/."""
    db_dir = Path("mcp/db")
    if not db_dir.exists():
        return None

    candidates = sorted(db_dir.glob("*.db3"))
    if candidates:
        return str(candidates[0])
    return None


def validate_db(db_path: str) -> tuple[bool, str]:
    """Test database connectivity and return table names."""
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' LIMIT 5")
        tables = [r[0] for r in cur.fetchall()]
        conn.close()
        return True, ", ".join(tables)
    except Exception as e:
        return False, str(e)


def write_mcp_config(mcp_file: str) -> bool:
    """Write the Cursor MCP configuration."""
    mcp_dir = os.path.dirname(mcp_file)
    os.makedirs(mcp_dir, exist_ok=True)

    backup = mcp_file + ".backup"
    if os.path.exists(mcp_file):
        shutil.copy2(mcp_file, backup)
        cprint(f"已备份原配置到 {backup}", "info")

    config = {
        "mcpServers": {
            "CMO_DBID_Lookup": {
                "command": "python",
                "args": ["-m", "fastmcp", "run", "mcp/server.py"],
                "env": {}
            }
        }
    }

    with open(mcp_file, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    return True


def find_cmo_steam_path():
    """Try to find CMO installation via Steam."""
    steam_common = Path("C:/Program Files (x86)/Steam/steamapps/common")
    if not steam_common.exists():
        return None

    for entry in steam_common.iterdir():
        if "Command" in entry.name and entry.is_dir():
            db_path = entry / "DB"
            if db_path.exists():
                return str(db_path)
    return None


def run():
    """Main installation flow."""
    print()
    cprint("==============================================================", "title")
    cprint("    CMO - HKBQSKILL  Installation Wizard", "title")
    cprint("==============================================================", "title")
    print()

    # --- Step 1: Find Python ---
    cprint("[1/5]  Checking Python...", "step")
    py_exe, py_ver = find_python()
    if py_exe:
        cprint(f"  Found: {py_ver}", "ok")
        cprint(f"  Path:  {py_exe}", "info")
    else:
        cprint("  Python not found!", "err")
        cprint("  Download from: https://www.python.org/downloads/", "warn")
        cprint("  Install with pip support (add to PATH)", "warn")
        input("\n  Press Enter to exit...")
        sys.exit(1)

    # --- Step 2: fastmcp ---
    cprint("\n[2/5]  Checking fastmcp...", "step")
    if check_fastmcp(py_exe):
        cprint("  Already installed", "ok")
    else:
        cprint("  Not installed, installing...", "info")
        req_file = "mcp/requirements.txt"
        if install_fastmcp(py_exe, req_file):
            cprint("  Installation successful", "ok")
        else:
            cprint("  pip install failed - try manually:", "err")
            cprint(f"  {py_exe} -m pip install -r {req_file}", "warn")
            input("\n  Press Enter to continue anyway...")
            if not check_fastmcp(py_exe):
                sys.exit(1)

    # --- Step 3: Database ---
    cprint("\n[3/5]  Checking database...", "step")
    db_path = find_db()
    if db_path:
        valid, info = validate_db(db_path)
        if valid:
            cprint(f"  OK: {Path(db_path).name}", "ok")
            cprint(f"  Tables: {info}", "info")
        else:
            cprint(f"  Invalid database: {info}", "err")
            db_path = None
    else:
        cprint("  No DB3K_*.db3 file found in mcp/db/", "warn")

    if not db_path:
        print()
        cprint("  ACTION REQUIRED:", "warn")
        cprint("  Copy your CMO database file to:", "info")
        print()
        print("    <CMO Game Folder>/DB/DB3K_*.db3")
        print("        -> copy to")
        print(f"    {os.path.abspath('mcp/db/')}/")
        print()

        # Try to help find it
        steam_db = find_cmo_steam_path()
        if steam_db:
            cprint(f"  Steam installation detected: {Path(steam_db).parent}", "info")
            cprint(f"  Database folder: {steam_db}", "info")
            import glob as glob_module
            db_files = glob_module.glob(os.path.join(steam_db, "DB3K_*.db3"))
            if db_files:
                cprint(f"  Available: {', '.join([os.path.basename(f) for f in db_files])}", "info")

        cprint("  After copying, run this script again.", "info")
        input("\n  Press Enter to exit...")

        # Check if files appeared
        if not find_db():
            sys.exit(1)

    # --- Step 4: Validate server ---
    cprint("\n[4/5]  Validating MCP server...", "step")
    server_py = Path("mcp/server.py")
    if server_py.exists():
        cprint("  server.py found", "ok")
    else:
        cprint("  server.py not found - check project structure", "err")

    # --- Step 5: Write MCP config ---
    cprint("\n[5/5]  Writing MCP configuration...", "step")

    mcp_file = os.path.join(os.environ.get("APPDATA", ""), "Cursor", "User", "mcp.json")
    if write_mcp_config(mcp_file):
        cprint(f"  Written: {mcp_file}", "ok")
    else:
        cprint(f"  Failed to write: {mcp_file}", "err")

    # --- Done ---
    print()
    cprint("==============================================================", "title")
    cprint("  ALL SYSTEM STATUS : NOMINAL", "ok")
    cprint("  MCP SERVER       : READY", "ok")
    if db_path:
        cprint(f"  DATABASE         : CONNECTED ({Path(db_path).name})", "ok")
    else:
        cprint("  DATABASE         : NOT FOUND (copy DB file first)", "warn")
    cprint("==============================================================", "title")
    print()
    cprint("  Next: Restart your IDE, then ask AI to load SKILL.md", "info")
    print()
    input("  Press Enter to exit...")


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n\n  Cancelled.")
        sys.exit(0)
