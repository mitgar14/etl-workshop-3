# Python Modules
from utils.transformation_utils import *

# Data Handling and Manipulation
import pandas as pd

# Logging
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")

def transforming_data(happiness_dataframes: dict) -> pd.DataFrame:
    """
    Transforms a dictionary of happiness DataFrames by normalizing columns, adding a year column,
    concatenating common columns, filling missing values, and adding a continent column.
    
    Args:
        happiness_dataframes (dict of str: pd.DataFrame): Dictionary of DataFrames containing happiness data.
        
    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    
    logging.info("Starting the data transformation process.")
    
    logging.info("Data Transformation: Normalizing columns")    
    happiness_dataframes = normalize_columns(happiness_dataframes)
    
    logging.info("Data Transformation: Adding year column")
    happiness_dataframes = add_year_column(happiness_dataframes)
    
    logging.info("Data Transformation: Concatenating common columns")
    df = concatenate_common_columns(happiness_dataframes)
    
    logging.info("Data Transformation: Filling missing values")
    df = fill_na_with_mean(df, "corruption_perception")
    
    logging.info("Data Transformation: Adding continent column")
    df = add_continent_column(df)
    
    new_order = [
        'country',
        'continent',
        'year',
        'economy',
        'health',
        'social_support',
        'freedom',
        'corruption_perception',
        'generosity',
        'happiness_rank',
        'happiness_score'
    ]

    logging.info("Data Transformation: Reordering columns")
    df = df[new_order]
    
    logging.info("Data transformation process completed.")
    
    return df