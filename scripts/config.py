#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CMO 数据库交互式配置工具
首次运行时引导用户配置数据库路径和其他选项
"""

import os
import sys
from pathlib import Path


def get_project_root():
    """获取项目根目录（脚本所在位置向上两级）"""
    return Path(__file__).parent.parent.resolve()


def get_default_db_path():
    """获取默认数据库路径"""
    root = get_project_root()
    db_dir = root / "mcp" / "db"
    candidates = list(db_dir.glob("*.db3")) if db_dir.exists() else []
    if candidates:
        return str(sorted(candidates, key=lambda x: x.stat().st_mtime, reverse=True)[0])
    return str(db_dir / "DB3K_514.db3")


def find_existing_db():
    """查找已存在的数据库文件"""
    root = get_project_root()
    db_dir = root / "mcp" / "db"

    if not db_dir.exists():
        return None

    candidates = sorted(db_dir.glob("*.db3"), key=lambda x: x.stat().st_mtime, reverse=True)
    return candidates[0] if candidates else None


def print_banner():
    print("=" * 60)
    print("  CMO Database Configuration Tool")
    print("  首次运行配置向导")
    print("=" * 60)
    print()


def print_status(message, status="info"):
    symbols = {"ok": "[OK]", "warn": "[!]", "info": "[*]", "fail": "[X]"}
    colors = {"ok": "\033[92m", "warn": "\033[93m", "info": "\033[94m", "fail": "\033[91m"}
    reset = "\033[0m"
    print(f"  {colors.get(status, '')}{symbols.get(status, '[*]')}{reset} {message}")


def interactive_config():
    """交互式配置流程"""
    print_banner()

    root = get_project_root()
    config_file = root / ".env"
    db_path = None

    # 步骤1: 检查现有配置
    print_status("检查现有配置...", "info")
    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("SQLITE_DB_PATH="):
                    db_path = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break

    if db_path and Path(db_path).exists():
        print_status(f"找到已保存的数据库: {db_path}", "ok")
        print()
        response = input("  是否使用此数据库? (Y/n): ").strip().lower()
        if response != "n":
            return db_path

    # 步骤2: 自动发现
    print_status("搜索本地数据库文件...", "info")
    existing_db = find_existing_db()

    if existing_db:
        print_status(f"自动发现: {existing_db.name}", "ok")
        print()
        response = input(f"  使用此数据库? (Y/n): ").strip().lower()
        if response != "n":
            save_config(str(existing_db))
            return str(existing_db)

    # 步骤3: 手动输入
    print_status("未找到数据库文件", "warn")
    print()
    print("  请选择数据库来源:")
    print("  1. 输入完整路径")
    print("  2. 拖拽文件到终端")
    print()

    while True:
        choice = input("  请选择 (1/2) 或直接粘贴路径: ").strip()

        if not choice:
            continue

        # 如果是直接粘贴的路径
        if Path(choice).exists() and Path(choice).suffix == ".db3":
            db_path = choice
            break

        # 如果是选项1
        if choice == "1":
            print()
            default_path = get_default_db_path()
            db_path = input(f"  请输入数据库路径 (直接回车使用默认): ").strip()
            if not db_path:
                db_path = default_path
            break

        # 如果是选项2，提示拖拽
        if choice == "2":
            print()
            print("  请将 .db3 文件拖拽到终端窗口中...")
            print()

    # 验证路径
    if not db_path:
        print_status("未提供有效路径", "fail")
        sys.exit(1)

    db_path = Path(db_path).resolve()

    if not db_path.exists():
        print_status(f"文件不存在: {db_path}", "fail")
        sys.exit(1)

    if db_path.suffix not in [".db3", ".db"]:
        print_status(f"警告: 文件扩展名不是 .db3: {db_path}", "warn")

    print_status(f"已选择: {db_path}", "ok")
    print()

    # 步骤4: 保存配置
    response = input("  是否保存此配置供以后使用? (Y/n): ").strip().lower()
    if response != "n":
        save_config(str(db_path))
        print_status("配置已保存到 .env 文件", "ok")
    else:
        print_status("配置未保存（仅本次有效）", "warn")

    print()
    return str(db_path)


def save_config(db_path):
    """保存配置到 .env 文件"""
    root = get_project_root()
    config_file = root / ".env"

    # 读取现有配置
    config = {}
    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    key, val = line.split("=", 1)
                    config[key.strip()] = val.strip().strip('"').strip("'")

    # 更新数据库路径
    config["SQLITE_DB_PATH"] = db_path

    # 写回文件
    with open(config_file, "w", encoding="utf-8") as f:
        f.write("# CMO Database Configuration\n")
        f.write("# 此文件由 config.py 自动生成\n\n")
        for key, val in config.items():
            f.write(f'{key}="{val}"\n')


def load_config_from_env():
    """从环境变量或 .env 文件加载配置"""
    # 1. 先检查环境变量
    env_path = os.environ.get("SQLITE_DB_PATH")
    if env_path and Path(env_path).exists():
        return env_path

    # 2. 检查 .env 文件
    root = get_project_root()
    config_file = root / ".env"
    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("SQLITE_DB_PATH="):
                    path = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if Path(path).exists():
                        return path

    # 3. 自动发现
    existing_db = find_existing_db()
    if existing_db:
        return str(existing_db)

    return None


def main():
    import argparse

    parser = argparse.ArgumentParser(description="CMO 数据库配置工具")
    parser.add_argument("--check", action="store_true", help="仅检查配置状态")
    parser.add_argument("--path", type=str, help="设置数据库路径")
    parser.add_argument("--interactive", "-i", action="store_true", help="交互式配置")
    args = parser.parse_args()

    if args.check:
        # 仅检查模式
        db_path = load_config_from_env()
        if db_path:
            print(f"Database: {db_path}")
            print("Status: Configured")
            sys.exit(0)
        else:
            print("Status: Not configured")
            sys.exit(1)

    elif args.path:
        # 直接设置路径
        db_path = Path(args.path).resolve()
        if not db_path.exists():
            print(f"Error: File not found: {db_path}")
            sys.exit(1)
        save_config(str(db_path))
        print(f"Database path saved: {db_path}")
        sys.exit(0)

    else:
        # 交互式配置
        db_path = interactive_config()
        print()
        print("=" * 60)
        print(f"  配置完成！数据库路径: {db_path}")
        print("=" * 60)
        print()
        print("  后续使用方式:")
        print(f"  1. 设置环境变量: set SQLITE_DB_PATH={db_path}")
        print(f"  2. 或确保 .env 文件已配置")
        print()


if __name__ == "__main__":
    main()
