import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

# App title
st.title("💳 Fraud Detection Dashboard")

# Sidebar for navigation
menu = ["Home", "Predict", "Dataset"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Fraud Detection MVP")
    st.write("""
    This is a demo app for detecting fraudulent transactions using a trained Machine Learning model.  
    Navigate to **Predict** to test transactions, or **Dataset** to view sample data.
    """)

elif choice == "Dataset":
    st.subheader("📊 Sample Data")
    df = pd.read_csv("sample_data.csv")
    st.dataframe(df.head(20))  # show first 20 rows
    st.download_button("Download Dataset", df.to_csv(index=False), "sample_data.csv", "text/csv")

elif choice == "Predict":
    st.subheader("🔮 Predict Fraud")

    # Example: your dataset probably has features like Time, Amount, etc.
    # Add input fields for them here
    time = st.number_input("Transaction Time", min_value=0, max_value=100000)
    amount = st.number_input("Transaction Amount", min_value=0.0, format="%.2f")
    
    # Collect inputs into dataframe (adjust features according to your model training)
    features = pd.DataFrame([[time, amount]], columns=["Time", "Amount"])

    if st.button("Predict"):
        prediction = model.predict(features)[0]
        result = "🚨 Fraudulent Transaction" if prediction == 1 else "✅ Legitimate Transaction"
        st.success(result)
