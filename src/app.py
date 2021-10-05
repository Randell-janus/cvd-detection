import uvicorn
from fastapi import FastAPI
from joblib import load
from src.schema import CVDRisk, BodyFat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

knn_clf_model = load('src/models/knn_clf_model.joblib') 
ridge_regr_model = load('src/models/ridge_regr_model.joblib') 

@app.get('/')
def index():
    return {'message': 'Go to /docs and try out the model'}

@app.post('/detect_cvd_risk')
def detect_cvd_risk(data: CVDRisk):
    data = data.dict()
    
    age = data['age']
    gender = data['gender']
    systolicBP = data['systolicBP']
    diastolicBP = data['diastolicBP']
    cholesterol = data['cholesterol']
    glucose = data['glucose']
    smoke = data['smoke']
    alcoholic = data['alcoholic']
    active = data['active']
    bmi = data['bmi']

    prediction = knn_clf_model.predict([[age, gender, systolicBP, diastolicBP, cholesterol, 
                                         glucose, smoke, alcoholic, active, bmi]])
    if(prediction[0] == 0):
        prediction = "There's no risk of Cardiovascular Disease!"
        result = 0
    else:
        prediction = "There's a risk of Cardiovascular Disease."
        result = 1
    return {
        'prediction': prediction,
        'result': result
    }

@app.post('/predict_body_fat')
def predict_body_fat(data: BodyFat):
    data = data.dict()
    
    age = data['age']
    weight = data['weight']
    height = data['height']
    neck = data['neck']
    chest = data['chest']
    abdomen = data['abdomen']
    hip = data['hip']
    thigh = data['thigh']
    knee = data['knee']
    ankle = data['ankle']
    biceps = data['biceps']
    forearm = data['forearm']
    wrist = data['wrist']
    
    predictors = [age, weight, height, neck, chest, abdomen, hip, thigh, knee, ankle, biceps, forearm, wrist]
    prediction = ridge_regr_model.predict([predictors])
    
    return {'prediction': prediction[0]}
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
