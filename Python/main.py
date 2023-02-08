# Importamos el archivo car y dentro de el la clase car
from car import car

if __name__ == "__main__" : 
    
    # Creacion de la instancia 
    car_1 = car()
    
    # Asignando valores a objeto
    car_1.license = "ZFY127"
    car_1.driver = "Horacio Granados"
    print(vars(car_1))
    
    # Objeto No.2
    car_2 = car()
    car_2.license = "XLS128"
    car_2.driver = "Juan Salvador"
    print(vars(car_2))