def diccionario ():#creamos la funcion
    dic = {} #inicializamos diccionario vacio
    

    while True : #usamos bucle while para que se repita el proceso hasta que se cumpla una condicion
        
        print ('escriba en clave: "ver" si desea ver el diccionario,y para terminar el programa: "off"')
        clave = input ('ingrese la clave del diccionario: ')
        

        if clave == 'off':
            print (dic) #mostramos el diccionario
            break


        if clave == 'ver':
            print (dic) #mostramos el diccionario
            clave = input ('ingrese la clave del diccionario: ')
            

        valor = input (f'ingrese el valor para la clave: {clave}: ')
        
            #guardamos las claves y los valores en el diccionario
        dic[clave.lower()] =valor.lower() + '|'
        
       
        
     #llamamos a la funcion   
diccionario ()
        
        
