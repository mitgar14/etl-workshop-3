# Data Handling and Manipulation
import pandas as pd
import country_converter as coco

# Utils functions
def normalize_columns(happiness_dataframes: dict) -> dict:    
    """
    Normalize column names in a dictionary of DataFrames containing the World Happiness Report data.
    
    This function takes a dictionary where keys are years and values are DataFrames.
    It renames the columns in each DataFrame to a standard set of column names for consistency across different datasets.
    
    Args:
        happiness_dataframes (dict):
            A dictionary where keys are years (int) and values are
            pandas DataFrames with varying column names.
    
    Returns:
        dict:
            A dictionary with the same keys (years) and DataFrames
            with normalized column names.
    """
    column_mapping = {    
        "Country": "country",
        "Country or region": "country",
        
        "Happiness Score": "happiness_score",
        "Happiness.Score": "happiness_score",
        "Score": "happiness_score",

        "Happiness Rank": "happiness_rank",
        "Happiness.Rank": "happiness_rank",
        "Overall rank": "happiness_rank",

        "Economy (GDP per Capita)": "economy",
        "Economy..GDP.per.Capita.": "economy",
        "GDP per capita": "economy",

        "Health (Life Expectancy)": "health",
        "Health..Life.Expectancy.": "health",
        "Healthy life expectancy": "health",

        "Family": "social_support",
        "Social support": "social_support",

        "Freedom": "freedom",
        "Freedom to make life choices": "freedom",

        "Trust (Government Corruption)": "corruption_perception",
        "Trust..Government.Corruption.": "corruption_perception",
        "Perceptions of corruption": "corruption_perception",

        "Generosity": "generosity",

        "Dystopia Residual": "dystopia_residual",
        "Dystopia.Residual": "dystopia_residual",
    }
    
    for year, df in happiness_dataframes.items():
        df = df.rename(columns=column_mapping)
        happiness_dataframes[year] = df
    
    return happiness_dataframes

def add_year_column(happiness_dataframes: dict) -> dict:
    """
    Adds a 'year' column to each DataFrame in the dictionary.
    
    Args:
        happiness_dataframes (dict):
            A dictionary where keys are years (int) and values are
            pandas DataFrames with normalized column names.
    
    Returns:
        dict:
            A dictionary with the same keys (years) and DataFrames
            with an additional 'year' column.
    """
    for year, df in happiness_dataframes.items():
        df["year"] = year
        happiness_dataframes[year] = df
    
    return happiness_dataframes

def concatenate_common_columns(happiness_dataframes: dict) -> pd.DataFrame:
    """
    Concatenate common columns from multiple DataFrames.
    
    This function takes a dictionary of DataFrames, identifies the common columns
    among them, and concatenates these columns into a single DataFrame.
    
    Args:
        happiness_dataframes (dict):
            A dictionary where the keys are identifiers
            and the values are pandas DataFrames.
    
    Returns:
        pd.DataFrame:
            A DataFrame containing the concatenated common columns from
            the input DataFrames.
    """
    common_columns = list(set.intersection(*(set(df.columns) for df in happiness_dataframes.values())))
    
    filtered_dataframes = [df[common_columns] for df in happiness_dataframes.values()]

    df = pd.concat(filtered_dataframes, ignore_index=True)
    
    return df

def fill_na_with_mean(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Fill missing values in a column with the mean of the non-missing values.
    
    Args:
        df (pd.DataFrame):
            The input DataFrame.       
        column (str):
            The column name for which missing values are to be filled.
    
    Returns:
        pd.DataFrame:
            The DataFrame with missing values filled with the mean.
    """
    df[column] = df[column].fillna(df[column].mean())
    return df
    
def add_continent_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a 'continent' column to the DataFrame by converting the 'country' column.
    
    Args:
        df (pd.DataFrame):
            The input DataFrame containing a 'country' column.
    
    Returns:
        pd.DataFrame:
            The DataFrame with an additional 'continent' column.
    """
    cc = coco.CountryConverter()
    
    df["continent"] = cc.convert(names=df["country"].tolist(), to="continent")
    
    continent_mapping = {
        "Canada": "North America",
        "Costa Rica": "Central America",
        "Mexico": "North America",
        "United States": "North America",
        "Brazil": "South America",
        "Venezuela": "South America",
        "Panama": "Central America",
        "Chile": "South America",
        "Argentina": "South America",
        "Uruguay": "South America",
        "Colombia": "South America",
        "Suriname": "South America",
        "Trinidad and Tobago": "South America",
        "El Salvador": "Central America",
        "Guatemala": "Central America",
        "Ecuador": "South America",
        "Bolivia": "South America",
        "Paraguay": "South America",
        "Nicaragua": "Central America",
        "Peru": "South America",
        "Jamaica": "Central America",
        "Dominican Republic": "Central America",
        "Honduras": "Central America",
        "Haiti": "Central America",
        "Puerto Rico": "Central America",
        "Belize": "Central America",
        "Trinidad & Tobago": "South America"
    }
    
    df["continent"] = df["country"].map(continent_mapping).fillna(df["continent"])
    
    return df