@echo off
echo === Correction: Ajout des concours ===

REM Vérifier si l'environnement virtuel existe
if not exist "venv" (
    echo Création de l'environnement virtuel...
    python -m venv venv
)

REM Activer l'environnement virtuel
call venv\Scripts\activate.bat

REM Installer Django si nécessaire
pip install django pillow

REM Créer les migrations si nécessaire
python manage.py makemigrations

REM Appliquer les migrations
python manage.py migrate

REM Créer les concours avec la commande personnalisée
echo Création des concours...
python manage.py create_concours

echo.
echo ✅ Concours ajoutés ! Vous pouvez maintenant:
echo 1. Aller sur http://127.0.0.1:8000
echo 2. Voir les concours disponibles
echo 3. Faire des inscriptions
echo.
echo Pour démarrer le serveur:
echo python manage.py runserver
echo.
pause