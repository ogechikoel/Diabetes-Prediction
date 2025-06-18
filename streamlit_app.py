import streamlit as st
import pickle as pkl
import pandas as pd

# Load the trained decision tree model
model = pkl.load(open("decision_trees_diabetes_pima.sav", "rb"))

# Sidebar navigation
page = st.sidebar.radio("Choose A Page:", ["Home", "Prediction", "Disclaimer"])

# Home Page
if page == "Home":
    st.title("Welcome to Diabetes Screening Test")
    st.subheader("🔍 About the App")

    st.markdown("""
    This app uses a Decision Tree classifier trained on the **Pima Indians Diabetes dataset**.
    It helps users estimate their likelihood of having diabetes based on medical and personal data.
    """)
    
    st.info("👉 Go to the **Prediction** page from the sidebar to start your screening.")


# Prediction Page
elif page == "Prediction":
    st.title("Screening Test")

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age (years)", min_value=15, max_value=110, value=45)
        bp = st.number_input("Systolic Blood Pressure (mm Hg)", min_value=40, max_value=200, value=110)
        insulin = st.number_input("Insulin (μU/mL)", min_value=0, max_value=1000, value=60)
        pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=15, value=2)

    with col2:
        glucose = st.number_input("Glucose (mg/dL)", min_value=40, max_value=300, value=75)
        skin = st.number_input("Skin Thickness (mm)", min_value=1, max_value=100, value=30)
        bmi = st.number_input("BMI (kg/m²)", min_value=10.0, max_value=70.0, value=20.0)
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)

    # Predict Button
    if st.button("Predict Diabetes Status"):
        input_df = pd.DataFrame([{
            "pregnancies": pregnancies,
            "glucose": glucose,
            "bloodpressure": bp,
            "skinthickness": skin,
            "insulin": insulin,
            "bmi": bmi,
            "diabetespedigreefunction": dpf,
            "age": age
        }])

        prediction = model.predict(input_df)
        proba = model.predict_proba(input_df)[0][1]

        #probabilities
        if prediction[0] == 1:
            result = f"Diabetic --Confidence: {proba*100:.2f}%"
            st.error(result)
        else:
            result = f"✅ Not Diabetic — Confidence: {proba*100:.2f}%"
            st.success(result)

elif page == "Disclaimer":
    st.subheader("⚠️ Disclaimer")
    st.markdown(""" This app is for **educational purposes only** and should not be used as a 
    substitute for professional medical advice, diagnosis, or treatment.""")
    


            
