# CMO-HKBQSKILL 目录结构验证脚本

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  CMO-HKBQSKILL 目录结构验证" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 源目录（CMO-HKBQSKILL 根目录，脚本在 scripts/ 子目录）
$SourceDir = Split-Path -Parent $PSScriptRoot

# 必需目录
$RequiredDirs = @(
    "mcp",
    "mcp\db",
    "references",
    "references\lua-api",
    "references\data-types",
    "templates",
    "templates\basic",
    "templates\advanced",
    "templates\event",
    "templates\utility",
    "examples",
    "examples\official",
    "examples\contributed",
    "scripts",
    "assets",
    "outputs"
)

# 必需文件
$RequiredFiles = @(
    "SKILL.md",
    "README.md",
    "mcp\sqlite_explorer.py",
    "mcp\requirements.txt",
    "scripts\install.py",
    "scripts\config.py",
    "scripts\scan_database.py",
    "references\index.md",
    "references\lua-api\functions.md",
    "references\data-types\overview.md",
    "templates\index.md",
    "templates\basic\add-aircraft.lua",
    "templates\basic\add-ship.lua",
    "templates\basic\create-mission.lua",
    "examples\index.md"
)

$errors = 0
$warnings = 0

# 检查目录
Write-Host "[1/2] 检查目录结构..." -ForegroundColor Yellow
foreach ($dir in $RequiredDirs) {
    $fullPath = Join-Path $SourceDir $dir
    if (Test-Path $fullPath) {
        Write-Host "  ✓ $dir" -ForegroundColor Green
    } else {
        Write-Host "  ✗ 缺失: $dir" -ForegroundColor Red
        $errors++
    }
}

# 检查文件
Write-Host ""
Write-Host "[2/2] 检查核心文件..." -ForegroundColor Yellow
foreach ($file in $RequiredFiles) {
    $fullPath = Join-Path $SourceDir $file
    if (Test-Path $fullPath) {
        $size = (Get-Item $fullPath).Length
        Write-Host "  ✓ $file ($size bytes)" -ForegroundColor Green
    } else {
        Write-Host "  ✗ 缺失: $file" -ForegroundColor Red
        $errors++
    }
}

# 统计文件数量
Write-Host ""
Write-Host "[统计]" -ForegroundColor Yellow
$totalFiles = (Get-ChildItem -Path $SourceDir -Recurse -File | Measure-Object).Count
$totalDirs = (Get-ChildItem -Path $SourceDir -Recurse -Directory | Measure-Object).Count
Write-Host "  文件总数: $totalFiles" -ForegroundColor Gray
Write-Host "  目录总数: $totalDirs" -ForegroundColor Gray

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
if ($errors -eq 0) {
    Write-Host "  ✓ 目录结构完整！" -ForegroundColor Green
} else {
    Write-Host "  ✗ 发现 $errors 个错误" -ForegroundColor Red
}
Write-Host "========================================" -ForegroundColor Cyan