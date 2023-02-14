# Importamos el archivo car y dentro de el la clase car
from car import car
from account import account

if __name__ == "__main__" :
     
    car_1 = car(123456,"Horacio Granados Argumedo") 
    car_1.printData()
    
    account_1 = account("Jeanett", "j_argumedo2271@hotmail.com")
    print(account_1.getData())