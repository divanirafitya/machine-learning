import pandas as pd
import numpy as np
import pickle
import streamlit as st

# load data from best model
with open('rf_gridcv_best.pkl', 'rb') as file_1:
    model = pickle.load(file_1)

def run():
    st.write('# Input Patient Information')

    # create form to input information
    with st.form(key='Diabetes Prediction'):
        
        # define all variables        
        st.write('## Demographic Information')
        gender = st.selectbox('Gender',options=['Female','Male','Others'],index=0)
        age = st.number_input('Age',min_value=0,value=30)
        st.markdown('---')

        st.write('## Medical History')
        hypertension = st.selectbox('Hypertension',options=['No','Yes'],index=0)
        if hypertension == 'No':
            hypertension = 0
        else:
            hypertension = 1
        heart_disease = st.selectbox('Heart Disease',options=['No','Yes'],index=0)
        if hypertension == 'No':
            heart_disease = 0
        else:
            heart_disease = 1
        smoking_history = st.selectbox('Smoking History',options=['Not Current','Former','Current','Never','Ever'],index=0)
        bmi = st.number_input('Body Mass Index',min_value=10,max_value=100,value=20)
        HbA1c_level = st.number_input('HbA1c Level',min_value=0,max_value=10,value=5)
        blood_glucose_level = st.number_input('Blood Sugar Level',min_value=0,max_value=100,value=20)
        st.markdown('---')

        # every form must have a submit button.
        submitted = st.form_submit_button('Predict')

    df_inf = {
        'gender': gender,
        'age': age,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'smoking_history': smoking_history,
        'bmi': bmi,
        'HbA1c_level': HbA1c_level,
        'blood_glucose_level': blood_glucose_level
    }

    df_inf = pd.DataFrame([df_inf])
    st.dataframe(df_inf)

    # prediction with best model
    if submitted:
        result= model.predict(df_inf)
        for i in result:
            if i == 0:
                st.write('## Patient has no risk of developing diabetes.')
            else:
                st.write('## Patient may be at risk of developing diabetes.')
        st.balloons()

if __name__ == '__main__':
   run()