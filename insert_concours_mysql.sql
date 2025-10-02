-- Script SQL pour insérer les concours directement dans MySQL
-- Exécuter avec: mysql -u root -p esatic_inscriptions < insert_concours_mysql.sql

USE esatic_inscriptions;

-- Vider la table des concours existants
DELETE FROM inscriptions_concours;

-- Insérer les nouveaux concours
INSERT INTO inscriptions_concours (nom, niveau_requis, description, frais_inscription, date_limite, actif) VALUES
('Concours d\'entrée en 1ère année - Cycle Ingénieur', 'BAC', 'Formation d\'ingénieur en télécommunications et réseaux. Programme de 5 ans pour former des ingénieurs capables de concevoir, déployer et maintenir des infrastructures de télécommunications modernes.', 25000.00, DATE_ADD(CURDATE(), INTERVAL 30 DAY), 1),

('Concours Bachelier en Informatique et Télécommunications', 'BACHELIER', 'Formation de niveau bachelier spécialisée en informatique et télécommunications. Programme de 3 ans orienté vers les technologies de l\'information et de la communication.', 20000.00, DATE_ADD(CURDATE(), INTERVAL 40 DAY), 1),

('Concours d\'entrée en 3ème année - Cycle Ingénieur', 'BAC+2', 'Admission directe en 3ème année du cycle ingénieur pour les titulaires d\'un BTS, DUT ou équivalent en électronique, informatique ou télécommunications.', 30000.00, DATE_ADD(CURDATE(), INTERVAL 25 DAY), 1),

('Concours Analyste Statisticien - Niveau Bac+2', 'BAC+2', 'Formation spécialisée en analyse statistique et traitement de données pour les secteurs public et privé. Programme axé sur les méthodes quantitatives et l\'analyse de données.', 20000.00, DATE_ADD(CURDATE(), INTERVAL 35 DAY), 1),

('Master en Data Science et Intelligence Artificielle', 'BAC+3', 'Formation avancée en science des données, machine learning et intelligence artificielle. Programme orienté vers la recherche et l\'innovation technologique.', 35000.00, DATE_ADD(CURDATE(), INTERVAL 20 DAY), 1),

('Master en Cybersécurité et Réseaux', 'BAC+3', 'Spécialisation en sécurité informatique, audit de sécurité, gestion des risques cyber et protection des infrastructures numériques.', 35000.00, DATE_ADD(CURDATE(), INTERVAL 15 DAY), 1);

-- Vérifier les données insérées
SELECT 'Concours créés avec succès!' as Message;
SELECT id, nom, niveau_requis, frais_inscription, date_limite, actif FROM inscriptions_concours;
SELECT CONCAT('Total concours: ', COUNT(*)) as Total FROM inscriptions_concours;