from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import load_model, prediction

app = FastAPI()

class LanguageInput(BaseModel):
    language: str

class FeaturesInput(BaseModel):
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

model = load_model()

@app.post('/predict')
def prediction_root(feature_input: FeaturesInput):
    features = [value for value in feature_input.dict().values()]
    predictions = prediction(model, [features])
    return PredictionOutput(Approve=predictions)

@app.post('/predict/v0')
def prediction_root_v0(feature_input: FeaturesInput):
    features = [feature_input.City, feature_input.State, feature_input.Bank, feature_input.BankState,
                feature_input.NAICS, feature_input.ApprovalDate, feature_input.ApprovalFY, feature_input.Term,
                feature_input.NoEmp, feature_input.NewExist, feature_input.CreateJob, feature_input.RetainedJob,
                feature_input.UrbanRural, feature_input.RevLineCr, feature_input.LowDoc, feature_input.GrAppv,
                feature_input.SBA_Appv, feature_input.Franchise]
    predictions = prediction(model, [features])
    return PredictionOutput(Approve=predictions)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}