@echo off
echo Configuration MySQL pour ESATIC...

echo.
echo IMPORTANT: Assurez-vous que MySQL est installé et en cours d'exécution
echo.

REM Demander les informations de connexion MySQL
set /p mysql_user="Nom d'utilisateur MySQL (par défaut: root): "
if "%mysql_user%"=="" set mysql_user=root

set /p mysql_password="Mot de passe MySQL: "

set /p db_name="Nom de la base de données (par défaut: esatic_inscriptions): "
if "%db_name%"=="" set db_name=esatic_inscriptions

echo.
echo Création de la base de données...
mysql -u %mysql_user% -p%mysql_password% -e "CREATE DATABASE IF NOT EXISTS %db_name% CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

if %ERRORLEVEL% EQU 0 (
    echo ✅ Base de données créée avec succès !
    echo.
    echo Configuration dans settings.py:
    echo DATABASES = {
    echo     'default': {
    echo         'ENGINE': 'django.db.backends.mysql',
    echo         'NAME': '%db_name%',
    echo         'USER': '%mysql_user%',
    echo         'PASSWORD': '%mysql_password%',
    echo         'HOST': 'localhost',
    echo         'PORT': '3306',
    echo     }
    echo }
) else (
    echo ❌ Erreur lors de la création de la base de données
    echo Vérifiez vos identifiants MySQL
)

echo.
echo Maintenant, mettez à jour le mot de passe dans GestionTaches/settings.py
echo puis exécutez: setup_project.bat
pause