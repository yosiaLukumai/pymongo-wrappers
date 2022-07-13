# importing some of the modules
from pymongo import MongoClient


class PyMongoWrappers:
    """
    PyMongoWrappers like Mongoose enables someone to fast create, Model(Collections)
    Use it to Search and navigate on the given cluster
    """
    url = ""
    def __init__(self, url=None):
        if url == None:
            # create the default from mongoclient
            self.connection = MongoClient()
        else:
            self.connection = MongoClient(url)

    def createModel(self, data:dict):
        """
        The method is very helpful in creating the model structure that one will be using
        To create a  colllection
        """
        pass

    def createCollection(self, data:dict):
        print('created the collection')
        pass

    def closeConnection(self, ):
        """
        The method will be closing the connection with the database disconnecting the server
        """
    def testDatabase(self, ):
        return self.connection['test_database']

    def searchData(self, data):
        pass



connection = PyMongoWrappers()

print(type(connection.testDatabase()))