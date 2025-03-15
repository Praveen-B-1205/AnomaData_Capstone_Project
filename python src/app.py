#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, request, jsonify
import joblib
import numpy as np


# In[3]:


# Load model
model = joblib.load("models/model.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """Predicts whether input data is an anomaly"""
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        result = "Anomaly" if prediction[0] == -1 else "Normal"
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




