class DataBase:
    _instance = None
    _data = {}
    
    def get_instance(self):
        if self._instance == None:
            self._instance = DataBase()
        return self._instance
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, str):
        self._data[len(self._data)] = str

def output(dict):
    for key, item in dict.items():
        print(f'{key}: {item}')

if __name__ == "__main__":
    DB = DataBase()
    DB1 = DB.get_instance()
    DB1.data = "Object 0; description of object 0; author of object 0."
    DB1.data = "Object 1; description of object 1; author of object 1."
    DB1.data = "Object 2; description of object 2; author of object 2."
    DB1.data = "Object 3; description of object 3; author of object 3."    

    DB2 = DB.get_instance()
    DB2.data = "Object 5; description of object 5; author of object 5."
    
    if id(DB1) == id(DB2):
        print("Success! Data Base has only one instance")
    else:
        print("Failture! Data Base has several instances.")
    
    output(DB1.data)