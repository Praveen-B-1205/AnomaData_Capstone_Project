#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

def load_data(file_path="data/AnomaData.xlsx"):
    """Loads dataset and returns DataFrame"""
    df = pd.read_excel(file_path, engine="openpyxl")
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())  # Test the function


# In[ ]:





# In[ ]:




