# AnomaData: Automated Anomaly Detection for Predictive Maintenance

👤 **Developed by: Praveen B**

## 📌 Project Overview

AnomaData is an automated machine learning-based anomaly detection system designed to help industries predict equipment failures before they happen. By analyzing sensor data, the system detects anomalies and alerts users to potential issues, improving maintenance efficiency and reducing downtime.

This project leverages machine learning techniques to identify patterns and predict potential breakdowns.

## Features
- **Data Preprocessing**: Cleans and prepares raw sensor data.
- **Anomaly Detection**: Uses machine learning models to identify outliers.
- **Predictive Maintenance**: Predicts potential failures before they occur.
- **Visualization**: Generates reports and dashboards for monitoring.
- **Automation**: Runs periodically with minimal human intervention.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Jupyter Notebook (optional for development)
- Required Python libraries (install using the command below)

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Dataset
- The dataset (AnomaData.xlsx) contains sensor readings from industrial equipment.
- Columns include timestamps, sensor values, and operational status.
- Duplicate and missing values should be handled during preprocessing.

## Steps to Run the Project
1. **Data Preprocessing**
   - Load and clean the dataset.
   - Handle missing and duplicate values.
   - Normalize sensor readings.
2. **Exploratory Data Analysis (EDA)**
   - Visualize trends and distributions.
   - Identify potential anomalies using statistical methods.
3. **Model Training**
   - Use algorithms like Isolation Forest, Autoencoder, or One-Class SVM.
   - Train on historical data and fine-tune hyperparameters.
4. **Anomaly Detection**
   - Apply the trained model to new data.
   - Label anomalies based on threshold values.
5. **Visualization and Reporting**
   - Generate anomaly reports.
   - Create dashboards using Matplotlib/Seaborn.
6. **Automation**
   - Schedule periodic anomaly detection.
   - Implement real-time monitoring (if applicable).

## Usage
Run the following command to start anomaly detection:
```bash
python main.py
```
For Jupyter Notebook:
```bash
jupyter notebook AnomaData.ipynb
```

## Output
- CSV file with detected anomalies.
- Visual reports highlighting anomalies.

## Dataset Information📊

•	Rows: 18,398  
•	Columns: 62  
•	Features: x1 to x60 (sensor readings), time (timestamp)  
•	Target Variable (y):   
   0 = Normal Operation  
   1 = Anomaly (Failure Detected)  

## Model Performance📈

•	Accuracy: 94.97%
•	Anomaly Recall: 48% (Imbalanced dataset challenge)
•	Further Improvements Needed: Hyperparameter tuning, Deep Learning models

## Future Enhancements
- Integrate real-time streaming data.
- Improve model accuracy using deep learning techniques.
- Deploy as a web application.


🛠️ Skills & Technologies Used

Machine Learning: Isolation Forest for anomaly detection

Data Science: Data preprocessing, feature engineering, EDA

Model Deployment: Flask API for real-time anomaly detection

Web Application: Streamlit UI for interactive visualization

Data Handling: Pandas, NumPy, Matplotlib, Seaborn

🛠️ Tools Used

✅ Python 🐍

✅ Flask 🌐

✅ Streamlit 📊

✅ Scikit-learn 🤖

✅ Pandas & NumPy 📊

✅ Matplotlib & Seaborn 📉

✅ Git & GitHub 🛠️

Visualizations to understand data distributions and anomalies

![image](https://github.com/user-attachments/assets/a9a814e4-0371-4271-a8b0-7ce841308925)


![image](https://github.com/user-attachments/assets/2bd703fd-3dd6-45ce-a66e-e224eb93b4ce)


Exploratory Data Analysis (EDA) Results

1️⃣ Anomaly Distribution: The dataset is imbalanced, with fewer anomalies (y=1). This might require resampling techniques.

2️⃣ Feature Correlation: Some features show strong correlation with anomalies, helping in feature selection.



## Contributor
- Praveen B

For queries, contact: praveen.vjrocks@gmail.com

