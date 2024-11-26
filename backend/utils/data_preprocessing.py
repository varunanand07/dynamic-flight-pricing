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
