/*
 * Projet Migration ERP - Tâche 1
 * Auteur : Nicolas
 * Date : 2025-12-24
 * Description : Extraction des articles > 01/01/2017 hors familles AAA/SOS
 * Syntaxe : HFSQL (WinDev)
 */

SELECT
    TENUESTOCK,
    ARCLEUNIK,
    DATECRE,
    CODEART,
    DESIGN,
    LIBART,
    CODEFAM,
    DEVISE,
    UNITE
FROM
    ARTICLE
WHERE
    DATECRE > '20170101'  
    AND CODEFAM NOT IN ('AAA', 'SOS');
