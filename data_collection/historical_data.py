# data_collection/historical_data.py

import psycopg2
import random
from datetime import datetime, timedelta

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="ryanair_pricing",
    user="postgres",
    password="Varunanand123",
    host="localhost"
)
cursor = conn.cursor()

# Generate synthetic flight data
origins = ['DUB', 'LHR', 'STN', 'WRO', 'SXF']
destinations = ['MAD', 'BCN', 'CDG', 'FCO', 'AMS']
aircraft_types = ['Airbus A320', 'Boeing 737']

for i in range(1, 101):
    origin = random.choice(origins)
    destination = random.choice([d for d in destinations if d != origin])
    departure_time = datetime.now() + timedelta(days=random.randint(1, 180))
    arrival_time = departure_time + timedelta(hours=2)
    aircraft = random.choice(aircraft_types)

    cursor.execute("""
        INSERT INTO flights (origin, destination, departure_time, arrival_time, aircraft_type)
        VALUES (%s, %s, %s, %s, %s)
    """, (origin, destination, departure_time, arrival_time, aircraft))

# Commit and close
conn.commit()
cursor.close()
conn.close()
