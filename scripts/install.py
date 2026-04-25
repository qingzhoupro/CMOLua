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
            Path(lp) / "Programs" / "Python" / "Python313" / "python.exe",
            Path(lp) / "Programs" / "Python" / "Python312" / "python.exe",
            Path(pf) / "Python313" / "python.exe",
            Path(pf) / "Python312" / "python.exe",
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
        return False, f"MCP 脚本不存在"

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
                # 检查是否是 __main__.py 缺失问题
                if "No module named fastmcp.__main__" in result.stderr or \
                   "'fastmcp' is a package" in result.stderr:
                    # 尝试自动修复
                    if fix_fastmcp_main(py_exe):
                        # 修复后再次检查
                        result = subprocess.run(
                            [py_exe, "-m", "fastmcp", "--version"],
                            capture_output=True, text=True, timeout=10
                        )
                        if result.returncode == 0:
                            return True, f"就绪 (已自动修复)"
                    else:
                        continue
                else:
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


def print_mcp_guide(selected_ide: str = "Cursor"):
    """打印 MCP 管理指南

    Args:
        selected_ide: 用户选择的 IDE 名称
    """
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
    print(f"  重启 MCP 服务 ({selected_ide} 已打开时):")
    print("    Ctrl+Shift+P → 输入 'MCP: Restart Server' → 选择 'CMO_DBID_Lookup'")
    print()
    print_divider("─", 70)
    print()
    print(f"{Colors.BOLD}【故障排除】{Colors.RESET}")
    print()
    print("  MCP 连接失败时尝试:")
    print("    1. 重启 IDE")
    print("    2. 检查 fastmcp: python -m fastmcp --version")
    print("    3. 重新运行安装: python scripts/install.py")
    print()
    print("  检查 MCP 日志:")
    print("    View → Output → 切换到 'MCP' 标签页")
    print()
    print_divider("─", 70)
    print()
    print(f"{Colors.BOLD}【卸载/重装】{Colors.RESET}")
    print()
    print("  完全重装:")
    print(f"    1. 删除 IDE 的 MCP 相关缓存")
    print(f"    2. 删除 mcp.json 中的 CMO_DBID_Lookup 配置")
    print("    3. 重新运行 python scripts/install.py")
    print()
    print_divider("=", 70)
    print()


def detect_running_ide() -> Optional[str]:
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


def detect_running_ide() -> Optional[str]:
    """检测当前运行的 IDE"""
    if IS_WINDOWS:
        # 检查进程名
        processes = ["Cursor.exe", "Trae.exe", "Code.exe"]
        for proc in processes:
            try:
                result = subprocess.run(
                    ["tasklist", "/FI", f"IMAGENAME eq {proc}"],
                    capture_output=True, text=True, timeout=5
                )
                if proc in result.stdout:
                    if proc == "Cursor.exe":
                        return "Cursor"
                    elif proc == "Trae.exe":
                        return "Trae"
                    elif proc == "Code.exe":
                        return "VS Code"
            except Exception:
                continue
    elif IS_MAC:
        for name in ["Cursor", "Trae", "Visual Studio Code"]:
            try:
                result = subprocess.run(
                    ["pgrep", "-x", name],
                    capture_output=True, text=True, timeout=5
                )
                if result.returncode == 0:
                    return name
            except Exception:
                continue
    return None


