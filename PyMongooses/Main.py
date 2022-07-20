from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.errors import ServerSelectionTimeoutError

class Main:
    """
    PyMongoWrappers like Mongoose enables someone to fast create, Model(Collections)
    Use it to Search and navigate on the given cluster 
    """
    # self.modelsNames = []
    def __init__(self, databaseName: str, url=None, modelsNames=None):
        if modelsNames == None:
            self.modelsNames = []
        else:
            self.modelsNames = modelsNames
        # self.url = f"{url}{databaseName}"
        try:
            if(url is not None):
                client = MongoClient(url)
            else:
                client = MongoClient()
            client.server_info()
            self.client = client
            # extract the database we want 
            self.databaseName = databaseName
            self.db = client[databaseName]
            self.connected = True
        except ServerSelectionTimeoutError as err:
            self.connected = False
            print(">> Check the Url Name its seems is not Okk, Example: mongodb://localhost:27017/ ")
            exit(-1)
        except Exception as e:
            self.connected = False
            print(e.args[0])
            exit(-1)
        # try:
        #     self.connectionUrl = MongoClient(url)
        #     # validating the database url
        #     if(self.connectionUrl.server_info()):
        #         pass
        #     else:
        #         raise ServerSelectionTimeoutError(message="Check the name of the url Provided")
        #     self.connected = True
        #     self.connection = self.connectionUrl[databaseName]
        #     print(">>> Succesful connection")
        #     # testing the connections 
        # except ConnectionFailure as e:
        #     print(">>> Check the server connection turn it on")
        #     print(e.args())
        #     exit(-1)
                
  
    def model(self, SchemaGiven: object, name: str):
        """
        The method is very helpful in creating the model structure that one will be using
        To create a  collection
        """
        try:
            # we start first with the assertation 
            assert isinstance(SchemaGiven, type(SchemaGiven)), "Sorry the type of Object passed should be from the Schema"
            if self.modelsNames is not None and name not in self.modelsNames:
                self.modelsNames.append(name)
            else:
                raise Exception("The names of the Model Already Exists")
            return SchemaGiven
        except Exception as e:
            print(f">>> {name:} {e.args[0]}, Try assingnig the other name")
            exit(-1)

    def createCollection(self, collectionName:str):
        """
        The method return the collection of the database name
        args:
                    Name of Collection 
        """
        try:
            return self.db.create_collection(collectionName)
        except Exception as e:
            print(">>> Error ")
            exit(-1)
        
    def dropTheCollection(self, collectionName: str):
        """
        The method delete the collection passed complely
        args:
                Name of the collection
        """
        try:
            return self.db.drop_collection(collectionName)
        except Exception as e:
            print(">>> Error ")
            exit(-1)
        

    def _getModels(self, ):
        return self.modelsNames

    def closeConnection(self, ):
        """
        The method will be closing the connection with the database disconnecting the server
        """
        pass


    def sizeOfDataBase(self):
        """
        Return the size of the given database
        """
        pass

    def getDatabase(self, databaseName:str):
        """
        Return the instance of the database passed
        Args: 
            databaseName: str example PyMongoose.connection.getDatabase("Testing")
        """
        try:
            return self.client.get_database(databaseName)
        except Exception as e:
            print(">>> Error ")
            exit(-1)
        
    

    def getCollectionNames(self):
        """
        The methods return the collections of the database name passed
        """
        try:
            return self.db.list_collection_names()
        except Exception as e:
            print(">>> Error ")
            exit(-1)
        
    def getPortAndHost(self):
        """
        Methods returns the port and the host
        return: 
            Tuple --> (Port, )
        """
        try:
            return (self.client.PORT, self.client.HOST)
        except Exception as e:
            print(">>> Error ")
            exit(-1)
        
    
    def testDatabase(self, ):
        try:
            return self.connection['test_database']
        except Exception as e:
            print(">>> Error ")
            exit(-1)
        return self.connection['test_database']

    def listMyDatabases(self,):
        """
        The methods return the list of the database that connection has accessed
        """
        try:
            return self.client.list_database_names()
        except Exception as e:
            print(">>> Error ")
            exit(-1)
    

    





# print(connection.listMyDatabases())

# connection = PyMongoose('testOnisa',"mongodb://localhost:27017/")

# col = db['users']






