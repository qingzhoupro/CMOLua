# CMO-HKBQSKILL start-mcp.ps1
# Starts the MCP server with a clean status display.

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$ServerScript = Join-Path $ProjectRoot "mcp\server.py"
$ReqFile      = Join-Path $ProjectRoot "mcp\requirements.txt"
$DbDir        = Join-Path $ProjectRoot "mcp\db"

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

# ── Banner ───────────────────────────────────────────────────────────────────
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

# Database
$dbCandidates = @(Get-ChildItem $DbDir -Filter "*.db3" -ErrorAction SilentlyContinue)
if ($dbCandidates.Count -eq 0) {
    Write-Host ""
    Write-Host "  [FAIL] No .db3 file found in mcp/db/" -ForegroundColor Red
    Write-Host "  Copy your DB3K_*.db3 file into mcp/db/ and re-run." -ForegroundColor Yellow
    exit 1
}
$dbFile = $dbCandidates[0]
Write-Host "  [OK]   Database: $($dbFile.Name)" -ForegroundColor Green
Write-Host ""

# Launch
Write-Host "  [INFO] Starting MCP server..." -ForegroundColor Cyan
Write-Host "  [INFO] Press Ctrl+C to stop" -ForegroundColor Gray
Write-Host ""

Push-Location $ProjectRoot
& $py.cmd -m fastmcp run $ServerScript
$exitCode = $LASTEXITCODE
Pop-Location

if ($exitCode -ne 0) {
    Write-Host ""
    Write-Host "  [FAIL] MCP server exited with code $exitCode" -ForegroundColor Red
}
exit $exitCode
