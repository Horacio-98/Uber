from car import car

class uberblack(car) :
    
    typeCarAccepted = []
    seatsMaterial = [] 
    
    
    def __init__(self, license, driver) -> None:
        super().__init__(license, driver)