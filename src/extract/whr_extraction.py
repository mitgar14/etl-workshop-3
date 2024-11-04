# Data Handling and Manipulation
import pandas as pd

def extracting_data() -> dict:
    """
    Loads World Happiness Report data from CSV files for the years 2015 to 2019.

    This function reads five CSV files, each named by year (e.g., '2015.csv' for the 2015 data)
    and returns a dictionary where keys are strings representing each year,
    and values are the corresponding pandas DataFrames.

    Returns:
        dict: A dictionary with keys as strings ('2015', '2016', '2017', '2018', '2019'),
              and values as pandas DataFrames containing the happiness data for each respective year.
    """
    df_2015 = pd.read_csv("../data/2015.csv")
    df_2016 = pd.read_csv("../data/2016.csv")
    df_2017 = pd.read_csv("../data/2017.csv")
    df_2018 = pd.read_csv("../data/2018.csv")
    df_2019 = pd.read_csv("../data/2019.csv")
    
    happiness_dataframes = {
        "2015": df_2015,
        "2016": df_2016,
        "2017": df_2017,
        "2018": df_2018,
        "2019": df_2019}

    return happiness_dataframes