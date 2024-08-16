import pandas as pd
import numpy as np
import pickle
import streamlit as st

# load data from best model
with open('svm_gridcv_best.pkl', 'rb') as file_1:
    model = pickle.load(file_1)

def run():
    st.write('# Input Credit Card Holder Information')

    # create form to input information
    with st.form(key='Default Prediction'):
        
        # define all variables
        limit = st.number_input('Limit Balance',min_value=0,value=50000)
        
        st.write('## Personal Data')
        sex = st.selectbox('Gender',options=['Male','Female'],index=1)
        education = st.selectbox('Education Level',options=['Graduate School','University','High School','Others'],index=1)
        status = st.selectbox('Status',options=['Married','Single','Others'],index=1)
        age = st.number_input('Age',min_value=21,value=21)
        st.markdown('---')

        st.write('## Repayment Status')
        pay_0 = st.number_input('Repayment Status in September',min_value=0,value=50000)
        pay_2 = st.number_input('Repayment Status in August',min_value=0,value=50000)
        pay_3 = st.number_input('Repayment Status in July',min_value=0,value=50000)
        pay_4 = st.number_input('Repayment Status in June',min_value=0,value=50000)
        pay_5 = st.number_input('Repayment Status in May',min_value=0,value=50000)
        pay_6 = st.number_input('Repayment Status in April',min_value=0,value=50000)
        st.markdown('---')

        st.write('## Amount of bill statement')
        bill_amt_1 = st.number_input('Amount of bill statement in September',min_value=0,value=50000)
        bill_amt_2 = st.number_input('Amount of bill statement in August',min_value=0,value=50000) 
        bill_amt_3 = st.number_input('Amount of bill statement in July',min_value=0,value=50000)
        bill_amt_4 = st.number_input('Amount of bill statement in June',min_value=0,value=50000)
        bill_amt_5 = st.number_input('Amount of bill statement in May',min_value=0,value=50000) 
        bill_amt_6 = st.number_input('Amount of bill statement in April',min_value=0,value=50000) 
        st.markdown('---')

        st.write('## Amount of previous payment')
        pay_amt_1 = st.number_input('Amount of previous payment in September',min_value=0,value=50000)
        pay_amt_2 = st.number_input('Amount of previous payment in August',min_value=0,value=50000)
        pay_amt_3 = st.number_input('Amount of previous payment in July',min_value=0,value=50000)
        pay_amt_4 = st.number_input('Amount of previous payment in June',min_value=0,value=50000)
        pay_amt_5 = st.number_input('Amount of previous payment in May',min_value=0,value=50000)
        pay_amt_6 = st.number_input('Amount of previous payment in April',min_value=0,value=50000)

        # every form must have a submit button.
        submitted = st.form_submit_button('Predict')

    df_inf = {
        'limit_balance': limit,
        'sex': sex,
        'education_level': education,
        'marital_status': status,
        'age': age,    
        'pay_0': pay_0,
        'pay_2': pay_2,
        'pay_3': pay_3,
        'pay_4': pay_4,
        'pay_5': pay_5,
        'pay_6': pay_6,
        'bill_amt_1': bill_amt_1,
        'bill_amt_2': bill_amt_2,
        'bill_amt_3': bill_amt_3,
        'bill_amt_4': bill_amt_4,
        'bill_amt_5': bill_amt_5,
        'bill_amt_6': bill_amt_6,
        'pay_amt_1': pay_amt_1,
        'pay_amt_2': pay_amt_2,
        'pay_amt_3': pay_amt_3,
        'pay_amt_4': pay_amt_4,
        'pay_amt_5': pay_amt_5,
        'pay_amt_6': pay_amt_6
    }

    df_inf = pd.DataFrame([df_inf])
    st.dataframe(df_inf)

    # prediction with best model
    if submitted:
        result= model.predict(df_inf)
        for i in result:
            if i == 0:
                st.write('## Customer kemungkinan diprediksi akan berhasil membayar tagihan kartu kredit bulan berikutnya.')
            else:
                st.write('## Customer kemungkinan diprediksi tidak dapat membayar tagihan kartu kredit bulan berikutnya.')
        st.balloons()

if __name__ == '__main__':
   run()