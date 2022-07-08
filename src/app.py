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
async def index():
    return {'message': 'Go to /docs and try out the model'}

@app.post('/detect_cvd_risk')
async def detect_cvd_risk(data: CVDRisk):
    data = data.dict()
    predictors = [data['age'], data['gender'], data['systolicBP'], data['diastolicBP'], data['cholesterol'], 
                                         data['glucose'], data['smoke'], data['alcoholic'], data['active'], data['bmi']]
    prediction = knn_clf_model.predict([predictors])
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
async def predict_body_fat(data: BodyFat):
    predictors = [data.age, data.weight, data.height, data.neck, data.chest, data.abdomen, data.hip, 
                  data.thigh, data.knee, data.ankle, data.biceps, data.forearm, data.wrist]
    prediction = ridge_regr_model.predict([predictors])

    return {'prediction': prediction[0]}
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
