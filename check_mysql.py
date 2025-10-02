"""
Script pour vérifier la configuration MySQL
"""
import os
import sys

print("🔍 Vérification de la configuration MySQL...")

# Vérifier PyMySQL
try:
    import pymysql
    pymysql.install_as_MySQLdb()
    print("✅ PyMySQL configuré")
except ImportError:
    print("❌ PyMySQL non installé")
    sys.exit(1)

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestionTaches.settings')

try:
    import django
    django.setup()
    print("✅ Django configuré")
except Exception as e:
    print(f"❌ Erreur Django: {e}")
    sys.exit(1)

# Tester la connexion à la base
try:
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()[0]
        print(f"✅ Connexion MySQL OK - Version: {version}")
        
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()[0]
        print(f"✅ Base de données: {db_name}")
        
except Exception as e:
    print(f"❌ Erreur connexion MySQL: {e}")
    print("\nSolutions:")
    print("1. Vérifiez que MySQL est démarré")
    print("2. Vérifiez le mot de passe dans settings.py")
    print("3. Créez la base: CREATE DATABASE esatic_inscriptions;")
    sys.exit(1)

# Vérifier les tables
try:
    from django.core.management import execute_from_command_line
    from inscriptions.models import Concours
    
    # Compter les concours
    count = Concours.objects.count()
    print(f"✅ Concours en base: {count}")
    
    if count == 0:
        print("⚠️  Aucun concours trouvé")
        print("Exécutez: python fix_mysql_pymysql.py")
    else:
        print("📋 Concours disponibles:")
        for concours in Concours.objects.all()[:3]:
            print(f"   - {concours.nom}")
        if count > 3:
            print(f"   ... et {count-3} autres")
            
except Exception as e:
    print(f"⚠️  Erreur modèles: {e}")
    print("Exécutez les migrations: python manage.py migrate")

print("\n🎯 Configuration MySQL vérifiée!")
print("\nPour démarrer:")
print("python manage.py runserver")