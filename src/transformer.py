import pandas as pd

def get_dtype(valeur):
    """Transforme le code TENUESTOCK (1,2,3) en libellé Axelor."""
    try:
        valeur = int(valeur)
        if valeur == 1: return 'Article'
        if valeur == 2: return 'Prestation'
        if valeur == 3: return 'Consignataire'
    except:
        pass
    return 'Prestation' # Valeur par défaut de sécurité

def transform_data(df_art, df_appro):
    """
    Applique la logique métier, les jointures et le nettoyage.
    """
    print("--- 2. Transformation des données ---")

    # 1. Nettoyage des clés de jointure (strip)
    df_art['CODEFAM'] = df_art['CODEFAM'].astype(str).str.strip()
    df_appro['CODEFAM'] = df_appro['CODEFAM'].astype(str).str.strip()

    # 2. Jointure (Left Join)
    df_merged = pd.merge(df_art, df_appro, on='CODEFAM', how='left')

    # 3. Application des règles métier
    
    # Type de produit
    df_merged['dtype productTypeSelect'] = df_merged['TENUESTOCK'].apply(get_dtype)

    # Booleans (Forcés à false)
    df_merged['allow_to_force_purchase_qty'] = 'false'
    df_merged['allow_to_force_sale_qty'] = 'false'
    
    # Stock Managed (Si 1 -> true, sinon false)
    # On convertit en str pour être sûr de la comparaison
    df_merged['stock_managed'] = df_merged['TENUESTOCK'].apply(lambda x: 'true' if str(x).strip() == '1' else 'false')

    # Full Name (Concaténation)
    df_merged['full_name'] = df_merged['CODEART'].astype(str).str.strip() + " " + df_merged['LIBART'].astype(str).str.strip()

    # Devise (Vide ou 46 -> EUR)
    # Regex : remplace '46' par 'EUR' ET les chaînes vides par 'EUR'
    df_merged['purchase_currency'] = df_merged['DEVISE'].fillna('EUR').astype(str).str.strip().replace({'46': 'EUR', '': 'EUR'})

    # Duplication de colonnes
    df_merged['start_date'] = df_merged['DATECRE']
    df_merged['internal_description'] = df_merged['DESIGN']

    # 4. Sélection et Renommage final des colonnes
    final_df = df_merged[[
    'dtype productTypeSelect',
    'ARCLEUNIK',
    'DATECRE',
    'allow_to_force_purchase_qty',
    'allow_to_force_sale_qty',
    'CODEART',
    'DESIGN',
    'full_name',
    'internal_description',
    'LIBART',    
    'procurement_method_select',
    'start_date',
    'stock_managed',
    'product_category',
    'product_family',
    'purchase_currency',
    'UNITE'
    ]].copy()

    final_df.rename(columns={
    'ARCLEUNIK' : 'productFamily.id',
    'CODEART': 'code',
    'LIBART': 'name',
    'DESIGN' : 'description',
    'DATECRE': 'created_on startDate',
    'UNITE' : 'unit'
    }, inplace=True)

    # Nettoyage final des chaînes (strip)
    for col in final_df.columns:
        final_df[col] = final_df[col].astype(str).str.strip()

    print(f"   -> Transformation terminée. {final_df.shape[0]} articles prêts à l'export.")
    return final_df