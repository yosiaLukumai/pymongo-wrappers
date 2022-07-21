import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 


from PyDbSchema.Schema import Schema
from PyDbSchema.Main import Main
connection = None
Schema.connection = connection



def connect(dataBaseN:str, urlNa=None):
    global connection
    dataBaseName = dataBaseN
    urlName = urlNa
    connection = Main(dataBaseN, urlNa)
    if connection.connected:
        Schema.connection = connection
        print(f">> DataBase Connected , DataBaseName:{dataBaseN}")
        return True
    else:
        print("Failed to connect the database")
        return False









