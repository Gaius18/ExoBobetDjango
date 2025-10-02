-- Configuration MySQL pour ESATIC
-- Exécuter ce script avec: mysql -u root -p < mysql_config.sql

-- Créer la base de données
CREATE DATABASE IF NOT EXISTS esatic_inscriptions 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Créer un utilisateur dédié (optionnel, pour la sécurité)
-- CREATE USER 'esatic_user'@'localhost' IDENTIFIED BY 'votre_mot_de_passe';
-- GRANT ALL PRIVILEGES ON esatic_inscriptions.* TO 'esatic_user'@'localhost';
-- FLUSH PRIVILEGES;

-- Utiliser la base de données
USE esatic_inscriptions;

-- Afficher les informations
SELECT 'Base de données esatic_inscriptions créée avec succès !' as Message;
SHOW DATABASES LIKE 'esatic_inscriptions';