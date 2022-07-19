# Written By: Yosia Lukumai || github.com/yosiaLukumai
import PyMongoose

class Schema(PyMongoose.PyMongoose):
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

    def __init__(self, data:dict, timeStamp=True):
        PyMongoose.PyMongoose.__init__(self)
        # let validate the data before allowing it to enter the model then one will be validating it
        self.keys = []
        
        self.passedConstruction = self.checkKeyWords(data)
        if(self.passedConstruction):
            self.Schema = data
        else:
            exit(-1)
        
    
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
        

        def createOne(self, data:dict):
            validation = self.validateSchema(data)
            if(validation and self.connectionSuccesful):
                pass
        
        def bulkInsert(self, data:list):
            pass

        def searchOne(self, condition: dict):
            pass
                

                

            
        


User = {
    'Attributes':[{ "Name": {
        "dtype": str,
        "req": True,
        "default": None
        }},
        { "email": {
        "dtype": str,
        "req": True,
        "default": None
        }},
        { "date": {
        "dtype": str,
        "req": True,
        "default": None
        }},
        { "tradition": {
        "dtype": str,
        "req": False,
        "default": 'uji na chai'},}
        ]
}

newData = {
    "Name": "Yosia",
    'date': '12/3/2002',
    'email': 'yosiaLukumai@gmail.com',
}

# NewChema = Schema(User, 'Users')

# NewChema.validateSchema(newData)

# if __name__ == "__main__":
#     pass