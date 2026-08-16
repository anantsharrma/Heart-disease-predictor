# Heart Disease Prediction

Deployed at:- https://heart-disease-predictorgit-auqzy2s99ubuwemnj9xvi9.streamlit.app/

A machine learning web application that predicts the likelihood of heart disease from patient health and clinical measurements.

The project compares multiple classification algorithms, evaluates them using **Accuracy and F1 Score**, and deploys the best-performing model through a **Streamlit** interface.

> **Note:** This project is intended for educational and demonstration purposes. It is not a medical diagnostic tool.

---

Features

* Exploratory data preprocessing for heart disease data
* Numerical feature imputation and standardization
* Categorical feature encoding using One-Hot Encoding
* Comparison of multiple classification algorithms
* Evaluation using:

  * Accuracy
  * F1 Score
* Scikit-learn `Pipeline` and `ColumnTransformer` for consistent preprocessing
* Trained model saved using `joblib`
* Interactive Streamlit web interface
* Prediction probability using Logistic Regression


 Machine Learning Models

The following classification models are evaluated:

| Model                  | Type                      |
| ---------------------- | ------------------------- |
| Logistic Regression    | Linear classifier         |
| K-Nearest Neighbors    | Instance-based classifier |
| Decision Tree          | Tree-based classifier     |
| Gaussian Naive Bayes   | Probabilistic classifier  |
| Support Vector Machine | Margin-based classifier   |
| Random Forest          | Ensemble classifier       |

Each model uses the **same preprocessing pipeline and train/test split**, making the comparison more consistent.

---

## Preprocessing

The raw dataset contains both numerical and categorical features.

### Numerical features

* Age
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Maximum Heart Rate
* Oldpeak

Numerical preprocessing:

```text
Missing values
      ↓
Median Imputation
      ↓
StandardScaler
```

### Categorical features

* Sex
* Chest Pain Type
* Resting ECG
* Exercise Angina
* ST Slope

Categorical preprocessing:

```text
Categorical values
      ↓
One-Hot Encoding
      ↓
Drop first category
```

The preprocessing is implemented using `ColumnTransformer` and `Pipeline`.

---

##  Model Pipeline

Instead of manually preprocessing data before prediction, the project combines preprocessing and the classifier into a single Scikit-learn pipeline:

```text
Raw Patient Data
       ↓
ColumnTransformer
       ↓
 ┌───────────────┐
 │               │
Numerical      Categorical
 │               │
Imputer        Imputer
 │               │
Scaler         OneHotEncoder
 │               │
 └───────┬───────┘
         ↓
   Classification
       Model
         ↓
    Prediction
```

This ensures that the exact same preprocessing learned during training is applied when new patient data is submitted through the application.

---

##  Model Evaluation

The models are evaluated using Accuracy and F1 Score.

Example comparison:

| Model               | Accuracy | F1 Score |
| ------------------- | -------: | -------: |
| Logistic Regression |   86.96% |   88.46% |
| KNN                 |   86.41% |   88.26% |
| Decision Tree       |   79.89% |   81.77% |
| Naive Bayes         |   84.78% |   86.14% |
| SVM                 |   84.24% |   86.26% |
| Random Forest       |   86.41% |   88.15% |

> Results depend on the train/test split, preprocessing, and model configuration.

For this experiment, **Logistic Regression achieved the highest F1 score** and was selected as the final model.

---

##  Streamlit Application

The trained pipeline is saved as:

```text
heart_model.pkl
```

The Streamlit application loads this pipeline and accepts raw patient information.

```text
User Input
    ↓
Streamlit
    ↓
Saved ML Pipeline
    ↓
Preprocessing
    ↓
Logistic Regression
    ↓
Prediction + Probability
```

Because preprocessing is included inside the saved pipeline, the Streamlit application does not need to manually perform One-Hot Encoding or feature scaling.

---

##  Project Structure

```text
Heart_disease_predictor/
│
├── app.py
├── heart_model.pkl
├── heart_disease_prediction.ipynb
├── requirements.txt
└── README.md
```

### Important files

**`app.py`**

Streamlit application responsible for collecting user input and generating predictions.

**`heart_model.pkl`**

Serialized Scikit-learn pipeline containing:

* Numerical preprocessing
* Categorical preprocessing
* Logistic Regression model

**`heart_disease_prediction.ipynb`**

Notebook containing data preprocessing, model training, evaluation, and model selection.

---

## Key Concepts Demonstrated

This project demonstrates practical use of:

* Exploratory Data Analysis
* Data preprocessing
* Missing-value imputation
* One-Hot Encoding
* Feature scaling
* Train/test splitting
* Classification
* Model comparison
* Accuracy
* F1 Score
* Scikit-learn Pipelines
* ColumnTransformer
* Model serialization
* Streamlit deployment



Interested in building practical AI-powered software systems.
