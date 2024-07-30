#Formas geométricas: Define una clase base FormaGeometrica con métodos calcular_area 
# y calcular_perimetro. Crea clases derivadas Rectangulo y Circulo que sobrescriban estos métodos.
import math

class FormaGeometrica:
    def __init__(self):
        pass
    def calcular_area(self):
        pass
    def calcular_perimetro(self):
        pass

class Rectangulo(FormaGeometrica):
    def __init__(self):
        super().__init__()
    
    def calcular_area(self,longitud,ancho):
        l = longitud 
        a = ancho
        area = l * a
        print(f'El area del rectangulo es: {area}')

    def calcular_perimetro(self,longitud,ancho):
       l = longitud 
       a = ancho
       perimetro = 2*(l +a)
       print(f'El perimetro del rectangulo es: {perimetro}')

class Circulo(FormaGeometrica):
    def __init__(self):
        super().__init__()
    
    def calcular_area(self,radio):
        area = math.pi * radio**2 #pi x radio^2
        print(f'El area del  circulo es: {area: .2f}')

    def calcular_perimetro(self,radio):
       circunferencia = 2 * math.pi * radio
       print(f'El circunferencia del circulo es: {circunferencia: .2f}')


rectangulo =    Rectangulo()
circulo = Circulo()
while True:
    consulta = input('Presione 1 para realizar operaciones con circulos, y 2 para rectangulo (para salir off): ')
    try:
        if consulta == '1':
            a_p = input('Presione 1 para calcular el area y 2 para calcular la circunferencia del circulo: ')
            if a_p == '1':
               radio = int(input('Ingrese el radio del circulo: '))
               circulo.calcular_area(radio)
            elif a_p == '2':
                radio = int(input('Ingrese el radio del circulo: '))
                circulo.calcular_perimetro(radio)
            else:
                print('ERROR, entrada no validaa')
                a_p = input('Presione 1 para calcular el area y 2 para calcular la circunferencia del circulo: ')
        elif consulta == '2':
            p_a = input('Presione 1 para calcular el area y 2 para calcular el perimetro del rectangulo: ')
            if p_a == '1':
              ancho = int(input('Igrese el ancho del rectangulo:'))
              longitud = int(input('Ingrese la longitud del rectangulo: '))
              rectangulo.calcular_area(longitud,ancho)
            elif p_a == '2':
              ancho = int(input('Igrese el ancho del rectangulo:'))
              longitud = int(input('Ingrese la longitud del rectangulo:'))
              rectangulo.calcular_perimetro(longitud,ancho)
            else:
                print('ERROR, entrada no valida')
                p_a = input('Presione 1 para calcular el area y 2 para calcular el perimetro del rectangulo: ')
        elif consulta.lower() == 'off':
            break
        

    except:
        print('ERROR, entrada no valida')
        consulta = input('Presione 1 para realizar operaciones con circulos, y 2 para rectangulo(para salir off): ')

