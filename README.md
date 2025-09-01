# Suspicious-Transaction-Detection

🚨 Suspicious Transaction Detection

This project is a Machine Learning Web Application built using Python, Streamlit, and scikit-learn to detect suspicious/fraudulent financial transactions. It allows users to explore datasets, train/load models, and predict fraud in real time through an interactive dashboard.

📌 Table of Contents

Project Overview

Features

Folder Structure

Setup Instructions

How to Run

Usage Guide

Dataset Information

Model Information

Screenshots

Contributing

License

📖 Project Overview

Financial fraud, especially in credit card and digital transactions, is a rising global challenge.
This project demonstrates a suspicious transaction detection system using a machine learning model trained on transaction datasets.

The dashboard has three major sections:

🏠 Home Page → Introduction & navigation.

📊 Dataset Viewer → Displays sample transaction data.

🤖 Fraud Prediction → Takes transaction details as input and predicts whether it’s Fraudulent or Genuine.

✨ Features

🏠 Home Page → Project overview & navigation.

📊 Dataset Viewer → Explore financial transaction data.

🔎 Suspicious Transaction Prediction → Input transaction details → get fraud probability.

⚡ Pre-trained Model → Stored in model.pkl for instant predictions.

🛠 Training Script → Train your own model with train_model.py.

📂 Folder Structure
STAH/
│── app.py              # Main Streamlit dashboard  
│── creditcard.csv      # Dataset (Kaggle Credit Card Fraud Dataset)  
│── model.pkl           # Saved trained ML model  
│── sample_data.csv     # Sample transaction records  
│── train_model.py      # Script to train model  
│── README.md           # Documentation  

⚙️ Setup Instructions

Clone the Repository

git clone https://github.com/sohombose/suspicious-transaction-detection.git
cd suspicious-transaction-detection


Create Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows


Install Dependencies

pip install -r requirements.txt


(If you don’t have requirements.txt, install manually:)

pip install streamlit scikit-learn pandas numpy

▶️ How to Run

Run the Streamlit app:

streamlit run app.py


Then open the link displayed in the terminal (usually http://localhost:8501/).

🖥 Usage Guide

Home Page → Learn about the project.

Dataset Page → View sample dataset (creditcard.csv).

Prediction Page → Enter transaction details → Model predicts:

✅ Genuine Transaction

🚨 Suspicious/Fraudulent Transaction

📊 Dataset Information

Source: Kaggle – Credit Card Fraud Detection Dataset

Total Transactions: 284,807

Fraudulent Transactions: 492 (0.17%) → Imbalanced dataset

Features: Time, V1…V28, Amount, Class (0=Genuine, 1=Fraud)

🧠 Model Information

Algorithm used: Logistic Regression / Random Forest / (based on your training script)

Trained on imbalanced dataset → Resampling/SMOTE applied

Model exported as model.pkl for fast loading in app.py

📸 Screenshots


<img width="1919" height="898" alt="Image" src="https://github.com/user-attachments/assets/e2debb53-c3a8-4ebe-8db9-82668f5c4bd9" />

<img width="1917" height="900" alt="Image" src="https://github.com/user-attachments/assets/c6d7a919-8524-4a41-9fcb-53e1f6610773" />

<img width="1919" height="890" alt="Image" src="https://github.com/user-attachments/assets/7dd134c3-2e04-4ec6-9ea2-59fe96e56542" />


🤝 Contributing

Contributions are welcome! 🎉

Fork the repo

Create a new branch (feature-new)

Commit changes

Open a Pull Request

📜 License

This project is licensed under the MIT License.
