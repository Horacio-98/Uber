from car import car 

class uberx(car) : 
    brand = str
    model = str
    
    def __init__(self, license, driver,brand,model) -> None:
        super().__init__(license, driver)
        self.brand = brand
        self.model = model
        
    def getbrand(self) : 
        return self.brand
    
    def getmodel(self) : 
        return self.model
    
