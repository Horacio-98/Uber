class account : 
    id = int
    name = str
    document = str
    email = str
    password = str
    
    def __init__(self, name, email) -> None:
        self.name = name 
        self.email = email
        
    def getData(self) : 
        return self.name, self.email
        
        
