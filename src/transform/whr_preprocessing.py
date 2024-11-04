# Python Modules
from utils.preprocessing_utils import *

# Data Handling and Manipulation
import pandas as pd

def preprocessing_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses the input DataFrame by creating dummy variables and splitting the data.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    df = creating_dummy_variables(df)
    
    X_train, X_test, y_train, y_test = splitting_data(df)
    
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
        'continent_Africa',
        'continent_Asia',
        'continent_Europe',
        'continent_North_America',
        'continent_Central_America',
        'continent_South_America',
        'continent_Oceania'
    ]

    X_test = X_test[new_order]
    
    return X_test