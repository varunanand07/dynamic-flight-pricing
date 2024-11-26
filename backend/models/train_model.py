# backend/models/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
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

    # Define the model
    rf = RandomForestRegressor(random_state=42)

    # Define hyperparameters to tune
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2]
    }

    # Set up GridSearchCV
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid,
                               cv=3, n_jobs=-1, verbose=2, scoring='r2')

    # Fit GridSearchCV
    grid_search.fit(X_train_scaled, y_train)

    # Best model
    best_model = grid_search.best_estimator_

    # Predict and evaluate
    y_pred = best_model.predict(X_test_scaled)
    score = r2_score(y_test, y_pred)
    print(f"Best Model R^2 Score: {score}")
    print(f"Best Parameters: {grid_search.best_params_}")

    # Save the best model
    joblib.dump(best_model, 'models/pricing_model.joblib')

if __name__ == "__main__":
    train()
