#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CMO-HKBQSKILL 交互式安装向导
跨平台兼容：Windows / macOS / Linux
纯 Python，无需额外依赖

入口脚本 (scripts/):
  install.py              ← 唯一安装入口 (主程序)
  config.py               ← 数据库路径配置工具
  check-deps.ps1          ← 依赖检查工具 (PowerShell)
  scan_database.py        ← 数据库结构扫描工具
  export_table_schemas.py ← 数据表字段导出工具
  uninstall.ps1           ← 卸载 MCP 配置工具
  validate-structure.ps1  ← 项目结构验证工具

用法:
  python install.py              # 完整安装向导
  python install.py --quick      # 快速启动 (检测已安装配置)
  python install.py --status     # 检查 MCP 服务状态
"""

import sys
import os
import shutil
import sqlite3
import json
import subprocess
import glob as glob_module
from pathlib import Path
from typing import Optional, Tuple

# =============================================================================
# 跨平台路径配置
# =============================================================================

PLATFORM = sys.platform
IS_WINDOWS = PLATFORM.startswith("win")
IS_MAC = PLATFORM == "darwin"
IS_LINUX = PLATFORM.startswith("linux")

def get_home_dir() -> Path:
    """获取用户主目录"""
    if IS_WINDOWS:
        return Path(os.environ.get("USERPROFILE", os.environ.get("HOME", "~")))
    return Path(os.environ.get("HOME", "~"))

def get_config_dir() -> Path:
    """获取配置目录"""
    if IS_WINDOWS:
        return Path(os.environ.get("APPDATA", get_home_dir() / "AppData" / "Roaming"))
    elif IS_MAC:
        return get_home_dir() / "Library" / "Application Support"
    else:
        return get_home_dir() / ".config"

# =============================================================================
# ANSI 颜色输出
# =============================================================================

class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    # 前景色
    BLACK = "\033[30m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

    # 背景色
    BG_BLACK = "\033[40m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_RED = "\033[41m"
    BG_CYAN = "\033[46m"

def has_ansi_support() -> bool:
    """检测终端是否支持ANSI颜色"""
    if not hasattr(sys.stdout, "isatty"):
        return False
    if not sys.stdout.isatty():
        return False
    if IS_WINDOWS:
        # Windows 10+ 支持 ANSI，但旧版可能不支持
        return True
    return True

# 全局颜色启用开关
USE_COLOR = has_ansi_support()

def cprint(msg: str = "", style: str = "normal", end: str = "\n"):
    """带颜色的打印输出

    style: ok(成功) | warn(警告) | err(错误) | info(信息) | step(步骤)
           title(标题) | header(页眉) | success(成功面板)
    """
    if not USE_COLOR:
        icons = {"ok": "[+]", "warn": "[!]", "err": "[X]", "info": "[*]", "step": "[>]"}
        prefix = icons.get(style, "")
        print(f"{prefix} {msg}" if prefix else msg, end=end)
        return

    icons = {"ok": "[+]", "warn": "[!]", "err": "[X]", "info": "[*]", "step": "[>]"}
    styles = {
        "ok": f"{Colors.GREEN}{Colors.BOLD}",
        "warn": f"{Colors.YELLOW}{Colors.BOLD}",
        "err": f"{Colors.RED}{Colors.BOLD}",
        "info": f"{Colors.CYAN}",
        "step": f"{Colors.CYAN}{Colors.BOLD}",
        "title": f"{Colors.GREEN}{Colors.BOLD}",
        "header": f"{Colors.CYAN}{Colors.BOLD}",
        "success": f"{Colors.GREEN}{Colors.BOLD}",
        "dim": f"{Colors.DIM}",
        "white": f"{Colors.WHITE}",
    }

    icon = icons.get(style, "")
    color = styles.get(style, "")
    print(f"{color}{icon} {msg}{Colors.RESET}", end=end)

def print_header(text: str, width: int = 60):
    """打印居中标题"""
    print()
    print(f"{Colors.CYAN}{Colors.BOLD}{'=' * width}{Colors.RESET}")
    # 计算居中位置
    padding = (width - len(text) - 2) // 2
    print(f"{Colors.CYAN}{Colors.BOLD}{' ' * padding} {text} {' ' * padding}{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}{'=' * width}{Colors.RESET}")
    print()

def print_divider(char: str = "─", width: int = 60):
    """打印分隔线"""
    print(f"{Colors.DIM}{char * width}{Colors.RESET}")

def input_prompt(prompt_text: str, default: str = "") -> str:
    """带样式的输入提示"""
    if default:
        result = input(f"{Colors.CYAN}{prompt_text}{Colors.RESET} [{default}]: ").strip()
        return result if result else default
    return input(f"{Colors.CYAN}{prompt_text}{Colors.RESET}: ").strip()

# =============================================================================
# 工具函数
# =============================================================================

def get_cursor_path() -> Optional[str]:
    """检测 Cursor 安装路径"""
    if IS_WINDOWS:
        candidates = [
            os.environ.get("ProgramFiles") + "/Cursor/Cursor.exe",
            os.environ.get("ProgramFiles(X86)") + "/Cursor/Cursor.exe",
            "C:/Program Files/Cursor/Cursor.exe",
            "C:/Program Files (x86)/Cursor/Cursor.exe",
        ]
    elif IS_MAC:
        candidates = ["/Applications/Cursor.app/Contents/MacOS/Cursor"]
    else:
        candidates = ["/usr/bin/cursor"]

    for path in candidates:
        if os.path.exists(path):
            return path
    return None


def launch_cursor(app_path: Optional[str] = None) -> bool:
    """启动 Cursor"""
    try:
        if app_path:
            cmd = [app_path]
        elif IS_WINDOWS:
            cmd = ["cmd", "/c", "start", "", "Cursor"]
        elif IS_MAC:
            cmd = ["open", "-a", "Cursor"]
        else:
            cmd = ["cursor"]

        subprocess.Popen(cmd, detached=True, start_new_session=True)
        return True
    except Exception:
        return False


def check_mcp_status(project_root: Path) -> Tuple[bool, str]:
    """检查 MCP 服务状态

    检查多个可能的 Python 安装，返回第一个可用的状态。

    Returns:
        (是否正常, 状态信息)
    """
    candidates = []

    # 收集可能的 Python 路径 (按优先级排序)
    if IS_WINDOWS:
        pf = os.environ.get("ProgramFiles", "C:\\Program Files")
        lp = os.environ.get("LOCALAPPDATA", "")
        # 显式路径优先
        candidates.extend([
            Path(pf) / "Python313" / "python.exe",
            Path(pf) / "Python312" / "python.exe",
            Path(pf) / "Python311" / "python.exe",
            Path(lp) / "Programs" / "Python" / "Python313" / "python.exe",
            Path(lp) / "Programs" / "Python" / "Python312" / "python.exe",
        ])
        # PATH 中的 python 放最后作为后备
        which_python = shutil.which("python")
        if which_python:
            candidates.append(Path(which_python))
    else:
        # Unix 系统
        candidates.extend([
            Path("/usr/bin/python3"),
            Path("/usr/local/bin/python3"),
        ])
        which_python = shutil.which("python3")
        if which_python:
            candidates.append(Path(which_python))

    script_path = project_root / "mcp" / "sqlite_explorer.py"
    if not os.path.exists(script_path):
        return False, f"MCP 脚本不存在: {script_path}"

    for py_path in candidates:
        if not py_path.exists():
            continue
        py_exe = str(py_path)

        try:
            # 检查 fastmcp 命令
            result = subprocess.run(
                [py_exe, "-m", "fastmcp", "--version"],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode != 0:
                continue

            # 检查脚本语法
            result = subprocess.run(
                [py_exe, "-c", "import ast; ast.parse(open(r'" + str(script_path).replace("\\", "\\\\") + "').read())"],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode != 0:
                return False, "MCP 脚本语法错误"

            return True, f"就绪 (Python: {py_path.name})"
        except Exception:
            continue

    return False, "未找到可用的 Python/fastmcp 环境"


def create_quick_launch_scripts(project_root: Path) -> bool:
    """创建快速启动脚本"""
    try:
        # Windows 批处理脚本
        bat_content = """@echo off
