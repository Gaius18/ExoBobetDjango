@echo off
echo ========================================
echo    CORRECTION MYSQL IMMEDIATE
echo ========================================

REM Vérifier que MySQL fonctionne
echo Test de MySQL...
mysql --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ MySQL non détecté. Installez MySQL Server
    pause
    exit /b 1
)

REM Environnement virtuel
if not exist "venv" (
    echo Création environnement virtuel...
    python -m venv venv
)

echo Activation environnement virtuel...
call venv\Scripts\activate.bat

REM Installation des dépendances
echo Installation Django et PyMySQL...
pip install django pillow PyMySQL --quiet

REM Demander le mot de passe MySQL
set /p mysql_password="Mot de passe MySQL (ou Entrée si vide): "

REM Créer la base de données
echo Création de la base de données...
echo CREATE DATABASE IF NOT EXISTS esatic_inscriptions CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; > temp_create_db.sql

if "%mysql_password%"=="" (
    mysql -u root < temp_create_db.sql
) else (
    mysql -u root -p%mysql_password% < temp_create_db.sql
)

if %ERRORLEVEL% NEQ 0 (
    echo ❌ Erreur création base de données
    echo Vérifiez votre mot de passe MySQL
    del temp_create_db.sql
    pause
    exit /b 1
)

echo ✅ Base de données créée

REM Mettre à jour le mot de passe dans settings.py
if not "%mysql_password%"=="" (
    echo Mise à jour du mot de passe...
    powershell -Command "(Get-Content 'GestionTaches\settings.py') -replace \"'PASSWORD': '',\", \"'PASSWORD': '%mysql_password%',\" | Set-Content 'GestionTaches\settings.py'"
)

REM Migrations
echo Migrations...
python manage.py makemigrations --verbosity=0
python manage.py migrate --verbosity=0

REM Créer les concours
echo Création des concours...
python fix_mysql_pymysql.py

REM Nettoyer
del temp_create_db.sql >nul 2>&1

echo.
echo ========================================
echo         CORRECTION TERMINEE !
echo ========================================
echo.
echo ✅ MySQL configuré
echo ✅ Base de données créée  
echo ✅ Concours ajoutés
echo.
echo MAINTENANT:
echo python manage.py runserver
echo.
echo Puis: http://127.0.0.1:8000
echo.

REM Proposer de démarrer automatiquement
set /p start_server="Démarrer le serveur maintenant? (o/n): "
if /i "%start_server%"=="o" (
    echo Démarrage du serveur...
    python manage.py runserver
)

pause