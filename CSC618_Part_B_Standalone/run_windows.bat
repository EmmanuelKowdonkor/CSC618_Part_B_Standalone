@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py part_b.py
) else (
  python part_b.py
)
if errorlevel 1 (echo ERROR: Run failed.& pause & exit /b 1)
echo.
echo SUCCESS: Open the results folder for CSV and JSON output.
pause
