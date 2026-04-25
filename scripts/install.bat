@echo off
:: Pure ASCII batch launcher - no encoding issues
:: Handles double-click by re-launching in a new console window
if not defined __INSIDE_BAT__ (
    set __INSIDE_BAT__=1
    start "CMO-HKBQSKILL Installer" cmd /k "%~f0"
    exit /b
)

:: Change to the script's directory so user can run from anywhere
cd /d "%~dp0.."

:: Run the Python installer (all output handled by Python)
python -B "%~dp0install.py" %*
