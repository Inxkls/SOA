@echo off
cd /d "c:\Users\PC PRIDE WHITE WOLF\OneDrive\Escritorio\calificaciones"
call .\venv_soap\Scripts\activate.bat
python inscripciones_soap/server_simple.py
pause
