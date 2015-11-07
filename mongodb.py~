import pymongo
from pymongo import MongoClient
class Mongodb:
        def __init__(self,database):
		self.client = MongoClient('localhost', 27017)
                self.db = self.client[database] 
        def set_collection(self,collection_name):
            self.collection = self.db[collection_name]
        
        def insert(self,data):
            return self.collection.insert_one(data).inserted_id

        def get_all(self):
            cursor = self.collection.find()
            return [doc for doc in cursor]
        
        def get_one(self):
            cursor = self.collection.find_one()
            return [ row for row in cursor]

        def get_range(self,start,end):
            cursor = self.collection.find()[start:end]
            return [ row for row in cursor]
        
        


