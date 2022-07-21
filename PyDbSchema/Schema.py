# Written By: Yosia Lukumai || github.com/yosiaLukumai
from pymongo.errors import ConnectionFailure
from pymongo import MongoClient
from bson.objectid import ObjectId

class Schema:
    """
    This creates a prototype structure of the given  database object to be stored in the given collection 
    This collection will be used and  passed all of the attributes during inserting
    req: True || Check if the given attribute is there if it's not there it will yell out error
    This will be taken from the Collection Level,
    """
    defaultKeys = ['dtype', 'req', 'default']
    defaultValues = [str, bool, None]
    Schema = {}
    passedConstruction = False

    def __init__(self, data:dict,schemaName:str, timeStamp=True):
        # let validate the data before allowing it to enter the model then one will be validating it
        self.keys = []
        self.schemaName = schemaName
        self.passedConstruction = self.checkKeyWords(data)
        if(self.passedConstruction):
            self.Schema = data
        else:
            exit(-1)
        if(self.connection.connected):
            self.collection = self.connection.db[self.schemaName]
        
    
    def checkKeyWords(self, data: dict):
        # print(data['A'])
        # layer one  the keys and the values
        # assert 
        keys = []
        """
        here we are checking the keys on our dictionary
        Here we check the attribtes such as os there the 
        key named as Atrribute
        """
        try:
            keys = ['Attributes']
            for key in keys:
                assert key in data.keys()
        except AssertionError as e:
            print(">> The key is not in the pyMongoose || Wrong syntax of the model")  
            return False              

        # layer two checking

        try:
            assert isinstance(data['Attributes'], list)
        except (Exception, AssertionError) as e:
            print("""Type of the Atrributes Value should be list
                    Example: Attributes:["Name": 
                                            {"type": str
                                            "req": true"
                                            }
                                        ]
                """)
            return False
        # Checking the keys inside the data if there 
        try:
            for attribute in data['Attributes']:
                passedValueDtypes = []
                assert isinstance(attribute, dict) # check the type of the attribute is Dictionary
                assert len(attribute.keys()) == 1 # check the type len of the attribute is one 
                # assert isinstance(attribute.values(), dict)
                self.keys.append(list(attribute.keys())[0])
                for attr in attribute.values():
                    # assert isinstance(type(attr['default']), type(attr['dtype']))  # have to be checked
                    assert isinstance(attr, dict)
                    # checking for the keys in the dict
                    for key in attr.keys():
                        assert key in self.defaultKeys
                    # checking for the inner atrributes of the class
                    for value in attr.values():
                        # assert isinstance(value, in self.defaultValues)
                        for valu in self.defaultValues:
                            passedValueDtypes.append(valu == value)
                assert True in passedValueDtypes # checks if the data Types are there in the 
                

                    # print(attr.keys())
        except Exception as e:
            print(""">>> Error check your keys should valid....
                            Example:User = {
                            'Attributes':[{ "Name": {
                                "dtype": str,
                                "req": True,
                                "default": None
                                }},]
                    """)
            print(" >>> The keys should be like req, dtype default")
            return False
        

        return True
            
    def getConnectionObject(self, ):
        pass

    def validateSchema(self, newData:dict):
        enteredField = newData.keys()
        if(self.passedConstruction):
            # validate required file
            try:
                for attribute in newData:
                    assert attribute in self.keys
            except Exception as e:
                print(">>>  The key is't there in the schema")
                exit(-1)
            

            # here we again pass the data 
            try:
                # here we start with the assertations of the  data 
                for key in newData.keys():
                    currentObject = {}
                    for dic in self.Schema['Attributes']:
                        """
                        Checking if the key's exists in the schema
                        """
                        if list(dic.keys())[0] == key:
                            # found the oject now we start the comparison
                            currentObject = dic[key]
                            break
                    # now we start the connection 
                    # print(currentObject['dtype'])
                    for rule in currentObject.keys():
                        if rule == 'dtype':
                            assert currentObject['dtype'] == type(newData[key])
                
               

            except Exception as e:
                print(">> Check the dtypes of the data entered don't match the required one")
                exit(-1)
            

            """
            This checks if the required fields are all filled
            """
            try:
             # checking the required fields
                for field in self.Schema['Attributes']:
                    # print(field)
                    fieldName = list(field.keys())[0]
                    if(field[fieldName]['req']):
                        # print(list(enteredField))
                        assert fieldName in list(enteredField)
            except Exception as e:
                print(">>> A required field is missing value check your Schema for more comparison")
                exit(-1)
            
            """
            Adding up the default value if is't provided
            """
            try:
             # checking if the field with default value is there and doesn't have the value
                for field in self.Schema['Attributes']:
                    # print(field)
                    fieldName = list(field.keys())[0]
                    if(field[fieldName]['default']):
                        if fieldName in list(enteredField):
                            pass
                        else:
                            newData[fieldName] = field[fieldName]['default']
            except Exception as e:
                print(">>> A required field is missing value check your Schema for more comparison")
                exit(-1)

            return True
    

    def bulkValidateSchema(self, data: list):
        # here we need to loop over the list of the inserted data 
        try:
            for item in data:
                self.validateSchema(item)
                return True
        except Exception as e:
            print(">>> Error in the List of the documents passed")

    def insertOne(self, data:dict):
        validation = self.validateSchema(data)
        try:
            if(validation and self.connection.connected):
                collection = self.connection.db[self.schemaName]
                res = collection.insert_one(data)
                return res.acknowledged
                # print(self.schemaName)
                # print(type(collection))

        except Exception as e:
            print(e.args[0])
            print(">>> Error while inserting the docs")
            exit(-1)
    
    def bulkInsert(self, data:list):
        try:
            assert isinstance(data, list), "Bulk creation takes more than one object in dictionary"
            validation = self.bulkValidateSchema(data)
            if(validation and self.connection.connected):
                collection = self.connection.db[self.schemaName]
                res = collection.insert_many(data)
                return res

        except Exception as e:
            print(e.args[0])
            print(">>> Error in inserting the Bulk documents")


    def deleteOne(self, credentials: dict):
        """
        The method returns if the given credential have been deleted
        arg: 
            credentials such as {_id: 2442q4w56}
        
        Returns:
            The number of the objects deleted
        """
        try:
            if(self.connection.connected):
                collection = self.connection.db[self.schemaName]
                res = collection.delete_one(credentials)
                return res
            else:
                raise Exception("The client isn't connected")
        
        except Exception as e:
            print(e.args[0])
            print(">>> Invalid Query Recheck the credentials")
    
    def deleteMany(self, credential:list):
        """
        The method returns if the given credential have been deleted
        arg: 
            credentials such as {_id: 2442q4w56}
        
        Returns:
            The number of the objects deleted
        """
        try:
            if(self.connection.connected):
                collection = self.connection.db[self.schemaName]
                res = collection.delete_many(credential)
                return res
            else:
                raise Exception("The client isn't connected")
        
        except Exception as e:
            print(e.args[0])
            print(">>> Invalid Query Recheck the credentials")
    

    # Searching queries
    def find(self, credential: dict):
        """
        The fuction return the document obtained from the given search Query
        Args:
                credenttials example Users.find({"name": "Yosia"})
        Return:
            pymongo.cursor.Cursor with some array for the given data to be found
        """
        try:
            if(self.connection.connected):
                collection = self.connection.db[self.schemaName]
                res = collection.find(credential)
                return res
            else:
                raise Exception("The client isn't connected")
        
        except Exception as e:
            print(e.args[0])
            print(">>> Invalid Query Recheck the credentials Or Server Connection")

    def findOne(self, credential: dict):
        """
        The fuction return the document obtained from the given search Query
        Args:
                credenttials example Users.findOne({"name": "Yosia"})
        Return:
            pymongo.cursor.Cursor with some array for the given data to be found
        """
        try:
            if(self.connection.connected):
                collection = self.connection.db[self.schemaName]
                res = collection.find_one(credential)
                return res
            else:
                raise Exception("The client isn't connected")
        
        except Exception as e:
            print(e.args[0])
            print(">>> Invalid Query Recheck the credentials Or Server Connection")

    # Updating functions

    def updateOne(self, credential:dict, newData:dict):
        """
        The methods can update one of the docs according to the query passed
        Args:
            credentials type: dict Ex: Users.updateOne({"Name"})
        """
        try:
            if(self.connection.connected):
                collection = self.connection.db[self.schemaName]
                # construction the update Query
                updatingCondition = {"$set": newData}
                res = collection.update_one(credential, updatingCondition)
                return res
            else:
                raise Exception("The client isn't connected")
        
        except Exception as e:
            print(e.args[0])
            print(">>> Invalid Query Recheck the credentials Or Server Connection")

    
    def updateMany(self, credential: dict, newData:dict):
        """
        The methods updates all of the document that passes the conditon of the credentials
        Args:
                credential: dict and NewData:dict
        """
        try:
            if(self.connection.connected):
                collection = self.connection.db[self.schemaName]
                # construction the update Query
                updatingCondition = {"$set": newData}
                res = collection.update_many(credential, updatingCondition)
                return res
            else:
                raise Exception("The client isn't connected")
        
        except Exception as e:
            print(e.args[0])
            print(">>> Invalid Query Recheck the credentials Or Server Connection")
    

    def findById(self, id:str):
        """
        The method returns the Object obtained after passing the id
        Args: 
            id: Users.finfById("4562dfn612hdsmf")
        return:
            PyMongo Object
        """
        try:
            if(self.connection.connected):
                collection = self.connection.db[self.schemaName]
                # construction the update Query
                credential = {"_id": ObjectId(id)}
                res = collection.find_one(credential)
                return res
            else:
                raise Exception("The client isn't connected")
        
        except Exception as e:
            print(e.args[0])
            print(">>> Invalid Query Recheck the credentials Or Server Connection")

    
                                
            
