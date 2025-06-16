from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import logging
import os
from dotenv import load_dotenv
import time
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

db_host = os.getenv("PG_HOST") # This should be 'db' when running in Docker
db_port = os.getenv("PG_PORT",5432) # This should be '5432'
db_name = os.getenv("PG_DB")
db_user = os.getenv("PG_USER")
db_pass = os.getenv("PG_PASSWORD")
database_url = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}/{db_name}"


def get_db_connection(max_attempts=10, delay_seconds=5):
    """
    Attempts to establish a SQLAlchemy engine connection with retries.
    Args:
        max_attempts (int): Maximum number of times to try connecting.
        delay_seconds (int): Time to wait (in seconds) between retries.
    Returns:
        sqlalchemy.engine.base.Engine: The SQLAlchemy engine if connection is successful.
    Raises:
        Exception: If connection fails after all attempts.
    """
    for attempt in range(1, max_attempts + 1):
        logging.info(f"Attempting to connect to database (Attempt {attempt}/{max_attempts})...")
        try:
            # Create the engine object inside the loop
            # This ensures a fresh attempt if a previous one failed
            engine = create_engine(database_url)

            # Try to establish a real connection to test if the DB is ready
            with engine.connect() as connection:
                connection.execute(text("SELECT 1")) # Execute a simple query to confirm readiness
            
            logging.info("Successfully connected to the database!")
            return engine # Return the engine if successful
            
        except OperationalError as e:
            # Catch specific errors related to connection issues
            error_message = str(e)
            
            if "Connection refused" in error_message or "could not connect to server" in error_message:
                logging.warning(f"Database not ready yet or connection refused. Retrying in {delay_seconds} seconds...")
                time.sleep(delay_seconds) # Wait before the next attempt
            elif "password authentication failed" in error_message:
                logging.critical("FATAL: Password authentication failed. Check PG_USER and PG_PASSWORD in .env.")
                raise # Re-raise immediately, no point in retrying this
            else:
                logging.error(f"An unexpected database operational error occurred: {error_message}")
                raise # Re-raise other operational errors

        except Exception as e:
            # Catch any other unexpected errors during the process
            logging.error(f"An unexpected error occurred during database connection attempt: {e}")
            raise # Re-raise general exceptions

    # If the loop finishes without returning, it means all attempts failed
    logging.critical(f"Failed to connect to the database after {max_attempts} attempts.")
    raise Exception("Could not establish a database connection.")

engine = get_db_connection()

def load_data(df,table_name="hourly_weather_forecast"):
    try:
        engine = get_db_connection()
        df.to_sql(table_name, engine, if_exists='append', index=False)
        logging.info("Data loaded successfully into the database.")
        print(pd.read_sql("SELECT * FROM hourly_weather_forecast LIMIT 5;", engine))
    except Exception as e:
        logging.error(f"Failed to load data into the database: {e}")
        raise