import pandas as pd

def generate_description(df):
    list_item = []
    for col in df.columns:
        list_item.append([
            col,
            df[col].dtype,
            df[col].isna().sum(),
            round((df[col].isna().sum() / len(df[col])) * 100, 2),
            df[col].nunique(),
            list(df[col].sample(5).drop_duplicates().values)
        ])
    dfDesc = pd.DataFrame(columns=['feature', 'data_type', 'null', 'nulPct', 'unique', 'uniqueSample'], data=list_item)
    return dfDesc






