import os
import pandas as pd

def diviser_csv(input_file, output_prefix, num_parts):
    """
    Divise un fichier CSV en plusieurs parties et supprime le fichier original.
    
    Args:
        input_file (str): Chemin d'accès au fichier CSV d'entrée.
        output_prefix (str): Préfixe pour les noms des fichiers de sortie.
        num_parts (int): Nombre de parties dans lesquelles diviser le fichier.
    """
    # Charger le fichier CSV
    data = pd.read_csv(input_file)
    
    # Calculer la taille de chaque partie
    num_rows = len(data)
    part_size = num_rows // num_parts
    
    # Diviser l'ensemble de données en parties
    for i in range(num_parts):
        start_idx = i * part_size
        end_idx = start_idx + part_size if i < num_parts - 1 else None
        part = data.iloc[start_idx:end_idx]
        part.to_csv(f"{output_prefix}_part{i + 1}.csv", index=False)
    
    # Supprimer le fichier original
    os.remove(input_file)
    print(f"Fichier {input_file} supprimé avec succès")

if __name__ == "__main__":
    # Utilisation de la fonction diviser_csv
    input_file = "dataset/SBAnational.csv"
    output_prefix = "dataset/SBAnational_part"
    num_parts = 4
    diviser_csv(input_file, output_prefix, num_parts)

