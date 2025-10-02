#!/usr/bin/env python
"""
Script simple pour créer les concours ESATIC
Exécuter avec: python manage.py shell -c "exec(open('create_concours.py').read())"
"""

from inscriptions.models import Concours
from datetime import date, timedelta

def create_concours():
    print("🎯 Création des concours ESATIC...")
    
    # Liste des concours à créer
    concours_list = [
        {
            'nom': 'Concours d\'entrée en 1ère année - Cycle Ingénieur',
            'niveau_requis': 'BAC',
            'description': 'Formation d\'ingénieur en télécommunications et réseaux. Programme de 5 ans pour former des ingénieurs capables de concevoir, déployer et maintenir des infrastructures de télécommunications modernes.',
            'frais_inscription': 25000,
            'date_limite': date.today() + timedelta(days=30),
            'actif': True
        },
        {
            'nom': 'Concours Bachelier en Informatique et Télécommunications',
            'niveau_requis': 'BACHELIER',
            'description': 'Formation de niveau bachelier spécialisée en informatique et télécommunications. Programme de 3 ans orienté vers les technologies de l\'information et de la communication.',
            'frais_inscription': 20000,
            'date_limite': date.today() + timedelta(days=40),
            'actif': True
        },
        {
            'nom': 'Concours d\'entrée en 3ème année - Cycle Ingénieur',
            'niveau_requis': 'BAC+2',
            'description': 'Admission directe en 3ème année du cycle ingénieur pour les titulaires d\'un BTS, DUT ou équivalent en électronique, informatique ou télécommunications.',
            'frais_inscription': 30000,
            'date_limite': date.today() + timedelta(days=25),
            'actif': True
        },
        {
            'nom': 'Concours Analyste Statisticien - Niveau Bac+2',
            'niveau_requis': 'BAC+2',
            'description': 'Formation spécialisée en analyse statistique et traitement de données pour les secteurs public et privé. Programme axé sur les méthodes quantitatives et l\'analyse de données.',
            'frais_inscription': 20000,
            'date_limite': date.today() + timedelta(days=35),
            'actif': True
        },
        {
            'nom': 'Master en Data Science et Intelligence Artificielle',
            'niveau_requis': 'BAC+3',
            'description': 'Formation avancée en science des données, machine learning et intelligence artificielle. Programme orienté vers la recherche et l\'innovation technologique.',
            'frais_inscription': 35000,
            'date_limite': date.today() + timedelta(days=20),
            'actif': True
        },
        {
            'nom': 'Master en Cybersécurité et Réseaux',
            'niveau_requis': 'BAC+3',
            'description': 'Spécialisation en sécurité informatique, audit de sécurité, gestion des risques cyber et protection des infrastructures numériques.',
            'frais_inscription': 35000,
            'date_limite': date.today() + timedelta(days=15),
            'actif': True
        }
    ]
    
    created_count = 0
    existing_count = 0
    
    for concours_data in concours_list:
        concours, created = Concours.objects.get_or_create(
            nom=concours_data['nom'],
            defaults=concours_data
        )
        
        if created:
            print(f"✅ Créé: {concours.nom}")
            created_count += 1
        else:
            print(f"ℹ️  Existe déjà: {concours.nom}")
            existing_count += 1
    
    print(f"\n📊 Résumé:")
    print(f"   - Concours créés: {created_count}")
    print(f"   - Concours existants: {existing_count}")
    print(f"   - Total: {Concours.objects.count()}")
    
    print(f"\n🎉 Concours disponibles maintenant:")
    for concours in Concours.objects.filter(actif=True):
        print(f"   - {concours.nom} ({concours.get_niveau_requis_display()})")
    
    return created_count

# Exécuter la création
if __name__ == '__main__':
    create_concours()