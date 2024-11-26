# backend/utils/data_preprocessing.py

import pandas as pd
from datetime import datetime
from .db import Database

def fetch_data():
    db = Database()
    conn = db.get_conn()
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
        GROUP BY f.flight_id, f.origin, f.destination, f.departure_time, f.arrival_time, f.aircraft_type
    """
    df = pd.read_sql_query(query, conn)
    db.return_conn(conn)
    return df

def preprocess_data(df):
    # Feature Engineering
    df['days_to_departure'] = (df['departure_time'] - datetime.now()).dt.days
    df['hour_of_day'] = df['departure_time'].dt.hour
    df['origin_code'] = df['origin'].astype('category').cat.codes
    df['destination_code'] = df['destination'].astype('category').cat.codes
    df['aircraft_code'] = df['aircraft_type'].astype('category').cat.codes

    # Fill missing values
    df['avg_price'].fillna(df['avg_price'].mean(), inplace=True)
    df['competitor_avg_price'].fillna(df['competitor_avg_price'].mean(), inplace=True)

    # Target Variable: avg_price
    X = df[['days_to_departure', 'hour_of_day', 'origin_code', 'destination_code', 'aircraft_code', 'total_bookings', 'competitor_count', 'competitor_avg_price']]
    y = df['avg_price']

    return X, y
