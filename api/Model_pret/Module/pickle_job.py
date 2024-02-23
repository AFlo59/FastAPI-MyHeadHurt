import os
import pickle

def sauvegarder_modele(model, nom_fichier):
    """
    Sauvegarde un modèle dans un fichier .pckl dans le dossier Model.
    
    Args:
        model: Le modèle à sauvegarder.
        nom_fichier (str): Le nom du fichier où sauvegarder le modèle.
    """
    chemin_fichier = os.path.join("..", "Model", nom_fichier + ".pkl")
    with open(chemin_fichier, 'wb') as f:
        pickle.dump(model, f)
    print(f"Le modèle a été sauvegardé dans '{chemin_fichier}'.")

def charger_modele(nom_fichier):
    """
    Charge un modèle à partir d'un fichier .pckl dans le dossier Model.
    
    Args:
        nom_fichier (str): Le nom du fichier où est enregistré le modèle.
    
    Returns:
        model: Le modèle chargé.
    """
    chemin_fichier = os.path.join("..", "Model", nom_fichier + ".pckl")
    with open(chemin_fichier, 'rb') as f:
        loaded_model = pickle.load(f)
    print(f"Le modèle a été chargé à partir de '{chemin_fichier}'.")
    return loaded_model
