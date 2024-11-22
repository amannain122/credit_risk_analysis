# Credit Risk Analysis

This project is a **Loan Default Prediction** model built using **XGBoost** and **RandomForest** and  using **Streamlit** for Web Interface. It calculates the probability of a loan default based on several user-provided features. 
The app is **Dockerized**, making it easy to deploy and run anywhere.

## Features
- **User Input**: The app takes various inputs such as:
  - Person Income(In USD)
  - Loan Amount
  - Loan Interest Rate(%)
  - Loan Percent Income (calculated automatically)
  - Default History (whether the person has a previous default)
  - Loan Grade (A-G)
  - Home Ownership (MORTGAGE, OWN, RENT)
  
- **Prediction**: The app predicts whether the loan is likely to default or not.

## Project Setup

### Clone this repository
```bash
git clone https://github.com/amannain122/credit_risk_analysis
```

### Requirements

1. Python 3.10 or higher
2. Docker (for containerization)

### Dependencies
You can install the dependencies by running:
```bash
pip install -r requirements.txt
```
- Streamlit
- XGBoost
- pandas
- joblib
- scikit-learn

### Run the app when in directory using
```bash
streamlit run app.py
```
### Docker Setup

1. Build the Image
```bash
docker build -t streamlit-app .
```
2. Run the Container
```bash
docker run -p 8501:8501 streamlit-app
```
