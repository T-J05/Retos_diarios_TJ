#Búsqueda en lista ordenada: Implementa una función de búsqueda binaria que determine si un número está en una lista ordenada de 10 elementos.
def busqueda_binaria(lista, elemento):
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        
        if lista[medio] == elemento:
            return medio  # Devuelve el índice donde se encontró el elemento
        
        elif lista[medio] < elemento:
            inicio = medio + 1  # Busca en la mitad superior
        
        else:
            fin = medio - 1  # Busca en la mitad inferior
    
    return None  # Elemento no encontrado

# Ejemplo de uso
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
nr = int(input("Ingrese el número que desea buscar: "))
resultado = busqueda_binaria(lis, nr)
if resultado is not None:
    print(f"El número {nr} se encontró en el índice {resultado}")
else:
    print(f"El número {nr} no se encontró en la lista.")