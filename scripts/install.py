#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CMO-HKBQSKILL 交互式安装向导
跨平台兼容：Windows / macOS / Linux
纯 Python，无需额外依赖
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
# 步骤3: IDE配置
# =============================================================================

IDE_OPTIONS = [
    ("Cursor", "Cursor", ["Cursor", "User", "mcp.json"]),
    ("Trae AI", "Trae", ["Trae", "User", "mcp.json"]),
    ("VS Code", "VSCode", ["Code", "User", "mcp.json"]),
    ("Claude Desktop", "Claude", ["Claude", "config.json"]),
]

def get_ide_config_path(ide_name: str) -> Optional[Path]:
    """获取IDE的MCP配置文件路径"""
    for display_name, folder_name, config_path in IDE_OPTIONS:
        if display_name == ide_name or folder_name == ide_name:
            if IS_WINDOWS:
                base = Path(os.environ.get("APPDATA", get_config_dir()))
            elif IS_MAC:
                base = get_home_dir() / "Library" / "Application Support"
            else:
                base = get_home_dir() / ".config"

            # Claude Desktop 使用不同的配置结构
            if folder_name == "Claude":
                # Claude Desktop: ~/.config/Claude/claude_desktop_config.json
                config_file = base / "Claude" / "claude_desktop_config.json"
            else:
                config_file = base / Path(*config_path)

            return config_file

    return None

def detect_installed_ides() -> list:
    """检测已安装的IDE"""
    detected = []
    for display_name, folder_name, _ in IDE_OPTIONS:
        config_path = get_ide_config_path(display_name)
        if config_path and (config_path.exists() or config_path.parent.exists()):
            detected.append((display_name, config_path))

    # 备用检测方式：检查常见路径
    if IS_WINDOWS:
        program_files = os.environ.get("ProgramFiles", "C:\\Program Files")
        program_files_x86 = os.environ.get("ProgramFiles(X86)", "C:\\Program Files (x86)")

        common_apps = [
            ("Cursor", Path(program_files) / "Cursor" / "Cursor.exe"),
            ("Trae AI", Path(program_files) / "Trae" / "Trae.exe"),
            ("VS Code", Path(program_files_x86) / "Microsoft VS Code" / "Code.exe"),
        ]

        for name, path in common_apps:
            if path.exists() and name not in [d[0] for d in detected]:
                detected.append((name, None))
        if Path(program_files) / "Microsoft VS Code" / "Code.exe" in [p for _, p in detected]:
            detected.append(("VS Code", None))

    return detected

def read_existing_config(config_file: Path) -> dict:
    """读取现有配置文件"""
    if not config_file.exists():
        return {}

    try:
        with open(config_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def write_mcp_config(config_file: Path, project_root: Path, script_name: str = "sqlite_explorer.py") -> bool:
    """写入MCP配置"""
    try:
        # 确保目录存在
        config_file.parent.mkdir(parents=True, exist_ok=True)

        # 读取现有配置
        config = read_existing_config(config_file)

        # 备份原配置
        if config_file.exists():
            backup_path = config_file.with_suffix(".json.backup")
            shutil.copy2(config_file, backup_path)
            cprint(f"已备份原配置到: {backup_path.name}", "info")

        # 构建MCP服务器配置
        mcp_server_config = {
            "command": "python",
            "args": ["-m", "fastmcp", "run", f"mcp/{script_name}"],
            "env": {
                "SQLITE_DB_PATH": str(project_root / "mcp" / "db" / "DB3K_514.db3")
            }
        }

        # 根据IDE类型选择配置结构
        if "claude_desktop" in config_file.name:
            # Claude Desktop 格式
            if "mcpServers" not in config:
                config["mcpServers"] = {}
            config["mcpServers"]["CMO_DBID_Lookup"] = mcp_server_config
        else:
            # Cursor/Trae/VSCode 格式
            if "mcpServers" not in config:
                config["mcpServers"] = {}
            config["mcpServers"]["CMO_DBID_Lookup"] = mcp_server_config

        # 写入配置
        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

        return True

    except Exception as e:
        cprint(f"写入配置失败: {e}", "err")
        return False

# =============================================================================
# 完成面板
# =============================================================================

def print_success_panel():
    """打印成功完成面板"""
    print()
    print_divider("─", 60)
    print()

    success_text = """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║                   海 空 兵 棋                             ║
    ║              CMO-Lua 安装向导                             ║
    ║                                                          ║
    ║     ALL SYSTEM STATUS : NOMINAL                          ║
    ║     MCP SERVER       : READY                             ║
    ║     DATABASE         : CONNECTED                         ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """

    if USE_COLOR:
        print(f"{Colors.GREEN}{Colors.BOLD}{success_text}{Colors.RESET}")
    else:
        print(success_text)

    print()
    cprint("安装完成!", "title")
    print()
    cprint("下一步操作:", "step")
    print("  1. 重启你的 IDE (Cursor / Trae / VS Code)")
    print("  2. 让 AI 加载 SKILL.md 文件")
    print("  3. 开始查询 CMO 数据库!")
    print()
    print_divider("─", 60)

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

    if not check_dependency(py_exe, "fastmcp"):
        cprint("检测到缺少 fastmcp 依赖", "warn")
        if not install_dependencies(py_exe, str(req_file)):
            cprint("依赖安装失败，继续安装...", "warn")
    else:
        cprint("fastmcp 已安装", "ok")

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
    cprint("步骤 3/3: IDE配置", "header")
    print_divider()

    cprint("支持的IDE:", "info")
    for i, (display_name, _, _) in enumerate(IDE_OPTIONS, 1):
        print(f"  {i}. {display_name}")
    print()

    ide_choice = input_prompt("选择要配置的IDE (输入编号)", "1")

    try:
        ide_index = int(ide_choice) - 1
        if ide_index < 0 or ide_index >= len(IDE_OPTIONS):
            raise ValueError()
        selected_ide = IDE_OPTIONS[ide_index][0]
    except ValueError:
        cprint("无效选择，默认为 Cursor", "warn")
        selected_ide = "Cursor"

    cprint(f"已选择: {selected_ide}", "ok")

    # 获取配置路径
    config_path = get_ide_config_path(selected_ide)
    if not config_path:
        cprint("无法确定配置文件位置", "err")
        input("\n按 Enter 键退出...")
        sys.exit(1)

    cprint(f"配置文件路径: {config_path}", "dim")

    # 写入配置
    if write_mcp_config(config_path, project_root):
        cprint("MCP配置写入成功!", "ok")
    else:
        cprint("MCP配置写入失败", "err")

    print()

    # -------------------------------------------------------------------------
    # 完成
    # -------------------------------------------------------------------------
    print_success_panel()

    print()
    cprint("感谢使用 CMO-HKBQSKILL!", "title")
    input("按 Enter 键退出...")

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n\n安装已取消。")
        sys.exit(0)
    except Exception as e:
        cprint(f"发生错误: {e}", "err")
        input("\n按 Enter 键退出...")
        sys.exit(1)
