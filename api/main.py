from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from model_utils import load_model, prediction

app = FastAPI()

class LoanInput(BaseModel):
    City: str
    State: str
    Bank: str
    BankState: str
    NAICS: str
<<<<<<< HEAD
#    ApprovalDate: str
#    ApprovalFY: int
=======
>>>>>>> efdc92fe11a7a189cd7006dedc1bab6197657122
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

class LoanOutput(BaseModel):
    Approve: bool

model = load_model()

@app.post('/predict', response_model=LoanOutput)
def predict_loan(input_data: LoanInput):
    features = input_data.dict()
    input_df = pd.DataFrame([features])
    predictions = prediction(model, input_df)

    return LoanOutput(Approve=bool(predictions[0]))