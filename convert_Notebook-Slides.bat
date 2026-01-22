@echo off
setlocal EnableExtensions EnableDelayedExpansion

REM Check argument
if "%~1"=="" (
    echo ERROR: No notebook path provided.
    exit /b 1
)

REM Resolve notebook path
set "NB_PATH=%~1"
set "NB_DIR=%~dp1"
set "NB_NAME=%~n1"

echo Notebook path: "%NB_PATH%"
echo Notebook dir : "%NB_DIR%"
echo Notebook name: "%NB_NAME%"
echo.

REM Change to notebook directory
cd /d "%NB_DIR%"

set "PY=%USERPROFILE%\.conda\envs\CEE6501-dev\python.exe"
if not exist "%PY%" (
    echo ERROR: Could not find env python: "%PY%"
    exit /b 1
)

@REM "%PY%" -m jupyter nbconvert --to slides "%NB_NAME%.ipynb" --post serve
"%PY%" -m jupyter nbconvert --to slides "%NB_NAME%.ipynb"
@REM "%PY%" -m jupyter nbconvert "%NB_NAME%.ipynb" --to slides ^
@REM   --TagRemovePreprocessor.enabled=True ^
@REM   --TagRemovePreprocessor.remove_input_tags="hide-input"
@REM   --TagRemovePreprocessor.remove_cell_tags="remove-cell"

endlocal
