class Muebles :
    
    def __init__(self,tipo,color,material) -> None:
        self.tipo = tipo
        self.color = color 
        self.material = material
        
        
    def utilidad(self) : 
        print(f'Este objeto es ', self.tipo)
    

class Auto:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed
    
class Rectangulo : 

    def __init__(self,largo,ancho):
        self.largo = largo
        self.ancho = ancho
        
    def operacion_area(self) :
        print(f'Area del rectangulo = ', self.ancho * self.largo) 
        
    def operacion_perimetro(self) : 
        print('Perimetro del rectangulo = ', ((self.ancho*2) + (self.largo*2)))
    

    
class Persona: 
    def __init__(self, nombre, apellido_m, apellido_p, edad):
        self.nombre=nombre
        self.apellido_p=apellido_p
        self.apellido_m=apellido_m
        self.edad=edad
        
    def saludar(self): 
        print(f'Hola mundo, me llamo {self.nombre} {self.apellido_p} {self.apellido_m} y tengo {self.edad} años')


class Perro: 
    def __init__(self, nombre, raza, color):
        self.nombre = nombre
        self.raza = raza
        self.color = color
        
        
    def ladrar(self):
        print('Guau Guau')
        
    def presentacion(self): 
        print(f'Hola soy el perro {self.nombre}, soy de color {self.color} y soy de raza {self.raza}. Cuando ladro hago {self.ladrar()}') 
        
'''

Perro_1 = Perro('Gazir','Golden','Cafe')
Perro_1.presentacion()     
        

car = Auto("Toyota", "Camry", 2020, 0)
print("Speed:", car.get_speed())
car.accelerate()
print("Speed:", car.get_speed())
car.accelerate()
print("Speed:", car.get_speed())
car.brake()
print("Speed:", car.get_speed())


Persona_1 = Persona('Horacio','Granados','Argumedo',24)
Persona_1.saludar()

'''

rectangulo_1 = Rectangulo(10,8)
rectangulo_1.operacion_area()
rectangulo_1.operacion_perimetro()

