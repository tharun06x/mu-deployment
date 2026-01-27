from fastapi import FastAPI
from fastapi.responses import JSONResponse
import joblib
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
from datetime import date
import streamlit as st
from main import Details
import pandas as pd
import numpy as np

app=FastAPI()
model=joblib.load('model/model.pkl')

@app.get('/')
def root():
    return{'status':'Cancer Prediction API Running'}

@app.post("/predict")
def prediction(prediction:Details):
    data=pd.DataFrame([{
        'age': prediction.age,
        'gender': prediction.gender,
        'cancer_stage': prediction.cancer_stage,
        'family_history':prediction.family_history,
        'smoking_status':prediction.smoking_status,
        'bmi':prediction.bmi,
        'cholesterol_level':prediction.cholesterol_level,
        'hypertension':prediction.hypertension,
        'asthma':prediction.asthma,
        'cirrhosis':prediction.cirrhosis,
        'other_cancer':prediction.other_cancer,
        'treatment_type':prediction.treatment_type,
        'totalduration':prediction.totalduration
    }])
    labelss={
        1:'Will Survive',
        0:'Will Not Survive'
    }
    prediction=model.predict(data)[0]
    return JSONResponse(status_code=200,content={'cancer_prediction':labelss[prediction]})



