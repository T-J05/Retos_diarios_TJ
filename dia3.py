def contar_vocales():
    contador = []
    palabra = input ("ingrese una palabra que desee saber la cantidad de vocales que tiene ")
    
    A=0
    e=0
    i=0
    o=0
    u=0

    #inicializamos una lista vacia 
    cuantas_vocales_hay = []

    #agregamos a la lista vacia una letra si es que se cumple alguna condicion 
    for palabra1 in palabra:    
        if "a" in palabra1:
                    contador.append ("a")
                    A = 0 + 1
                    cuantas_vocales_hay.append(f"A={A}")

        if "e" in palabra1:
                    contador.append ("e")
                    e = 0 + 1
                    cuantas_vocales_hay.append(f"E ={e}")
        if "i" in palabra1:
                    contador.append ("i")
                    i = 0 + 1
                    cuantas_vocales_hay.append(f"I = {i}")
        if "o" in palabra1:
                    contador.append ("o")
                    o = 0 + 1
                    cuantas_vocales_hay.append(f"O = {o}")
        if "u" in palabra1:
                    contador.append ("u")
                    u = 0 + 1
                    cuantas_vocales_hay.append(f"U = {u}")


    #Ve si es que hay alguna mayuscula en la palabra 
    for palabra1 in palabra:    
        if "A" in palabra1:
                    contador.append ("A")
                    A = 0 + 1
                    cuantas_vocales_hay.append(f"A={A}")

        if "E" in palabra1:
                    contador.append ("E")
                    e = 0 + 1
                    cuantas_vocales_hay.append(f"E ={e}")
        if "I" in palabra1:
                    contador.append ("I")
                    i = 0 + 1
                    cuantas_vocales_hay.append(f"I = {i}")
        if "O" in palabra1:
                    contador.append ("O")
                    o = 0 + 1
                    cuantas_vocales_hay.append(f"O = {o}")
        if "U" in palabra1:
                    contador.append ("U")
                    u = 0 + 1
                    cuantas_vocales_hay.append(f"U = {u}")
        
    #usamos len para saber cuantos elementos fueron agregados en lista 
    print(f"esta palabra tiene {len(contador)} vocales")
    #imprimimos el contenido de la lista
    print(cuantas_vocales_hay)
    
   

    
    
contar_vocales ()