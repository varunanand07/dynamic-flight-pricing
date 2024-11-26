# backend/models/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
from utils.data_preprocessing import fetch_data, preprocess_data

def train():
    df = fetch_data()
    X, y = preprocess_data(df)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    score = model.score(X_test, y_test)
    print(f"Model R^2 Score: {score}")

    # Save the model
    joblib.dump(model, 'models/pricing_model.joblib')

if __name__ == "__main__":
    train()
