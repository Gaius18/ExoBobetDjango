@echo off
echo Déploiement de la plateforme ESATIC...

REM Activer l'environnement virtuel
call venv\Scripts\activate.bat

REM Installer/mettre à jour les dépendances
echo Installation des dépendances...
pip install -r requirements.txt

REM Créer et appliquer les migrations
echo Mise à jour de la base de données...
python manage.py makemigrations
python manage.py migrate

REM Collecter les fichiers statiques (pour la production)
echo Collecte des fichiers statiques...
python manage.py collectstatic --noinput

REM Créer des données de test si nécessaire
echo Création des données de test...
python create_test_data.py

echo.
echo ✅ Déploiement terminé !
echo.
echo Pour démarrer le serveur:
echo python manage.py runserver
echo.
pause