# CMO DBID MCP 一键启动脚本
# 运行前请先安装依赖：pip install -r mcp/requirements.txt

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

Push-Location $ProjectRoot

# 查找可用的 Python
$PythonCmd = $null
$PythonPaths = @(
    "python",
    "python3",
    "C:\Program Files\Python313\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe"
)
foreach ($py in $PythonPaths) {
    try {
        $result = & $py --version 2>$null
        if ($LASTEXITCODE -eq 0) {
            $PythonCmd = $py
            Write-Host "    找到 Python: $PythonCmd ($result)" -ForegroundColor Green
            break
        }
    } catch { continue }
}

if (-not $PythonCmd) {
    Write-Host "    ❌ 未找到 Python，请先安装 Python 3.8+" -ForegroundColor Red
    Pop-Location
    exit 1
}

# 检查依赖
Write-Host "[1/3] 检查依赖..." -ForegroundColor Cyan
$installed = & $PythonCmd -m pip show fastmcp 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "    正在安装 fastmcp..." -ForegroundColor Yellow
    & $PythonCmd -m pip install -r mcp/requirements.txt
}

# 检查数据库
$dbPath = "$ProjectRoot\mcp\db\DB3K_514.db3"
Write-Host "[2/3] 检查数据库文件..." -ForegroundColor Cyan
if (-not (Test-Path $dbPath)) {
    Write-Host ""
    Write-Host "    ⚠ 数据库文件未找到！" -ForegroundColor Red
    Write-Host "    请将 CMO 数据库文件复制到:" -ForegroundColor Yellow
    Write-Host "    $dbPath" -ForegroundColor White
    Write-Host ""
    Write-Host "    CMO 数据库通常位于:" -ForegroundColor Yellow
    Write-Host "    Command - Modern Operations\DB\DB3K_xxx.db3" -ForegroundColor White
    Write-Host ""
    $response = Read-Host "按回车退出，或输入自定义路径后回车继续..."
    if ($response -ne "") {
        $env:SQLITE_DB_PATH = $response
        Write-Host "    已设置 SQLITE_DB_PATH=$env:SQLITE_DB_PATH" -ForegroundColor Green
    } else {
        Pop-Location
        exit 1
    }
} else {
    Write-Host "    ✅ 数据库文件已就绪" -ForegroundColor Green
}

# 启动 MCP
Write-Host ""
Write-Host "[3/3] 启动 MCP 服务..." -ForegroundColor Cyan
Write-Host ""
Write-Host "    保持此窗口运行，然后在 IDE 中加载 SKILL.md 开始对话" -ForegroundColor White
Write-Host ""
Write-Host "    💡 提示：Cursor/Trae 可以通过 MCP 自动连接此服务" -ForegroundColor Gray
Write-Host ""

# 设置环境变量
$env:SQLITE_DB_PATH = $dbPath

& $PythonCmd mcp/server.py

Pop-Location
