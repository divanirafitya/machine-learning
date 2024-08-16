import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title='Diabetes Prediction - EDA',
    layout='wide',
    initial_sidebar_state='expanded')

def run():
    # create title/header
    st.title('Presence of Diabetes Predictions')
    # create subheader
    st.subheader('Exploratory Data Analysis for Diabetes')
    # add image
    st.image('https://www.semana.com/resizer/myYkqUMF4ALvGeNyXkSBZpIa3y4=/1200x675/filters:format(jpg):quality(50)//cloudfront-us-east-1.images.arcpublishing.com/semana/TGSRFRDSGFHNNHSIORXUALONLQ.jpg',
             caption='Presence of Diabetes Analysis')
    # add description
    st.write('### Problem Statement')
    st.write("Identify patients who may be at risk of developing diabetes based on the patient's medical history and minimizing a condition when the patient may have diabetes (testing positive) despite negative test results.")
    st.write('### Objective')
    st.write("Predict whether a patient is at risk of developing diabetes or not developing diabetes based on the patient's medical history to provide an appropriate treatment plan that suits each patient's condition.")
    st.markdown('---')

    # show dataframe
    df = pd.read_csv('diabetes_prediction_dataset.csv')

    # create submenu
    submenu = st.sidebar.selectbox('EDA Navigation',['Dataset','Percentage of Diabetes Presence','Gender by Diabetes Presence','Hypertension by Diabetes Presence','Heart Disease by Diabetes Presence','Smoking History by Diabetes Presence','BMI Category','HbA1c Level Category','Blood Sugar Level Category'])
    if submenu == 'Dataset':
        st.write('### Dataset')
        st.write('Simple exploration using the Diabetes Prediction Dataset taken from [Kaggle](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset/data)')
        st.dataframe(df)
        st.markdown('---')

    elif submenu == 'Percentage of Diabetes Presence':
        # create visualization 1
        st.write('### Percentage of Diabetes Presence')
        fig = plt.figure(figsize=(5,5))
        df['diabetes'].value_counts().plot(kind='pie',autopct='%.2f%%')
        plt.legend(labels=['0 = No Diabetes, 1 = Diabetes'])
        st.pyplot(fig)
        st.write("The difference between patients diagnosed with diabetes and without diabetes is very significant, with only 8.82 percent of the total patients having diabetes.")

    elif submenu == 'Gender by Diabetes Presence':
        # create visualization 2
        st.write('### Gender by Diabetes Presence')
        fig = plt.figure(figsize=(5,5))
        sns.countplot(x='gender', hue='diabetes', data=df)
        plt.legend(labels=['0 = No Diabetes', '1 = Diabetes'])
        st.pyplot(fig)
        st.write("Gender that dominates is Female for both patients with diabetes and without diabetes. This may indicate that the female gender has a greater risk of diabetes, which usually occurs after menopause due to hormonal changes.")

    elif submenu == 'Hypertension by Diabetes Presence':
        # create visualization 3
        st.write('### Hypertension by Diabetes Presence')
        fig = plt.figure(figsize=(10,6))
        sns.countplot(x='hypertension', hue='diabetes', data=df)
        plt.legend(labels=['0 = No Diabetes', '1 = Diabetes'])
        st.pyplot(fig)
        st.write("Less than half of the patients with hypertension have diabetes. This indicates that a patient can experience hypertension without having diabetes because hypertension occurs when blood pressure in the arteries continues to increase consistently. On the other hand, patients who have a history of diabetes tend to experience hypertension, which is caused by various factors such as genetics, unhealthy lifestyle, age, overweight or obesity, and environmental factors.")

    elif submenu == 'Heart Disease by Diabetes Presence':
        # create visualization 4
        st.write('### Heart Disease by Diabetes Presence')
        fig = plt.figure(figsize=(5,5))
        sns.countplot(x='heart_disease', hue='diabetes', data=df)
        plt.legend(labels=['0 = No Diabetes', '1 = Diabetes'])
        st.pyplot(fig)
        st.write("The majority of patients do not have a history of heart disease. This indicates that many patients with heart disease do not have diabetes. However, people with diabetes have a higher risk of developing heart disease compared to patients who do not have diabetes.")

    elif submenu == 'Smoking History by Diabetes Presence':
        # create visualization 5
        st.write('### Smoking History by Diabetes Presence')
        fig = plt.figure(figsize=(10,5))
        sns.countplot(x='smoking_history', hue='diabetes', data=df)
        plt.legend(labels=['0 = No Diabetes', '1 = Diabetes'])
        st.pyplot(fig)
        st.write("The majority of patients are included in the category of never smoking based on patients smoking history. This indicates that the majority of patients do not have a high risk for diabetes. This is because smoking can increase a person's risk of diabetes. After all, it can cause the body to become less responsive to the insulin produced (insulin resistance), which will increase the risk of diabetes.")

    elif submenu == 'BMI Category':
        # create visualization 6
        lists = []
        for i in df.bmi:
            bmi = float(i)
            if (bmi > 30):
                lists.append('Obesity')
            elif (25 <= bmi <= 30):
                lists.append('Overweight')
            elif (18.5 <= bmi < 25):
                lists.append('Normal')
            elif (bmi < 18.5):
                lists.append('Underweight')
        df['bmi_cat'] = lists
        st.write('### BMI Category')
        fig = plt.figure(figsize=(5,5))
        df.groupby('bmi_cat')['bmi'].count().plot(kind='bar')
        plt.legend()
        st.pyplot(fig)
        st.write("Many patients are included in the Overweight and Obesity categories based on body mass index (BMI). This indicates that patients in these two categories are at high risk for diabetes because excessive body fat can interfere with the body's ability to use insulin effectively (insulin resistance), which will increase the risk of diabetes.")

    elif submenu == 'HbA1c Level Category':
        # create visualization 7
        lists = []
        for i in df.HbA1c_level:
            HbA1c_level = float(i)
            if (HbA1c_level >= 6.5):
                lists.append('Diabetes')
            elif (5.7 <= HbA1c_level < 6.5):
                lists.append('Prediabetes')
            elif (HbA1c_level < 5.7):
                lists.append('Normal')
        df['HbA1c_level_cat'] = lists
        st.write('### HbA1c Level Category')
        fig = plt.figure(figsize=(5,5))
        df.groupby('HbA1c_level_cat')['HbA1c_level'].count().plot(kind='bar')
        plt.legend()
        st.pyplot(fig)
        st.write("Many patients are included in the prediabetes category based on the average blood sugar during the last 2-3 months of 5.7% - 6.4%, where this category has a high risk of diabetes. Although further examination by a doctor is needed, high HbA1c levels indicate a person has diabetes because it assesses long-term blood sugar control over the last 2-3 months.")
    
    elif submenu == 'Blood Sugar Level Category':
        # create visualization 8
        lists = []
        for i in df.blood_glucose_level:
            blood_glucose_level = float(i)
            if (blood_glucose_level > 125):
                lists.append('Diabetes')
            elif (100 <= blood_glucose_level <= 125):
                lists.append('Prediabetes')
            elif (blood_glucose_level < 100):
                lists.append('Normal')
        df['blood_glucose_level_cat'] = lists
        st.write('### Blood Sugar Level Category')
        fig = plt.figure(figsize=(5,5))
        df.groupby('blood_glucose_level_cat')['blood_glucose_level'].count().plot(kind='bar')
        plt.legend()
        st.pyplot(fig)
        st.write("Many patients are included in the diabetes category based on their blood sugar levels, which are above 125mg/dL. Although further examination by a doctor is needed, high blood sugar usually indicates the main symptom of someone suffering from diabetes.")

if __name__ == '__main__':
    run()