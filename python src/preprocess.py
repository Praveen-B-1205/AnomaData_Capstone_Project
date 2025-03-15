#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from data_loader import load_data


# In[2]:


def preprocess_data():
    """Cleans and preprocesses the dataset"""
    df = load_data()

    # Drop duplicate target column if exists
    if 'y.1' in df.columns:
        df = df.drop(columns=['y.1'])

    # Convert timestamp to datetime
    df["time"] = pd.to_datetime(df["time"])

    return df

if __name__ == "__main__":
    df = preprocess_data()
    print(df.info())  # Test preprocessing


# In[8]:


get_ipython().system('jupyter nbconvert --to script "preprocess.ipynb"')


# In[ ]:




