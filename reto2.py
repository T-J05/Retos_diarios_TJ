#Ordenamiento simple: Escribe una función que ordene una lista de 5 enteros utilizando cualquier método de ordenamiento que prefieras (por ejemplo, burbuja, inserción, selección).
def Ordenamiento_simple(lista):
    new = []
    tamaño = len(lista)
    while tamaño > 0:
        minimo = min(lista)
        lista.remove(minimo)
        new.append(minimo)
        tamaño = len(lista)
    return new

lista = []
p = True

while p:
    p = input("Si desea añadir números a la lista escriba 'si', cuando termine escriba 'ver': ").lower()
    if p == "si":
        nr = int(input("Ingrese el número: "))
        lista.append(nr)
    elif p == "ver":
        lista_ordenada = Ordenamiento_simple(lista)
        print("Lista ordenada:", lista_ordenada)
        break