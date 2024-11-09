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

def get_kafka_consumer(topic: str) -> list:
    """
    Initializes a Kafka consumer to listen to a specified topic.
    
    This function creates a Kafka consumer that connects to a local Kafka broker, listens to the
    specified topic, and collects messages. Each message is logged with its offset and timestamp.

    Args:
        topic (str):
            The name of the Kafka topic to listen to.

    Returns:
        list:
            A list containing all received messages from the Kafka topic.

    Raises:
        Exception:
            If an error occurs during consumer initialization or message processing.
    """
    logging.info(f'Starting to listen to topic "{topic}".')
    
    try:
        consumer = KafkaConsumer(topic, bootstrap_servers="localhost:9092",
                                 value_deserializer=lambda v: json.loads(v.decode('utf-8')),
                                 consumer_timeout_ms=3000,
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=True)
        
        data = []
        
        for kafka_message in consumer:
            message = kafka_message.value
            
            data.append(message)
            
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            offset = kafka_message.offset
            logging.info(f"Message with offset {offset} received at {timestamp}: {message}")
        
        logging.info("All messages received successfully. Closing the consumer.")
        consumer.close()
        logging.info("Consumer closed.")

        return data   
    except Exception as e:
        logging.exception(f"An error was encountered: {e}")

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