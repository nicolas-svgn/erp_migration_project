import xml.etree.ElementTree as ET
import os

def generate_xml(df, output_folder, filename="import_axelor_final.xml"):
    """
    Génère le fichier XML avec la balise <product_root_product>.
    """
    print("--- 3. Génération du XML ---")
    
    root = ET.Element("root")

    for _, row in df.iterrows():
        # Utilisation du nom technique de la TABLE cible
        record = ET.SubElement(root, "product_root_product") 
        
        for col in df.columns:
            child = ET.SubElement(record, col)
            # Gestion des valeurs nulles/nan qui pourraient rester
            val = str(row[col]) if row[col] != 'nan' else ""
            child.text = val

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ", level=0) # Pour rendre le XML lisible (Pretty Print)
    
    # Création du dossier output s'il n'existe pas
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, filename)
    tree.write(output_path, encoding='utf-8', xml_declaration=True)
    
    print(f"   -> SUCCÈS ! Fichier généré ici : {output_path}")