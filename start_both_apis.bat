@echo off
chcp 65001 >nul
cls

echo ========================================
echo   INICIANDO AMBAS APIs
echo ========================================
echo.

REM Matar procesos previos
taskkill /F /IM java.exe 2>nul
taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul

REM Iniciar SOAP Server en background
echo [1/2] Iniciando SOAP API en puerto 8000...
start "SOAP API" cmd /k "cd /d "%cd%" && call venv_soap\Scripts\activate.bat && python inscripciones_soap\server_simple.py"
timeout /t 3 /nobreak >nul

REM Iniciar REST API
echo [2/2] Iniciando REST API en puerto 9090...
start "REST API" cmd /k "cd /d "%cd%" && java -jar target\calificaciones-0.0.1-SNAPSHOT.jar"

echo.
echo ========================================
echo   APIs INICIADAS
echo ========================================
echo   SOAP:  http://127.0.0.1:8000
echo   REST:  http://localhost:9090
echo ========================================
echo.
pause
