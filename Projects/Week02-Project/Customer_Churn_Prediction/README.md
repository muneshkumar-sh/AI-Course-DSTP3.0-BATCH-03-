# Customer Churn Prediction Using Machine Learning

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to **churn (leave the service)** or **stay**, based on customer demographics, services, contract details, and billing information.

The project covers the complete Machine Learning workflow from data preprocessing and exploratory data analysis to model training, class imbalance handling, hyperparameter tuning, model deployment, and a Flask-based web application.

---

## Project Objective

Customer churn is an important business problem for telecom companies because retaining existing customers is often more cost-effective than acquiring new ones.

The objective of this project is to build a Machine Learning model that can identify customers who are at risk of leaving the company.

The model predicts:

- **0 — No Churn:** Customer is likely to stay
- **1 — Churn:** Customer is likely to leave

---

## Dataset

The project uses the **Telco Customer Churn Dataset**.

The dataset contains information about telecom customers, including:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges
- Churn

The original dataset contains approximately **7,000 customer records**.

---

## Machine Learning Workflow

The project follows the complete Machine Learning lifecycle:

1. Data Loading
2. Data Understanding
3. Data Cleaning
4. Handling Missing Values
5. Exploratory Data Analysis (EDA)
6. Categorical Feature Encoding
7. Feature Scaling
8. Train-Test Split
9. Model Training
10. Model Evaluation
11. Handling Class Imbalance
12. Hyperparameter Tuning
13. Model Selection
14. Scikit-learn Pipeline
15. Model Serialization
16. Flask Web Application
17. Deployment

---

## Exploratory Data Analysis

EDA was performed to understand the relationship between customer characteristics and churn.

Some important observations were:

- Customers with **month-to-month contracts** showed higher churn.
- Customers with **shorter tenure** were more likely to churn.
- Churned customers had higher average monthly charges.
- Customers using **fiber optic internet** showed relatively higher churn.
- Long-term customers were generally less likely to leave.

---

## Machine Learning Models

The following Machine Learning algorithms were trained and evaluated:

### 1. Logistic Regression

The baseline Logistic Regression model achieved approximately:

- **Accuracy: 80.88%**
- **Churn Recall: 54%**
- **Churn F1-Score: 60%**

---

### 2. Decision Tree

The Decision Tree achieved approximately:

- **Testing Accuracy: 72.68%**

The model showed significant overfitting:

- Training Accuracy: approximately **99.8%**
- Testing Accuracy: approximately **72.68%**

---

### 3. Random Forest

Random Forest achieved approximately:

- **Testing Accuracy: 78.96%**
- **Churn Recall: 48%**
- **Churn F1-Score: 55%**

---

## Handling Class Imbalance

The dataset contains more non-churn customers than churn customers.

Two approaches were tested to improve churn detection:

### Class Weight Balancing

Logistic Regression was trained using:

`class_weight="balanced"`

This significantly improved the recall for churn customers.

Results:

- **Accuracy: 74.32%**
- **Churn Recall: 78%**
- **Churn F1-Score: 62%**

The number of missed churn customers was reduced significantly compared with the original Logistic Regression model.

---

### SMOTE

SMOTE (Synthetic Minority Oversampling Technique) was also tested to balance the training dataset.

Results were approximately:

- **Accuracy: 74.61%**
- **Churn Recall: 77%**
- **Churn F1-Score: 62%**

SMOTE and class weighting produced similar results for this dataset.

---

## Hyperparameter Tuning

`GridSearchCV` with 5-fold cross-validation was used to optimize the Logistic Regression model.

The best parameters were:

- **C:** 10
- **Penalty:** L2
- **Solver:** lbfgs
- **Class Weight:** balanced

The tuned model maintained approximately **78% recall for the churn class**.

---

## Model Comparison

| Model | Accuracy | Churn Recall | Churn F1 |
|---|---:|---:|---:|
| Logistic Regression | 80.88% | 54% | 60% |
| Decision Tree | 72.68% | 48% | 48% |
| Random Forest | 78.96% | 48% | 55% |
| Balanced Logistic Regression | 74.32% | 78% | 62% |
| SMOTE Logistic Regression | 74.61% | 77% | 62% |
| Tuned Logistic Regression | ~74% | 78% | 61% |

---

## Final Model

For this project, the **Balanced Logistic Regression model** was selected for deployment.

Although the original Logistic Regression achieved higher overall accuracy, the balanced model achieved significantly better **recall for churn customers**.

This is important because the primary business objective is to identify as many customers at risk of leaving as possible.

The final model is stored inside a complete Scikit-learn pipeline containing:

- One-Hot Encoding
- Standard Scaling
- Logistic Regression

The trained pipeline is saved as:

`churn_pipeline.pkl`

---

## Web Application

A Flask-based web application was developed to allow users to enter customer information and receive a real-time churn prediction.

The application displays:

- Customer churn prediction
- Churn / Stay result
- Prediction confidence percentage

Example output:

**Customer is likely to Churn**

**Confidence: 87.93%**

---

## Technologies Used

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn
- Imbalanced-learn (SMOTE)

### Web Development

- Flask
- HTML
- CSS

### Deployment

- Gunicorn
- Render

### Development Tools

- Jupyter Notebook
- Visual Studio Code
- Git
- GitHub

---

## Project Structure

    Customer_Churn_Prediction/
    │
    ├── app.py
    ├── prediction.py
    ├── churn_pipeline.pkl
    ├── Customer_Churn_Prediction.ipynb
    ├── Telco-Customer-Churn.csv
    ├── requirements.txt
    ├── Procfile
    ├── .gitignore
    ├── README.md
    │
    ├── templates/
    │   └── index.html
    │
    └── static/
        └── style.css

---

## Installation

Clone the repository:

    git clone <your-repository-url>

Move into the project directory:

    cd Customer_Churn_Prediction

Install the required libraries:

    pip install -r requirements.txt

---

## Run the Application

Run the Flask application:

    python app.py

Then open the following address in your browser:

    http://127.0.0.1:5000

---

## Future Improvements

Possible improvements to the project include:

- Explainable AI using SHAP
- Advanced feature engineering
- Threshold optimization
- XGBoost or LightGBM models
- Improved user interface
- Prediction risk levels
- Churn probability visualization
- Cloud deployment improvements

---

## Live Demo

The live application link will be added after deployment.

---

## Author

**Munesh Kumar**

Software Engineering Student | Python | Machine Learning | Artificial Intelligence

---

## Acknowledgment

This project was developed as part of my practical learning journey after completing the **AI with Python** course from DigiSkills.