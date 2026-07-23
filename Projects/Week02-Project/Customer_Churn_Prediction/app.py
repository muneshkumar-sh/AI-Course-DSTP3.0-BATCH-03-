# ==========================================================
# app.py
# Customer Churn Prediction Web Application
# ==========================================================

# Import required libraries
from flask import Flask, render_template, request

# Import prediction function
from prediction import predict_churn

# Create Flask application
app = Flask(__name__)


# ==========================================================
# Home Page
# ==========================================================

@app.route("/")
def home():
    """
    Display the home page.
    """
    return render_template("index.html")


# ==========================================================
# Predict Customer Churn
# ==========================================================

@app.route("/predict", methods=["POST"])
def predict():

    # Collect user input from HTML form
    customer = {

        "gender": request.form["gender"],
        "SeniorCitizen": int(request.form["SeniorCitizen"]),
        "Partner": request.form["Partner"],
        "Dependents": request.form["Dependents"],
        "tenure": int(request.form["tenure"]),
        "PhoneService": request.form["PhoneService"],
        "MultipleLines": request.form["MultipleLines"],
        "InternetService": request.form["InternetService"],
        "OnlineSecurity": request.form["OnlineSecurity"],
        "OnlineBackup": request.form["OnlineBackup"],
        "DeviceProtection": request.form["DeviceProtection"],
        "TechSupport": request.form["TechSupport"],
        "StreamingTV": request.form["StreamingTV"],
        "StreamingMovies": request.form["StreamingMovies"],
        "Contract": request.form["Contract"],
        "PaperlessBilling": request.form["PaperlessBilling"],
        "PaymentMethod": request.form["PaymentMethod"],
        "MonthlyCharges": float(request.form["MonthlyCharges"]),
        "TotalCharges": float(request.form["TotalCharges"])
    }

    # Predict customer churn
    prediction, confidence = predict_churn(customer)

    # Return result to webpage
    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence
    )


# ==========================================================
# Run Application
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)