# Cancer Prediction System

A machine learning-powered web application that predicts cancer survival and risk based on patient medical history and demographic details. This project utilizes **FastAPI** for a high-performance backend API and **Streamlit** for an interactive, user-friendly frontend.

---

## Live Demo

The application is currently deployed and available online:

* **Frontend (User Interface):** [https://mu-cancerprediction.streamlit.app/](https://mu-cancerprediction.streamlit.app/)
* **Backend (API & Docs):** [https://mu-deployment.onrender.com/docs](https://mu-deployment.onrender.com/docs)

---

## Tech Stack

* **Frontend:** Streamlit, Python
* **Backend:** FastAPI, Uvicorn
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Deployment:** Render (Backend), Streamlit Cloud (Frontend)
* **Containerization:** Docker

---

##  How to Run Locally

Follow these steps to set up the project on your local machine.

### Prerequisites
* Python 3.10
* Git

### 1. Clone the Repository
```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>

```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate

```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run the Backend (FastAPI)

Start the FastAPI server. This handles the machine learning inference.

```bash
uvicorn app.main:app --reload

```
* The API will start at: `http://127.0.0.1:8000`
* You can view the interactive API docs at: `http://127.0.0.1:8000/docs`

### 5. Run the Frontend (Streamlit)

Open a **new terminal** (keep the backend running) and start the Streamlit app.

```bash
streamlit run streamlit_app.py

```
* The app will open in your browser at: `http://localhost:8501`

> **Note for Local Testing:**
> Ensure the `API_URL` variable in `streamlit_app.py` is pointing to your local backend:
> `API_URL = "http://127.0.0.1:8000/predict"`

---

## How to Run with Docker

If you have Docker installed, you can run the backend container easily.

1. **Build the Docker Image:**
```bash
docker build -t cancer-prediction-app .

```


2. **Run the Container:**
```bash
docker run -p 8000:8000 cancer-prediction-app

```



---

## How to Test the API

You can test the prediction API directly without using the frontend interface.

### Option 1: Using Swagger UI (Recommended)

Visit the interactive documentation to test endpoints directly in your browser:

* **Live:** [https://mu-deployment.onrender.com/docs](https://www.google.com/url?sa=E&source=gmail&q=https://mu-deployment.onrender.com/docs)
* **Local:** [http://127.0.0.1:8000/docs](https://www.google.com/url?sa=E&source=gmail&q=http://127.0.0.1:8000/docs)

### Option 2: Using cURL

Copy and paste this command into your terminal to send a test request:

```bash
curl -X 'POST' \
  '[https://mu-deployment.onrender.com/predict](https://mu-deployment.onrender.com/predict)' \
  -H 'Content-Type: application/json' \
  -d '{
    "age": 45,
    "gender": "Male",
    "diagnosis_date": "2023-01-01",
    "cancer_stage": "Stage II",
    "family_history": 1,
    "smoking_status": "Never Smoked",
    "bmi": 24.5,
    "cholesterol_level": 220,
    "hypertension": 0,
    "asthma": 0,
    "cirrhosis": 0,
    "other_cancer": 0,
    "treatment_type": "Surgery",
    "end_treatment_date": "2023-06-01"
  }'

```

### Option 3: Using Postman

1. Open Postman and create a new **POST** request.
2. **URL:** `https://mu-deployment.onrender.com/predict`
3. Go to the **Body** tab → select **raw** → select **JSON**.
4. Paste the following JSON data:
```json
{
  "age": 55,
  "gender": "Female",
  "diagnosis_date": "2023-05-20",
  "cancer_stage": "Stage I",
  "family_history": 0,
  "smoking_status": "Former Smoker",
  "bmi": 28.0,
  "cholesterol_level": 200,
  "hypertension": 1,
  "asthma": 0,
  "cirrhosis": 0,
  "other_cancer": 0,
  "treatment_type": "Chemotherapy",
  "end_treatment_date": "2023-11-20"
}

```


5. Click **Send**.

```

```
