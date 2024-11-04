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

def get_kafka_consumer(topic: str) -> None:
    """
    Initializes a Kafka consumer to listen to a specified topic.
    
    Args:
        topic (str): The name of the Kafka topic to listen to.
    """
    
    logging.info(f'Starting to listen to topic "{topic}".')
    
    try:
        consumer = KafkaConsumer(topic, bootstrap_servers="localhost:9092",
                                 value_deserializer=lambda v: json.loads(v.decode('utf-8')))
        
        data = []
        
        for message in consumer:
            message = message.value
            
            data.append(message)
            
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            offset = message.offset
            logging.info(f"Message with offset {offset} received at {timestamp}: {message}")
            
        consumer.close()
        logging.info("All messages received successfully. Consumer closed.")

        return data   
    except Exception as e:
        logging.exception(f"An error was encountered: {e}")

def get_kafka_producer(df: pd.DataFrame, topic: str) -> None:
    """
    Sends messages from a DataFrame to a specified Kafka topic.
    
    This function initializes a Kafka producer, iterates over the rows of the provided DataFrame,
    converts each row to JSON, and sends it to the specified Kafka topic.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the data to be sent.
        topic (str): The Kafka topic to which the messages will be sent.
    """
    
    logging.info(f'Starting to send messages to topic "{topic}".')
    
    try:
        producer = KafkaProducer(bootstrap_servers="localhost:9092",
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        
        for index, row in df.iterrows():
            json_row = row.to_json()
            producer.send(topic, value=json_row)
            time.sleep(1)
            
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            logging.info(f"Message sent at {timestamp}")

        producer.close()
        
        logging.info("All messages sent successfully. Producer closed.")
    except Exception as e:
        logging.exception(f"An error was encountered: {e}")