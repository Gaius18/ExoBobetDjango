-- Script pour vérifier les concours dans MySQL
USE esatic_inscriptions;

SELECT 'VERIFICATION DES CONCOURS' as Status;
SELECT '=========================' as Separator;

-- Compter les concours
SELECT CONCAT('Total concours: ', COUNT(*)) as Total FROM inscriptions_concours;

-- Afficher tous les concours
SELECT 
    id as ID,
    nom as 'Nom du concours',
    niveau_requis as 'Niveau',
    frais_inscription as 'Frais (FCFA)',
    date_limite as 'Date limite',
    CASE WHEN actif = 1 THEN 'Actif' ELSE 'Inactif' END as 'Statut'
FROM inscriptions_concours
ORDER BY niveau_requis, nom;

-- Statistiques par niveau
SELECT 
    niveau_requis as 'Niveau',
    COUNT(*) as 'Nombre de concours'
FROM inscriptions_concours 
WHERE actif = 1
GROUP BY niveau_requis
ORDER BY niveau_requis;