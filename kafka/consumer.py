# Setting the work directory
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Python Modules
from src.extract.whr_extraction import *
from src.transform.whr_transformation import *
from src.load.whr_loading import *
from src.services.kafka import *

# Python Libraries
import pandas as pd
import json
import joblib

if __name__ == "__main__":
    consumer_messages = [get_kafka_consumer("whr_kafka_topic")]
    
    df = pd.DataFrame(consumer_messages)
    
    gb_model = joblib.load("./model/gb_model.pkl")
    df_test = df.drop(columns=["id", "happiness_score"], axis=1)  
    predictions = gb_model.predict(df_test)
    
    df["predicted_happiness_score"] = predictions
    
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
        'predicted_happiness_score',
        'continent_Africa',
        'continent_Asia',
        'continent_Europe',
        'continent_North_America',
        'continent_Central_America',
        'continent_South_America',
        'continent_Oceania'
    ]

    df = df[new_order]

    loading_data(df, "whr_predictions")