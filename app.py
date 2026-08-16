import streamlit as st
import pandas as pd
import joblib


model = joblib.load("heart_model.pkl")


st.set_page_config(
    page_title="Heart Disease Predictor",
    layout="centered"
)



st.title("Heart Disease Predictor")

st.write(
    "Enter the patient's information below to get a "
    "machine-learning prediction."
)


col1, col2 = st.columns(2)


with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=50
    )

    resting_bp = st.number_input(
        "Resting Blood Pressure",
        min_value=50,
        max_value=250,
        value=120
    )

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=0,
        max_value=600,
        value=200
    )

    fasting_bs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dl?",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    max_hr = st.number_input(
        "Maximum Heart Rate",
        min_value=50,
        max_value=250,
        value=150
    )

    oldpeak = st.number_input(
        "Oldpeak",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1
    )


with col2:

    sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )

    chest_pain = st.selectbox(
        "Chest Pain Type",
        ["ATA", "NAP", "TA", "ASY"]
    )

    resting_ecg = st.selectbox(
        "Resting ECG",
        ["Normal", "ST", "LVH"]
    )

    exercise_angina = st.selectbox(
        "Exercise Induced Angina",
        ["Yes", "No"]
    )

    st_slope = st.selectbox(
        "ST Slope",
        ["Flat", "Up", "Down"]
    )



input_data = pd.DataFrame({
    "Age": [age],
    "Sex": [sex],
    "ChestPainType": [chest_pain],
    "RestingBP": [resting_bp],
    "Cholesterol": [cholesterol],
    "FastingBS": [fasting_bs],
    "RestingECG": [resting_ecg],
    "MaxHR": [max_hr],
    "ExerciseAngina": [exercise_angina],
    "Oldpeak": [oldpeak],
    "ST_Slope": [st_slope]
})



if st.button("Predict", type="primary"):

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]


    st.divider()

    st.subheader("Prediction Result")


    if prediction == 1:

        st.error(
            " Higher likelihood of heart disease"
        )

    else:

        st.success(
            "Lower likelihood of heart disease"
        )


    st.metric(
        "Estimated Probability",
        f"{probability * 100:.2f}%"
    )

    st.progress(float(probability))


    with st.expander("View Input Data"):
        st.dataframe(input_data)