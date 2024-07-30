#Polimorfismo: Crea una clase base Animal con un método hacerSonido y una clase derivada Perro que sobrescriba este método.
class Animal:
    def __init__(self):
        pass

    def hacer_sonido (self):
        pass


class Perro(Animal):
    def __init__(self):
        super().__init__()
    
    def hacer_sonido(self,sonido,nombre):
        print(f'Hola soy {nombre},{sonido} {sonido}!')



perro = Perro()
perro.hacer_sonido('guau','Leo')

        