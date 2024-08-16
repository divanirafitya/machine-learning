import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title='Crefit Card - EDA',
    layout='wide',
    initial_sidebar_state='expanded')

def run():
    # create title/header
    st.title('Credit Card Default Predictions')
    # create subheader
    st.subheader('Exploratory Data Analysis for Credit Card Default')
    # add image
    st.image('https://imgx.sonora.id/crop/0x0:0x0/700x465/photo/2023/02/08/edukatips-rentetankartubanyakjp-20230208043054.jpeg',
             caption='Credit Card Default Analysis')
    # add description
    st.write('### Problem Statement')
    st.write('Meminimalisir penolakan transaksi yang sah dan tidak terdeteksinya transaksi curang yang dilakukan secara tidak sah untuk mengurangi kerugian bank.')
    st.write('### Objective')
    st.write('Memprediksi apakah customer dapat membayar tagihan kartu kredit (No Default) atau gagal bayar (Default) di bulan berikutnya dengan menilai kemampuan customer dalam membayar pinjaman kartu kredit di bulan tersebut sebelum memberikan pinjaman.')
    st.markdown('---')

    # show dataframe
    df = pd.read_csv('P1G5_Set_1_divani.csv')
    st.write('### Dataset')
    st.write('Eksplorasi sederhana dengan menggunakan Credit Card Default Dataset yang diambil dari [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=ml_datasets&t=credit_card_default&page=table&project=gc-5-credit-card&ws=!1m5!1m4!4m3!1sbigquery-public-data!2sml_datasets!3scredit_card_default)')
    st.dataframe(df)
    st.markdown('---')

    # create visualization 1
    st.write('### Percentage of Default Credit Card Payment')
    fig = plt.figure(figsize=(5,5))
    df['default_payment_next_month'].value_counts().plot(kind='pie', autopct='%.2f%%')
    plt.legend(['0 = No Default','1 = Default'])
    st.pyplot(fig)

    # create visualization 2
    st.write('### Percentage of Marital Status')
    df['marital_status'] = df['marital_status'].replace(0,3)
    fig = plt.figure(figsize=(5,5))
    df['marital_status'].value_counts().plot(kind='pie', autopct='%.2f%%')
    plt.legend(['2 = Single','1 = Married','3 = Others'])
    st.pyplot(fig)
    
    # create visualization 3
    st.write('### Education Level')
    df['education_level'] = df['education_level'].replace([0,5,6],4)
    fig = plt.figure(figsize=(10,6))
    df['education_level'].value_counts().plot(kind='bar')
    plt.legend(labels=['1 = Graduate School, 2 = University, 3 = High School, 4 = Others'])
    st.pyplot(fig)

    # create visualization 4
    st.write('### Age')
    fig = plt.figure(figsize=(10,6))
    df['age'].value_counts().plot(kind='bar')
    st.pyplot(fig)

    # create visualization 5
    st.write('### Distribution of Limit Balance')
    fig = plt.figure(figsize=(10,6))
    sns.histplot(df['limit_balance'], bins=30, kde=True)
    st.pyplot(fig)

    # create visualization 6
    st.write('### Distribution of Limit Balance by Default Payment Next Month')
    fig = plt.figure(figsize=(10,6))
    sns.barplot(data=df,x='default_payment_next_month',y='limit_balance')
    plt.legend(labels=['0 = No, 1 = Yes'])
    st.pyplot(fig)

    # create visualization 7
    st.write('### Default Payment Next Month by Sex')
    fig = plt.figure(figsize=(10,6))
    sns.countplot(data=df,x='sex', hue='default_payment_next_month')
    plt.legend(title='Default Payment Next Month', labels=['No', 'Yes'])
    st.pyplot(fig)
    
    
if __name__ == '__main__':
    run()