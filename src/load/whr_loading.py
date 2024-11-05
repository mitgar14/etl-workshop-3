# Python Modules
from src.database.db_operations import creating_engine, disposing_engine, load_clean_data

# Data Handling and Manipulation
import pandas as pd

def loading_data(df: pd.DataFrame, table_name: str) -> None:
    """
    Load cleaned data from a Pandas DataFrame into a database table.

    This function creates a new table in the database using the provided engine and loads data from
    the DataFrame into it. If the table already exists, it appends the data to it. The database
    connection is properly disposed of after the operation.

    Args:
        df (pd.DataFrame):
            The cleaned DataFrame containing the data to be loaded.
        table_name (str):
            The name of the table to be created in the database.

    Returns:
        None

    Raises:
        Exception:
            If an error occurs during the creation of the engine, loading data,
            or disposing of the engine.
    """
    engine = creating_engine()
    
    load_clean_data(engine, df, table_name)
    
    disposing_engine(engine)