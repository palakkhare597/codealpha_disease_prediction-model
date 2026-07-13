# ❤️ Heart Disease Prediction using Machine Learning

A Machine Learning-based web application that predicts the likelihood of heart disease using patient medical information. The project compares multiple classification algorithms, applies hyperparameter tuning using GridSearchCV, and deploys the best-performing model with Streamlit.

---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. This project aims to assist in early heart disease prediction by analyzing patient health parameters using supervised machine learning classification algorithms.

The application allows users to enter medical information through an interactive web interface and instantly predicts whether a patient is at risk of heart disease.

---

## 🚀 Features

- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Scaling using StandardScaler
- Multiple Classification Models
  - Decision Tree
  - Random Forest
  - XGBoost
- Hyperparameter Tuning using GridSearchCV
- Model Performance Comparison
- Feature Importance Visualization
- Confusion Matrix
- Classification Report
- ROC-AUC Score
- Interactive Streamlit Web Application
- Model Serialization using Joblib

---

## 📂 Dataset

**Dataset:** Heart Disease UCI Dataset

The dataset contains patient medical attributes such as:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- ST Depression
- Slope
- Number of Major Vessels
- Thalassemia

**Target Variable**

- 0 → No Heart Disease
- 1 → Heart Disease

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib
- Streamlit

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis
4. Feature Scaling
5. Train-Test Split
6. Model Training
7. Hyperparameter Tuning using GridSearchCV
8. Model Evaluation
9. Model Comparison
10. Feature Importance Analysis
11. Save Best Model
12. Streamlit Deployment

---

## 🤖 Machine Learning Models

- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier

The best model is selected based on evaluation metrics after GridSearchCV optimization.

---

## 📈 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix
- Classification Report

---

## 📁 Project Structure

```
Heart-Disease-Prediction/
│
├── app.py
├── train_model.py
├── heart.csv
├── disease_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── images/
    ├── confusion_matrix.png
    └── feature_importance.png
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Heart-Disease-Prediction.git
```

Move to the project directory

```bash
cd Heart-Disease-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📷 Application Preview

The application provides:

- Interactive patient input form
- Heart disease prediction
- Prediction probability
- Feature importance chart
- User-friendly interface

---

## 📊 Results

The models are compared using multiple evaluation metrics, and the best-performing model is selected after hyperparameter tuning.

Example comparison:

| Model | Accuracy |
|--------|----------|
| Decision Tree | 84.7% |
| Random Forest | 91.5% |
| XGBoost | 93.8% |

*(Results may vary depending on dataset version and train-test split.)*

---

## 🔮 Future Enhancements

- Deep Learning Models
- SHAP Explainability
- PDF Prediction Report
- Batch Prediction using CSV Upload
- Cloud Deployment
- Integration with Electronic Health Records (EHR)

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---


