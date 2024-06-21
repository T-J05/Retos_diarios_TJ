import random

movimientos = ["-", "*", "<"]
cont = 0
def evaluacion(movimientop, movimientom):
    if movimientop == movimientom:
        return "empate"
    elif (movimientop == "-" and movimientom == "*") or (movimientop == "*" and movimientom == "<") or (movimientop == "<" and movimientom == "-"):
        return "humano"
    else:
        return "maquina"

print ("piedra= *, papel = -, tijera = <")
movimientopp = input("Ingresa el movimiento que quieras (-, *, <): ")

if movimientopp in movimientos:
    movimientomm = random.choice(movimientos)
    print("Movimiento de la máquina:", movimientomm)

    resultado = evaluacion(movimientopp, movimientomm)

    if resultado == "empate":
        print("Empate.")
    elif resultado == "humano":
        print("GANASTE")
    elif resultado == "maquina":
        print("LA MAQUINA GANO(TERMINEITOR)")

    else:
        print("Movimiento inválido. Debes ingresar uno de los siguientes movimientos: -, *, <.")
  
