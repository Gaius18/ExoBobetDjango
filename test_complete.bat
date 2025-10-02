@echo off
echo ========================================
echo    TEST COMPLET ESATIC - NOUVEAU DESIGN
echo ========================================

REM Étape 1: Insérer les concours
echo 1/3 Insertion des concours...
call fix_concours_mysql.bat

REM Étape 2: Activer l'environnement
echo 2/3 Activation environnement...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo Création environnement virtuel...
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install django pillow PyMySQL --quiet
)

REM Étape 3: Démarrer le serveur
echo 3/3 Démarrage du serveur...
echo.
echo ========================================
echo    PLATEFORME ESATIC PRÊTE !
echo ========================================
echo.
echo ✅ Nouveau design professionnel
echo ✅ Logo ESATIC partout
echo ✅ Reçu d'inscription amélioré
echo ✅ 6 concours disponibles
echo.
echo Fonctionnalités:
echo - Inscription avec formulaire complet
echo - Upload de documents
echo - Reçu d'inscription imprimable
echo - Recherche par numéro
echo - Interface moderne et responsive
echo.
echo Accès: http://127.0.0.1:8000
echo Admin: http://127.0.0.1:8000/admin
echo.
echo Appuyez sur une touche pour démarrer...
pause > nul

python manage.py runserver