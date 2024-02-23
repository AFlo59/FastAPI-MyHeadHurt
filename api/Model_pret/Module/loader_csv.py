import os
import pandas as pd

def charger_csv(partie1, partie2, partie3, partie4):
    # Charger chaque partie du CSV découpé en DataFrame
    df_partie1 = pd.read_csv(partie1)
    df_partie2 = pd.read_csv(partie2)
    df_partie3 = pd.read_csv(partie3)
    df_partie4 = pd.read_csv(partie4)
    
    # Réassembler les parties dans l'ordre
    df_reassemble = pd.concat([df_partie1, df_partie2, df_partie3, df_partie4], ignore_index=True)
    
    return df_reassemble
