# Python Modules
from utils.transformation_utils import *

# Data Handling and Manipulation
import pandas as pd

def transforming_data(happiness_dataframes: dict) -> pd.DataFrame:
    """
    Transforms a dictionary of happiness DataFrames by normalizing columns, adding a year column,
    concatenating common columns, filling missing values, and adding a continent column.
    
    Args:
        happiness_dataframes (dict of str: pd.DataFrame): Dictionary of DataFrames containing happiness data.
        
    Returns:
        pd.DataFrame: Transformed DataFrame with selected columns in a specified order.
    """
    happiness_dataframes = normalize_columns(happiness_dataframes)
    
    happiness_dataframes = add_year_column(happiness_dataframes)
    
    df = concatenate_common_columns(happiness_dataframes)
    
    df = fill_na_with_mean(df, "corruption_perception")
    
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
    df = df[new_order]
    
    return df