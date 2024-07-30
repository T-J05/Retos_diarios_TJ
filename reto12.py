#Figura y Círculo: Crea una clase base Figura con un método imprimir y una clase derivada 
# Círculo que extienda Figura y sobreescriba el método imprimir
class Figura:
    def __init__(self):
        
        pass
    def imprimir(self,lado,alto,ancho,figura):

        print(f'El lado del {figura}: {lado}')
        print(f'El alto del {figura}: {alto}')
        print(f'El ancho del {figura}: {ancho}')


class Circulo(Figura):
    def __init__(self):
        super().__init__()
    
    def imprimir(self,circunferencia,radio):
        print(f'La circunferencia del circulo es de : {circunferencia}')
        print(f'El radio del circulo es de : {radio}')


circulo = Circulo()
circulo.imprimir(12,4)
