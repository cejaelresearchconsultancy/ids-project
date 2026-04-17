import streamlit as st
import joblib
import pandas as pd

model = joblib.load("ids_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

st.title("Lightweight Intrusion Detection System (IDS)")

input_data = {}
for feature in features:
    input_data[feature] = st.number_input(feature, value=0.0)

if st.button("Detect Intrusion"):

    input_df = pd.DataFrame([input_data])

    input_scaled = pd.DataFrame(
        scaler.transform(input_df),
        columns=features
    )

    pred = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    if pred == 1:
        st.error(f"🚨 Attack Detected (Confidence: {prob:.4f})")
    else:
        st.success(f"✅ Benign Traffic (Confidence: {1 - prob:.4f})")
