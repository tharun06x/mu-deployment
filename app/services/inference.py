import joblib
import pandas as pd

model = joblib.load("model/model.pkl")

LABELS = {
    1: "Will Survive",
    0: "Will Not Survive"
}

def predict_survival(details):
    data = pd.DataFrame([{
        "age": details.age,
        "gender": details.gender,
        "cancer_stage": details.cancer_stage,
        "family_history": details.family_history,
        "smoking_status": details.smoking_status,
        "bmi": details.bmi,
        "cholesterol_level": details.cholesterol_level,
        "hypertension": details.hypertension,
        "asthma": details.asthma,
        "cirrhosis": details.cirrhosis,
        "other_cancer": details.other_cancer,
        "treatment_type": details.treatment_type,
        "totalduration": details.totalduration
    }])

    prediction = model.predict(data)[0]
    return LABELS[prediction]
