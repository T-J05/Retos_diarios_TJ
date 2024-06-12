def multiplicar (numero):
    #recorre en un rango de 1 al 11 
    for i in range (1,11):
        tabla_numero = numero * i #agg a una variable el numero que deseas multiplicar y lo multiplica por cada numero recien iterado
        print (f'{numero_multiplicar}x{i}={tabla_numero}') #imprimimos el numero a multiplicar por cada numero multiplicado y sus resultados
numero_multiplicar = int (input ('ingrese el numero que desea multiplicar ')) #pedimos al usuario que ingrese el numero del cual desea su tabla
multiplicar (numero_multiplicar) #llamamos a la funcion y le cargamos la varible en donde esta alogado el nr que ingreso el usuario