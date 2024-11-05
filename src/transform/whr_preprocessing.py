# Python Modules
from utils.preprocessing_utils import *

# Data Handling and Manipulation
import pandas as pd

# Logging
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")

def preprocessing_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses the input DataFrame by creating dummy variables and splitting the data.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
        
    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    
    logging.info("Starting the data preprocessing process.")
    
    logging.info("Data Preprocessing: Creating dummy variables")    
    df = creating_dummy_variables(df)
    
    logging.info("Data Preprocessing: Splitting the data")
    X_train, X_test, y_train, y_test = splitting_data(df)
    
    logging.info('Data Preprocessing: Creating a column for the index named "id"')
    X_test["id"] = X_test.index
    
    new_order = [
        'id',
        'year',
        'economy',
        'health',
        'social_support',
        'freedom',
        'corruption_perception',
        'generosity',
        'happiness_score',
        'continent_Africa',
        'continent_Asia',
        'continent_Central_America',
        'continent_Europe',
        'continent_North_America',
        'continent_Oceania',
        'continent_South_America'
    ]

    logging.info("Data Preprocessing: Reordering columns")
    X_test['happiness_score'] = y_test
    X_test = X_test[new_order]
    
    logging.info("Data preprocessing process completed.")
    
    return X_test