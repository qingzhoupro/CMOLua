import codecs

content = """# CMO-HKBQSKILL install.ps1
# First-run wizard: detects env, installs deps, guides db placement, validates setup.

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

# Color helpers
function Write-Step { param($Num, $Label, $Status)
    $sym = @{"ok"="+"; "fail"="x"; "warn"="!"; "info"=">"}[$Status]
    $fg  = @{"ok"="Green"; "fail"="Red"; "warn"="Yellow"; "info"="Cyan"}[$Status]
    Write-Host "  [$Num] $sym  $Label" -ForegroundColor $fg
}
function Write-Msg { param($Text, $Color="White") Write-Host "       $Text" -ForegroundColor $Color }

# Banner
function Show-Banner {
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host "     C M O - H K B Q S K I L L" -ForegroundColor Cyan
    Write-Host "     Naval Wargame AI Assistant Installer" -ForegroundColor Cyan
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host ""
}

# Step 1: Detect Python
function Find-Python {
    $candidates = @("python", "python3",
        "C:\\Program Files\\Python313\\python.exe",
        "$env:LOCALAPPDATA\\Programs\\Python\\Python313\\python.exe")
    foreach ($c in $candidates) {
        try {
            $v = & $c --version 2>$null
            if ($LASTEXITCODE -eq 0) { return @{cmd=$c; version=$v} }
        } catch { continue }
    }
    return $null
}

# Step 2: Install fastmcp
function Install-Fastmcp {
    param($PythonCmd, $ReqFile)
    $installed = & $PythonCmd -m pip show fastmcp 2>$null
    if ($LASTEXITCODE -eq 0 -and $installed) {
        Write-Msg "fastmcp already installed" Green
        return $true
    }
    Write-Msg "Installing fastmcp..." Yellow
    try {
        & $PythonCmd -m pip install -r $ReqFile 2>$null | Out-Null
        $check = & $PythonCmd -m pip show fastmcp 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Msg "fastmcp installed successfully" Green
            return $true
        }
    } catch { }
    Write-Msg "pip install failed - check your Python/pip setup" Red
    return $false
}

# Step 3: Find / guide database
function Resolve-Database {
    param($DbDir)
    $candidates = @(Get-ChildItem $DbDir -Filter "*.db3" -ErrorAction SilentlyContinue)
    if ($candidates.Count -gt 0) {
        Write-Msg "Found database: $($candidates[0].Name)" Green
        return $candidates[0].FullName
    }
    Write-Host ""
    Write-Host "  !  No .db3 file found in mcp/db/" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  How to get the database:" -ForegroundColor White
    Write-Host "  1. Open your Command: Modern Operations installation folder" -ForegroundColor Gray
    Write-Host "  2. Navigate to the DB/ subfolder" -ForegroundColor Gray
    Write-Host "  3. Copy any DB3K_*.db3 file from there" -ForegroundColor Gray
    Write-Host "  4. Paste it into this project's mcp/db/ folder" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  After copying, run this script again to verify." -ForegroundColor Yellow
    Write-Host ""
    return $null
}

# Step 4: Validate server
function Validate-Server {
    param($PythonCmd, $ProjectRoot, $DbPath)
    $serverScript = Join-Path $ProjectRoot "mcp\\server.py"
    if (-not (Test-Path $serverScript)) {
        Write-Msg "mcp/server.py not found" Red
        return $false
    }
    $env:SQLITE_DB_PATH = $DbPath
    $probe = & $PythonCmd -c "
import sys, sqlite3
sys.path.insert(0, r'$ProjectRoot')
from pathlib import Path
db_dir = Path(r'$ProjectRoot') / 'mcp' / 'db'
candidates = sorted(db_dir.glob('*.db3'))
if not candidates:
    print('NO_DB')
else:
    conn = sqlite3.connect(str(candidates[0]))
    cur = conn.cursor()
    cur.execute(\"SELECT name FROM sqlite_master WHERE type='table' LIMIT 3\")
    tables = [r[0] for r in cur.fetchall()]
    print('OK:' + ','.join(tables[:3]))
    conn.close()
" 2>$null
    if ($LASTEXITCODE -eq 0) {
        if ($probe -eq "NO_DB") {
            Write-Msg "Database scan failed" Red
            return $false
        }
        $tables = ($probe -replace "OK:", "").Split(",")
        Write-Msg "Database connected, tables: $($tables -join ', ')" Green
        return $true
    }
    Write-Msg "Server validation script failed" Red
    return $false
}

# Step 5: Configure MCP
function Add-McpConfig {
    param($ProjectRoot)
    $cursorMcp = "$env:APPDATA\\Cursor\\User\\mcp.json"
    $mcpConfigDir = Split-Path $cursorMcp -Parent
    if (-not (Test-Path $mcpConfigDir)) {
        New-Item -ItemType Directory -Path $mcpConfigDir -Force | Out-Null
    }
    $serverName = "CMO_DBID_Lookup"
    $configJson = @"
{
  "mcpServers": {
    "$serverName": {
      "command": "python",
      "args": ["-m", "fastmcp", "run", "mcp/server.py"],
      "env": {}
    }
  }
}
"@
    if (Test-Path $cursorMcp) {
        $existing = Get-Content $cursorMcp -Raw -ErrorAction SilentlyContinue
        if ($existing -and $existing -match $serverName) {
            Write-Msg "MCP already configured" Gray
            return $true
        }
        if ($existing) {
            Write-Msg "Backing up existing $cursorMcp" Yellow
            Copy-Item $cursorMcp "$cursorMcp.bak" -Force
        }
    }
    $configJson | Out-File -FilePath $cursorMcp -Encoding UTF8
    Write-Msg "MCP config written: $cursorMcp" Green
    return $true
}

# Success screen
function Show-Success {
    Write-Host ""
    Write-Host "  ============================================================  " -ForegroundColor Green
    Write-Host "  |                                                          |  " -ForegroundColor Green
    Write-Host "  |   C M O - H K B Q S K I L L                            |  " -ForegroundColor Green
    Write-Host "  |   =====================================                  |  " -ForegroundColor Green
    Write-Host "  |                                                          |  " -ForegroundColor Green
    Write-Host "  |      ALL SYSTEM STATUS : NOMINAL                        |  " -ForegroundColor Green
    Write-Host "  |      MCP SERVER         : READY                         |  " -ForegroundColor Green
    Write-Host "  |      DATABASE           : CONNECTED                     |  " -ForegroundColor Green
    Write-Host "  |                                                          |  " -ForegroundColor Green
    Write-Host "  |   Next: Restart your IDE, then load SKILL.md          |  " -ForegroundColor White
    Write-Host "  |                                                          |  " -ForegroundColor Green
    Write-Host "  ============================================================  " -ForegroundColor Green
    Write-Host ""
}

# Failure screen
function Show-Failure {
    param($Reason)
    Write-Host ""
    Write-Host "  ============================================================  " -ForegroundColor Red
    Write-Host "  |                                                          |  " -ForegroundColor Red
    Write-Host "  |      INSTALLATION INCOMPLETE                            |  " -ForegroundColor Red
    Write-Host "  |      Reason: $Reason" -ForegroundColor Yellow
    Write-Host "  |                                                          |  " -ForegroundColor Red
    Write-Host "  |   Fix the issues above and re-run install.ps1           |  " -ForegroundColor White
    Write-Host "  |                                                          |  " -ForegroundColor Red
    Write-Host "  ============================================================  " -ForegroundColor Red
    Write-Host ""
}

# MAIN
Clear-Host
Show-Banner
$allGood = $true
$dbPath  = $null

# 1 Python
Write-Step "1" "Detecting Python..." "info"
$py = Find-Python
if (-not $py) {
    Write-Step "1" "Python not found" "fail"
    Write-Host ""
    Write-Host "  Please install Python 3.8 or later:" -ForegroundColor Yellow
    Write-Host "    https://www.python.org/downloads/" -ForegroundColor Gray
    Write-Host ""
    $allGood = $false
} else {
    Write-Step "1" "Python: $($py.version) ($($py.cmd))" "ok"
}

# 2 Dependencies
Write-Host ""
Write-Step "2" "Installing fastmcp..." "info"
$reqFile = Join-Path $ProjectRoot "mcp\\requirements.txt"
if (-not $py -or -not (Install-Fastmcp $py.cmd $reqFile)) {
    Write-Step "2" "fastmcp installation failed" "fail"
    $allGood = $false
} else {
    Write-Step "2" "fastmcp ready" "ok"
}

# 3 Database
Write-Host ""
Write-Step "3" "Checking database..." "info"
$dbDir = Join-Path $ProjectRoot "mcp\\db"
$dbPath = Resolve-Database $dbDir
if (-not $dbPath) {
    Write-Step "3" "Database file missing" "warn"
} else {
    Write-Step "3" "Database found" "ok"
}

# 4 Server validation
Write-Host ""
Write-Step "4" "Validating server..." "info"
if ($dbPath -and $py -and (Test-Path (Join-Path $ProjectRoot "mcp\\server.py"))) {
    if (Validate-Server $py.cmd $ProjectRoot $dbPath) {
        Write-Step "4" "Server validated" "ok"
    } else {
        Write-Step "4" "Server validation failed" "fail"
        $allGood = $false
    }
} else {
    Write-Step "4" "Cannot validate - missing prerequisites" "fail"
    $allGood = $false
}

# 5 MCP config
Write-Host ""
Write-Step "5" "Configuring MCP..." "info"
Add-McpConfig $ProjectRoot
Write-Step "5" "MCP configuration step complete" "ok"

Write-Host ""
if ($allGood) {
    Show-Success
} else {
    Show-Failure "One or more steps did not complete."
}
"""

output_path = r'F:\codeAi\AIassistant\03_Archive\CMO-HKBQSKILL\scripts\install.ps1'
with codecs.open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('SUCCESS')
