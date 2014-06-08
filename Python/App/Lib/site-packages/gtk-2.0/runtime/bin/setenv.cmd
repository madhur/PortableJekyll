@echo off

goto:main

:: ------------------------------------------------------------
:: abspath "function"
::     %1: variable name
::     %2: double quoted path
::
::     Sets the value of the variable named by %1 to the
::     equivalent of os.path.abspath(os.path.dirname(%2))
:: ------------------------------------------------------------
:abspath
for %%F in (%2) do set TMP_PATH=%%~dpF
set %1=%TMP_PATH%
goto:eof

:main
call:abspath RUNTIME_BIN "%~f0"
call:abspath RUNTIME_PKGCONFIG "%RUNTIME_BIN%\..\lib\pkgconfig\"
call:abspath PYTHON_ROOT "%RUNTIME_BIN%\..\..\..\..\..\"
call:abspath PYTHON_SCRIPTS "%PYTHON_ROOT%\Scripts\"
call:abspath PYTHON_PKGCONFIG "%PYTHON_ROOT%\Lib\pkgconfig\"

if defined PATH (
    set PATH="%PYTHON_ROOT%;%PYTHON_SCRIPTS%;%RUNTIME_BIN%;%PATH%"
) else (
    set PATH="%PYTHON_ROOT%;%PYTHON_SCRIPTS%;%RUNTIME_BIN%"
)
if defined PKG_CONFIG_PATH (
    set PKG_CONFIG_PATH="%PYTHON_PKGCONFIG%;%RUNTIME_PKGCONFIG%;%PKGCONFIG_PATH%"
) else (
    set PKG_CONFIG_PATH="%PYTHON_PKGCONFIG%;%RUNTIME_PKGCONFIG%"
)

cls
