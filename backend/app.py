# backend/app.py

from flask import Flask, jsonify, request
from utils.db import Database
import joblib
import pandas as pd
from utils.data_preprocessing import preprocess_data, fetch_data
from datetime import datetime

app = Flask(__name__)

# Load the trained model
model = joblib.load('models/pricing_model.joblib')

# Initialize Database
db = Database()

@app.route('/api/predict', methods=['GET'])
def predict_price():
    # Fetch latest data
    df = fetch_data()
    X, _ = preprocess_data(df)

    # Predict
    predictions = model.predict(X)

    # Attach predictions to dataframe
    df['predicted_price'] = predictions

    # Convert to JSON
    result = df[['flight_id', 'origin', 'destination', 'departure_time', 'predicted_price']].to_dict(orient='records')

    return jsonify(result), 200

@app.route('/api/train', methods=['POST'])
def retrain_model():
    # Endpoint to trigger retraining
    from models.train_model import train
    train()
    return jsonify({"message": "Model retrained successfully."}), 200

@app.route('/api/flight/<int:flight_id>', methods=['GET'])
def get_flight(flight_id):
    conn = db.get_conn()
    cursor = conn.cursor()
    query = """
        SELECT 
            f.flight_id,
            f.origin,
            f.destination,
            f.departure_time,
            f.arrival_time,
            f.aircraft_type,
            COUNT(b.booking_id) as total_bookings,
            AVG(b.price) as avg_price,
            COUNT(cp.competitor_id) as competitor_count,
            AVG(cp.price) as competitor_avg_price
        FROM flights f
        LEFT JOIN bookings b ON f.flight_id = b.flight_id
        LEFT JOIN competitor_prices cp ON f.flight_id = cp.flight_id
        WHERE f.flight_id = %s
        GROUP BY f.flight_id, f.origin, f.destination, f.departure_time, f.arrival_time, f.aircraft_type
    """
    cursor.execute(query, (flight_id,))
    record = cursor.fetchone()
    db.return_conn(conn)

    if not record:
        return jsonify({"error": "Flight not found"}), 404

    # Convert to DataFrame
    columns = ['flight_id', 'origin', 'destination', 'departure_time', 'arrival_time', 'aircraft_type', 'total_bookings', 'avg_price', 'competitor_count', 'competitor_avg_price']
    df = pd.DataFrame([record], columns=columns)
    X, _ = preprocess_data(df)

    # Predict
    predicted_price = model.predict(X)[0]

    response = {
        "flight_id": flight_id,
        "origin": record[1],
        "destination": record[2],
        "departure_time": record[3],
        "predicted_price": predicted_price
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
