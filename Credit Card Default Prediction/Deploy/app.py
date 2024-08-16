import streamlit as st
import eda
import predict

st.sidebar.markdown('# About')
st.sidebar.write('''Click here to see Exploratory Data Analysis and Credit Card Default Predictions''')

navigation = st.sidebar.selectbox('Navigation',['EDA','Predict Credit Card Default'])

if navigation == 'EDA':
    eda.run()
else:
    predict.run()