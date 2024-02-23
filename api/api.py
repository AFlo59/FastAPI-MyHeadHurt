from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import load_model, predict_prod
import pandas as pd

model = load_model()

app = FastAPI()

# Modèle Pydantic pour la structure de données d'entrée
class PredictionInput(BaseModel):
    City: str
    State: str
    Bank: str
    BankState: str
    NAICS: str
    ApprovalDate: str
    ApprovalFY: int
    Term: int
    NoEmp: int
    NewExist: bool
    CreateJob: int
    RetainedJob: int
    UrbanRural: str
    RevLineCr: bool
    LowDoc: bool
    GrAppv: int
    SBA_Appv: int
    Franchise: int

class PredictionOutput(BaseModel):
    Approve: bool

@app.post('/predict')
def predict(pinput: PredictionInput):
    # Convert input data into DataFrame
    data = pd.DataFrame([pinput.dict()])

    # Preprocess data if needed
    # ...

    # Make prediction
    predictions = predict_prod(model, data)  

    return PredictionOutput(Approve=predictions)