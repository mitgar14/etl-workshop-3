# Python Modules
from src.database.db_operations import create_engine, disposing_engine, load_clean_data

def loading_data(df, table_name):
    """
    Load cleaned data from a Pandas DataFrame into a database table.

    This function creates a new table in the database using the provided engine and loads data from
    the DataFrame into it. If the table already exists, it appends the data to it.

    Args:
        df: The cleaned DataFrame containing the data to be loaded.
        table_name: The name of the table to be created in the database.
    """
    engine = create_engine()
    
    load_clean_data(engine, df, table_name)
    
    disposing_engine(engine)