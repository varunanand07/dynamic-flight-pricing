# backend/models/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import joblib
from utils.data_preprocessing import fetch_data, preprocess_data

def train():
    df = fetch_data()
    X, y = preprocess_data(df)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Feature Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Save the scaler for future use
    joblib.dump(scaler, 'models/scaler.joblib')

    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test_scaled)
    score = r2_score(y_test, y_pred)
    print(f"Model R^2 Score: {score}")

    # Save the model
    joblib.dump(model, 'models/pricing_model.joblib')

if __name__ == "__main__":
    train()
