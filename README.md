# 🎓 Student Performance Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)

A Machine Learning web application that predicts a student's **Math Score** based on demographic and academic information. The project is built using **Python, Scikit-Learn, Streamlit, and Machine Learning Pipelines**.

---

## 🚀 Live Demo

🔗 **Live Application:**  
**https://student-performance-ml-saif.streamlit.app/**

---

## 📌 Project Overview

This project predicts a student's **Math Score** using Machine Learning by considering factors such as:

- Gender
- Race / Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

The application performs data preprocessing, feature transformation, model prediction, and displays the predicted score through an interactive Streamlit interface.

---

## ✨ Features

- 📊 Interactive Streamlit Dashboard
- 🤖 Machine Learning Prediction
- ⚡ Fast Real-Time Prediction
- 📈 Data Preprocessing Pipeline
- 🎯 Predict Student Math Score
- 📱 Responsive User Interface
- 💾 Saved Model & Preprocessor
- 🛡 Custom Exception Handling
- 📝 Logging Support

---

## 🛠 Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- XGBoost
- CatBoost

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Web Framework

- Streamlit

### Model Serialization

- Pickle

---

## 📂 Project Structure

```text
STUD_PERF_ML
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   ├── test.csv
│   └── raw.csv
│
├── notebook/
│   ├── 1_EDA_STUDENT_PERFORMANCE.ipynb
│   └── 2_MODEL_TRAINING.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── ui/
│   ├── styles.py
│   ├── sidebar.py
│   ├── form.py
│   ├── prediction.py
│   └── footer.py
│
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ Machine Learning Workflow

```
Student Data
      │
      ▼
Data Ingestion
      │
      ▼
Data Transformation
      │
      ▼
Feature Engineering
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Model Saved (.pkl)
      │
      ▼
Prediction Pipeline
      │
      ▼
Streamlit Web App
```

---

## 🤖 Models Used

The following regression models were trained and evaluated:

- Linear Regression
- Lasso Regression
- Ridge Regression
- K-Neighbors Regressor
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

The model with the highest **R² Score** was automatically selected and saved.

---

## 📊 Input Features

| Feature | Type |
|----------|------|
| Gender | Categorical |
| Race / Ethnicity | Categorical |
| Parental Education | Categorical |
| Lunch Type | Categorical |
| Test Preparation Course | Categorical |
| Reading Score | Numerical |
| Writing Score | Numerical |

---

## 📈 Output

The application predicts:

- 🎯 Math Score
- 🏆 Student Grade
- 📊 Performance Percentage
- 💬 Performance Feedback

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Move into the project directory

```bash
cd STUD_PERF_ML
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
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

## 📸 Application Preview

### Home Page

*(Add a screenshot here)*

---

### Prediction Result

*(Add a screenshot here)*

---

## 🎯 Future Improvements

- User Authentication
- Database Integration
- Model Explainability (SHAP)
- Prediction History
- REST API using FastAPI
- Docker Deployment
- CI/CD Pipeline

---

## 👨‍💻 Author

**Saif Ali Khan**

Artificial Intelligence & Machine Learning Engineer

- 💼 LinkedIn: *https://www.linkedin.com/in/saif-ali-khan-ai/*
- 💻 GitHub: *https://github.com/SaifAK45*
- 📧 Email: *saifalikhan8050@gmail.com*

---

**Made with ❤️ using Python, Scikit-Learn & Streamlit**