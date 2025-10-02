@echo off
echo ========================================
echo    INSERTION CONCOURS MYSQL DIRECT
echo ========================================

REM Demander le mot de passe MySQL
set /p mysql_password="Mot de passe MySQL (ou Entrée si vide): "

echo Insertion des concours dans la base esatic_inscriptions...

REM Exécuter le script SQL
if "%mysql_password%"=="" (
    mysql -u root esatic_inscriptions < insert_concours_mysql.sql
) else (
    mysql -u root -p%mysql_password% esatic_inscriptions < insert_concours_mysql.sql
)

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo         CONCOURS AJOUTES !
    echo ========================================
    echo.
    echo ✅ 6 concours ont été ajoutés à votre base MySQL
    echo.
    echo Concours disponibles:
    echo - Concours Ingénieur 1ère année (BAC)
    echo - Concours Bachelier Informatique (BACHELIER)
    echo - Concours Ingénieur 3ème année (BAC+2)
    echo - Concours Analyste Statisticien (BAC+2)
    echo - Master Data Science (BAC+3)
    echo - Master Cybersécurité (BAC+3)
    echo.
    echo MAINTENANT:
    echo 1. Activez votre environnement: venv\Scripts\activate
    echo 2. Démarrez le serveur: python manage.py runserver
    echo 3. Allez sur: http://127.0.0.1:8000
    echo.
    echo Le formulaire d'inscription aura maintenant des concours disponibles!
    echo.
) else (
    echo ❌ Erreur lors de l'insertion
    echo Vérifiez votre mot de passe MySQL
)

pause