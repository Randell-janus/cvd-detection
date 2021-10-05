from pydantic import BaseModel, condecimal

class CVDRisk(BaseModel):
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

class BodyFat(BaseModel):
    age: condecimal(decimal_places=0, ge=20, le=80)
    weight: condecimal(decimal_places=2, ge=120, le=365)
    height: condecimal(decimal_places=2, ge=30, le=80)
    neck: condecimal(decimal_places=2, ge=30, le=50)
    chest: condecimal(decimal_places=2, ge=80, le=135)
    abdomen: condecimal(decimal_places=2, ge=70, le=150)
    hip: condecimal(decimal_places=2, ge=85, le=150)
    thigh: condecimal(decimal_places=2, ge=50, le=90)
    knee: condecimal(decimal_places=2, ge=35, le=50)
    ankle: condecimal(decimal_places=2, ge=20, le=35)
    biceps: condecimal(decimal_places=2, ge=25, le=45)
    forearm: condecimal(decimal_places=2, ge=20, le=35)
    wrist: condecimal(decimal_places=2, ge=15, le=20)
    