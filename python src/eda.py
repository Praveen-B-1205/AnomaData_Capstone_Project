#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import load_data


# In[ ]:


def perform_eda():
    """Performs Exploratory Data Analysis"""
    df = load_data()

    # Plot class distribution
    plt.figure(figsize=(6, 4))
    sns.countplot(x=df["y"], palette="viridis")
    plt.title("Anomaly Distribution")
    plt.show()

if __name__ == "__main__":
    perform_eda()  # Test EDA function


# In[ ]:




