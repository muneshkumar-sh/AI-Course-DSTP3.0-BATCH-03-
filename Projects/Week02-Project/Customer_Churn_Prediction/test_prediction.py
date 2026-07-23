# ==========================================================
# test_prediction.py
# Test Customer Churn Prediction Module
# ==========================================================

# Import prediction function
from prediction import predict_churn

# ==========================================================
# Sample Customer Data
# ==========================================================

customer = {

    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 24,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "Yes",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 80.50,
    "TotalCharges": 1932.00
}

# ==========================================================
# Predict Customer Churn
# ==========================================================

prediction, confidence = predict_churn(customer)

# ==========================================================
# Display Result
# ==========================================================

print("=" * 50)
print("Customer Churn Prediction")
print("=" * 50)

print("Prediction :", prediction)
print("Confidence :", confidence, "%")