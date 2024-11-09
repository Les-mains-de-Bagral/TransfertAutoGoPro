@echo off

:: Definition utf-8 pour utilisation de caractères spéciaux
chcp 65001 > nul

:: Récupération du répertoire dans lequel est le script .bat
set "script_dir=%~dp0"

:: Changement de répertoire de travail pour celui dans lequel est stocké le programme python
::cd /d "G:\Programme"

echo on

:: Exécution du programme Python
python "PrgmTransfertAutoGoPro.py" "%script_dir%"
pause