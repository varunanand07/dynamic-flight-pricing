# backend/utils/db.py

import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import pool

load_dotenv()

class Database:
    """
    Database connection pool handler.
    """
    def __init__(self):
        """
        Initializes the connection pool.
        """
        self.connection_pool = psycopg2.pool.SimpleConnectionPool(
            1,
            10,
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            host=os.getenv('DATABASE_HOST'),
            port=os.getenv('DATABASE_PORT'),
            database=os.getenv('DATABASE_NAME')
        )
    
    def get_conn(self):
        """
        Retrieves a connection from the pool.
        """
        return self.connection_pool.getconn()
    
    def return_conn(self, conn):
        """
        Returns a connection back to the pool.
        """
        self.connection_pool.putconn(conn)
