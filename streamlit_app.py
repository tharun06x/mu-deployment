import streamlit as st
import requests
from datetime import date
st.set_page_config(
    page_title="Cancer Prediction App",
    page_icon="🧬",
    layout="centered"
)
st.title("🧬 Cancer Prediction System")
st.write("Enter patient details to get prediction results")

API_URL = "http://127.0.0.1:8000/predict"

with st.form("patient_form"):
    age = st.number_input("Age", min_value=1, max_value=120, step=1)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    diagnosis_date = st.date_input(
        "Diagnosis Date",
        value=date.today()
    )

    cancer_stage = st.selectbox(
        "Cancer Stage",
        ["Stage I", "Stage II", "Stage III", "Stage IV"]
    )

    family_history = st.selectbox(
        "Family History of Cancer",
        ["Yes", "No"]
    )

    smoking_status = st.selectbox(
        "Smoking Status",
        [
            "Passive Smoker",
            "Former Smoker",
            "Never Smoked",
            "Current Smoker"
        ]
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=50.0,
        step=0.1
    )

    cholesterol_level = st.number_input(
        "Cholesterol Level",
        min_value=50.0,
        max_value=300.0,
        step=1.0
    )

    hypertension = st.selectbox(
        "Hypertension",
        options=[1, 0],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    asthma = st.selectbox(
        "Asthma",
        options=[1, 0],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    cirrhosis = st.selectbox(
        "Cirrhosis",
        options=[1, 0],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    other_cancer = st.selectbox(
        "Other Cancer",
        options=[1, 0],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    treatment_type = st.selectbox(
        "Treatment Type",
        ["Chemotherapy", "Surgery", "Combined"]
    )

    end_treatment_date = st.date_input(
        "End of Treatment Date",
        value=date.today()
    )

    submit = st.form_submit_button("🔍 Predict")
if submit:
    payload = {
        "age": age,
        "gender": gender,
        "diagnosis_date": diagnosis_date.isoformat(),
        "cancer_stage": cancer_stage,
        "family_history": family_history,
        "smoking_status": smoking_status,
        "bmi": bmi,
        "cholesterol_level": cholesterol_level,
        "hypertension": hypertension,
        "asthma": asthma,
        "cirrhosis": cirrhosis,
        "other_cancer": other_cancer,
        "treatment_type": treatment_type,
        "end_treatment_date": end_treatment_date.isoformat()
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            st.success("Prediction Successful ✅")
            st.json(response.json())
        else:
            st.error(f"Error {response.status_code}")
            st.text(response.text)

    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to FastAPI server. Is it running?")
