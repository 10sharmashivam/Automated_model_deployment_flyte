from fastapi import FastAPI
from pydantic import BaseModel
import xgboost as xgb
import numpy as np

app = FastAPI()

model = xgb.XGBClassifier()
model.load_model("model.json")

class Item(BaseModel):
    feature: float

@app.post("/predict/")
def predict(item: Item):
    prediction = model.predict(np.array([item.feature]).reshape(1, -1))
    return {"prediction": prediction.tolist()}