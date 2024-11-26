# backend/models/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib
from utils.data_preprocessing import fetch_data, preprocess_data
import logging
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def train():
    logging.info("Starting data fetching and preprocessing")
    df = fetch_data()
    X, y = preprocess_data(df)

    # Visualize target distribution
    plt.figure(figsize=(10,6))
    plt.hist(y, bins=50, color='blue', edgecolor='black')
    plt.title('Distribution of Average Prices')
    plt.xlabel('Average Price (€)')
    plt.ylabel('Frequency')
    plt.savefig('models/avg_price_distribution.png')
    plt.close()
    logging.info("Saved average price distribution plot to models/avg_price_distribution.png")

    logging.info("Splitting data into training and testing sets")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    logging.info("Applying feature scaling")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Save the scaler for future use
    joblib.dump(scaler, 'models/scaler.joblib')
    logging.info("Saved the scaler to models/scaler.joblib")

    logging.info("Setting up hyperparameter tuning with GridSearchCV")
    rf = RandomForestRegressor(random_state=42)
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'bootstrap': [True, False]
    }

    grid_search = GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        cv=3,
        n_jobs=-1,
        verbose=2,
        scoring='r2'
    )

    logging.info("Starting GridSearchCV")
    grid_search.fit(X_train_scaled, y_train)

    best_model = grid_search.best_estimator_
    logging.info(f"Best Parameters: {grid_search.best_params_}")

    logging.info("Evaluating the best model on test set")
    y_pred = best_model.predict(X_test_scaled)
    score = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    logging.info(f"Best Model R^2 Score: {score}")
    logging.info(f"Best Model MAE: {mae}")
    logging.info(f"Best Model RMSE: {rmse}")

    # Cross-validation
    logging.info("Performing cross-validation")
    cv_scores = cross_val_score(best_model, X_train_scaled, y_train, cv=5, scoring='r2')
    logging.info(f"Cross-validation R² scores: {cv_scores}")
    logging.info(f"Mean CV R² score: {cv_scores.mean()}")

    # Save the best model
    joblib.dump(best_model, 'models/pricing_model.joblib')
    logging.info("Saved the best model to models/pricing_model.joblib")

if __name__ == "__main__":
    train()
