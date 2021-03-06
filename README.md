# **Powerful python library like Mongoose**


## ***PyDbSchema Features***
The library enable one to create Schema validates the Schema.

The Library will also insert the Default values when one provided
and it in schema but didn't provide during insertation.

The library is very hand and it's objects are directly Pymongo 
collection Object do one configuration the all of the.

Schema can access pymongo Object method the Shema are Collection Level,
Let Bring the Mongoose Flavour.


## ***Requirements || dependecies***
pymongo >= 3.0


# Usage
## ***Configuration***
Create a folder with the database configuration then pass
database name and url or name only

        # import the module
        import PyDbSchema
        PyDbSchema.connect(<DatabaseName: str>)
        # Test if the database if connected
        if PyDbSchema.connection.connected:
            print("Connected")

So by this one folder all the database Configuration are ready
Note: This code mostly should be at the top so as to enable Schema to access conection



### ***Models Creation***

Create a folder and insert all of your model Rules here 

        # For Example here
        import PyDbSchema
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
        }

        ## Creating the Schema
        User = PyDbSchema.Schema(<Skelrton:dict>, <NameSchema: str>)
        # The Schema object is Collection Object by nature and pymongo methods can be used in itds


## ***Using the Schema Object Method***

The Schema Object perform all of the methods like how pymongo Object will perform
but Crud( Create Read Update Delete) operation are easier as follows


## ***Creating***
Note: Advantages of PyDbSchema is that it's Schema are validated and default value are passed if not there
### **Methods**

Model.insertOne(data<dic>)     -> # Insert One object passed into the collection Used

Model.bulkInsert(data<list>)  -> # Insert list of object passed into the collection Used

        Example
        # Inserting Document
        # Create a folder and database configuration
        # Create the Models  Folder
        # Inside creates Schema Objects
        Example 
        from Models.User import User # We were having a folder with py file having User Object of the class of Schema
        mydata = {
        "Name": "Jack",
        'email': 'yosiaLukumai@gmail.com',
        }
        response = User.insertOne(credentials)
        print(response) #Return pymongo result object

        # Inserting Many Objects 
        ListOfData [
        {
                "Name": "Jack",
                'email': 'yosiaLukumai@gmail.com'
        },
        {
                "Name": "Onisa",
                'email': 'jr@gmail.com'
        }      
        ]

        response = User.bulkInsert(credentials)




## ***Finding***
Note: The Schema skeleton will be used for all of this methods
### **Methods**

Model.find(credential<dict>)     -> # find the Documents required and return list according to the credential passed

Model.findOne(data<dict>)       -> # Find and return only one document if credentials passed

        # Find One Result
        # Import the Schema Objects
        # Example 
        from Models.User import User # We were having a folder with py file having User Object of the class of Schema
        credentials = {"Name": 'Yosia'}
        response = User.findOne(credentials)
        print(response) # Check the Response

        # To find many Use the findMany
        credentials = {"Name": 'Yosia'}
        response = User.find(credentials) # Return multiple of the instance found


## ***Updating***
Note: The Schema skeleton will be used for all of this methods
### **Methods**

Model.updateOne(credentialForSearching<dict>, newdata,dict>)     -> # update one according to credentil passed and new data to be inserted

Model.updateMany(credentialForSearching<dict>, newdata,dict>)     -> # update Many according to credentil passed and new data to be inserted

        # Find One Result
        # Import the Schema Objects
        Example 
        
        from Models.User import User # We were having a folder with py file having User Object of the class of Schema
        myquery = { "Name": "Yosia" }
        newvalues = {"Name": "Shadrack" }
        response = User.updateOne(myquery, newvalues)
        print(response) # Check the Response

        # To updateMany  Use the <Model>.updateMany(dataForSearching<dict>, newData<dict>)
        response = User.updateMany(dataForSearching<dict>, newData<dic>)
        # check response like how pymongo insert method does like
        print(response.matched_count)


## ***Deleting***
Note: The Schema skeleton will be used for all of this methods
### **Methods**

Model.deleteOne(credential<dict>)      -> # delete one according to credentil passed 

Model.deleteMany(credential<dict>)     -> # delete Many according to credentil passed 

        # Find One Result
        # Import the Schema Objects
        Example 
        
        from Models.User import User # We were having a folder with py file having User Object of the class of Schema
        response = User.deleteMany(myquery, newvalues)
        print(response) # Check the Response
        credentials = {"Name": 'Yosia'}
        # To updateMany  Use the <Model>.deleteMany(credentials:dict)
        credentials = {"Name": 'Yosia'}
        response = User.deleteOne(credentials<dict>)
        # check response like how pymongo insert method does like



## ***FindById***
Just pass the id and model will give you the back whole document

        # Example
        from Models.User import User # We were having a folder with py file having User Object of the class of Schema
        response = User.findById(id)
        print(response) # Check the Response


## ***Using Schema as Object as Pymongo Collection***
Just Use the attribute inside the Schema the collection attribute example

        # Example
        from Models.User import User # We were having a folder with py file having User Object of the class of Schema
        # collection
        collection = User.collection
        type(User.collection) # Return <class 'pymongo.collection.Collection'>
        # so all of the pymongo collection methods can be used
        # like
        collection.create_index,  next, watch






## Powered By: Yosia Lukumai

Github Account: <https://github.com/yosiaLukumai>

Email me trough: <a href = "mailto:yosialukumai.com?subject = Feedback&body = Message">yosiadev@gmail.com</a>
