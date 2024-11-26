# backend/utils/data_preprocessing.py

import pandas as pd
from datetime import datetime
from .db import Database
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_data():
    db = Database()
    conn = db.get_conn()
    
    # Create SQLAlchemy engine
    engine = create_engine(
        f"postgresql+psycopg2://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
    )
    
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
    df = pd.read_sql_query(query, engine)
    
    db.return_conn(conn)
    return df

def preprocess_data(df):
    # Feature Engineering
    df['days_to_departure'] = (df['departure_time'] - datetime.now()).dt.days
    df['hour_of_day'] = df['departure_time'].dt.hour

    # One-Hot Encoding for categorical variables
    df = pd.get_dummies(df, columns=['origin', 'destination', 'aircraft_type'], drop_first=True)

    # Fill missing values without using inplace
    df['avg_price'] = df['avg_price'].fillna(df['avg_price'].mean())
    df['competitor_avg_price'] = df['competitor_avg_price'].fillna(df['competitor_avg_price'].mean())

    # Target Variable: avg_price
    feature_columns = ['days_to_departure', 'hour_of_day', 'total_bookings', 'competitor_count', 'competitor_avg_price']
    # Add all one-hot encoded columns
    feature_columns += [col for col in df.columns if col.startswith('origin_') or col.startswith('destination_') or col.startswith('aircraft_type_')]

    X = df[feature_columns]
    y = df['avg_price']

    return X, y
