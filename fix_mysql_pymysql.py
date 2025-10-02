"""
Script pour configurer MySQL avec PyMySQL comme alternative à mysqlclient
"""
import os
import sys

# Installer PyMySQL si mysqlclient ne fonctionne pas
try:
    import pymysql
    pymysql.install_as_MySQLdb()
    print("✅ PyMySQL configuré comme MySQLdb")
except ImportError:
    print("❌ PyMySQL non installé. Installation...")
    os.system("pip install PyMySQL")
    import pymysql
    pymysql.install_as_MySQLdb()

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestionTaches.settings')

import django
django.setup()

from inscriptions.models import Concours
from datetime import date, timedelta

print("🎯 Création des concours avec MySQL...")

# Vérifier la connexion
from django.db import connection
try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
    print("✅ Connexion MySQL OK")
except Exception as e:
    print(f"❌ Erreur connexion MySQL: {e}")
    print("Vérifiez:")
    print("1. MySQL est démarré")
    print("2. Base de données 'esatic_inscriptions' existe")
    print("3. Mot de passe dans settings.py")
    sys.exit(1)

# Créer les concours
concours_data = [
    {
        'nom': 'Concours d\'entrée en 1ère année - Cycle Ingénieur',
        'niveau_requis': 'BAC',
        'description': 'Formation d\'ingénieur en télécommunications et réseaux. Programme de 5 ans.',
        'frais_inscription': 25000.00,
        'date_limite': date.today() + timedelta(days=30),
        'actif': True
    },
    {
        'nom': 'Concours Bachelier en Informatique et Télécommunications',
        'niveau_requis': 'BACHELIER',
        'description': 'Formation de niveau bachelier spécialisée en informatique et télécommunications.',
        'frais_inscription': 20000.00,
        'date_limite': date.today() + timedelta(days=40),
        'actif': True
    },
    {
        'nom': 'Concours d\'entrée en 3ème année - Cycle Ingénieur',
        'niveau_requis': 'BAC+2',
        'description': 'Admission directe en 3ème année du cycle ingénieur.',
        'frais_inscription': 30000.00,
        'date_limite': date.today() + timedelta(days=25),
        'actif': True
    },
    {
        'nom': 'Concours Analyste Statisticien',
        'niveau_requis': 'BAC+2',
        'description': 'Formation spécialisée en analyse statistique et traitement de données.',
        'frais_inscription': 20000.00,
        'date_limite': date.today() + timedelta(days=35),
        'actif': True
    },
    {
        'nom': 'Master en Data Science et Intelligence Artificielle',
        'niveau_requis': 'BAC+3',
        'description': 'Formation avancée en science des données et IA.',
        'frais_inscription': 35000.00,
        'date_limite': date.today() + timedelta(days=20),
        'actif': True
    },
    {
        'nom': 'Master en Cybersécurité et Réseaux',
        'niveau_requis': 'BAC+3',
        'description': 'Spécialisation en sécurité informatique et réseaux.',
        'frais_inscription': 35000.00,
        'date_limite': date.today() + timedelta(days=15),
        'actif': True
    }
]

# Supprimer les anciens concours
Concours.objects.all().delete()
print("🗑️  Anciens concours supprimés")

# Créer les nouveaux concours
created_count = 0
for data in concours_data:
    concours = Concours.objects.create(**data)
    print(f"✅ Créé: {concours.nom} ({concours.get_niveau_requis_display()})")
    created_count += 1

print(f"\n📊 Résumé:")
print(f"   - Concours créés: {created_count}")
print(f"   - Total en base: {Concours.objects.count()}")

print(f"\n🎉 Concours disponibles:")
for concours in Concours.objects.filter(actif=True):
    print(f"   - {concours.nom}")
    print(f"     Niveau: {concours.get_niveau_requis_display()}")
    print(f"     Frais: {concours.frais_inscription} FCFA")
    print(f"     Date limite: {concours.date_limite}")
    print()

print("✅ Configuration MySQL terminée!")
print("\nMaintenant vous pouvez:")
print("1. python manage.py runserver")
print("2. Aller sur http://127.0.0.1:8000")
print("3. Faire une inscription (les concours sont disponibles!)")