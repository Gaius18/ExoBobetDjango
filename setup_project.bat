@echo off
echo Installation et configuration du projet ESATIC...

REM Créer l'environnement virtuel s'il n'existe pas
if not exist "venv" (
    echo Création de l'environnement virtuel...
    python -m venv venv
)

REM Activer l'environnement virtuel
echo Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

REM Installer les dépendances
echo Installation des dépendances (Django, Pillow, MySQL)...
pip install django pillow mysqlclient

REM Vérifier la connexion MySQL et créer la base si nécessaire
echo Vérification de MySQL...
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS esatic_inscriptions CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

REM Créer les migrations
echo Création des migrations...
python manage.py makemigrations

REM Appliquer les migrations
echo Application des migrations...
python manage.py migrate

REM Créer un superutilisateur (optionnel)
echo.
echo Pour créer un compte administrateur, exécutez:
echo python manage.py createsuperuser

REM Créer quelques données de test
echo Création de données de test...
python manage.py shell -c "
from inscriptions.models import Concours
from datetime import date, timedelta

# Créer des concours de test
concours_data = [
    {
        'nom': 'Concours d\'entrée en 1ère année - Cycle Ingénieur',
        'niveau_requis': 'BAC',
        'description': 'Formation d\'ingénieur en télécommunications et réseaux',
        'frais_inscription': 25000,
        'date_limite': date.today() + timedelta(days=30)
    },
    {
        'nom': 'Concours d\'entrée en 3ème année - Cycle Ingénieur',
        'niveau_requis': 'BAC+2',
        'description': 'Admission directe en 3ème année du cycle ingénieur',
        'frais_inscription': 30000,
        'date_limite': date.today() + timedelta(days=25)
    },
    {
        'nom': 'Master en Data Science et Intelligence Artificielle',
        'niveau_requis': 'BAC+3',
        'description': 'Formation avancée en science des données',
        'frais_inscription': 35000,
        'date_limite': date.today() + timedelta(days=20)
    }
]

for data in concours_data:
    concours, created = Concours.objects.get_or_create(
        nom=data['nom'],
        defaults=data
    )
    if created:
        print(f'Concours créé: {concours.nom}')
    else:
        print(f'Concours existe déjà: {concours.nom}')
"

echo.
echo Configuration terminée !
echo.
echo Pour démarrer le serveur:
echo python manage.py runserver
echo.
echo Puis ouvrez http://127.0.0.1:8000 dans votre navigateur
pause