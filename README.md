# FastAPI server
- https://fastapi-ml-server.herokuapp.com/docs

## Available APIs
### Cardiovascular Disease Risk Detection
Request URL (POST method)
```
https://fastapi-ml-server.herokuapp.com/predict
``` 
Schema
```
{
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
}
```
Sample Response Body
```
{
  "prediction": "There's no risk of Cardiovascular Disease!",
  "result": 0
}
```
## Disclaimer
Server is currently deployed with a heroku free tier and goes to sleep after 30 mins of no web traffic, a short delay may occur on the initial load.
