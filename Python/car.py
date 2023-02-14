class car : 
    id = int
    license = str 
    driver = str
    passenger = str
    
    
    def __init__(self, license, driver) -> None:
        self.license = license
        self.driver = driver
        
    def printData(self):
        print("Nombre del conductor : ", self.driver)
        print("Licencia del conductor : ", self.license)
        