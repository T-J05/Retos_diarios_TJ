#10 eliminar duplicados: Implementa una función que elimine los elementos duplicados de una lista de 10 enteros.

def eliminar_duplicados(lista):
    listanew = []
    for elemento in lista:
        if elemento in listanew:
            listanew.remove(elemento)
            lista.append(elemento)
        else:
            listanew.append(elemento)
       
    print (listanew)

lista = [1,2,3,4,5,6,7,8,9,10,4,5,7,9]

eliminar_duplicados(lista)