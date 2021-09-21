from pydantic import BaseModel

class Features(BaseModel):
    age: int
    gender: int
    systolicBP: int
    diastolicBP: int
    cholesterol: int
    glucose: int
    smoke: int
    alcoholic: int
    active: int
    bmi: int
    
    