chcp 65001 > nul
title CMO-HKBQSKILL 启动器

echo.
echo ═══════════════════════════════════════════════════════════════
echo                    CMO-HKBQSKILL 启动器
echo ═══════════════════════════════════════════════════════════════
echo.
echo 正在启动 Cursor...
echo.

python "%~dp0scripts\\install.py" --quick

if errorlevel 1 (
    echo.
    echo 启动失败，请检查安装状态
    pause
)
"""
        bat_path = project_root / "start.bat"
        with open(bat_path, "w", encoding="utf-8") as f:
            f.write(bat_content)

        # Unix Shell 脚本 (macOS/Linux)
        sh_content = """#!/bin/bash

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "                   CMO-HKBQSKILL 启动器"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "正在启动 Cursor..."
echo ""

python3 "$(dirname "$0")/../scripts/install.py" --quick

if [ $? -ne 0 ]; then
    echo ""
    echo "启动失败，请检查安装状态"
    read -p "按 Enter 键退出..."
fi
"""
        sh_path = project_root / "start.sh"
        with open(sh_path, "w", encoding="utf-8") as f:
            f.write(sh_content)

        # 设置执行权限 (Unix)
        if not IS_WINDOWS:
            os.chmod(sh_path, 0o755)

        return True
    except Exception:
        return False


def print_mcp_guide():
    """打印 MCP 管理指南"""
    print()
    print_divider("=", 70)
    print()
    print(f"{Colors.BOLD}{Colors.CYAN}  MCP 服务管理指南{Colors.RESET}")
    print()
    print_divider("─", 70)
    print()
    print(f"{Colors.BOLD}【日常使用】{Colors.RESET}")
    print()
    print("  启动项目:")
    if IS_WINDOWS:
        print("    方法1: 双击运行 scripts/start.bat")
        print("    方法2: 在项目目录执行: python scripts\\install.py --quick")
    else:
        print("    方法1: 运行 scripts/start.sh")
        print("    方法2: 在项目目录执行: python3 scripts/install.py --quick")
    print()
    print("  重启 MCP 服务 (Cursor 已打开时):")
    print("    Ctrl+Shift+P → 输入 'MCP: Restart Server' → 选择 'CMO_DBID_Lookup'")
    print()
    print_divider("─", 70)
    print()
    print(f"{Colors.BOLD}【故障排除】{Colors.RESET}")
    print()
    print("  MCP 连接失败时尝试:")
    print("    1. 重启 Cursor")
    print("    2. 检查 fastmcp: python -m fastmcp --version")
    print("    3. 重新运行安装: python scripts/install.py")
    print()
    print("  检查 MCP 日志:")
    if IS_WINDOWS:
        print("    View → Output → 切换到 'MCP' 标签页")
    else:
        print("    View → Output → 切换到 'MCP' 标签页")
    print()
    print_divider("─", 70)
    print()
    print(f"{Colors.BOLD}【卸载/重装】{Colors.RESET}")
    print()
    print("  完全重装:")
    if IS_WINDOWS:
        print("    1. 删除 %APPDATA%\\Cursor\\User\\globalStorage\\... 下的 MCP 相关缓存")
        print("    2. 删除 %APPDATA%\\Cursor\\User\\mcp.json 中的 CMO_DBID_Lookup 配置")
    else:
        print("    1. 删除 ~/.config/Cursor/User/globalStorage/... 下的 MCP 相关缓存")
        print("    2. 删除 ~/.config/Cursor/User/mcp.json 中的 CMO_DBID_Lookup 配置")
    print("    3. 重新运行 python scripts/install.py")
    print()
    print_divider("=", 70)
    print()


def print_quick_start():
    """打印快速启动信息"""
    print()
    print_divider("─", 60)
    print()
    cprint("检测到已安装配置，正在启动 MCP 服务...", "info")
    print()
    print("  启动方式:")
    if IS_WINDOWS:
        print("    • 双击: start.bat")
        print("    • 命令: python scripts\\install.py --quick")
    else:
        print("    • 运行: scripts/start.sh")
        print("    • 命令: python3 scripts/install.py --quick")
    print()
    cprint("MCP 服务将在 Cursor 启动后自动加载", "ok")
    print()


def is_cursor_running() -> bool:
    """检测 Cursor 是否正在运行"""
    if IS_WINDOWS:
        try:
            result = subprocess.run(
                ["tasklist", "/FI", "IMAGENAME eq Cursor.exe"],
                capture_output=True, text=True, timeout=5
            )
            return "Cursor.exe" in result.stdout
        except Exception:
            return False
    elif IS_MAC:
        try:
            result = subprocess.run(
                ["pgrep", "-x", "Cursor"],
                capture_output=True, text=True, timeout=5
            )
            return result.returncode == 0
        except Exception:
            return False
    else:
        try:
            result = subprocess.run(
                ["pgrep", "-f", "cursor"],
                capture_output=True, text=True, timeout=5
            )
            return result.returncode == 0
        except Exception:
            return False


def restart_mcp_in_cursor() -> bool:
    """尝试在已运行的 Cursor 中重启 MCP

    使用 Cursor CLI 发送命令
    """
    if IS_WINDOWS:
        # Windows: 尝试使用 PowerShell 向 Cursor 发送命令
        try:
            # 方法1: 尝试通过 Cursor 的命令行接口
            cursor_cli = get_cursor_path()
            if cursor_cli:
                # Cursor 支持 --profile 参数但不直接支持重启 MCP
                # 我们可以尝试触发配置重新加载
                result = subprocess.run(
                    [cursor_cli, "--disable-extensions"],
                    capture_output=True, text=True, timeout=2
                )
        except Exception:
            pass
    return False


def run_quick_start(python_exe: str, project_root: Path) -> bool:
    """快速启动模式 - 检测现有配置并启动 MCP"""
    script_path = project_root / "mcp" / "sqlite_explorer.py"
    cursor_path = get_cursor_path()
    cursor_running = is_cursor_running()

    if not cursor_path:
        cprint("未找到 Cursor 安装，请先运行完整安装", "err")
        return False

    if not os.path.exists(script_path):
        cprint("MCP 脚本不存在，请先运行完整安装", "err")
        return False

    # 确保启动脚本存在
    create_quick_launch_scripts(project_root)

    print()
    print_divider("─", 60)
    print()

    if cursor_running:
        # Cursor 已在运行
        cprint("检测到 Cursor 已在运行", "info")
        print()
        print("  正在尝试重启 MCP 服务...")
        print()

        # 尝试通过各种方式重启 MCP
        restart_ok = False

        # 方法1: 检查并确保 __main__.py 存在
        pf = os.environ.get("ProgramFiles", "C:\\Program Files")
        lp = os.environ.get("LOCALAPPDATA", "")
        fastmcp_main_paths = [
            Path(pf) / "Python313" / "Lib" / "site-packages" / "fastmcp" / "__main__.py",
            Path(pf) / "Python312" / "Lib" / "site-packages" / "fastmcp" / "__main__.py",
            Path(lp) / "Programs" / "Python" / "Python313" / "Lib" / "site-packages" / "fastmcp" / "__main__.py",
            Path("C:\\ProgramData\\miniconda3\\Lib\\site-packages\\fastmcp\\__main__.py"),
        ]

        for main_path in fastmcp_main_paths:
            if main_path.exists():
                cprint(f"  ✓ fastmcp __main__.py 已存在: {main_path.parent.name}", "ok")
                restart_ok = True
                break

        if not restart_ok:
            cprint("  需要先运行完整安装来修复 fastmcp", "warn")

        print()
        print_divider("─", 60)
        print()
        cprint("MCP 重启提示:", "step")
        print()
        print("  请在 Cursor 中按:")
        print("  Ctrl+Shift+P → 输入 'MCP: Restart Server' → 回车")
        print("  → 选择 'CMO_DBID_Lookup'")
        print()
        print("  或直接重启 Cursor (关闭后重新打开)")
        print()
        print_mcp_guide()
        return True
    else:
        # Cursor 未运行，启动它
        cprint("检测到 Cursor 未运行，正在启动...", "info")
        print()

        if launch_cursor(cursor_path):
            cprint("Cursor 启动中，MCP 将自动连接...", "ok")
            print()
            print("  等待 5-10 秒后检查 MCP 状态")
            print()
            print("  如 MCP 未自动连接，请在 Cursor 中:")
            print("  Ctrl+Shift+P → MCP: Restart Server → CMO_DBID_Lookup")
            print()
            return True
        else:
            cprint("Cursor 启动失败，请手动启动", "err")
            print()
            return False


# =============================================================================
# 步骤1: 环境检查
# =============================================================================

def check_python() -> Tuple[Optional[str], Optional[str]]:
    """检测Python环境"""
    cprint("检测 Python 环境...", "step")

    # 常见Python路径
    candidates = []

    # 从PATH中查找
    for name in ["python", "python3"]:
        path = shutil.which(name)
        if path:
            candidates.append(path)

    # Windows额外路径
    if IS_WINDOWS:
        program_files = os.environ.get("ProgramFiles", "C:\\Program Files")
        local_appdata = os.environ.get("LOCALAPPDATA", "")

        windows_paths = [
            Path(program_files) / "Python313" / "python.exe",
            Path(program_files) / "Python312" / "python.exe",
            Path(program_files) / "Python311" / "python.exe",
            Path(program_files) / "Python310" / "python.exe",
            Path(local_appdata) / "Programs" / "Python" / "Python313" / "python.exe",
            Path(local_appdata) / "Programs" / "Python" / "Python312" / "python.exe",
            Path(local_appdata) / "Programs" / "Python" / "Python311" / "python.exe",
            Path("C:/Program Files/Python313/python.exe"),
            Path("C:/Program Files/Python312/python.exe"),
        ]
        for p in windows_paths:
            if p.exists() and str(p) not in candidates:
                candidates.append(str(p))

    # 测试每个候选
    for path in candidates:
        try:
            result = subprocess.run(
                [path, "--version"], capture_output=True, text=True, timeout=5
            )
            version = result.stdout.strip() or result.stderr.strip()
            if "Python" in version:
                cprint(f"找到: {version}", "ok")
                cprint(f"路径: {path}", "dim")
                return path, version
        except Exception:
            continue

    return None, None

def check_python_version(python_exe: str) -> bool:
    """检查Python版本是否满足要求 (>= 3.8)"""
    try:
        result = subprocess.run(
            [python_exe, "-c", "import sys; print(sys.version_info.major * 10 + sys.version_info.minor)"],
            capture_output=True, text=True, timeout=5
        )
        version_num = int(result.stdout.strip())
        return version_num >= 38  # 3.8+ = 38
    except Exception:
        return False

def install_dependencies(python_exe: str, req_file: str) -> bool:
    """安装依赖"""
    if not Path(req_file).exists():
        cprint(f"requirements.txt 不存在: {req_file}", "err")
        return False

    cprint("正在安装依赖 (fastmcp)...", "info")
    cprint("(这可能需要几分钟，请耐心等待)", "dim")

    try:
        result = subprocess.run(
            [python_exe, "-m", "pip", "install", "-r", req_file],
            capture_output=True, text=True, timeout=180
        )
        if result.returncode == 0:
            cprint("依赖安装成功!", "ok")
            return True
        else:
            cprint(f"安装失败: {result.stderr[:200]}", "err")
            return False
    except subprocess.TimeoutExpired:
        cprint("安装超时 (超过3分钟)", "err")
        return False
    except Exception as e:
        cprint(f"安装出错: {e}", "err")
        return False

def check_dependency(python_exe: str, package: str) -> bool:
    """检查包是否已安装"""
    try:
        result = subprocess.run(
            [python_exe, "-m", "pip", "show", package],
            capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0
    except Exception:
        return False


def fix_fastmcp_main(python_exe: str) -> bool:
    """修复 fastmcp 3.x 缺少 __main__.py 的问题

    fastmcp 3.x 移除了 __main__.py，导致 python -m fastmcp 无法工作。
    此函数创建缺失的 __main__.py 文件。
    """
    try:
        result = subprocess.run(
            [python_exe, "-c", "import fastmcp; import os; print(os.path.dirname(fastmcp.__file__))"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            return False

        fastmcp_dir = result.stdout.strip()
        main_py = os.path.join(fastmcp_dir, "__main__.py")

        if os.path.exists(main_py):
            return True  # 已存在，无需修复

        # 创建 __main__.py
        main_content = '''"""Entry point for running fastmcp as a module."""

import sys
from fastmcp.cli.cli import app

if __name__ == "__main__":
    app()
'''
        with open(main_py, "w", encoding="utf-8") as f:
            f.write(main_content)

        return True
    except Exception:
        return False

# =============================================================================
# 步骤2: 数据库配置
# =============================================================================

def get_project_root() -> Path:
    """获取项目根目录（脚本所在位置向上两级）"""
    return Path(__file__).parent.parent.resolve()

def find_cmo_db_in_directory(base_path: Path) -> list:
    """在指定目录下查找CMO数据库文件"""
    db_patterns = [
        base_path / "DB" / "DB3K_*.db3",
        base_path / "DB" / "*.db3",
        base_path / "*.db3",
    ]

    found = []
    for pattern in db_patterns:
        matches = list(Path(pattern).parent.glob(pattern.name))
        found.extend([str(p) for p in matches if p.is_file()])

    return list(dict.fromkeys(found))  # 去重

def try_detect_steam_installation() -> Optional[str]:
    """尝试通过Steam检测CMO安装路径"""
    steam_base = None

    if IS_WINDOWS:
        # Steam默认安装位置
        steam_paths = [
            Path("C:/Program Files (x86)/Steam"),
            Path("C:/Program Files/Steam"),
            Path(os.environ.get("PROGRAMFILES(X86)", "C:/Program Files (x86)")) / "Steam",
        ]
    elif IS_MAC:
        steam_paths = [get_home_dir() / "Library" / "Application Support" / "Steam"]
    else:
        steam_paths = [get_home_dir() / ".local" / "share" / "Steam"]

    for sp in steam_paths:
        if sp.exists():
            steam_base = sp
            break

    if not steam_base:
        return None

    # 查找CMO游戏目录
    if IS_WINDOWS:
        common = steam_base / "steamapps" / "common"
    elif IS_MAC:
        common = steam_base / "Steam" / "steamapps" / "common"
    else:
        common = steam_base / "steamapps" / "common"

    if not common.exists():
        return None

    for entry in common.iterdir():
        if entry.is_dir() and ("Command" in entry.name or "CMO" in entry.name.upper()):
            db_folder = entry / "DB"
            if db_folder.exists():
                cprint(f"Steam安装检测: {entry.name}", "info")
                return str(db_folder)

    return None

def copy_database(source_path: str) -> Tuple[bool, str]:
    """复制数据库文件到项目目录"""
    source = Path(source_path)
    if not source.exists():
        return False, "源文件不存在"

    project_root = get_project_root()
    dest_dir = project_root / "mcp" / "db"
    dest_dir.mkdir(parents=True, exist_ok=True)

    dest_path = dest_dir / source.name

    try:
        shutil.copy2(source, dest_path)
        return True, str(dest_path)
    except Exception as e:
        return False, str(e)

def validate_database(db_path: str) -> Tuple[bool, str]:
    """验证数据库有效性"""
    try:
        conn = sqlite3.connect(db_path, timeout=5)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' LIMIT 5")
        tables = [r[0] for r in cur.fetchall()]
        cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
        total = cur.fetchone()[0]
        conn.close()
        return True, f"{total}张表, 示例: {', '.join(tables[:3])}"
    except Exception as e:
        return False, str(e)

# =============================================================================
# 步骤3: IDE配置（跨平台精准路径映射）
# =============================================================================

# 各 IDE 在不同操作系统下的标准 MCP 配置路径映射
# key: IDE 标识符
#   config_file      - 配置文件基础名
#   paths            - 按 sys.platform (win32 / darwin / linux) 映射相对路径
#   is_project_path  - True 表示相对于项目根目录（如 VS Code 的 .vscode/settings.json）
#   config_format    - 配置节点格式: "mcpServers" | "mcp" (VS Code Insiders)
IDE_CONFIG_MAP: dict = {
    "Cursor": {
        "config_file": "mcp.json",
        "paths": {
            "win32":  "Cursor/User/mcp.json",
            "darwin": "Cursor/User/mcp.json",
            "linux":  "Cursor/User/mcp.json",
        },
        "is_project_path": False,
        "config_format": "mcpServers",
    },
    "Trae": {
        "config_file": "mcp.json",
        "paths": {
            "win32":  "Trae/mcp.json",
            "darwin": "Trae/mcp.json",
            "linux":  "Trae/mcp.json",
        },
        "is_project_path": False,
        "config_format": "mcpServers",
    },
    "VS Code": {
        "config_file": "settings.json",
        "paths": {
            "win32":  ".vscode/settings.json",
            "darwin": ".vscode/settings.json",
            "linux":  ".vscode/settings.json",
        },
        "is_project_path": True,
        "config_format": "mcp",
    },
    "Claude Desktop": {
        "config_file": "claude_desktop_config.json",
        "paths": {
            "win32":  "Claude/claude_desktop_config.json",
            "darwin": "Claude/claude_desktop_config.json",
            "linux":  "Claude/claude_desktop_config.json",
        },
        "is_project_path": False,
        "config_format": "mcpServers",
    },
}


def get_ide_base_dir() -> Path:
    """根据当前操作系统返回配置根目录（不含 IDE 子路径）"""
    if IS_WINDOWS:
        base = os.environ.get("APPDATA", str(Path.home() / "AppData" / "Roaming"))
        return Path(base)
    elif IS_MAC:
        return Path.home() / "Library" / "Application Support"
    else:
        # Linux: 优先 XDG_CONFIG_HOME，否则 ~/.config
        xdg = os.environ.get("XDG_CONFIG_HOME", "")
        if xdg:
            return Path(xdg)
        return Path.home() / ".config"


def get_ide_config_path(ide_name: str, project_root: Optional[Path] = None) -> Optional[Path]:
    """根据 IDE 名称和当前平台解析出精确的配置文件路径

    Args:
        ide_name: IDE 显示名称，如 "Cursor", "Trae", "VS Code", "Claude Desktop"
        project_root: 项目根目录（VS Code 需要）

    Returns:
        完整的配置文件 Path，失败返回 None
    """
    entry = IDE_CONFIG_MAP.get(ide_name)
    if not entry:
        return None

    rel_path = entry["paths"].get(PLATFORM)
    if not rel_path:
        return None

    if entry["is_project_path"]:
        # VS Code: 相对于项目根目录
        if project_root is None:
            project_root = get_project_root()
        return project_root / rel_path
    else:
        # Cursor / Trae / Claude Desktop: 相对于配置根目录
        base = get_ide_base_dir()
        return base / rel_path


def detect_installed_ides() -> list:
    """检测本机可能已安装的 IDE（通过可执行文件路径 + 配置父目录是否存在）"""
    detected = []
    project_root = get_project_root()

    for ide_name in IDE_CONFIG_MAP:
        config_path = get_ide_config_path(ide_name, project_root)
        if config_path is None:
            continue
        # 任一条件满足即认为"可能已安装"：
        # 1. 配置文件本身已存在
        # 2. 配置文件的父目录已存在（说明 IDE 至少运行过一次）
        if config_path.exists() or config_path.parent.exists():
            detected.append((ide_name, config_path))

    # 补充检测：直接扫描可执行文件（Windows）
    if IS_WINDOWS:
        program_files = Path(os.environ.get("ProgramFiles", "C:\\Program Files"))
        program_files_x86 = Path(os.environ.get("ProgramFiles(X86)", "C:\\Program Files (x86)"))

        exe_map = {
            "Cursor":          program_files_x86 / "Cursor" / "Cursor.exe",
            "Trae":            program_files / "Trae" / "Trae.exe",
            "VS Code":         program_files_x86 / "Microsoft VS Code" / "Code.exe",
            "Claude Desktop":  program_files_x86 / "Claude" / "Claude.exe",
        }
        for name, exe_path in exe_map.items():
            if exe_path.exists() and name not in [d[0] for d in detected]:
                detected.append((name, None))

    return detected


def detect_db_file(project_root: Path) -> Optional[str]:
    """在项目 mcp/db/ 目录下查找最新的 DB3K_*.db3 文件"""
    db_dir = project_root / "mcp" / "db"
    if not db_dir.exists():
        return None
    db_files = sorted(db_dir.glob("DB3K_*.db3"), key=lambda p: p.stat().st_mtime, reverse=True)
    if db_files:
        return str(db_files[0])
    return None


def read_json_safe(path: Path) -> dict:
    """安全读取 JSON 文件，不存在或解析失败时返回空字典"""
    if not path.exists():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def write_json_safe(path: Path, data: dict) -> bool:
    """安全写入 JSON 文件（先写 .tmp，再 rename）"""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = path.with_suffix(".json.tmp")
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        tmp_path.replace(path)
        return True
    except OSError as e:
        cprint(f"文件写入失败: {e}", "err")
        return False


def build_mcp_server_entry(project_root: Path) -> dict:
    """构建单个 MCP 服务器的 JSON 配置条目"""
    db_path = detect_db_file(project_root)
    return {
        "command": "python",
        "args": ["-m", "fastmcp", "run", "mcp/sqlite_explorer.py"],
        "env": {
            "SQLITE_DB_PATH": db_path or "mcp/db/DB3K_514.db3",
        }
    }


def write_mcp_config(ide_name: str, project_root: Path) -> Tuple[bool, Path]:
    """向目标 IDE 写入 MCP 配置（安全读写 + 备份）

    Args:
        ide_name:      IDE 名称
        project_root:  项目根目录

    Returns:
        (是否成功, 配置文件的实际路径)
    """
    config_path = get_ide_config_path(ide_name, project_root)
    if not config_path:
        return False, Path()

    config_entry = IDE_CONFIG_MAP.get(ide_name, {})
    config_format = config_entry.get("config_format", "mcpServers")

    # ── 1. 读取已有配置（保留其他内容） ────────────────────────────────
    existing = read_json_safe(config_path)

    # ── 2. 备份（如已存在） ────────────────────────────────────────────
    if config_path.exists():
        backup_path = config_path.with_suffix(".json.backup")
        try:
            shutil.copy2(config_path, backup_path)
            cprint(f"已备份原配置 → {backup_path.name}", "info")
        except OSError:
            pass  # 备份失败不影响主流程

    # ── 3. 构造要写入的配置 ────────────────────────────────────────────
    server_key = "CMO_DBID_Lookup"
    mcp_entry  = build_mcp_server_entry(project_root)

    if config_format == "mcpServers":
        # Cursor / Trae / Claude Desktop 格式: { "mcpServers": { "CMO_DBID_Lookup": {...} } }
        if "mcpServers" not in existing:
            existing["mcpServers"] = {}
        existing["mcpServers"][server_key] = mcp_entry
    else:
        # VS Code 格式: { "mcp": { "servers": { "CMO_DBID_Lookup": {...} } } }
        if "mcp" not in existing:
            existing["mcp"] = {}
        if "servers" not in existing["mcp"]:
            existing["mcp"]["servers"] = {}
        existing["mcp"]["servers"][server_key] = mcp_entry

    # ── 4. 写入（原子操作） ────────────────────────────────────────────
    if write_json_safe(config_path, existing):
        return True, config_path
    return False, config_path


def configure_ide_interactive(project_root: Path):
    """交互式 IDE 配置向导（步骤3核心）"""
    print()
    print_divider("─", 70)
    print()
    cprint("  步骤 3/3: IDE 配置  ─  一键配置 MCP", "header")
    print()
    print_divider("─", 70)
    print()

    # ── A. 展示支持的 IDE 列表 ────────────────────────────────────────
    cprint("支持的 IDE:", "step")
    print()
    for i, ide_name in enumerate(IDE_CONFIG_MAP, 1):
        icon = "○"
        if IS_WINDOWS:
            base = get_ide_base_dir()
            entry = IDE_CONFIG_MAP[ide_name]
            path_hint = base / entry["paths"]["win32"]
        elif IS_MAC:
            base = get_ide_base_dir()
            entry = IDE_CONFIG_MAP[ide_name]
            path_hint = base / entry["paths"]["darwin"]
        else:
            base = get_ide_base_dir()
            entry = IDE_CONFIG_MAP[ide_name]
            path_hint = base / entry["paths"]["linux"]

        exists_str = ""
        if path_hint.exists():
            icon = "●"
            exists_str = f"  {Colors.GREEN}(已找到配置文件){Colors.RESET}"

        print(f"  {Colors.CYAN}{i}.{Colors.RESET} {icon} {ide_name}")
        print(f"      {Colors.DIM}{path_hint}{Colors.RESET}{exists_str}")

    print()

    # ── B. 用户选择 ──────────────────────────────────────────────────
    ide_names = list(IDE_CONFIG_MAP.keys())
    while True:
        raw = input_prompt("请输入 IDE 编号 (1-4)", "1")
        try:
            idx = int(raw) - 1
            if 0 <= idx < len(ide_names):
                selected_ide = ide_names[idx]
                break
            raise ValueError()
        except ValueError:
            cprint("无效输入，请输入 1 到 4 之间的数字", "warn")
            print()

    cprint(f"已选择: {selected_ide}", "ok")
    print()

    # ── C. 解析目标路径 ──────────────────────────────────────────────
    config_path = get_ide_config_path(selected_ide, project_root)

    if config_path is None:
        cprint("无法解析该 IDE 的配置文件路径，请检查系统平台支持", "err")
        _print_manual_paste_guide(selected_ide, project_root)
        return

    cprint(f"目标路径: {config_path}", "info")

    # ── D. 校验目标目录是否存在（IDE 是否真正安装） ──────────────────────
    parent = config_path.parent
    if not parent.exists():
        cprint(
            f"配置文件目录不存在: {parent}", "err"
        )
        print()
        cprint("该 IDE 可能尚未安装或从未运行过。", "warn")
        print()
        retry = input_prompt("是否仍尝试创建配置？(y/n)", "n")
        if retry.lower() not in ("y", "yes"):
            cprint("已取消配置", "warn")
            _print_manual_paste_guide(selected_ide, project_root)
            return
        print()
        cprint("将自动创建目录和文件...", "info")

    # ── E. 写入配置 ──────────────────────────────────────────────────
    success, final_path = write_mcp_config(selected_ide, project_root)

    if success:
        print()
        print_divider("─", 70)
        print()
        cprint("MCP 配置写入成功!", "success")

        if IS_WINDOWS:
            vscode_hint = "或直接在 VS Code 中运行: code ."
        elif IS_MAC:
            vscode_hint = "或直接在 VS Code 中运行: code ."
        else:
            vscode_hint = "或直接在 VS Code 中运行: code ."

        print()
        print(f"  配置文件: {final_path}")
        if final_path.exists():
            print(f"  文件大小: {final_path.stat().st_size} bytes")

        print()
        cprint("请重启 IDE 以加载 MCP 服务", "step")
        if selected_ide == "Cursor":
            print("  重启后按: Ctrl+Shift+P → MCP: Restart Server → CMO_DBID_Lookup")
        elif selected_ide == "Trae":
            print("  重启后按: Ctrl+Shift+P → MCP: Restart Server → CMO_DBID_Lookup")
        elif selected_ide == "VS Code":
            print(f"  {vscode_hint}")
            print("  重启后按: Ctrl+Shift+P → MCP: Restart Server → CMO_DBID_Lookup")
        elif selected_ide == "Claude Desktop":
            print("  重启 Claude Desktop 应用后配置自动生效")
    else:
        print()
        cprint("MCP 配置写入失败，请检查权限或手动配置", "err")
        _print_manual_paste_guide(selected_ide, project_root)


def _print_manual_paste_guide(ide_name: str, project_root: Path):
    """打印手动粘贴配置的指引"""
    mcp_entry = build_mcp_server_entry(project_root)
    config_entry = IDE_CONFIG_MAP.get(ide_name, {})
    config_format = config_entry.get("config_format", "mcpServers")

    print()
    print_divider("─", 70)
    print()
    cprint(f"手动配置指南 ({ide_name})", "step")
    print()

    if config_format == "mcpServers":
        full_config = {"mcpServers": {"CMO_DBID_Lookup": mcp_entry}}
    else:
        full_config = {"mcp": {"servers": {"CMO_DBID_Lookup": mcp_entry}}}

    json_str = json.dumps(full_config, indent=2, ensure_ascii=False)

    if ide_name == "VS Code":
        config_path = project_root / ".vscode" / "settings.json"
        print(f"请打开文件: {Colors.CYAN}{config_path}{Colors.RESET}")
    else:
        base = get_ide_base_dir()
        entry = IDE_CONFIG_MAP.get(ide_name, {})
        rel = entry.get("paths", {}).get(PLATFORM, "unknown")
        config_path = base / rel
        print(f"请打开文件: {Colors.CYAN}{config_path}{Colors.RESET}")

    print()
    print(f"{Colors.BOLD}将以下内容添加到 JSON 文件的根级别:{Colors.RESET}")
    print()
    print(f"{Colors.DIM}{json_str}{Colors.RESET}")
    print()
    print_divider("─", 70)

# =============================================================================
# 完成面板
# =============================================================================

def print_success_panel(python_exe: str, project_root: Path):
    """打印成功完成面板并启动 Cursor"""
    script_path = project_root / "mcp" / "sqlite_explorer.py"
    cursor_path = get_cursor_path()

    # 检查 MCP 状态
    mcp_ok, mcp_status = check_mcp_status(project_root)

    print()
    print_divider("─", 70)
    print()

    success_text = """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║                   海 空 兵 棋                             ║
    ║              CMO-HKBQSKILL 安装完成                        ║
    ║                                                          ║"""
    if mcp_ok:
        success_text += """
    ║     SYSTEM STATUS    : NOMINAL                            ║
    ║     MCP SERVER      : READY                              ║
    ║     DATABASE        : CONNECTED                          ║"""
    else:
        success_text += """
    ║     SYSTEM STATUS    : PARTIAL                           ║
    ║     MCP SERVER      : """ + mcp_status[:16].ljust(16) + """                    ║
    ║     DATABASE        : """ + mcp_status[16:].ljust(16) + """                    ║"""

    success_text += """║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """

    if USE_COLOR:
        print(f"{Colors.GREEN}{Colors.BOLD}{success_text}{Colors.RESET}")
    else:
        print(success_text)

    print()
    cprint("安装完成!", "title")
    print()

    # 自动启动 Cursor
    if cursor_path:
        print_divider("─", 70)
        print()
        launch_choice = input_prompt("是否立即启动 Cursor? (y/n)", "y")
        print()

        if launch_choice.lower() in ("y", "yes", ""):
            if launch_cursor(cursor_path):
                cprint("Cursor 启动中...", "ok")
                print()
                print("  MCP 服务将在 Cursor 启动后自动连接")
                print()
            else:
                cprint("Cursor 启动失败，请手动启动", "warn")
                print()
        else:
            print("  稍后可运行以下命令启动 Cursor:")
            if IS_WINDOWS:
                print("    start.bat")
                print("    或: python scripts\\install.py --quick")
            else:
                print("    start.sh")
                print("    或: python3 scripts/install.py --quick")
            print()
    else:
        cprint("未找到 Cursor 安装路径", "warn")
        print()
        if IS_WINDOWS:
            print("请手动启动 Cursor")
            print("  开始菜单搜索 'Cursor'")
            print("  或运行: start.bat")
        else:
            print("请手动启动 Cursor")
            print("  终端运行: open -a Cursor")
            print("  或运行: scripts/start.sh")

    print()
    print_divider("─", 70)

    # 打印 MCP 管理指南
    print_mcp_guide()

# =============================================================================
# 主流程
# =============================================================================

def run():
    """主安装流程"""
    print_header("CMO-HKBQSKILL 安装向导")

    # -------------------------------------------------------------------------
    # 步骤1: 环境检查
    # -------------------------------------------------------------------------
    cprint("步骤 1/3: 环境检查", "header")
    print_divider()

    # 检测Python
    py_exe, py_ver = check_python()
    if not py_exe:
        cprint("未找到 Python!", "err")
        print()
        print("请先安装 Python 3.8+: https://www.python.org/downloads/")
        print()
        if IS_WINDOWS:
            print("Windows用户推荐从 Microsoft Store 安装 Python")
        input("\n按 Enter 键退出...")
        sys.exit(1)

    # 检查版本
    if not check_python_version(py_exe):
        cprint(f"Python版本过低! 需要 3.8+, 当前: {py_ver}", "err")
        input("\n按 Enter 键退出...")
        sys.exit(1)

    # 安装依赖
    project_root = get_project_root()
    req_file = project_root / "mcp" / "requirements.txt"

    fastmcp_installed = check_dependency(py_exe, "fastmcp")

    if not fastmcp_installed:
        cprint("检测到缺少 fastmcp 依赖", "warn")
        if not install_dependencies(py_exe, str(req_file)):
            cprint("依赖安装失败，继续安装...", "warn")
            fastmcp_installed = check_dependency(py_exe, "fastmcp")  # 再次检查
    else:
        cprint("fastmcp 已安装", "ok")

    # 修复 fastmcp __main__.py 问题（如果需要）
    if fastmcp_installed:
        if fix_fastmcp_main(py_exe):
            cprint("fastmcp 模块入口正常", "ok")
        else:
            cprint("fastmcp 模块入口修复失败", "warn")

    print()

    # -------------------------------------------------------------------------
    # 步骤2: 数据库配置
    # -------------------------------------------------------------------------
    cprint("步骤 2/3: 数据库配置", "header")
    print_divider()

    db_dir = project_root / "mcp" / "db"
    db_dir.mkdir(parents=True, exist_ok=True)

    # 检查是否已有数据库
    existing_dbs = list(db_dir.glob("*.db3"))
    if existing_dbs:
        cprint(f"检测到已有数据库: {existing_dbs[0].name}", "ok")
        db_path = str(existing_dbs[0])
    else:
        cprint("未在 mcp/db/ 找到数据库文件", "warn")
        print()

        # 尝试自动检测Steam安装
        steam_db_path = try_detect_steam_installation()
        if steam_db_path:
            cprint(f"找到Steam安装目录: {steam_db_path}", "info")
            db_files = find_cmo_db_in_directory(Path(steam_db_path))
            if db_files:
                print()
                for i, df in enumerate(db_files, 1):
                    cprint(f"  {i}. {Path(df).name}", "info")
                print()
                choice = input_prompt("选择数据库编号", "1")
                try:
                    db_path = db_files[int(choice) - 1]
                except (ValueError, IndexError):
                    db_path = db_files[0]
            else:
                db_path = None
        else:
            # 询问用户输入路径
            print()
            cprint("请提供CMO游戏安装目录路径", "step")
            print("(例如: Steam目录下的 Command_Operations 文件夹)")
            print()

            while True:
                game_path = input_prompt("CMO游戏目录")
                if not game_path:
                    cprint("请输入路径", "warn")
                    continue

                game_dir = Path(game_path)
                if not game_dir.exists():
                    cprint("路径不存在，请重试", "err")
                    continue

                # 查找DB文件夹
                db_folder = game_dir / "DB"
                if not db_folder.exists():
                    cprint("未找到DB文件夹，尝试在同级目录搜索...", "warn")
                    db_files = find_cmo_db_in_directory(game_dir)
                else:
                    db_files = find_cmo_db_in_directory(db_folder)

                if db_files:
                    print()
                    cprint("找到以下数据库文件:", "ok")
                    for i, df in enumerate(db_files, 1):
                        print(f"  {i}. {Path(df).name}")
                    print()

                    choice = input_prompt("选择数据库编号", "1")
                    try:
                        db_path = db_files[int(choice) - 1]
                        break
                    except (ValueError, IndexError):
                        db_path = db_files[0]
                        break
                else:
                    cprint("未找到 DB3K_*.db3 文件", "err")
                    print()
                    retry = input_prompt("重试? (y/n)", "y")
                    if retry.lower() != "y":
                        db_path = None
                        break

        # 复制数据库
        if db_path:
            print()
            cprint(f"准备复制数据库: {Path(db_path).name}", "info")
            success, result = copy_database(db_path)
            if success:
                cprint(f"数据库已复制到: {result}", "ok")
                db_path = result
            else:
                cprint(f"复制失败: {result}", "err")
                db_path = None

    # 验证数据库
    if db_path:
        valid, info = validate_database(db_path)
        if valid:
            cprint(f"数据库验证通过 ({info})", "ok")
        else:
            cprint(f"数据库验证失败: {info}", "err")
            db_path = None

    if not db_path:
        cprint("跳过数据库配置 (稍后手动复制)", "warn")

    print()

    # -------------------------------------------------------------------------
    # 步骤3: IDE配置
    # -------------------------------------------------------------------------
    configure_ide_interactive(project_root)

    # -------------------------------------------------------------------------
    # 完成
    # -------------------------------------------------------------------------
    print_success_panel(py_exe, project_root)

    # 创建快速启动脚本
    if create_quick_launch_scripts(project_root):
        cprint("快速启动脚本已创建 (start.bat/start.sh)", "ok")

    print()
    cprint("感谢使用 CMO-HKBQSKILL!", "title")
    input("按 Enter 键退出...")


def main():
    """主入口函数，支持命令行参数"""
    import argparse

    parser = argparse.ArgumentParser(
        description="CMO-HKBQSKILL 安装与启动工具",
        add_help=False
    )
    parser.add_argument(
        "--quick", "-q",
        action="store_true",
        help="快速启动模式 - 检测现有配置并启动 Cursor"
    )
    parser.add_argument(
        "--status", "-s",
        action="store_true",
        help="检查 MCP 服务状态"
    )
    parser.add_argument(
        "--help", "-h",
        action="store_true",
        help="显示帮助信息"
    )

    args = parser.parse_args()

    if args.help:
        print()
        print(f"{Colors.BOLD}{Colors.CYAN}CMO-HKBQSKILL 安装与启动工具{Colors.RESET}")
        print()
        print("用法:")
        print("  python install.py              # 完整安装向导")
        print("  python install.py --quick      # 快速启动 (检测已安装配置)")
        print("  python install.py --status     # 检查 MCP 服务状态")
        print("  python install.py --help       # 显示此帮助")
        print()
        print("快捷方式:")
        if IS_WINDOWS:
            print("  双击 start.bat 启动项目")
        else:
            print("  运行 scripts/start.sh 启动项目")
        print()
        return

    if args.status:
        # 检查状态模式
        print_header("MCP 服务状态检查")
        ok, status = check_mcp_status(get_project_root())

        print()
        print("检查项目:")
        print("  1. Python + fastmcp 环境")
        print("  2. MCP 脚本文件")
        print()
        print(f"  结果: {status}")
        print()

        if ok:
            cprint("环境就绪 ✓", "ok")
            print()
            cprint("Cursor MCP 连接状态需在 Cursor 中查看", "info")
            print()
            print("  可能原因:")
            print("    • Cursor 尚未重启（安装后需要重启）")
            print("    • MCP 服务器未启动")
            print()
            print("  解决方法:")
            print("    1. 重启 Cursor")
            print("    2. Ctrl+Shift+P → MCP: Restart Server → CMO_DBID_Lookup")
            print("    3. View → Output → 选择 'MCP' 查看日志")
        else:
            cprint("环境未就绪 ✗", "err")
            print()
            cprint("请重新运行完整安装: python scripts/install.py", "warn")
        print()
        return

    if args.quick:
        # 快速启动模式
        py_exe, _ = check_python()
        if not py_exe:
            cprint("未找到 Python!", "err")
            sys.exit(1)

        run_quick_start(py_exe, get_project_root())
        return

    # 默认: 完整安装向导
    run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n操作已取消。")
        sys.exit(0)
    except Exception as e:
        cprint(f"发生错误: {e}", "err")
        input("\n按 Enter 键退出...")
        sys.exit(1)
