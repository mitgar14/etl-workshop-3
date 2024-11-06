# Setting the work directory
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Python Modules
from src.extract.whr_extraction import *
from src.transform.whr_transformation import *
from src.load.whr_loading import *
from src.services.kafka import *

# Data Handling and Manipulation
import pandas as pd
import json

# Machine Learning
import joblib

# Logging
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")

if __name__ == "__main__":
    logging.info("Starting the Consumer script.")   
    
    consumer = get_kafka_consumer("whr_kafka_topic")
    
    logging.info("Consuming messages from the Kafka topic.")
    consumer_messages = [json.loads(message) for message in consumer]
    
    logging.info("Data Transformation: Converting the messages into a DataFrame.")
    df = pd.DataFrame(consumer_messages)
    
    logging.info("Machine Learning: Loading the Random Forest model.")
    rf_model = joblib.load("./model/rf_model.pkl")
    df_test = df.drop(columns=["id", "happiness_score"], axis=1)
    
    logging.info("Machine Learning: Making predictions using the Random Forest model.")
    predictions = rf_model.predict(df_test)
    
    logging.info("Data Transformation: Adding the predicted happiness score to the DataFrame.")
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
        'continent_Africa',
        'continent_Asia',
        'continent_Europe',
        'continent_North_America',
        'continent_Central_America',
        'continent_South_America',
        'continent_Oceania',
        'happiness_score',
        'predicted_happiness_score'
    ]

    logging.info("Data Transformation: Reordering the columns.")
    df = df[new_order]

    logging.info("Data Loading: Loading the predictions into the database.")
    loading_data(df, "whr_predictions")
    
    logging.info("Consumer script completed.")