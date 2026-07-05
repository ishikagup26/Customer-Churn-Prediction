import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "logistic_regression.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

st.title("📊 Customer Churn Prediction")

st.write(
    "Predict whether a telecom customer is likely to churn based on customer information."
)

st.write(
    "Predict whether a telecom customer is likely to churn based on customer information."
)

st.subheader("Customer Information")

col1, col2 = st.columns(2)