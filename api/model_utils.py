from joblib import load
from catboost import CatBoostClassifier  

def load_model(path='Model_pret/Model/catboost_model.pkl'):
    model = CatBoostClassifier()
    model.load_model(path)
    return model

def prediction(model, data):
    predictions = model.predict(data)
    return predictions