def run_quick_start(python_exe: str, project_root: Path) -> bool:
    """快速启动模式 - 检测现有配置并启动 IDE"""
    script_path = project_root / "mcp" / "sqlite_explorer.py"
    
    # 检测所有已安装的 IDE
    installed_ides = detect_installed_ides()
    running_ide = detect_running_ide()
    
    print()
    print_divider("─", 60)
    print()
    cprint("快速启动模式", "header")
    print()
    
    # 检测 Python 和 fastmcp
    cprint("检测环境...", "step")
    py_exe, py_ver = check_python()
    if py_exe:
        cprint(f"  Python: {py_ver}", "ok")
    else:
        cprint("  未找到 Python", "err")
    
    fastmcp_ok = check_dependency(python_exe, "fastmcp")
    if fastmcp_ok:
        cprint("  fastmcp: 已安装", "ok")
    else:
        cprint("  fastmcp: 未安装", "warn")
    
    # 检测数据库
    db_path = detect_db_file(project_root)
    if db_path:
        db_name = Path(db_path).name
        cprint(f"  数据库: {db_name}", "ok")
    else:
        cprint("  数据库: 未找到", "warn")
    
    print()
    
    # 显示已安装的 IDE
    if installed_ides:
        cprint("已检测到的 IDE:", "step")
        for ide_name, config_path in installed_ides:
            running_marker = " (运行中)" if ide_name == running_ide else ""
            exists_marker = " ●" if config_path and config_path.exists() else " ○"
            print(f"  {exists_marker} {ide_name}{running_marker}")
            if config_path:
                print(f"      {Colors.DIM}{config_path}{Colors.RESET}")
    else:
        cprint("未检测到支持的 IDE", "warn")
        print()
        print("  请先运行完整安装: python scripts/install.py")
        return False
    
    print()
    
    # 如果有 IDE 在运行，提示重启 MCP
    if running_ide:
        cprint(f"检测到 {running_ide} 已在运行", "info")
        print()
        print("  请在 IDE 中重启 MCP 服务:")
        print("  Ctrl+Shift+P → 输入 'MCP: Restart Server'")
        print("  → 选择 'CMO_DBID_Lookup'")
        print()
        print("  或直接重启 IDE")
    else:
        # 尝试启动第一个检测到的 IDE
        first_ide = installed_ides[0][0] if installed_ides else None
        if first_ide:
            cprint(f"准备启动 {first_ide}...", "info")
            ide_path = _get_ide_exe_path(first_ide)
            if ide_path and ide_path.exists():
                if launch_ide(first_ide, str(ide_path)):
                    cprint(f"{first_ide} 启动中...", "ok")
                else:
                    cprint("启动失败，请手动启动", "err")
            else:
                print(f"  请手动启动 {first_ide}")
    
    # 确保启动脚本存在
    create_quick_launch_scripts(project_root)
    
    print()
    return True


