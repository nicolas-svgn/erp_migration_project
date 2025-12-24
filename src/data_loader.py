import pandas as pd
import os

def load_data(article_path, appro_path):
    """
    Charge les fichiers CSV ARTICLE et APPRO.
    """
    print("--- 1. Chargement des données ---")
    
    if not os.path.exists(article_path):
        raise FileNotFoundError(f"ERREUR : Le fichier {article_path} est introuvable.")
    if not os.path.exists(appro_path):
        raise FileNotFoundError(f"ERREUR : Le fichier {appro_path} est introuvable.")
    
    # Chargement ARTICLE (Attention au séparateur : souvent ';' pour les exports français/WinDev)
    # On force dtype=str pour préserver les codes postaux ou codes articles commençant par 0
    try:
        # Chargement ARTICLE
        df_art= pd.read_csv(article_path, sep=',', encoding='utf-8-sig')
        # Chargement APPRO
        df_appro = pd.read_csv(appro_path, sep=',', encoding='utf-8-sig')
    except Exception as e:
        raise ValueError(f"Erreur de lecture du fichier ARTICLE: {e}")

    

    # Nettoyage des noms de colonnes
    df_art.columns = df_art.columns.str.strip()
    df_appro.columns = df_appro.columns.str.strip()

    print(f"   -> Article chargé : {df_art.shape[0]} lignes")
    print(f"   -> Appro chargé : {df_appro.shape[0]} lignes")
    
    return df_art, df_appro