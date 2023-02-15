# Importamos el archivo car y dentro de el la clase car
from car import car
from account import account
from uberx import uberx

if __name__ == "__main__" :
    
    uberx_1 = uberx("127ZFY","Horacio","Suzuki","2019")
    print(vars(uberx_1))