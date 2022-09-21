
import pandas as pd
import streamlit as st
import joblib
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

#model = joblib.load(r"./default_model.sav")

#df_final = pd.read_csv('loan_dataset.csv')

def main():

    st.set_page_config(
        page_title = 'Alura Ca$h - Client Default Prediction',
        page_icon = '✅',
        layout = 'wide')

    st.sidebar.title('Client Default Prediction')

    image = Image.open('alura_cash.png')

    st.image(image)


    person_age = st.sidebar.number_input('Client age: ', min_value = 18, max_value = 120, value = 18)


    person_home_ownership = st.sidebar.selectbox('Type of home ownership: ', ('Mortgage', 'Rent', 'Own', 'Other'))


    person_income = st.sidebar.number_input('Client annual income: ', min_value = 0.0, max_value = 1000000000.0, value = 0.0, step = 0.1)


    person_emp_length = st.sidebar.slider('Employment length (years): ', min_value = 0, max_value = 50, value = 0)


    loan_intent = st.sidebar.radio('Loan intent: ', ('Homeimprovement', 'Venture', 'Personal', 'Medical', 'Education', 'Debtconsolidation'))


    loan_amnt = st.sidebar.number_input('Loan amount: ', min_value = 0.0, max_value = 1000000000.0, value = 0.0, step = 0.1)


    loan_int_rate = st.sidebar.number_input('Loan interest rate: ', min_value = 0.00, max_value = 40.00, value = 0.00, step = 0.01)


    loan_percent_income = st.sidebar.number_input('Loan percentage of income: ', min_value = 0.00, max_value = 1.00, value = 0.00, step = 0.01)


    person_default_on_file = st.sidebar.selectbox('Historical default: ', ('Yes', 'No'))

    if person_default_on_file == 'Yes':
        cb_person_default_on_file = 1
    else:
        cb_person_default_on_file = 0


    loan_grade = st.sidebar.radio('Loan grade: ', ('A', 'B', 'C', 'D', 'E', 'F', 'G'))

    if person_home_ownership == 'Mortgage':
        person_home_ownership_Mortgage = 1
        person_home_ownership_Other = 0
        person_home_ownership_Own = 0
        person_home_ownership_Rent = 0

    if person_home_ownership == 'Other':
        person_home_ownership_Mortgage = 0
        person_home_ownership_Other = 1
        person_home_ownership_Own = 0
        person_home_ownership_Rent = 0

    if person_home_ownership == 'Own':
        person_home_ownership_Mortgage = 0
        person_home_ownership_Other = 0
        person_home_ownership_Own = 1
        person_home_ownership_Rent = 0

    if person_home_ownership == 'Rent':
        person_home_ownership_Mortgage = 0
        person_home_ownership_Other = 0
        person_home_ownership_Own = 0
        person_home_ownership_Rent = 1

    if loan_intent == 'Homeimprovement':
        loan_intent_Homeimprovement = 1
        loan_intent_Venture = 0
        loan_intent_Personal = 0
        loan_intent_Medical = 0
        loan_intent_Education = 0
        loan_intent_Debtconsolidation = 0

    if loan_intent == 'Venture':
        loan_intent_Homeimprovement = 0
        loan_intent_Venture = 1
        loan_intent_Personal = 0
        loan_intent_Medical = 0
        loan_intent_Education = 0
        loan_intent_Debtconsolidation = 0

    if loan_intent == 'Personal':
        loan_intent_Homeimprovement = 0
        loan_intent_Venture = 0
        loan_intent_Personal = 1
        loan_intent_Medical = 0
        loan_intent_Education = 0
        loan_intent_Debtconsolidation = 0

    if loan_intent == 'Medical':
        loan_intent_Homeimprovement = 0
        loan_intent_Venture = 0
        loan_intent_Personal = 0
        loan_intent_Medical = 1
        loan_intent_Education = 0
        loan_intent_Debtconsolidation = 0

    if loan_intent == 'Education':
        loan_intent_Homeimprovement = 0
        loan_intent_Venture = 0
        loan_intent_Personal = 0
        loan_intent_Medical = 0
        loan_intent_Education = 1
        loan_intent_Debtconsolidation = 0

    if loan_intent == 'Debtconsolidation':
        loan_intent_Homeimprovement = 0
        loan_intent_Venture = 0
        loan_intent_Personal = 0
        loan_intent_Medical = 0
        loan_intent_Education = 0
        loan_intent_Debtconsolidation = 1

    if loan_grade == 'A':
        loan_grade_A = 1
        loan_grade_B = 0
        loan_grade_C = 0
        loan_grade_D = 0
        loan_grade_E = 0
        loan_grade_F = 0
        loan_grade_G = 0

    if loan_grade == 'B':
        loan_grade_A = 0
        loan_grade_B = 1
        loan_grade_C = 0
        loan_grade_D = 0
        loan_grade_E = 0
        loan_grade_F = 0
        loan_grade_G = 0

    if loan_grade == 'C':
        loan_grade_A = 0
        loan_grade_B = 0
        loan_grade_C = 1
        loan_grade_D = 0
        loan_grade_E = 0
        loan_grade_F = 0
        loan_grade_G = 0

    if loan_grade == 'D':
        loan_grade_A = 0
        loan_grade_B = 0
        loan_grade_C = 0
        loan_grade_D = 1
        loan_grade_E = 0
        loan_grade_F = 0
        loan_grade_G = 0

    if loan_grade == 'E':
        loan_grade_A = 0
        loan_grade_B = 0
        loan_grade_C = 0
        loan_grade_D = 0
        loan_grade_E = 1
        loan_grade_F = 0
        loan_grade_G = 0

    if loan_grade == 'F':
        loan_grade_A = 0
        loan_grade_B = 0
        loan_grade_C = 0
        loan_grade_D = 0
        loan_grade_E = 0
        loan_grade_F = 1
        loan_grade_G = 0

    if loan_grade == 'G':
        loan_grade_A = 0
        loan_grade_B = 0
        loan_grade_C = 0
        loan_grade_D = 0
        loan_grade_E = 0
        loan_grade_F = 0
        loan_grade_G = 1


    predict_button = st.sidebar.button('Predict')

    st.sidebar.markdown("""&copy; Fabiano Manetti - 2022""", unsafe_allow_html=True)
