@echo off
echo ========================================
echo    SOLUTION SQLITE IMMEDIATE
echo ========================================

REM Créer l'environnement virtuel
if not exist "venv" (
    echo Création environnement virtuel...
    python -m venv venv
)

REM Activer l'environnement
call venv\Scripts\activate.bat

REM Installer Django
echo Installation Django...
pip install django pillow --quiet

REM Configurer SQLite et créer les concours
echo Configuration SQLite et création des concours...
python fix_sqlite.py

REM Faire les migrations avec SQLite
echo Migrations...
set DJANGO_SETTINGS_MODULE=temp_settings
python manage.py makemigrations --verbosity=0
python manage.py migrate --verbosity=0

echo.
echo ========================================
echo        SOLUTION PRETE !
echo ========================================
echo.
echo Les concours sont maintenant disponibles !
echo.
echo Pour démarrer:
echo set DJANGO_SETTINGS_MODULE=temp_settings
echo python manage.py runserver
echo.
echo Puis aller sur: http://127.0.0.1:8000
echo.

REM Démarrer automatiquement
set DJANGO_SETTINGS_MODULE=temp_settings
echo Démarrage automatique du serveur...
python manage.py runserver