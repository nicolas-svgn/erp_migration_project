# Projet Migration ERP - Données Articles

Ce projet assure l'extraction, la transformation et le chargement des données articles de l'ancien système (WinDev) vers le format XML requis par le nouvel ERP Axelor.

## Fonctionnalités
- Récupération des données articles filtrées.
- Enrichissement des données via le fichier de mapping (APPRO).
- Transformation des règles métiers (Types, Devises, Booleans).
- Génération d'un fichier XML structuré (`product_root_product`).

## Structure du projet
```text
erp_migration_project/
├── data/               # Fichiers sources CSV (ARTICLE.csv, APPRO.csv)
├── output/             # Résultat de la conversion (import_axelor_final.xml)
├── sql/                # Requêtes SQL d'extraction pour WinDev/HFSQL
├── src/                # Code source du module 
│   ├── __init__.py     # Rend le dossier src transformable en package
│   ├── data_loader.py  # Chargement et lecture des fichiers CSV
│   ├── transformer.py  # Logique métier et nettoyage des données Pandas
│   └── xml_generator.py# Transformation du DataFrame en fichier XML
├── main.py             # Point d'entrée principal du programme
├── requirements.txt    # Liste des dépendances (pandas)
├── .gitignore          # Fichiers à exclure du versioning (venv, cache)
└── README.md           # Documentation du projet

## Prérequis
- Python 3.10.12
- Git

## Installation et Exécution

### 1. Cloner et configurer l'environnement
Ouvrez un terminal dans le dossier du projet :

```bash
# Création de l'environnement virtuel
python3 -m venv venv

# Activation de l'environnement (Linux/Mac)
source venv/bin/activate

# Installation des dépendances
pip install -r requirements.txt