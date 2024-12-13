# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 21:59:36 2024

@author: vijayalakshmi
"""

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Genetic Disorder",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

genetic_disorder_model = pickle.load(open('./genetic_disorder_prediction.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Genetic Disorder Prediction System',

                           ['Genetic Disorder Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity'],
                           default_index=0)


# Genetic Disorder Prediction Page
if selected == "Genetic Disorder Prediction":

    # page title
    st.title("Genetic Disorder Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        a1 = st.text_input('White Blood cell count (thousand per microliter)')

    with col2:
        a2 = st.text_input('Blood cell count (mcL)')

    with col3:
        a3 = st.text_input('Patient Age')

    with col1:
        a4 = st.text_input("Father's age")

    with col2:
        a5 = st.text_input("Mother's age")

    with col3:
        a6 = st.text_input('No. of previous abortion')

    with col1:
        a7 = st.text_input('Blood test result')

    with col2:
        a8 = st.text_input('Gender')

    with col3:
        a9 = st.text_input('Birth asphyxia')

    with col1:
        a10 = st.text_input('Symptom 5')

    with col2:
        a11 = st.text_input('Heart Rate (rates/mins)')

    with col3:
        a12 = st.text_input('Respiratory Rate (breaths/mins)')

    with col1:
        a13 = st.text_input('Folic acid details (peri-conceptional)')

    with col2:
        a14 = st.text_input('History of anomalies in previous pregnancies')

    with col3:
        a15 = st.text_input('Autopsy shows birth defect (if applicable)')

    with col1:
        a16 = st.text_input('Assisted conception IVF/ART')

    with col2:
        a17 = st.text_input('Symptom 4')

    with col3:
        a18 = st.text_input('Follow-up')

    with col1:
        a19 = st.text_input('Birth defects')
    # code for Prediction
    genetic_disorder = ''
    prediction1=''
    prediction2=''

    # creating a button for Prediction    
    if st.button("Genetic Disorder Test Result"):

        user_input = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,
                      a12,a13,a14,a15,a16,a17,a18,a19]

        user_input = [float(x) for x in user_input]

        prediction = genetic_disorder_model.predict([user_input])

        #if genetic_disorder[0][0] == 1:
         #   genetic_disorder = "The person has Parkinson's disease"
        #else:
            #genetic_disorder = "The person does not have Parkinson's disease"
        if(prediction[0][0]==0):
            prediction1='Mitochondrial genetic inheritance disorders'
        elif(prediction[0][0]==1):
            prediction1='Multifactorial genetic inheritance disorders'
        elif(prediction[0][0]==2):
            prediction1='Single-gene inheritance diseases'
        else:
           prediction1='Other genetic disorders'

        #print("Disorder Subclass - ",end=" ")
        if(prediction[0][1]==1):
            prediction2='Cancer'
        elif(prediction[0][1]==2):
            prediction2='Cystic fibrosis'
        elif(prediction[0][1]==3):
            prediction2='Diabetes'
        elif(prediction[0][1]==4):
            prediction2='Hemochromatosis'
        elif(prediction[0][1]==5):
            prediction2='Leber\'s hereditary optic neuropathy'
        elif(prediction[0][1]==6):
            prediction2='Leigh syndrome'
        elif(prediction[0][1]==7):
            prediction2='Mitochondrial myopathy'
        elif(prediction[0][1]==8):
            prediction2='Tay-Sachs'
        elif(prediction[0][1]==9):
            prediction2='Rheumatoid arthritis'
        else:
            prediction2='Other Disorder Subclass'
    st.write("Genetic Disorder - ",end="")
    st.success(prediction1)
    st.write("Disorder Subclass - ")
    st.success(prediction2)
