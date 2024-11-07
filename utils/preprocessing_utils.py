# Machine Learning
from sklearn.model_selection import train_test_split

# Data Handling and Manipulation
import pandas as pd

# Utils functions
def creating_dummy_variables(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts the 'continent' column in the DataFrame to dummy variables and renames specific columns.
    
    Args:
        df (pd.DataFrame):
            The input DataFrame containing a 'continent' column.
    
    Returns:
        pd.DataFrame:
            The DataFrame with dummy variables for 'continent' and
            renamed columns.
    """
    df = pd.get_dummies(df, columns=["continent"])
    
    columns_rename = {
        "continent_North America": "continent_North_America",
        "continent_Central America": "continent_Central_America",
        "continent_South America": "continent_South_America"
    }

    df = df.rename(columns=columns_rename)
    
    return df

def splitting_data(df: pd.DataFrame) -> tuple:
    """
    Splits the input DataFrame into training and testing sets.
    
    Args:
        df (pd.DataFrame):
            The input DataFrame.
    
    Returns:
        tuple:
            A tuple containing the training and testing DataFrames.
    """
    X = df.drop(["happiness_score", "happiness_rank", "country"], axis = 1)
    y = df["happiness_score"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=200)
    
    return X_train, X_test, y_train, y_test