# Plateforme d'Inscription ESATIC

## Description
Plateforme web développée avec Django pour gérer les inscriptions aux concours d'entrée de l'ESATIC (École Supérieure Africaine des TIC).

## Fonctionnalités

### ✅ Fonctionnalités implémentées
- **Inscription des candidats** : Formulaire complet avec toutes les informations requises
- **Gestion des concours** : Différents types de concours selon le niveau d'études
- **Upload de documents** : Téléchargement des pièces justificatives (PDF, JPG, PNG)
- **Numérotation automatique** : Génération automatique des numéros d'inscription
- **Reçu d'inscription** : Page de confirmation imprimable
- **Recherche d'inscription** : Retrouver une inscription par son numéro
- **Interface moderne** : Design responsive et professionnel
- **Administration** : Interface d'administration Django pour gérer les données

### 📋 Documents supportés
- Extrait de naissance
- Certificat de scolarité
- Diplôme ou relevés de notes
- Lettre de motivation
- Photo d'identité
- Autres documents

## Installation et Configuration

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)
- MySQL Server 5.7+ ou MariaDB 10.3+
- MySQL client (pour mysqlclient)

### Installation rapide

#### Option 1: Script PowerShell (recommandé)
```powershell
.\setup_project.ps1
```

#### Option 2: Script Batch
1. **Configurer MySQL** :
   ```bash
   setup_mysql.bat
   ```
2. **Installer le projet** :
   ```bash
   setup_project.bat
   ```

### Installation manuelle
1. **Créer un environnement virtuel** :
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer MySQL** :
   - Créer la base de données :
   ```sql
   CREATE DATABASE esatic_inscriptions CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
   - Mettre à jour le mot de passe MySQL dans `GestionTaches/settings.py`

4. **Créer et appliquer les migrations** :
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Créer un superutilisateur** (optionnel) :
   ```bash
   python manage.py createsuperuser
   ```

6. **Démarrer le serveur** :
   ```bash
   python manage.py runserver
   ```

7. **Accéder à l'application** :
   - Site web : http://127.0.0.1:8000
   - Administration : http://127.0.0.1:8000/admin

## Structure du Projet

```
GestionTaches/
├── inscriptions/           # Application principale
│   ├── models.py          # Modèles de données
│   ├── views.py           # Vues et logique métier
│   ├── forms.py           # Formulaires
│   ├── urls.py            # URLs de l'application
│   ├── admin.py           # Configuration admin
│   ├── templates/         # Templates HTML
│   └── static/            # Fichiers CSS, JS, images
├── GestionTaches/         # Configuration Django
├── media/                 # Fichiers uploadés
├── db.sqlite3            # Base de données
└── manage.py             # Script de gestion Django
```

## Utilisation

### Pour les candidats
1. **Accéder au site** : Ouvrir la page d'accueil
2. **Choisir un concours** : Sélectionner le concours souhaité
3. **Remplir le formulaire** : Saisir toutes les informations personnelles
4. **Télécharger les documents** : Ajouter les pièces justificatives
5. **Confirmer l'inscription** : Valider et imprimer le reçu
6. **Rechercher son inscription** : Utiliser le numéro pour retrouver son dossier

### Pour les administrateurs
1. **Accéder à l'admin** : http://127.0.0.1:8000/admin
2. **Gérer les concours** : Créer, modifier, activer/désactiver
3. **Consulter les inscriptions** : Voir tous les candidats inscrits
4. **Valider les dossiers** : Marquer les inscriptions comme validées
5. **Gérer les documents** : Consulter les pièces téléchargées

## Modèles de Données

### Concours
- Nom du concours
- Niveau requis (Bac, Bachelier, Bac+2, Bac+3, Master)
- Description
- Frais d'inscription
- Date limite
- Statut (actif/inactif)

**Niveaux disponibles :**
- **Bac** : Concours d'entrée post-baccalauréat
- **Bachelier** : Formation de niveau bachelier (3 ans)
- **Bac+2** : Admission directe en 3ème année
- **Bac+3** : Masters et formations avancées
- **Master** : Formations de niveau master

### Candidat
- Informations personnelles (nom, prénoms, date de naissance, etc.)
- Coordonnées (email, téléphone, adresse)
- Informations académiques (niveau, établissement, année)
- Concours choisi
- Numéro d'inscription (généré automatiquement)
- Statut de validation

### Document
- Type de document
- Fichier (PDF, JPG, PNG)
- Date d'upload
- Lien vers le candidat

## Sécurité et Validation

- **Validation des emails** : Vérification de l'unicité
- **Validation des fichiers** : Taille max 5MB, formats autorisés
- **Validation des dates** : Cohérence des années d'obtention
- **Protection CSRF** : Sécurisation des formulaires
- **Gestion des erreurs** : Messages d'erreur explicites

## Personnalisation

### Ajouter un nouveau type de concours
1. Modifier `NIVEAUX_CHOICES` dans `models.py`
2. Créer les migrations : `python manage.py makemigrations`
3. Appliquer : `python manage.py migrate`

### Modifier les types de documents
1. Éditer `TYPE_DOCUMENT_CHOICES` dans `models.py`
2. Créer et appliquer les migrations

### Personnaliser le design
- Modifier `inscriptions/static/inscriptions/style.css`
- Éditer les templates dans `inscriptions/templates/`

## Support et Maintenance

### Sauvegarde des données
```bash
python manage.py dumpdata > backup.json
```

### Restauration
```bash
python manage.py loaddata backup.json
```

### Logs et débogage
- Activer `DEBUG = True` dans `settings.py` pour le développement
- Consulter les logs Django pour les erreurs

## Technologies Utilisées
- **Backend** : Django 4.2+
- **Base de données** : SQLite (développement)
- **Frontend** : HTML5, CSS3, JavaScript vanilla
- **Upload de fichiers** : Pillow pour le traitement d'images

## Auteur
Développé pour l'ESATIC dans le cadre d'un exercice pratique.

---

**Note** : Cette plateforme est fonctionnelle et prête pour la production avec quelques ajustements de configuration (base de données, serveur web, etc.).