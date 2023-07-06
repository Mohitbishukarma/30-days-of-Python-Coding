@echo off
set "x=%~dp0"
set "pyfile=password_manager.py"

python.exe "%x%\%pyfile%" %*

pause