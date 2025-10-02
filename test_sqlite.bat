@echo off
echo === Test rapide avec SQLite ===

REM Créer l'environnement virtuel
if not exist "venv" (
    python -m venv venv
)

REM Activer l'environnement virtuel
call venv\Scripts\activate.bat

REM Installer Django
pip install django pillow

REM Utiliser SQLite temporairement
set DJANGO_SETTINGS_MODULE=settings_sqlite

REM Créer et appliquer les migrations
python manage.py makemigrations
python manage.py migrate

REM Créer les concours
python manage.py create_concours

REM Créer un superutilisateur (optionnel)
echo.
echo Voulez-vous créer un compte administrateur? (o/n)
set /p create_admin=
if /i "%create_admin%"=="o" (
    python manage.py createsuperuser
)

echo.
echo ✅ Test SQLite prêt !
echo.
echo Pour démarrer:
echo set DJANGO_SETTINGS_MODULE=settings_sqlite
echo python manage.py runserver
echo.
echo Accès:
echo - Site: http://127.0.0.1:8000
echo - Admin: http://127.0.0.1:8000/admin
echo.
pause