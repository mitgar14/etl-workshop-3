import pandas as pd
import logging as log

log.basicConfig(level=log.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")

def dataframe_briefing(data: dict) -> pd.DataFrame:
    """
    Generates a summary DataFrame for the given dictionary of DataFrames, containing
    information about rows, columns, null values, and duplicate values for each year.

    Args:
        data (dict): 
            A dictionary where the keys are years (from 2015 to 2019) and the values 
            are pandas DataFrames corresponding to those years.

    Returns:
        pd.DataFrame: 
            A DataFrame containing the year, number of rows, number of columns, 
            number of null values, and number of duplicate values for each year.
    """
    
    summary_list = []

    for year, df in data.items():
        num_rows = df.shape[0]
        num_columns = df.shape[1]
        num_nulls = df.isnull().sum().sum()
        num_duplicates = df.duplicated().sum()
        
        summary_list.append({
            "Year": year,
            "Number of rows": num_rows,
            "Number of columns": num_columns,
            "Number of null values": num_nulls,
            "Number of duplicate values": num_duplicates
        })
    
    briefing = pd.DataFrame(summary_list)
    
    return briefing

def comparing_names(data: dict) -> pd.DataFrame:
    """
    Generates a DataFrame comparing the names of the columns for each year and marks 
    if each column is present in all years.

    Args:
        data (dict): 
            A dictionary where the keys are years (from 2015 to 2019) and the values 
            are pandas DataFrames corresponding to those years.

    Returns:
        pd.DataFrame: 
            A DataFrame where the rows are the column names and the columns are the years,
            with '✔' indicating the presence of the column in that year and '✘' indicating
            its absence.
    """
    
    all_columns = set()
    for df in data.values():
        all_columns.update(df.columns)
    
    comparison_dict = {col: {year: ('✔' if col in df.columns else '✘') for year, df in data.items()} for col in all_columns}
    
    comparison_df = pd.DataFrame(comparison_dict).T
    comparison_df.index.name = 'Column Name'
    
    return comparison_df