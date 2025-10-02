@echo off
echo === Installation rapide ESATIC ===

REM Créer l'environnement virtuel
if not exist "venv" (
    echo Création de l'environnement virtuel...
    python -m venv venv
)

REM Activer l'environnement virtuel
echo Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

REM Installer Django et dépendances
echo Installation de Django...
pip install django pillow

REM Note: mysqlclient nécessite des outils de compilation
echo.
echo IMPORTANT: Pour MySQL, vous devez installer mysqlclient séparément:
echo pip install mysqlclient
echo.
echo Si l'installation échoue, utilisez SQLite temporairement.
echo.

REM Demander si on veut utiliser SQLite pour les tests
set /p use_sqlite="Utiliser SQLite pour les tests? (o/n): "

if /i "%use_sqlite%"=="o" (
    echo Configuration SQLite...
    
    REM Créer un settings temporaire pour SQLite
    echo # Configuration temporaire SQLite > temp_settings.py
    echo from GestionTaches.settings import * >> temp_settings.py
    echo. >> temp_settings.py
    echo DATABASES = { >> temp_settings.py
    echo     'default': { >> temp_settings.py
    echo         'ENGINE': 'django.db.backends.sqlite3', >> temp_settings.py
    echo         'NAME': BASE_DIR / 'db.sqlite3', >> temp_settings.py
    echo     } >> temp_settings.py
    echo } >> temp_settings.py
    
    REM Utiliser SQLite temporairement
    set DJANGO_SETTINGS_MODULE=temp_settings
)

REM Créer les migrations
echo Création des migrations...
python manage.py makemigrations

REM Appliquer les migrations
echo Application des migrations...
python manage.py migrate

REM Créer les concours
echo Création des concours...
python manage.py shell -c "exec(open('create_concours.py').read())"

echo.
echo ✅ Installation terminée !
echo.
echo Pour créer un admin:
echo python manage.py createsuperuser
echo.
echo Pour démarrer:
echo python manage.py runserver
echo.
pause