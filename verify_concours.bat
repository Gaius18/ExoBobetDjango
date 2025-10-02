@echo off
echo ========================================
echo    VERIFICATION CONCOURS MYSQL
echo ========================================

set /p mysql_password="Mot de passe MySQL (ou Entrée si vide): "

echo Vérification des concours dans la base...

if "%mysql_password%"=="" (
    mysql -u root esatic_inscriptions < check_concours_mysql.sql
) else (
    mysql -u root -p%mysql_password% esatic_inscriptions < check_concours_mysql.sql
)

echo.
echo ========================================
echo    VERIFICATION TERMINEE
echo ========================================
pause