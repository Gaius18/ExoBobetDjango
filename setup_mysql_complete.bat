@echo off
echo ========================================
echo    CONFIGURATION MYSQL COMPLETE
echo ========================================

REM Étape 1: Vérifier MySQL
echo 1/7 Vérification de MySQL...
mysql --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ MySQL n'est pas installé ou pas dans le PATH
    echo Installez MySQL et ajoutez-le au PATH
    pause
    exit /b 1
)
echo ✅ MySQL détecté

REM Étape 2: Environnement virtuel
echo 2/7 Configuration environnement virtuel...
if not exist "venv" (
    python -m venv venv
)
call venv\Scripts\activate.bat

REM Étape 3: Installation des dépendances
echo 3/7 Installation des dépendances...
pip install django pillow

REM Étape 4: Installation mysqlclient
echo 4/7 Installation du connecteur MySQL...
pip install mysqlclient
if %ERRORLEVEL% NEQ 0 (
    echo ⚠️  Erreur avec mysqlclient, essai avec une alternative...
    pip install PyMySQL
    echo import pymysql > pymysql_setup.py
    echo pymysql.install_as_MySQLdb() >> pymysql_setup.py
)

REM Étape 5: Configuration de la base de données
echo 5/7 Configuration de la base de données...
set /p mysql_password="Entrez le mot de passe MySQL (ou appuyez sur Entrée si vide): "

REM Créer la base de données
echo CREATE DATABASE IF NOT EXISTS esatic_inscriptions CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; > create_db.sql
mysql -u root -p%mysql_password% < create_db.sql
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Erreur lors de la création de la base de données
    echo Vérifiez votre mot de passe MySQL
    pause
    exit /b 1
)
echo ✅ Base de données créée

REM Étape 6: Mettre à jour le mot de passe dans settings.py
echo 6/7 Mise à jour de la configuration...
powershell -Command "(Get-Content 'GestionTaches\settings.py') -replace \"'PASSWORD': '',\", \"'PASSWORD': '%mysql_password%',\" | Set-Content 'GestionTaches\settings.py'"

REM Étape 7: Migrations et création des concours
echo 7/7 Migrations et création des concours...
python manage.py makemigrations
python manage.py migrate

REM Créer les concours directement
python -c "
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestionTaches.settings')
django.setup()
from inscriptions.models import Concours
from datetime import date, timedelta

concours_data = [
    {'nom': 'Concours Ingénieur 1ère année', 'niveau_requis': 'BAC', 'description': 'Formation ingénieur télécoms', 'frais_inscription': 25000, 'date_limite': date.today() + timedelta(days=30), 'actif': True},
    {'nom': 'Concours Bachelier Informatique', 'niveau_requis': 'BACHELIER', 'description': 'Formation bachelier informatique', 'frais_inscription': 20000, 'date_limite': date.today() + timedelta(days=40), 'actif': True},
    {'nom': 'Concours Ingénieur 3ème année', 'niveau_requis': 'BAC+2', 'description': 'Admission directe 3ème année', 'frais_inscription': 30000, 'date_limite': date.today() + timedelta(days=25), 'actif': True},
    {'nom': 'Master Data Science', 'niveau_requis': 'BAC+3', 'description': 'Master en science des données', 'frais_inscription': 35000, 'date_limite': date.today() + timedelta(days=20), 'actif': True}
]

for data in concours_data:
    concours, created = Concours.objects.get_or_create(nom=data['nom'], defaults=data)
    print(f'✅ {concours.nom}' if created else f'ℹ️  {concours.nom} existe')

print(f'📊 Total concours: {Concours.objects.count()}')
"

REM Nettoyer les fichiers temporaires
del create_db.sql >nul 2>&1
del pymysql_setup.py >nul 2>&1

echo.
echo ========================================
echo        CONFIGURATION TERMINEE !
echo ========================================
echo.
echo ✅ MySQL configuré
echo ✅ Base de données créée
echo ✅ Concours ajoutés
echo.
echo Pour démarrer:
echo python manage.py runserver
echo.
echo Puis aller sur: http://127.0.0.1:8000
echo.
pause