# Setting the work directory
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Python Modules
from src.services.kafka import *

# Machine Learning
import joblib

# Logging
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")

if __name__ == "__main__":
    logging.info("Starting the Consumer script.")   
    
    logging.info("Machine Learning: Loading the Random Forest model.")
    rf_model = joblib.load("./model/rf_model.pkl")
    
    logging.info("Starting consumer to process messages in real-time.")
    get_kafka_consumer("whr_kafka_topic", rf_model)
    
    logging.info("Consumer script completed.")