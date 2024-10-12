import sqlite3
import pandas as pd
import os
from utils import logger

def push_data_to_sqlite(input_csv, sqlite_db, table_name):
    """
    Pushes the data from a CSV file to a SQLite database.

    This function attempts to connect to the specified SQLite database, read the data from the specified CSV file, and write the data to a table in the database. If the table already exists, it will be replaced.

    Parameters
    ----------
    input_csv : str
        The path to the CSV file containing the data to be pushed to the database.
    sqlite_db : str
        The path to the SQLite database file.
    table_name : str
        The name of the table to which the data should be written.

    Returns
    -------
    None
    """
    try:
        # Connect to the SQLite database (it will create the database if it doesn't exist)
        conn = sqlite3.connect(sqlite_db)
        logger.info(f"Connected to SQLite database: {sqlite_db}")
        
        # Read the CSV data
        data = pd.read_csv(input_csv)
        logger.info(f"CSV file {input_csv} read successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
        
        # Write the data to the specified SQLite table (if table exists, replace it)
        data.to_sql(table_name, conn, if_exists='replace', index=False)
        logger.info(f"Data successfully pushed to SQLite table: {table_name}")

        # Close the connection
        conn.close()
        logger.info(f"Connection to SQLite database {sqlite_db} closed.")
    
    except sqlite3.Error as sql_err:
        logger.error(f"SQLite error occurred: {sql_err}")
    except FileNotFoundError as fnf_error:
        logger.error(f"File not found error: {fnf_error}")
    except pd.errors.EmptyDataError as empty_data_err:
        logger.error(f"Empty data error: {empty_data_err}")
    except Exception as e:
        logger.error(f"An unexpected error occurred while pushing data to SQLite: {e}")

# Example usage (can be removed or modified for actual implementation)
if __name__ == "__main__":
    input_file = os.path.join("data", "cleaned_data.csv")
    sqlite_db = os.path.join("database", "github_data.db")
    table_name = "github_repositories"
    push_data_to_sqlite(input_file, sqlite_db, table_name)
