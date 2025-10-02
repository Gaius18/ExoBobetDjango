import os
import sys
import django
from datetime import date, timedelta

# Ajouter le répertoire du projet au path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestionTaches.settings')

try:
    django.setup()
    from inscriptions.models import Concours
    
    print("🎯 Insertion directe des concours...")
    
    # Supprimer tous les concours existants pour repartir à zéro
    Concours.objects.all().delete()
    print("🗑️  Anciens concours supprimés")
    
    # Créer les nouveaux concours
    concours_data = [
        {
            'nom': 'Concours d\'entrée en 1ère année - Cycle Ingénieur',
            'niveau_requis': 'BAC',
            'description': 'Formation d\'ingénieur en télécommunications et réseaux',
            'frais_inscription': 25000.00,
            'date_limite': date.today() + timedelta(days=30),
            'actif': True
        },
        {
            'nom': 'Concours Bachelier en Informatique',
            'niveau_requis': 'BACHELIER',
            'description': 'Formation bachelier en informatique et télécommunications',
            'frais_inscription': 20000.00,
            'date_limite': date.today() + timedelta(days=40),
            'actif': True
        },
        {
            'nom': 'Concours d\'entrée en 3ème année',
            'niveau_requis': 'BAC+2',
            'description': 'Admission directe en 3ème année du cycle ingénieur',
            'frais_inscription': 30000.00,
            'date_limite': date.today() + timedelta(days=25),
            'actif': True
        },
        {
            'nom': 'Master Data Science',
            'niveau_requis': 'BAC+3',
            'description': 'Master en science des données et IA',
            'frais_inscription': 35000.00,
            'date_limite': date.today() + timedelta(days=20),
            'actif': True
        }
    ]
    
    created_concours = []
    for data in concours_data:
        concours = Concours.objects.create(**data)
        created_concours.append(concours)
        print(f"✅ Créé: {concours.nom}")
    
    print(f"\n📊 Total concours créés: {len(created_concours)}")
    print(f"📊 Total concours en base: {Concours.objects.count()}")
    
    # Vérifier que les concours sont bien là
    print("\n🎉 Concours disponibles:")
    for concours in Concours.objects.all():
        print(f"   - ID: {concours.id} | {concours.nom} ({concours.niveau_requis})")
    
    print("\n✅ Concours insérés avec succès!")
    print("Vous pouvez maintenant utiliser le formulaire d'inscription.")
    
except Exception as e:
    print(f"❌ Erreur: {e}")
    print("\nSolutions possibles:")
    print("1. Vérifiez que Django est installé: pip install django")
    print("2. Vérifiez la configuration de la base de données")
    print("3. Exécutez les migrations: python manage.py migrate")