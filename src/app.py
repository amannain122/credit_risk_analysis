import streamlit as st
import joblib
import pandas as pd
import os

# Check if the app is running inside a Docker container
if os.path.exists('/app/models'):
    # If inside Docker, use the Docker container path
    model_path = '/app/models/'
else:
    # If running locally, use the local path
    model_path = './models/'

# Load the models
rf = joblib.load(os.path.join(model_path, 'rf.pkl'))  # Random Forest model
xgb = joblib.load(os.path.join(model_path, 'best_model.pkl'))  # XGBoost model

# Streamlit UI for input
st.title('Loan Default Prediction')

# Input fields for the user
person_income = st.number_input('Person Income', min_value=0)
loan_amnt = st.number_input('Loan Amount', min_value=0)
loan_int_rate = st.number_input('Loan Interest Rate', min_value=0.0)
default_history = st.selectbox('Default History (0=No, 1=Yes)', [0, 1])

# Automatically calculate Loan Percent Income
if person_income > 0:
    loan_percent_income = (loan_amnt / person_income) * 100
    st.write(f'**Loan Percent Income**: {loan_percent_income:.2f}% (calculated automatically)')
else:
    loan_percent_income = 0  # Handle division by zero if income is 0
    st.write('**Loan Percent Income**: 0% (calculated automatically)')

# Grade mapping for loan grades (A-G mapped to 1-7)
grade_mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
loan_grades = st.selectbox('Loan Grade (A-G)', list(grade_mapping.keys()))

# Home Ownership (one option out of the three)
home_ownership = st.selectbox('Home Ownership', ['MORTGAGE', 'OWN', 'RENT'])

# Map selected home ownership option to corresponding columns
home_ownership_mortgage = 1 if home_ownership == 'MORTGAGE' else 0
home_ownership_own = 1 if home_ownership == 'OWN' else 0
home_ownership_rent = 1 if home_ownership == 'RENT' else 0

# Convert loan grade from letter to numeric value
loan_grade_numeric = grade_mapping[loan_grades]

# Option to choose between Random Forest and XGBoost
model_choice = st.selectbox('Choose Model', ['Random Forest', 'XGBoost'])

# Make prediction when button is pressed
if st.button('Predict'):
    # Collect input into a DataFrame
    input_data = pd.DataFrame({
        'person_income': [person_income],
        'loan_amnt': [loan_amnt],
        'loan_int_rate': [loan_int_rate],
        'loan_percent_income': [loan_percent_income],
        'default_history': [default_history],
        'loan_grades': [loan_grade_numeric],
        'person_home_ownership_MORTGAGE': [home_ownership_mortgage],
        'person_home_ownership_OWN': [home_ownership_own],
        'person_home_ownership_RENT': [home_ownership_rent]
    })

    # Predict based on the selected model
    if model_choice == 'Random Forest':
        prediction = rf.predict(input_data)
    else:
        prediction = xgb.predict(input_data)

    # Display the result
    if prediction[0] == 1:
        st.write('Prediction: Default')
    else:
        st.write('Prediction: No Default')