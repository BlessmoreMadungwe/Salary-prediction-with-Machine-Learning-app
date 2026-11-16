import streamlit as st
import pickle
import pandas as pd
from pathlib import Path


def load_model():
    with open(Path(__file__).with_name('saved_steps.pkl'), 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = le_education.classes_.tolist()

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)

    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        X = pd.DataFrame({
            "Country": le_country.transform([country]),
            "EdLevel": le_education.transform([education]),
            "YearsCodePro": [float(experience)],
        })

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")


if __name__ == "__main__":
    show_predict_page()
