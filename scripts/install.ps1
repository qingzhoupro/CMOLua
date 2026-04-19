# CMO-HKBQSKILL 安装脚本

# 目标目录
$TargetDir = "$env:USERPROFILE\.cursor\skills\cmo-hkbq-skill"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  CMO-HKBQSKILL 安装程序" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 检查管理员权限
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

# 源目录（CMO-HKBQSKILL 根目录，脚本在 scripts/ 子目录）
$SourceDir = Split-Path -Parent $PSScriptRoot

Write-Host "[1/5] 创建目标目录..." -ForegroundColor Yellow
if (!(Test-Path $TargetDir)) {
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
    Write-Host "  ✓ 目录已创建: $TargetDir" -ForegroundColor Green
} else {
    Write-Host "  ✓ 目录已存在: $TargetDir" -ForegroundColor Green
}

Write-Host ""
Write-Host "[2/5] 复制文件..." -ForegroundColor Yellow
# 复制所有文件（排除 .gitkeep 和安装脚本自身）
$FilesToCopy = Get-ChildItem -Path $SourceDir -Recurse -File | Where-Object {
    $_.Name -ne "install.ps1" -and
    $_.Name -ne ".gitkeep" -and
    $_.Name -ne "README.md"
}
foreach ($file in $FilesToCopy) {
    $relativePath = $file.FullName.Replace($SourceDir, "").TrimStart("\")
    $destPath = Join-Path $TargetDir $relativePath
    $destDir = Split-Path $destPath -Parent
    
    if (!(Test-Path $destDir)) {
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    }
    
    Copy-Item -Path $file.FullName -Destination $destPath -Force
}
Write-Host "  ✓ 文件已复制" -ForegroundColor Green

Write-Host ""
Write-Host "[3/5] 创建 MCP 配置..." -ForegroundColor Yellow

# MCP 配置文件路径
$McpSettingsPath = "$env:APPDATA\Cursor\User\settings.json"
$McpConfigPath = "$env:APPDATA\Cursor\User\mcp.json"

# 确保目录存在
$McpConfigDir = Split-Path $McpConfigPath -Parent
if (!(Test-Path $McpConfigDir)) {
    New-Item -ItemType Directory -Path $McpConfigDir -Force | Out-Null
}

# MCP 配置内容
$McpConfig = @{
    mcpServers = @{
        "cmo-dbid" = @{
            command = "uv"
            args = @("run", "--directory", "$TargetDir\mcp", "server.py")
            env = @{
                SQLITE_DB_PATH = "$TargetDir\mcp\db\DB3K_514.db3"
            }
        }
    }
} | ConvertTo-Json -Depth 10

# 写入 MCP 配置
if (Test-Path $McpConfigPath) {
    Write-Host "  ⚠ MCP 配置已存在，将在备份后更新" -ForegroundColor Yellow
    Copy-Item $McpConfigPath "$McpConfigPath.backup" -Force
}
$McpConfig | Out-File -FilePath $McpConfigPath -Encoding UTF8
Write-Host "  ✓ MCP 配置已创建: $McpConfigPath" -ForegroundColor Green

Write-Host ""
Write-Host "[4/5] 数据库设置..." -ForegroundColor Yellow
$DbDir = "$TargetDir\mcp\db"
$DbFile = "$DbDir\DB3K_514.db3"

if (!(Test-Path $DbFile)) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Yellow
    Write-Host "  ⚠ 重要：请手动复制数据库文件" -ForegroundColor Yellow
    Write-Host "========================================" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "请将 CMO 数据库文件复制到以下位置：" -ForegroundColor White
    Write-Host ""
    Write-Host "  源文件示例: D:\Program Files (x86)\Steam\steamapps\common\" -ForegroundColor Gray
    Write-Host "    Command - Modern Operations\DB\DB3K_511.db3" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  目标路径: $DbFile" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "复制完成后，按任意键继续..." -ForegroundColor Yellow
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
} else {
    Write-Host "  ✓ 数据库文件已存在" -ForegroundColor Green
}

Write-Host ""
Write-Host "[5/5] 验证安装..." -ForegroundColor Yellow
$Success = $true

# 检查关键文件
$KeyFiles = @(
    "$TargetDir\SKILL.md",
    "$TargetDir\mcp\server.py",
    "$TargetDir\references\index.md",
    "$TargetDir\templates\index.md"
)

foreach ($file in $KeyFiles) {
    if (Test-Path $file) {
        Write-Host "  ✓ $(Split-Path $file -Leaf)" -ForegroundColor Green
    } else {
        Write-Host "  ✗ 缺失: $(Split-Path $file -Leaf)" -ForegroundColor Red
        $Success = $false
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
if ($Success) {
    Write-Host "  ✓ 安装完成！" -ForegroundColor Green
    Write-Host ""
    Write-Host "  下一步：" -ForegroundColor White
    Write-Host "  1. 重启 Cursor IDE" -ForegroundColor Gray
    Write-Host "  2. 在 Lua Console 中测试" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  安装路径: $TargetDir" -ForegroundColor Gray
} else {
    Write-Host "  ⚠ 安装可能不完整，请检查上述错误" -ForegroundColor Yellow
}
Write-Host "========================================" -ForegroundColor Cyan