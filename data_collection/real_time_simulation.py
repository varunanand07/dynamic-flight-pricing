# data_collection/real_time_simulation.py

import psycopg2
import random
from datetime import datetime
import time

def get_flight_details(cursor, flight_id):
    cursor.execute("""
        SELECT origin, destination, aircraft_type, departure_time
        FROM flights
        WHERE flight_id = %s
    """, (flight_id,))
    return cursor.fetchone()

def simulate_bookings(cursor, conn):
    while True:
        flight_id = random.randint(1, 100)
        flight = get_flight_details(cursor, flight_id)
        if flight:
            origin, destination, aircraft_type, departure_time = flight
            booking_time = datetime.now()
            days_to_departure = (departure_time - booking_time).days

            # Base price influenced by origin and destination
            origin_multiplier = {
                'DUB': 1.0,
                'LHR': 1.2,
                'STN': 0.9,
                'WRO': 0.8,
                'SXF': 1.1
            }.get(origin, 1.0)

            destination_multiplier = {
                'MAD': 1.3,
                'BCN': 1.4,
                'CDG': 1.5,
                'FCO': 1.2,
                'AMS': 1.3
            }.get(destination, 1.0)

            # Aircraft type influence
            aircraft_multiplier = {
                'Airbus A320': 1.0,
                'Boeing 737': 1.1
            }.get(aircraft_type, 1.0)

            # Days to departure influence
            if days_to_departure > 60:
                time_multiplier = 0.8
            elif days_to_departure > 30:
                time_multiplier = 1.0
            elif days_to_departure > 7:
                time_multiplier = 1.2
            else:
                time_multiplier = 1.5

            # Calculate price with some randomness
            base_price = 50  # Base price in €
            price = base_price * origin_multiplier * destination_multiplier * aircraft_multiplier * time_multiplier
            price += random.uniform(-10, 10)  # Adding some noise

            # Ensure price is within realistic bounds
            price = max(30, min(price, 500))

            cursor.execute("""
                INSERT INTO bookings (flight_id, booking_time, price)
                VALUES (%s, %s, %s)
            """, (flight_id, booking_time, round(price, 2)))

            conn.commit()
        time.sleep(random.randint(1, 5))  # Simulate booking every 1-5 seconds

def simulate_competitor_prices(cursor, conn):
    competitors = ['CompA', 'CompB', 'CompC']
    while True:
        flight_id = random.randint(1, 100)
        flight = get_flight_details(cursor, flight_id)
        if flight:
            origin, destination, aircraft_type, departure_time = flight
            competitor = random.choice(competitors)
            booking_time = datetime.now()
            days_to_departure = (departure_time - booking_time).days

            # Similar multipliers as bookings to generate competitor prices
            origin_multiplier = {
                'DUB': 1.0,
                'LHR': 1.2,
                'STN': 0.9,
                'WRO': 0.8,
                'SXF': 1.1
            }.get(origin, 1.0)

            destination_multiplier = {
                'MAD': 1.3,
                'BCN': 1.4,
                'CDG': 1.5,
                'FCO': 1.2,
                'AMS': 1.3
            }.get(destination, 1.0)

            aircraft_multiplier = {
                'Airbus A320': 1.0,
                'Boeing 737': 1.1
            }.get(aircraft_type, 1.0)

            if days_to_departure > 60:
                time_multiplier = 0.8
            elif days_to_departure > 30:
                time_multiplier = 1.0
            elif days_to_departure > 7:
                time_multiplier = 1.2
            else:
                time_multiplier = 1.5

            base_price = 50
            price = base_price * origin_multiplier * destination_multiplier * aircraft_multiplier * time_multiplier
            price += random.uniform(-10, 10)

            price = max(30, min(price, 500))

            cursor.execute("""
                INSERT INTO competitor_prices (flight_id, competitor_name, price, timestamp)
                VALUES (%s, %s, %s, %s)
            """, (flight_id, competitor, round(price, 2), datetime.now()))

            conn.commit()
        time.sleep(random.randint(5, 10))  # Simulate competitor price updates every 5-10 seconds

def main():
    conn = psycopg2.connect(
        dbname="ryanair_pricing",
        user="postgres",
        password="Varunanand123",
        host="localhost"
    )
    cursor = conn.cursor()

    from threading import Thread
    booking_thread = Thread(target=simulate_bookings, args=(cursor, conn))
    competitor_thread = Thread(target=simulate_competitor_prices, args=(cursor, conn))

    booking_thread.start()
    competitor_thread.start()

    booking_thread.join()
    competitor_thread.join()

if __name__ == "__main__":
    main()
