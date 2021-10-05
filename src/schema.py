from pydantic import BaseModel, condecimal

class CvdRisk(BaseModel):
    age: condecimal(decimal_places=0, ge=20, le=65)
    gender: condecimal(decimal_places=0, ge=0, le=1)
    systolicBP: condecimal(decimal_places=0, ge=90, le=200)
    diastolicBP: condecimal(decimal_places=0, ge=60, le=130)
    cholesterol: condecimal(decimal_places=0, ge=1, le=3)
    glucose: condecimal(decimal_places=0, ge=1, le=3)
    smoke: condecimal(decimal_places=0, ge=0, le=1)
    alcoholic: condecimal(decimal_places=0, ge=0, le=1)
    active: condecimal(decimal_places=0, ge=0, le=1)
    bmi: int
    