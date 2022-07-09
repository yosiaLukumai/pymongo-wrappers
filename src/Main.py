# importing some of the modules
from pymongo import MongoClient


class PyMongoWrappers:
    url = ""
    def __init__(self, url: str):
        self.client = MongoClient(url)
        print('initiated...')
        pass

    def createCollection(self, data:dict):
        print('created the collection')
        pass

    def searchData(self, data):
        pass



myPY = PyMongoWrappers('mongodb://localhost:27017/')