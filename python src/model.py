#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from preprocess import preprocess_data
import joblib


# In[2]:


def train_model():
    """Trains the Isolation Forest Model"""
    df = preprocess_data()
    X = df.drop(columns=["y", "time"])  # Drop target & timestamp
    y = df["y"]

    # Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Model
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(X_train)

    # Save Model
    joblib.dump(model, "models/model.pkl")

    # Predict & Evaluate
    y_pred = model.predict(X_test)
    y_pred = [1 if pred == -1 else 0 for pred in y_pred]

    print(classification_report(y_test, y_pred))
    return model

if __name__ == "__main__":
    model = train_model()


# In[ ]:




