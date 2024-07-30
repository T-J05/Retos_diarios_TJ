#Cuenta bancaria: Implementa una clase CuentaBancaria con métodos para depositar y consultar el saldo.

class CuentaBancaria:
    def __init__(self,saldo):
        self.saldo = saldo
        

    def depositar (self,monto):
        if monto:
            self.saldo = self.saldo + monto
            print(f'El monto que ha depositado es de: {monto}')
            


    def consultar(self):
        if self.saldo :
            print(f'Su saldo es de: {self.saldo}')
        else: 
            print('No tienes nada nde sogue')

saldo = int (input('Ingrese su saldo actual: '))
banco = CuentaBancaria(saldo)

while True:
    accion = input ('Si desea consultar el saldo presione 1, si desea depositar 2, para salir 3: ')
    if accion == "3":
        break
    elif accion == '1':
        banco.consultar()
    elif accion == '2':
        monto = int(input('Ingrese el monto que desee ingresar: '))
        banco.depositar(monto)
    else: 
        print('Presiona una accion correcta')

