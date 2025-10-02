"""
Configuration temporaire avec SQLite pour les tests
"""
from GestionTaches.settings import *

# Remplacer MySQL par SQLite pour les tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

print("🔄 Utilisation de SQLite pour les tests")