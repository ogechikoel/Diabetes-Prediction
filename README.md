# 🩺 Diabetes Prediction Tool

This project focuses on building a web-based application to predict diabetes using machine learning models. After evaluating multiple algorithms, the **Decision Tree Classifier** was selected as the best-performing model and deployed using **Streamlit**.

🔗 **Live App**: [Diabetes Prediction Tool](https://diabetes-prediction-72yqsvfdmtxa6xar2fcj5d.streamlit.app/)

---

## 📌 Objective

To develop a reliable machine learning model for predicting diabetes based on clinical and demographic data, and to deploy the best model in a user-friendly interface using Streamlit.

---

## 🧬 Features Used

The model was trained on the following features:

- **BMI** (Body Mass Index)  
- **Systolic Blood Pressure**  
- **Diabetes Pedigree Function**  
- **Age**  
- **Glucose Level**  
- **Number of Pregnancies**  
- **Insulin**  
- **Skin Thickness**  

---

## ⚙️ Model Performance Comparison

| Model               | Training Accuracy | Testing Accuracy | AUC Score |
|---------------------|-------------------|------------------|-----------|
| Decision Tree       | 0.80625           | 0.76623          | 0.78167   |
| Logistic Regression | 0.75000           | 0.75974          | 0.75963   |
| XGBoost             | 0.79875           | 0.74675          | 0.75815   |
| Random Forest       | 1.00000           | 0.76623          | 0.75185   |
| Support Vector      | 0.79750           | 0.74026          | 0.73185   |
| K-Nearest Neighbors | 0.86000           | 0.70130          | 0.70185   |
| Naive Bayes         | 0.74125           | 0.70130          | 0.69759   |

📌 **Best Model**: Decision Tree – selected based on a balance of accuracy and AUC.

---

## 🚀 Deployment

The app was developed using **Streamlit**, a Python framework for building interactive dashboards and web apps.

Access it here:  
👉 [https://diabetes-prediction-72yqsvfdmtxa6xar2fcj5d.streamlit.app/](https://diabetes-prediction-72yqsvfdmtxa6xar2fcj5d.streamlit.app/)

---

## 📂 Project Structure

```bash
📁 diabetes-prediction
├── README.md                           # Project documentation
├── diabetes-1.csv                      # The Diabetes dataset
├── diabetes_pima                       # Data Preprocessing and model training
├── requirements.txt                    # Dependencies
├── decision_trees_diabetes_pima.sav    # Trained Decision Tree Model
└── streamlit_app.py                    # Streamlit web app script
