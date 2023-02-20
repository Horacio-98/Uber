# Importamos el archivo car y dentro de el la clase car
from car import car
from account import account
from uberx import uberx
from payment import payment
from paypal import paypal

if __name__ == "__main__" :
    
    paypal_1 = paypal('5','dawdawd')
    print(paypal_1.info())
    