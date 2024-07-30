#11 Clase de Punto 2D: Crea una clase Punto2D con atributos x & y, y un método para imprimir sus coordenadas.

class Punto2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def imprimir_coordenadas(self):
        print (f"Coordenada x: {self.x},coordenada y: {self.y}")


punto2d = Punto2d(3,5)
punto2d.imprimir_coordenadas()