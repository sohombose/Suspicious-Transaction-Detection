# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
from google.colab import files

# Load the dataset
print("Loading dataset...")
df = pd.read_csv('creditcard.csv')
print(f"Dataset loaded with shape: {df.shape}")

# Explore the data
print("\nDataset Overview:")
print(df.info())
print("\nClass Distribution:")
print(df['Class'].value_counts())
print(f"Fraud percentage: {df['Class'].mean()*100:.4f}%")

# Prepare data for modeling
X = df.drop('Class', axis=1)
y = df['Class']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTraining set: {X_train.shape}")
print(f"Test set: {X_test.shape}")

# Initialize and train Random Forest model
print("\nTraining Random Forest model...")
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight='balanced',
    n_jobs=-1
)

model.fit(X_train, y_train)
print("Model training completed!")

# Evaluate the model
y_pred = model.predict(X_test)

print("\nModel Performance:")
print("Accuracy: {:.4f}".format(accuracy_score(y_test, y_pred)))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the model and sample data
joblib.dump(model, 'model.pkl')
print("Model saved as 'model.pkl'")

# Create sample data for demonstration
sample_data = X_test.head(50)
sample_data.to_csv('sample_data.csv', index=False)
print("Sample data saved as 'sample_data.csv'")

# Download the files
files.download('model.pkl')
files.download('sample_data.csv')

print("\nImplementation complete! Files are ready for your Streamlit dashboard.")
