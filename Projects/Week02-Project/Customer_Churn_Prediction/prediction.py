# ==========================================================
# prediction.py
# Customer Churn Prediction Module
# ==========================================================

# Import required libraries
import joblib
import pandas as pd
from pathlib import Path


# ==========================================================
# Load the Trained Pipeline
# ==========================================================

# Get the directory where prediction.py is located
BASE_DIR = Path(__file__).resolve().parent

# Create complete path to the trained model
MODEL_PATH = BASE_DIR / "churn_pipeline.pkl"

# Load the trained pipeline
pipeline = joblib.load(MODEL_PATH)


# ==========================================================
# Prediction Function
# ==========================================================

def predict_churn(customer_data):

    # Convert customer dictionary into DataFrame
    customer_df = pd.DataFrame([customer_data])

    # Make prediction
    prediction = pipeline.predict(customer_df)[0]

    # Get prediction probabilities
    probability = pipeline.predict_proba(customer_df)[0]

    # Convert result into readable format
    if prediction == 1:
        result = "Customer is likely to Churn"
        confidence = probability[1] * 100
    else:
        result = "Customer is likely to Stay"
        confidence = probability[0] * 100

    return result, round(confidence, 2)