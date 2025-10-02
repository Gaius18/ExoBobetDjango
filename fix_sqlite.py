import os
import sys
from pathlib import Path

# Configuration pour utiliser SQLite temporairement
BASE_DIR = Path(__file__).resolve().parent

# Créer un fichier settings temporaire
settings_content = f'''
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = 'django-insecure-temp-key-for-testing'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inscriptions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'GestionTaches.urls'

TEMPLATES = [
    {{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {{
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        }},
    }},
]

WSGI_APPLICATION = 'GestionTaches.wsgi.application'

# Base de données SQLite
DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_temp.sqlite3',
    }}
}}

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Abidjan'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
'''

# Écrire le fichier settings temporaire
with open('temp_settings.py', 'w', encoding='utf-8') as f:
    f.write(settings_content)

print("✅ Configuration SQLite temporaire créée")

# Maintenant configurer Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'temp_settings')

import django
django.setup()

from inscriptions.models import Concours
from datetime import date, timedelta

print("🎯 Création des concours avec SQLite...")

# Créer les concours
concours_data = [
    {
        'nom': 'Concours Ingénieur 1ère année',
        'niveau_requis': 'BAC',
        'description': 'Formation ingénieur télécoms et réseaux',
        'frais_inscription': 25000.00,
        'date_limite': date.today() + timedelta(days=30),
        'actif': True
    },
    {
        'nom': 'Concours Bachelier Informatique',
        'niveau_requis': 'BACHELIER',
        'description': 'Formation bachelier informatique',
        'frais_inscription': 20000.00,
        'date_limite': date.today() + timedelta(days=40),
        'actif': True
    },
    {
        'nom': 'Concours Ingénieur 3ème année',
        'niveau_requis': 'BAC+2',
        'description': 'Admission directe 3ème année',
        'frais_inscription': 30000.00,
        'date_limite': date.today() + timedelta(days=25),
        'actif': True
    },
    {
        'nom': 'Master Data Science',
        'niveau_requis': 'BAC+3',
        'description': 'Master en science des données',
        'frais_inscription': 35000.00,
        'date_limite': date.today() + timedelta(days=20),
        'actif': True
    }
]

for data in concours_data:
    concours, created = Concours.objects.get_or_create(
        nom=data['nom'],
        defaults=data
    )
    if created:
        print(f"✅ Créé: {concours.nom}")
    else:
        print(f"ℹ️  Existe: {concours.nom}")

print(f"\n📊 Total concours: {Concours.objects.count()}")
print("\n🎉 Concours disponibles:")
for concours in Concours.objects.all():
    print(f"   - {concours.nom} ({concours.get_niveau_requis_display()})")

print("\n✅ Configuration SQLite prête!")
print("\nPour utiliser cette configuration:")
print("1. set DJANGO_SETTINGS_MODULE=temp_settings")
print("2. python manage.py runserver")
print("3. Aller sur http://127.0.0.1:8000")