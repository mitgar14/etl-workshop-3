# Data Handling and Manipulation
import pandas as pd

def extracting_data():
    """
    Loads World Happiness Report data from CSV files for the years 2015 to 2019.

    This function reads five CSV files from the './data' directory, each containing the World
    Happiness Report data for a specific year. The files are named by year (e.g., '2015.csv').
    
    Returns:
        dict: 
            A dictionary where keys are year strings ('2015' to '2019') and values
            are pandas DataFrames containing the happiness data for each year.
    
    Raises:
        FileNotFoundError: 
            If any of the required CSV files are not found in the './data' directory.
    """
    df_2015 = pd.read_csv("./data/2015.csv")
    df_2016 = pd.read_csv("./data/2016.csv")
    df_2017 = pd.read_csv("./data/2017.csv")
    df_2018 = pd.read_csv("./data/2018.csv")
    df_2019 = pd.read_csv("./data/2019.csv")
    
    happiness_dataframes = {
        "2015": df_2015,
        "2016": df_2016,
        "2017": df_2017,
        "2018": df_2018,
        "2019": df_2019
    }

    return happiness_dataframes