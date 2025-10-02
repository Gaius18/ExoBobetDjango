#!/usr/bin/env python
"""
Script pour tester la connexion MySQL
"""
import os
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestionTaches.settings')
django.setup()

from django.db import connection
from django.core.management.color import make_style

style = make_style()

def test_mysql_connection():
    """Tester la connexion à MySQL"""
    try:
        print("🔍 Test de connexion à MySQL...")
        
        # Tester la connexion
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()[0]
            print(f"✅ Connexion MySQL réussie !")
            print(f"📊 Version MySQL: {version}")
            
            # Tester la base de données
            cursor.execute("SELECT DATABASE()")
            db_name = cursor.fetchone()[0]
            print(f"🗄️  Base de données active: {db_name}")
            
            # Vérifier les tables
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            if tables:
                print(f"📋 Tables trouvées: {len(tables)}")
                for table in tables:
                    print(f"   - {table[0]}")
            else:
                print("⚠️  Aucune table trouvée. Exécutez les migrations:")
                print("   python manage.py makemigrations")
                print("   python manage.py migrate")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur de connexion MySQL: {e}")
        print("\n🔧 Solutions possibles:")
        print("1. Vérifiez que MySQL est démarré")
        print("2. Vérifiez les paramètres dans settings.py:")
        print("   - Nom de la base de données")
        print("   - Nom d'utilisateur")
        print("   - Mot de passe")
        print("   - Host et port")
        print("3. Créez la base de données:")
        print("   mysql -u root -p < mysql_config.sql")
        print("4. Installez mysqlclient:")
        print("   pip install mysqlclient")
        
        return False

if __name__ == '__main__':
    print("=== Test de configuration MySQL pour ESATIC ===\n")
    
    # Afficher la configuration actuelle
    from django.conf import settings
    db_config = settings.DATABASES['default']
    print("📋 Configuration actuelle:")
    print(f"   Engine: {db_config['ENGINE']}")
    print(f"   Database: {db_config['NAME']}")
    print(f"   User: {db_config['USER']}")
    print(f"   Host: {db_config['HOST']}")
    print(f"   Port: {db_config['PORT']}")
    print()
    
    # Tester la connexion
    if test_mysql_connection():
        print("\n🎉 Configuration MySQL OK !")
        print("\nÉtapes suivantes:")
        print("1. python manage.py makemigrations")
        print("2. python manage.py migrate")
        print("3. python create_test_data.py")
        print("4. python manage.py runserver")
    else:
        print("\n❌ Configuration MySQL à corriger")
        exit(1)