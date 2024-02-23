def currency_cleaning(x):
    if isinstance(x, str):
        x = x[1:].replace(',', '')
    return x