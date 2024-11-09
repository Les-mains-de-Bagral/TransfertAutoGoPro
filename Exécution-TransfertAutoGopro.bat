@echo off

:: Definir en utf-8 pour utilisation de caractères spéciaux
chcp 65001 > nul

:: Récupérer le répertoire dans lequel est le script .bat
set "script_dir=%~dp0"

echo on

:: Exécution du programme Python
python "PrgmTransfertAutoGoPro.py" "%script_dir%"
pause