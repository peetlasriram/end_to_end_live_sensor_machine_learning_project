import sys
from sensor.exception import SensorException
from sensor.logger import logging
import os
from sensor.constants import DATABASE_NAME,MONGODB_URL_KEY
import pymongo
import certifi


ca=certifi.where()

class MongoDBClient:
    """
    class name: Export_data_into_feature_store
    Description: This method exports the dataframe from mongoDB feature store as dataframe
    output: Connection to mongoDB data base
    on failure: raise an Exception """
    client=None
    def __init__(self,data_base_name=DATABASE_NAME):
        try:
            if MongoDBClient.client is None:
                mongo_db_url=os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key :{MONGODB_URL_KEY} is not set")
                MongoDBClient.client= pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
            self.client=MongoDBClient.client
            self.database=self.client[data_base_name]
            self.database_name=data_base_name
            logging.info("MongoDB Connection successfull")
        except Exception as e:
            raise SensorException(e,sys)
