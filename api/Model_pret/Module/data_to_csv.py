import os
import pandas as pd

def df_to_csv(dataframe, folder_path, filename):
    """
    Convertit un DataFrame en fichier CSV.

    Args:
        dataframe (pandas.DataFrame): Le DataFrame à convertir.
        folder_path (str): Le chemin du dossier où le fichier CSV doit être enregistré.
        filename (str): Le nom du fichier CSV à créer.

    Returns:
        None
    """
    # Assurez-vous que le dossier existe, sinon créez-le
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_path = os.path.join(folder_path, filename)
    dataframe.to_csv(file_path, index=False)
    print(f"Le DataFrame a été converti avec succès en fichier CSV : {file_path}")
