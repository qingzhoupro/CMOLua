# CMO-HKBQSKILL start-mcp.ps1
# Starts the MCP server with a clean status display.
# 首次运行时会引导用户配置数据库路径

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$ServerScript = Join-Path $ProjectRoot "mcp\sqlite_explorer.py"
$ReqFile      = Join-Path $ProjectRoot "mcp\requirements.txt"
$DbDir        = Join-Path $ProjectRoot "mcp\db"
$EnvFile      = Join-Path $ProjectRoot ".env"

function Find-Python {
    $candidates = @("python", "python3",
        "C:\Program Files\Python313\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe")
    foreach ($c in $candidates) {
        try {
            $v = & $c --version 2>$null
            if ($LASTEXITCODE -eq 0) { return @{cmd=$c; version=$v} }
        } catch { continue }
    }
    return $null
}

function Get-SavedDbPath {
    if (Test-Path $EnvFile) {
        $content = Get-Content $EnvFile -Raw
        if ($content -match 'SQLITE_DB_PATH="([^"]+)"') {
            $path = $matches[1]
            if (Test-Path $path) { return $path }
        }
    }
    return $null
}

function Save-DbPath {
    param($Path)
    $env:SQLITE_DB_PATH = $Path
    @"
# CMO Database Configuration
# Created by start-mcp.ps1

SQLITE_DB_PATH="$Path"
"@ | Out-File -FilePath $EnvFile -Encoding UTF8
    Write-Host "  [SAVE] Path saved to .env" -ForegroundColor Green
}

function Find-Database {
    $candidates = @(Get-ChildItem $DbDir -Filter "*.db3" -ErrorAction SilentlyContinue)
    if ($candidates.Count -gt 0) {
        return $candidates[0].FullName
    }
    return $null
}

function Show-FirstRun-Wizard {
    Write-Host ""
    Write-Host "  ============================================" -ForegroundColor Yellow
    Write-Host "  First Run Setup - Database Configuration" -ForegroundColor Yellow
    Write-Host "  ============================================" -ForegroundColor Yellow
    Write-Host ""

    # 1. Check for existing .db3 files
    $found = Find-Database

    if ($found) {
        Write-Host "  [FOUND] $found" -ForegroundColor Green
        Write-Host ""
        $ans = Read-Host "  Use this database? [Y/n]"
        if ($ans -ne "n") {
            Save-DbPath $found
            return $found
        }
    }

    # 2. Prompt for path
    Write-Host ""
    Write-Host "  No .db3 file found in mcp\db\" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  Please copy your DB3K_*.db3 file to mcp\db\" -ForegroundColor White
    Write-Host "  Or enter the full path below:" -ForegroundColor White
    Write-Host ""

    while ($true) {
        $path = Read-Host "  Database path (or 'q' to quit)"
        if ($path -eq "q") { exit 0 }
        if (Test-Path $path) {
            if (-not $path.EndsWith(".db3") -and -not $path.EndsWith(".db")) {
                Write-Host "  [WARN] File does not have .db3 extension" -ForegroundColor Yellow
            }
            Save-DbPath $path
            return $path
        }
        Write-Host "  [ERROR] File not found" -ForegroundColor Red
    }
}

# Banner
Write-Host ""
Write-Host "  ============================================" -ForegroundColor Cyan
Write-Host "     CMO DBID Lookup MCP Server" -ForegroundColor Cyan
Write-Host "  ============================================" -ForegroundColor Cyan
Write-Host ""

# Python
$py = Find-Python
if (-not $py) {
    Write-Host "  [FAIL] Python not found. Install Python 3.8+ and add to PATH." -ForegroundColor Red
    exit 1
}
Write-Host "  [OK]   Python: $($py.version)" -ForegroundColor Green

# Dependencies
$installed = & $py.cmd -m pip show fastmcp 2>$null
if ($LASTEXITCODE -ne 0 -or -not $installed) {
    Write-Host "  [INFO] Installing fastmcp..." -ForegroundColor Yellow
    & $py.cmd -m pip install -r $ReqFile 2>$null | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  [FAIL] pip install failed." -ForegroundColor Red
        exit 1
    }
    Write-Host "  [OK]   fastmcp installed" -ForegroundColor Green
} else {
    Write-Host "  [OK]   fastmcp already installed" -ForegroundColor Green
}

# Database - First run wizard or saved config
$dbFile = $null

# Try saved config first
$savedPath = Get-SavedDbPath
if ($savedPath) {
    $dbFile = $savedPath
    Write-Host "  [OK]   Database: $(Split-Path $dbFile -Leaf)" -ForegroundColor Green
} else {
    # First run wizard
    $dbFile = Show-FirstRun-Wizard
}

Write-Host ""

# Launch
Write-Host "  [INFO] Starting MCP server..." -ForegroundColor Cyan
Write-Host "  [INFO] Press Ctrl+C to stop" -ForegroundColor Gray
Write-Host ""

Push-Location $ProjectRoot
$env:SQLITE_DB_PATH = $dbFile
& $py.cmd -m fastmcp run $ServerScript
$exitCode = $LASTEXITCODE
Pop-Location

if ($exitCode -ne 0) {
    Write-Host ""
    Write-Host "  [FAIL] MCP server exited with code $exitCode" -ForegroundColor Red
}
exit $exitCode
