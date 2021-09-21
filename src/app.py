import uvicorn
from fastapi import FastAPI
from joblib import load
from src.features import Features

app = FastAPI()

knn_clf_model = load('src/knn_clf_model.joblib') 

@app.get('/')
def index():
    return {'message': 'Go to /docs and try out the model'}

@app.post('/predict')
def predict_data(data: Features):
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
        prediction = "There's no presence of Cardiovascular Disease!"
    else:
        prediction = "There is a presence of Cardiovascular Disease."
    return {
        'prediction': prediction
    }
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
