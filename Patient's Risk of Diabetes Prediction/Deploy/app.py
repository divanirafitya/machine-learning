import streamlit as st
import eda
import predict

st.sidebar.markdown('# About')
st.sidebar.write('''Click here to see Exploratory Data Analysis for Diabetes and Presence of Diabetes Predictions''')

navigation = st.sidebar.selectbox('Navigation',['EDA','Diabetes Prediction'])

if navigation == 'EDA':
    eda.run()
else:
    predict.run()