#Auto y Motor: Implementa una clase Auto que contenga una instancia de una clase Motor con un método para describir el motor.
class Motor:
    def __init__(self):
        self.tipo = 'Diesel'
        self.potencia = ' 130 caballos de fuerza (hp).'
    def describir_motor(self):
        print(f'Motor: {self.tipo}\nSu potencia es: {self.potencia}')
        
    

class Auto:
    def __init__(self,marca):
        self.marca =  marca
        self.motor = Motor()

    def describir_auto(self):
        print(f'La marca del auto es: {self.marca}')
        print('Descripcion del motor: ')
        self.motor.describir_motor()


aut = Auto("Toyota")
aut.describir_auto()