# Setting the work directory
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Python Modules
from src.extract.whr_extraction import *
from src.transform.whr_transformation import *
from src.transform.whr_preprocessing import *
from src.services.kafka import *

if __name__ == "__main__":
    happiness_dataframes = extracting_data()
    
    df = transforming_data(happiness_dataframes)
    
    df = preprocessing_data(df)
    
    get_kafka_producer(df, "whr_kafka_topic")