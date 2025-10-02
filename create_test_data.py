#!/usr/bin/env python
"""
Script pour créer des données de test pour la plateforme ESATIC
Exécuter avec: python manage.py shell < create_test_data.py
"""

import os
import django
from datetime import date, timedelta

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestionTaches.settings')
django.setup()

from inscriptions.models import Concours, Candidat, Document

def create_test_data():
    print("Création des données de test...")
    
    # Créer des concours
    concours_data = [
        {
            'nom': 'Concours d\'entrée en 1ère année - Cycle Ingénieur',
            'niveau_requis': 'BAC',
            'description': 'Formation d\'ingénieur en télécommunications et réseaux. Ce programme forme des ingénieurs capables de concevoir, déployer et maintenir des infrastructures de télécommunications modernes.',
            'frais_inscription': 25000,
            'date_limite': date.today() + timedelta(days=30),
            'actif': True
        },
        {
            'nom': 'Concours Bachelier en Informatique et Télécommunications',
            'niveau_requis': 'BACHELIER',
            'description': 'Formation de niveau bachelier spécialisée en informatique et télécommunications. Programme de 3 ans orienté vers les technologies de l\'information.',
            'frais_inscription': 20000,
            'date_limite': date.today() + timedelta(days=40),
            'actif': True
        },
        {
            'nom': 'Concours d\'entrée en 3ème année - Cycle Ingénieur',
            'niveau_requis': 'BAC+2',
            'description': 'Admission directe en 3ème année du cycle ingénieur pour les titulaires d\'un BTS ou DUT en électronique, informatique ou télécommunications.',
            'frais_inscription': 30000,
            'date_limite': date.today() + timedelta(days=25),
            'actif': True
        },
        {
            'nom': 'Master en Data Science et Intelligence Artificielle',
            'niveau_requis': 'BAC+3',
            'description': 'Formation avancée en science des données, machine learning et intelligence artificielle. Programme orienté vers la recherche et l\'innovation.',
            'frais_inscription': 35000,
            'date_limite': date.today() + timedelta(days=20),
            'actif': True
        },
        {
            'nom': 'Master en Cybersécurité et Réseaux',
            'niveau_requis': 'BAC+3',
            'description': 'Spécialisation en sécurité informatique, audit de sécurité et gestion des risques cyber.',
            'frais_inscription': 35000,
            'date_limite': date.today() + timedelta(days=15),
            'actif': True
        },
        {
            'nom': 'Concours Analyste Statisticien - Niveau Bac+2',
            'niveau_requis': 'BAC+2',
            'description': 'Formation spécialisée en analyse statistique et traitement de données pour les secteurs public et privé.',
            'frais_inscription': 20000,
            'date_limite': date.today() + timedelta(days=35),
            'actif': True
        }
    ]
    
    concours_created = []
    for data in concours_data:
        concours, created = Concours.objects.get_or_create(
            nom=data['nom'],
            defaults=data
        )
        if created:
            print(f'✓ Concours créé: {concours.nom}')
            concours_created.append(concours)
        else:
            print(f'- Concours existe déjà: {concours.nom}')
            concours_created.append(concours)
    
    # Créer quelques candidats de test
    candidats_data = [
        {
            'nom': 'KOUAME',
            'prenoms': 'Jean Baptiste',
            'date_naissance': date(2000, 5, 15),
            'lieu_naissance': 'Abidjan',
            'sexe': 'M',
            'nationalite': 'Ivoirienne',
            'email': 'jean.kouame@example.com',
            'telephone': '+225 07 12 34 56 78',
            'adresse': 'Cocody, Riviera 2, Abidjan',
            'niveau_etudes': 'Bac Série C',
            'etablissement_origine': 'Lycée Moderne de Cocody',
            'annee_obtention': 2023,
        },
        {
            'nom': 'TRAORE',
            'prenoms': 'Aminata',
            'date_naissance': date(1999, 8, 22),
            'lieu_naissance': 'Bouaké',
            'sexe': 'F',
            'nationalite': 'Ivoirienne',
            'email': 'aminata.traore@example.com',
            'telephone': '+225 05 98 76 54 32',
            'adresse': 'Yopougon, Niangon, Abidjan',
            'niveau_etudes': 'BTS Informatique',
            'etablissement_origine': 'ESATIC',
            'annee_obtention': 2022,
        }
    ]
    
    for i, data in enumerate(candidats_data):
        # Assigner un concours aléatoire
        data['concours_souhaite'] = concours_created[i % len(concours_created)]
        
        candidat, created = Candidat.objects.get_or_create(
            email=data['email'],
            defaults=data
        )
        if created:
            print(f'✓ Candidat créé: {candidat.nom} {candidat.prenoms} - {candidat.numero_inscription}')
        else:
            print(f'- Candidat existe déjà: {candidat.nom} {candidat.prenoms}')
    
    print(f"\n📊 Résumé:")
    print(f"- Concours: {Concours.objects.count()}")
    print(f"- Candidats: {Candidat.objects.count()}")
    print(f"- Documents: {Document.objects.count()}")
    print("\n✅ Données de test créées avec succès!")
    print("\nPour démarrer le serveur:")
    print("python manage.py runserver")
    print("\nAccès:")
    print("- Site web: http://127.0.0.1:8000")
    print("- Administration: http://127.0.0.1:8000/admin")

if __name__ == '__main__':
    create_test_data()