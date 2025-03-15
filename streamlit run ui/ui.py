#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
import joblib


# In[2]:


# Load model
model = joblib.load("models/model.pkl")

# Streamlit UI setup
st.title("AnomaData: Anomaly Detection System")
st.write("Enter sensor values to detect anomalies in real-time.")

# Dynamic feature input fields
num_features = 60  # Adjust based on dataset features
input_data = []
for i in range(num_features):
    value = st.number_input(f"Feature {i+1}", value=0.0, step=0.01)
    input_data.append(value)

# Predict anomaly
if st.button("Detect Anomaly"):
    features = np.array(input_data).reshape(1, -1)
    prediction = model.predict(features)
    result = "🔴 Anomaly Detected!" if prediction[0] == -1 else "🟢 Normal Operation"
    st.subheader(f"Prediction: {result}")


# In[ ]:




