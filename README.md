# Projet Migration ERP - Données Articles

Ce projet assure l'extraction, la transformation et le chargement des données articles de l'ancien système (WinDev) vers le format XML requis par le nouvel ERP Axelor.

## Fonctionnalités
- Récupération des données articles filtrées.
- Enrichissement des données via le fichier de mapping (APPRO).
- Transformation des règles métiers (Types, Devises, Booleans).
- Génération d'un fichier XML structuré (`product_root_product`).

## Structure du projet
- `src/`: Code source Python (Loader, Transformer, Generator).
- `data/`: Dossier destiné aux fichiers sources CSV.
- `output/`: Dossier de destination du fichier XML généré.
- `venv/`: Environnement virtuel Python.

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