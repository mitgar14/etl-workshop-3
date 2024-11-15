# Python Modules
from src.extract.whr_extraction import *
from src.transform.whr_transformation import *
from src.load.whr_loading import *

# Kafka
from kafka import KafkaProducer, KafkaConsumer

# Time 
import time

# Data Handling and Manipulation
import pandas as pd
import json

# Logging
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")

def get_kafka_consumer(topic: str, rf_model) -> None:
    """
    Initializes a Kafka consumer to listen to a specified topic and process messages in real-time.

    This function creates a Kafka consumer that connects to a local Kafka broker, subscribes to the
    specified topic, and processes each incoming message as it arrives. For every message, it performs
    the following steps:
        - Converts the message to a Pandas DataFrame.
        - Prepares the data for prediction by dropping the 'id' and 'happiness_score' columns.
        - Uses the provided Random Forest model (`rf_model`) to make predictions.
        - Adds the prediction result as a new column 'predicted_happiness_score'.
        - Reorders the DataFrame columns to a predefined order.
        - Loads the processed data into the database using the [`loading_data`](src/load/whr_loading.py) function.

    Each processed message is logged with its timestamp, actual happiness score, and the predicted score.

    Args:
        topic (str):
            The name of the Kafka topic to subscribe to.
        rf_model:
            The pre-trained Random Forest model used for making predictions.

    Raises:
        Exception:
            If an error occurs during consumer initialization or message processing.
    """
    logging.info(f'Starting to listen to topic "{topic}".')
    
    try:
        consumer = KafkaConsumer(
            topic, 
            bootstrap_servers="localhost:9092",
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True
        )
        
        for kafka_message in consumer:
            try:
                # Obtener mensaje y timestamp
                message = kafka_message.value
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                
                # Convertir mensaje a DataFrame
                df = pd.DataFrame([message])
                
                # Preparar datos para predicción
                df_test = df.drop(columns=["id", "happiness_score"], axis=1)
                
                # Realizar predicción
                predictions = rf_model.predict(df_test)
                
                # Agregar predicción al DataFrame
                df["predicted_happiness_score"] = predictions
                
                # Reordenar columnas
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
                df = df[new_order]
                
                loading_data(df, "whr_predictions")
                
                logging.info(f"Processed message at {timestamp} - "
                           f"Actual: {message['happiness_score']:.3f}, "
                           f"Predicted: {predictions[0]:.3f}")
                
            except Exception as e:
                logging.error(f"Error processing message: {e}")
                continue
                
    except Exception as e:
        logging.exception(f"Error in consumer: {e}")

def get_kafka_producer(df: pd.DataFrame, topic: str) -> None:
    """
    Sends messages from a DataFrame to a specified Kafka topic.
    
    This function initializes a Kafka producer that connects to a local Kafka broker, converts each
    row of the DataFrame to JSON format, and sends it to the specified topic. A 1-second delay is
    added between messages to control the flow rate.

    Args:
        df (pd.DataFrame):
            The DataFrame containing the data to be sent to Kafka.
        topic (str):
            The Kafka topic to which the messages will be sent.

    Returns:
        None

    Raises:
        Exception:
            If an error occurs during producer initialization or message sending.
    """
    logging.info(f'Starting to send messages to topic "{topic}".')
    
    try:
        producer = KafkaProducer(bootstrap_servers="localhost:9092",
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        
        for index, row in df.iterrows():
            dict_row = dict(row)
            json_row = json.dumps(dict_row)
            producer.send(topic, value=json_row)
            time.sleep(1)
            
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            logging.info(f"Message sent at {timestamp}")
        
        producer.close()
        
    except Exception as e:
        logging.exception(f"An error was encountered: {e}")