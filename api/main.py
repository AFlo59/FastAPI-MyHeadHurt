from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import load_model, prediction

app = FastAPI()

class LoanInput(BaseModel):
    City: str
    State: str
    Bank: str
    BankState: str
    NAICS: str
#    ApprovalDate: str
#    ApprovalFY: int
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
    predictions = prediction(model, [features])
    return LoanOutput(Approve=predictions)