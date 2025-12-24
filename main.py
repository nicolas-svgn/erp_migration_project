from src.data_loader import load_data
from src.transformer import transform_data
from src.xml_generator import generate_xml
import os
import sys

def main():
    # Définition des chemins dynamiques
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
    
    # Noms des fichiers (Modifie ici si tes fichiers changent de nom)
    FILE_ARTICLE = os.path.join(DATA_DIR, 'ARTICLE.csv') 
    FILE_APPRO = os.path.join(DATA_DIR, 'Appro.csv')

    try:
        df_art, df_appro = load_data(FILE_ARTICLE, FILE_APPRO)
        final_df = transform_data(df_art, df_appro)
        generate_xml(final_df, OUTPUT_DIR)
        
    except Exception as e:
        print(f"\n[ERREUR CRITIQUE] : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()