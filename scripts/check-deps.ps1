# CMO-HKBQSKILL 依赖检查脚本

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  CMO-HKBQSKILL 依赖检查" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$allPassed = $true

# 检查 Python
Write-Host "[1/5] 检查 Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    if ($pythonVersion -match "Python (\d+)\.(\d+)") {
        $major = [int]$Matches[1]
        $minor = [int]$Matches[2]
        if ($major -ge 3 -and $minor -ge 6) {
            Write-Host "  ✓ Python $major.$minor 已安装" -ForegroundColor Green
        } else {
            Write-Host "  ✗ Python 版本过低 (需要 3.6+)" -ForegroundColor Red
            $allPassed = $false
        }
    }
} catch {
    Write-Host "  ✗ Python 未安装" -ForegroundColor Red
    $allPassed = $false
}

# 检查 uv
Write-Host ""
Write-Host "[2/5] 检查 uv 工具..." -ForegroundColor Yellow
try {
    $uvVersion = uv --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ uv 已安装" -ForegroundColor Green
    } else {
        Write-Host "  ✗ uv 未安装" -ForegroundColor Red
        $allPassed = $false
    }
} catch {
    Write-Host "  ✗ uv 未安装" -ForegroundColor Red
    $allPassed = $false
}

# 检查 Cursor 配置目录
Write-Host ""
Write-Host "[3/5] 检查 Cursor 配置..." -ForegroundColor Yellow
$cursorSettingsPath = "$env:APPDATA\Cursor\User\settings.json"
if (Test-Path $cursorSettingsPath) {
    Write-Host "  ✓ Cursor 配置目录存在" -ForegroundColor Green
} else {
    Write-Host "  ⚠ Cursor 配置目录不存在（可能未安装 Cursor）" -ForegroundColor Yellow
}

# 检查 MCP 配置
Write-Host ""
Write-Host "[4/5] 检查 MCP 配置..." -ForegroundColor Yellow
$McpConfigPath = "$env:APPDATA\Cursor\User\mcp.json"
if (Test-Path $McpConfigPath) {
    Write-Host "  ✓ MCP 配置文件存在" -ForegroundColor Green
} else {
    Write-Host "  ⚠ MCP 配置文件不存在（安装后会创建）" -ForegroundColor Yellow
}

# 检查网络连接
Write-Host ""
Write-Host "[5/5] 检查网络连接..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "https://commandlua.github.io" -Method Head -TimeoutSec 5 -ErrorAction Stop
    if ($response.StatusCode -eq 200) {
        Write-Host "  ✓ 可以访问 commandlua.github.io" -ForegroundColor Green
    }
} catch {
    Write-Host "  ⚠ 无法访问 commandlua.github.io（离线文档可用）" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
if ($allPassed) {
    Write-Host "  ✓ 所有依赖检查通过！" -ForegroundColor Green
    Write-Host "  可以运行 install.ps1 进行安装" -ForegroundColor Gray
} else {
    Write-Host "  ⚠ 部分依赖缺失，请先安装" -ForegroundColor Yellow
}
Write-Host "========================================" -ForegroundColor Cyan