def launch_ide(ide_name: str, app_path: Optional[str] = None) -> bool:
    """启动 IDE"""
    try:
        if app_path and os.path.exists(app_path):
            cmd = [app_path]
        elif IS_WINDOWS:
            if ide_name == "Cursor":
                cmd = ["cmd", "/c", "start", "", "Cursor"]
            elif ide_name == "Trae":
                cmd = ["cmd", "/c", "start", "", "Trae"]
            elif ide_name == "VS Code":
                cmd = ["cmd", "/c", "start", "", "Code"]
            else:
                cmd = ["cmd", "/c", "start", "", ide_name]
        elif IS_MAC:
            cmd = ["open", "-a", ide_name]
        else:
            cmd = [ide_name.lower().replace(" ", "-")]
        
        subprocess.Popen(cmd, detached=True, start_new_session=True)
        return True
    except Exception:
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
        # 获取 fastmcp 包的实际安装路径
        result = subprocess.run(
            [python_exe, "-c", "import fastmcp; import os; print(os.path.dirname(fastmcp.__file__))"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            cprint(f"无法定位 fastmcp 包: {result.stderr[:100]}", "warn")
            return False

        fastmcp_dir = result.stdout.strip()
        if not fastmcp_dir:
            cprint("fastmcp 路径为空", "warn")
            return False

        main_py = os.path.join(fastmcp_dir, "__main__.py")

        if os.path.exists(main_py):
            cprint(f"fastmcp __main__.py 已存在: {main_py}", "ok")
            return True

        # 创建 __main__.py
        main_content = '''"""Entry point for running fastmcp as a module."""

import sys
from fastmcp.cli.cli import app

if __name__ == "__main__":
    app()
'''
        # 确保目录存在
        os.makedirs(os.path.dirname(main_py), exist_ok=True)
        
        with open(main_py, "w", encoding="utf-8") as f:
            f.write(main_content)

        cprint(f"已创建 fastmcp __main__.py: {main_py}", "ok")
        return True
    except PermissionError:
        cprint("权限不足，无法创建 __main__.py，请以管理员身份运行", "err")
        return False
    except Exception as e:
        cprint(f"修复 fastmcp 失败: {e}", "warn")
        return False


def ensure_fastmcp_works(python_exe: str) -> bool:
    """确保 fastmcp 可以作为模块运行
    
    尝试多种方式确保 python -m fastmcp 能工作：
    1. 检查 __main__.py 是否存在
    2. 如果不存在则创建
    3. 验证修复是否成功
    """
    cprint("检查 fastmcp 模块...", "step")
    
    # 首先测试当前状态
    test_result = subprocess.run(
        [python_exe, "-m", "fastmcp", "--version"],
        capture_output=True, text=True, timeout=10
    )
    
    if test_result.returncode == 0:
        cprint("fastmcp 模块可正常运行", "ok")
        return True
    
    # 尝试修复
    cprint("尝试修复 fastmcp 模块...", "info")
    
    if fix_fastmcp_main(python_exe):
        # 验证修复
        verify_result = subprocess.run(
            [python_exe, "-m", "fastmcp", "--version"],
            capture_output=True, text=True, timeout=10
        )
        if verify_result.returncode == 0:
            cprint("fastmcp 修复成功", "ok")
            return True
        else:
            cprint(f"fastmcp 仍无法运行: {verify_result.stderr[:100]}", "warn")
            return False
    
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
#   aliases          - 其他已知的目录名称（如 Trae CN 的 "Trae" 文件夹）
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
        "aliases": [],
    },
    "Trae": {
        "config_file": "mcp.json",
        "paths": {
            "win32":  "Trae/User/mcp.json",
            "darwin": "Trae/User/mcp.json",
            "linux":  "Trae/User/mcp.json",
        },
        "is_project_path": False,
        "config_format": "mcpServers",
        # Trae CN 版本可能安装在 "Trae" 子目录下
        "aliases": ["Trae"],
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
        "aliases": [],
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
        "aliases": [],
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
    config_base = get_ide_base_dir()

    for ide_name in IDE_CONFIG_MAP:
        config_path = get_ide_config_path(ide_name, project_root)
        if config_path is None:
            continue
        
        found = False
        
        # 1. 检查主路径
        if config_path.exists() or config_path.parent.exists():
            detected.append((ide_name, config_path))
            continue
        
        # 2. 检查别名路径（如 Trae CN 可能是 "Trae" 子目录）
        entry = IDE_CONFIG_MAP[ide_name]
        if entry.get("aliases"):
            for alias in entry["aliases"]:
                # 构造别名路径
                if IS_WINDOWS:
                    alias_base = config_base / alias
                else:
                    alias_base = config_base / alias
                alias_path = alias_base / "User" / entry["config_file"]
                if alias_path.exists() or alias_base.exists():
                    detected.append((ide_name, alias_path))
                    found = True
                    break
        
        if not found:
            # 3. 也检查可执行文件
            exe_path = _get_ide_exe_path(ide_name)
            if exe_path and exe_path.exists():
                detected.append((ide_name, config_path))

    return detected


def _get_ide_exe_path(ide_name: str) -> Optional[Path]:
    """获取 IDE 可执行文件路径"""
    if not IS_WINDOWS:
        return None
    
    program_files = Path(os.environ.get("ProgramFiles", "C:\\Program Files"))
    program_files_x86 = Path(os.environ.get("ProgramFiles(X86)", "C:\\Program Files (x86)"))
    
    exe_map = {
        "Cursor":          program_files_x86 / "Cursor" / "Cursor.exe",
        "Trae":            program_files / "Trae" / "Trae.exe",
        "VS Code":         program_files_x86 / "Microsoft VS Code" / "Code.exe",
        "Claude Desktop":  program_files_x86 / "Claude" / "Claude.exe",
    }
    
    # Trae CN 可能安装在不同的位置
    trae_paths = [
        program_files / "Trae" / "Trae.exe",
        Path("C:/Program Files/Trae/Trae.exe"),
    ]
    
    if ide_name == "Trae":
        for p in trae_paths:
            if p.exists():
                return p
        return exe_map.get("Trae")
    
    return exe_map.get(ide_name)


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


def configure_ide_interactive(project_root: Path) -> str:
    """交互式 IDE 配置向导（步骤3核心）

    Returns:
        用户选择的 IDE 名称
    """
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
        return selected_ide

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
            return selected_ide
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

    return selected_ide


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

def print_success_panel(python_exe: str, project_root: Path, selected_ide: str = "Cursor"):
    """打印成功完成面板并启动 IDE

    Args:
        python_exe: Python 可执行文件路径
        project_root: 项目根目录
        selected_ide: 用户选择的 IDE 名称
    """
    script_path = project_root / "mcp" / "sqlite_explorer.py"
    ide_path = _get_ide_exe_path(selected_ide)

    # 检查 MCP 状态
    mcp_ok, mcp_status = check_mcp_status(project_root)

    print()
    print_divider("─", 70)
    print()

    success_text = f"""
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
        # 截断状态信息以适应面板宽度
        status_line1 = mcp_status[:18].ljust(18)
        status_line2 = mcp_status[18:36].ljust(18) if len(mcp_status) > 18 else "                  "
        success_text += f"""
    ║     SYSTEM STATUS    : PARTIAL                           ║
    ║     MCP SERVER      : {status_line1}                 ║
    ║     DATABASE        : {status_line2}                 ║"""

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

    # 自动启动 IDE
    if ide_path and os.path.exists(ide_path):
        print_divider("─", 70)
        print()
        launch_choice = input_prompt(f"是否立即启动 {selected_ide}? (y/n)", "y")
        print()

        if launch_choice.lower() in ("y", "yes", ""):
            if launch_ide(selected_ide, str(ide_path)):
                cprint(f"{selected_ide} 启动中...", "ok")
                print()
                print(f"  MCP 服务将在 {selected_ide} 启动后自动连接")
                print()
            else:
                cprint(f"{selected_ide} 启动失败，请手动启动", "warn")
                print()
        else:
            print(f"  稍后可运行以下命令启动 {selected_ide}:")
            if IS_WINDOWS:
                print("    start.bat")
                print("    或: python scripts\\install.py --quick")
            else:
                print("    start.sh")
                print("    或: python3 scripts/install.py --quick")
            print()
    else:
        cprint(f"未找到 {selected_ide} 安装路径", "warn")
        print()
        if IS_WINDOWS:
            print(f"请手动启动 {selected_ide}")
            print("  开始菜单搜索")
            print("  或运行: start.bat")
        else:
            print(f"请手动启动 {selected_ide}")
            print("  终端运行相关命令")

    print()
    print_divider("─", 70)

    # 打印 MCP 管理指南
    print_mcp_guide(selected_ide)

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

    # 确保 fastmcp 可以作为模块运行
    if fastmcp_installed:
        if not ensure_fastmcp_works(py_exe):
            cprint("fastmcp 无法正常运行，可能影响 MCP 服务", "warn")

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
    selected_ide = configure_ide_interactive(project_root)

    # -------------------------------------------------------------------------
    # 完成
    # -------------------------------------------------------------------------
    print_success_panel(py_exe, project_root, selected_ide)

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
