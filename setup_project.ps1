# Script PowerShell pour configurer le projet ESATIC avec MySQL
Write-Host "=== Configuration du projet ESATIC ===" -ForegroundColor Green

# Vérifier si Python est installé
try {
    $pythonVersion = python --version
    Write-Host "✅ Python détecté: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python n'est pas installé ou pas dans le PATH" -ForegroundColor Red
    exit 1
}

# Créer l'environnement virtuel
if (!(Test-Path "venv")) {
    Write-Host "Création de l'environnement virtuel..." -ForegroundColor Yellow
    python -m venv venv
}

# Activer l'environnement virtuel
Write-Host "Activation de l'environnement virtuel..." -ForegroundColor Yellow
& "venv\Scripts\Activate.ps1"

# Installer les dépendances
Write-Host "Installation des dépendances..." -ForegroundColor Yellow
pip install django pillow mysqlclient

# Vérifier MySQL
Write-Host "Vérification de MySQL..." -ForegroundColor Yellow
try {
    mysql --version
    Write-Host "✅ MySQL détecté" -ForegroundColor Green
} catch {
    Write-Host "⚠️  MySQL non détecté. Assurez-vous qu'il est installé et dans le PATH" -ForegroundColor Yellow
}

# Configuration de la base de données
$dbName = Read-Host "Nom de la base de données (défaut: esatic_inscriptions)"
if ([string]::IsNullOrEmpty($dbName)) { $dbName = "esatic_inscriptions" }

$mysqlUser = Read-Host "Utilisateur MySQL (défaut: root)"
if ([string]::IsNullOrEmpty($mysqlUser)) { $mysqlUser = "root" }

$mysqlPassword = Read-Host "Mot de passe MySQL" -AsSecureString
$mysqlPasswordPlain = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($mysqlPassword))

# Créer la base de données
Write-Host "Création de la base de données..." -ForegroundColor Yellow
$createDbCommand = "CREATE DATABASE IF NOT EXISTS $dbName CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
mysql -u $mysqlUser -p$mysqlPasswordPlain -e $createDbCommand

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Base de données créée avec succès !" -ForegroundColor Green
    
    # Mettre à jour settings.py avec le mot de passe
    $settingsPath = "GestionTaches\settings.py"
    $settingsContent = Get-Content $settingsPath -Raw
    $settingsContent = $settingsContent -replace "'PASSWORD': '',", "'PASSWORD': '$mysqlPasswordPlain',"
    $settingsContent = $settingsContent -replace "'NAME': 'esatic_inscriptions',", "'NAME': '$dbName',"
    $settingsContent = $settingsContent -replace "'USER': 'root',", "'USER': '$mysqlUser',"
    Set-Content $settingsPath $settingsContent
    
    Write-Host "✅ Configuration mise à jour dans settings.py" -ForegroundColor Green
} else {
    Write-Host "❌ Erreur lors de la création de la base de données" -ForegroundColor Red
    Write-Host "Vérifiez vos identifiants MySQL" -ForegroundColor Yellow
    exit 1
}

# Créer et appliquer les migrations
Write-Host "Création des migrations..." -ForegroundColor Yellow
python manage.py makemigrations

Write-Host "Application des migrations..." -ForegroundColor Yellow
python manage.py migrate

# Créer des données de test
Write-Host "Création des données de test..." -ForegroundColor Yellow
python create_test_data.py

Write-Host ""
Write-Host "=== Configuration terminée ! ===" -ForegroundColor Green
Write-Host ""
Write-Host "Pour créer un superutilisateur:" -ForegroundColor Cyan
Write-Host "python manage.py createsuperuser" -ForegroundColor White
Write-Host ""
Write-Host "Pour démarrer le serveur:" -ForegroundColor Cyan
Write-Host "python manage.py runserver" -ForegroundColor White
Write-Host ""
Write-Host "Accès:" -ForegroundColor Cyan
Write-Host "- Site web: http://127.0.0.1:8000" -ForegroundColor White
Write-Host "- Administration: http://127.0.0.1:8000/admin" -ForegroundColor White