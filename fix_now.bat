@echo off
echo ========================================
echo    CORRECTION IMMEDIATE - ESATIC
echo ========================================

REM Étape 1: Environnement virtuel
if not exist "venv" (
    echo 1/5 Création environnement virtuel...
    python -m venv venv
) else (
    echo 1/5 Environnement virtuel existe
)

REM Étape 2: Activation
echo 2/5 Activation environnement...
call venv\Scripts\activate.bat

REM Étape 3: Installation Django
echo 3/5 Installation Django...
pip install django pillow --quiet

REM Étape 4: Migrations
echo 4/5 Migrations base de données...
python manage.py makemigrations --verbosity=0
python manage.py migrate --verbosity=0

REM Étape 5: Création des concours
echo 5/5 Création des concours...
python insert_concours_direct.py

echo.
echo ========================================
echo           CORRECTION TERMINEE
echo ========================================
echo.
echo Maintenant vous pouvez:
echo 1. Démarrer le serveur: python manage.py runserver
echo 2. Aller sur http://127.0.0.1:8000
echo 3. Faire une inscription (les concours sont là!)
echo.
echo Appuyez sur une touche pour démarrer le serveur...
pause > nul

echo Démarrage du serveur...
python manage.py runserver