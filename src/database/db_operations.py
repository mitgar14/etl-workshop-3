# Environmental Variables
from dotenv import load_dotenv
import os

# SQLAlchemy
from sqlalchemy import create_engine, inspect, BigInteger, Boolean, Integer, Float, String, Text, DateTime, MetaData, Table, Column
from sqlalchemy_utils import database_exists, create_database

# Data Handling and Manipulation
import pandas as pd

# Logging
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")

# Reading the environment variables
load_dotenv("./env/.env")

user = os.getenv("PG_USER")
password = os.getenv("PG_PASSWORD")

host = os.getenv("PG_HOST")
port = os.getenv("PG_PORT")

database = os.getenv("PG_DATABASE")

def creating_engine():
    """
    Create a SQLAlchemy engine for connecting to a PostgreSQL database.
    
    This function constructs a connection URL using predefined environment variables and creates a SQLAlchemy engine.
    If the database doesn't exist, it creates one.

    Returns:
        sqlalchemy.engine.Engine:
            An instance of SQLAlchemy engine connected to the specified database.
    """
    url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(url)
    
    if not database_exists(url):
        create_database(url)
        logging.info(f'The database "{database}" was created.')
    
    logging.info("Engine created. You can now connect to the database.")
    
    return engine

def disposing_engine(engine):
    """
    Dispose of the given SQLAlchemy engine.

    This function disposes of the provided SQLAlchemy engine, releasing any resources held by the engine.

    Args:
        engine (sqlalchemy.engine.Engine):
            The SQLAlchemy engine to be disposed.

    Returns:
        None
    """
    engine.dispose()
    logging.info("Engine disposed.")

def infering_types(dtype, column_name, df):
    """
    Infer the SQLAlchemy data type for a given pandas DataFrame column based on its dtype.

    This function analyzes the dtype of a DataFrame column and returns the appropriate SQLAlchemy
    data type. For string columns, it determines whether to use String(255) or Text based on
    the maximum string length.

    Args:
        dtype (numpy.dtype):
            The data type of the column to be analyzed.
        column_name (str):
            The name of the column in the DataFrame.
        df (pd.DataFrame):
            The DataFrame containing the column to be analyzed.

    Returns:
        sqlalchemy.types.TypeEngine:
            The inferred SQLAlchemy data type (Integer, Float, String, Text,
            DateTime, or Boolean).
    """
    if "int" in dtype.name:
        return Integer
    elif "float" in dtype.name:
        return Float
    elif "object" in dtype.name:
        max_len = df[column_name].astype(str).str.len().max()
        if max_len > 255:
            logging.info(f"Adjusting column {column_name} to Text due to length {max_len}.")
            return Text
        else:
            return String(255)
    elif "datetime" in dtype.name:
        return DateTime
    elif "bool" in dtype.name:
        return Boolean
    else:
        return Text

def load_raw_data(engine, df: pd.DataFrame, table_name: str) -> None:
    """
    Load raw data from a Pandas DataFrame into a database table.

    This function creates a new table in the database using the provided engine and loads data from
    the DataFrame into it. If the table already exists, it replaces it.

    Args:
        engine (sqlalchemy.engine.Engine):
            The SQLAlchemy engine connected to the database.
        df (pd.DataFrame):
            The DataFrame containing the data to be loaded.
        table_name (str):
            The name of the table to be created in the database.

    Returns:
        None

    Raises:
        Exception:
            If an error occurs during the creation of the table or loading data.
    """
    logging.info(f"Creating table {table_name} from Pandas DataFrame.")
    
    try:   
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        logging.info(f"Table {table_name} created successfully.")
    except Exception as e:
        logging.exception(f"Error creating table {table_name}: {e}")

def load_clean_data(engine, df: pd.DataFrame, table_name: str) -> None:
    """
    Create a database table with inferred column types from a cleaned Pandas DataFrame and load the data into it.

    This function checks if the table does not exist in the database, then creates it with columns inferred
    from the DataFrame's dtypes. It then loads the data into the table. If the table already exists, it logs an error.

    Args:
        engine (sqlalchemy.engine.Engine):
            The SQLAlchemy engine connected to the database.
        df (pd.DataFrame):
            The cleaned DataFrame containing the data to be loaded.
        table_name (str):
            The name of the table to be created in the database.

    Returns:
        None

    Raises:
        Exception:
            If an error occurs during the creation of the table or loading data.
    """
    logging.info(f"Creating table {table_name} from Pandas DataFrame.")
    
    try:
        if not inspect(engine).has_table(table_name):
            metadata = MetaData()
            
            columns = [Column(
                name,
                infering_types(dtype, name, df),
                primary_key=(name == "id")
            ) for name, dtype in df.dtypes.items()]
            
            table = Table(table_name, metadata, *columns)
            table.create(engine)
            
            logging.info(f"Table {table_name} created successfully.")

            df.to_sql(table_name, con=engine, if_exists="append", index=False)
            logging.info(f"Data loaded succesfully to table {table_name}.")
        else:
            logging.error(f"Table {table_name} already exists.")
    except Exception as e:
        logging.exception(f"Error creating table {table_name}: {e}")