#Piloto de eventos (Priority Queue): Implementa una cola de prioridad utilizando una lista para insertar y eliminar 5 elementos.


def PriorityQueue():
    lista = []
    while True:
        accion = input("escriba lo que desea hacer con la lista añadir/eliminar/ver/stop: ").lower()
        if accion == "stop":
            break
        elif accion == "eliminar":
            if lista:
                lista.pop(0)  
            else:
                print("La lista está vacía.")
        elif accion == "añadir":
            nr = int(input("Ingrese el número que desea añadir a la lista: "))
            lista.append(nr)
            lista.sort(reverse=True)  
        elif accion == "ver":
            print(lista)
        else:
            print("Acción no válida. Intente de nuevo.")

PriorityQueue()