import uvicorn
from fastapi import FastAPI
from joblib import load
from src.schemas.features import Features

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#adding cors policy
origins = [
    "*"
]

#add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

knn_clf_model = load('src/models/knn_clf_model.joblib') 

@app.get('/')
def index():
    return {'message': 'Go to /docs and try out the model'}

@app.post('/predict')
def detect_cvd_risk(data: Features):
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
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
