# CMO-HKBQSKILL 卸载脚本

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  CMO-HKBQSKILL 卸载程序" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 目标目录
$TargetDir = "$env:USERPROFILE\.cursor\skills\cmo-hkbq-skill"

# MCP 配置文件路径
$McpConfigPath = "$env:APPDATA\Cursor\User\mcp.json"
$BackupPath = "$env:APPDATA\Cursor\User\mcp.json.backup"

Write-Host "[1/3] 确认卸载..." -ForegroundColor Yellow
$confirm = Read-Host "确定要卸载 CMO-HKBQSKILL 吗？(y/N)"
if ($confirm -ne "y" -and $confirm -ne "Y") {
    Write-Host "取消卸载。" -ForegroundColor Gray
    exit
}

Write-Host ""
Write-Host "[2/3] 删除安装文件..." -ForegroundColor Yellow
if (Test-Path $TargetDir) {
    Remove-Item -Path $TargetDir -Recurse -Force
    Write-Host "  ✓ 已删除: $TargetDir" -ForegroundColor Green
} else {
    Write-Host "  ⚠ 未找到安装目录" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "[3/3] 恢复 MCP 配置..." -ForegroundColor Yellow
if (Test-Path $BackupPath) {
    Copy-Item -Path $BackupPath -Destination $McpConfigPath -Force
    Remove-Item -Path $BackupPath -Force
    Write-Host "  ✓ 已恢复 MCP 配置" -ForegroundColor Green
} elseif (Test-Path $McpConfigPath) {
    # 移除 cmo-dbid 配置
    Write-Host "  ⚠ 请手动编辑 $McpConfigPath 移除 cmo-dbid 配置" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  ✓ 卸载完成！" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "请重启 Cursor IDE 使更改生效。" -ForegroundColor Gray