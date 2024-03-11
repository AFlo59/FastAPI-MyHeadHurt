from joblib import load
from catboost import CatBoostClassifier  

def load_model(path='api/Model_pret/Model/catboost_model.pkl'):
    try:
        model = CatBoostClassifier()
        model.load_model(path)
        return model
    except Exception as e:
        print(f"An error occurred while loading the model: {e}")
        return None


def prediction(model, data):
    predictions = model.predict(data)
    return predictions