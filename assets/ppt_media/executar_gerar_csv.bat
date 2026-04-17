@echo off
setlocal

cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
    py -3 "gerar_csv_arquivos no diretório.py"
    goto :fim
)

where python >nul 2>nul
if %errorlevel%==0 (
    python "gerar_csv_arquivos no diretório.py"
    goto :fim
)

echo Python nao foi encontrado no PATH.
echo Instale o Python ou adicione-o ao PATH e tente novamente.
pause
exit /b 1

:fim
pause