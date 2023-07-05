import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the model
diabetes_model = pickle.load(open('/Users/shreyamahajan/Desktop/DS Project/diabetes_model.sav','rb'))

#sidebar for navigate
with st.sidebar:
    selected = option_menu("Diabetes Prediction",
    ['Diabetes Prediction'],
    default_index=0)

if (selected == 'Diabetes Prediction'):
    #page title
    st.title("Diabetes Prediction using ML")
    #getting the input data from user
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('BloodPressure value')
    with col1:
        SkinThickness = st.text_input('SkinThickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')

        #code for prediction
        diabetes_diagnosis = ''

        #creating a button for prediction
        if st.button('Diabetes Test Result'):
            diabetes_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

            if(diabetes_prediction[0]==1):
                diabetes_diagnosis = 'The Person is Diabetic'
            else:
                diabetes_diagnosis = 'The Person is Non-Diabetic'
        st.success(diabetes_diagnosis)
