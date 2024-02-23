# Dans le fichier naics_engineering.py

def naicsEngineering(x):
    x = str(x)
    x = x[:2]
    if (x == '31') or (x == '32') or (x == '33'):
        x = '31-33'
    elif (x == '44') or (x == '45'):
        x = '44-45'
    elif (x == '48') or (x == '49'):
        x = '48-49'
    return x
