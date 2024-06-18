def convertor_C_a_F (): #iniciamos una funcion

    red = '\033[91m' #ponemos el codigo ANSI del color rojo
    end = '\033[0m'  #ponemos el codigo ANSI para delimitar hasta donde va el color que inicalizamos anteriormente

    while True: #iniciamos el bucle 
        print('si desea parar el programa digite "00"') 
        #pedimos al usuario que ingrese la temperatura en grados celsius 
        celsius = ( input('Ingrese una temperatura en grados celsius para obtenerlo en grados Fahrenheit: '))


        if celsius.isdigit(): #verificamos si es que es un nr flotante o entero haga la operacion
            celsius = float(celsius)
            Fahrenheit = (celsius * 1.8) + 32
            Fahrenheitt = round(Fahrenheit,3) #redondeamos el resultado a maximo dos a tres numeros luego de la coma
            print (f'El grado que ingreso es de {Fahrenheitt} Fahrenheit') #mostramos el resultado ya redondeado


            #si es que el usuario ingreso una cadena de caracteres se devuelve un msj de error con los colores 
            #antes definidos
        if celsius == str(celsius): 
           
            print (f'{red} "error ingrese un numero entero o en decimales"{end}')

        #si es que el usuario ingresa 00 se termina el programa
        if celsius == 00:
            break
        
        
convertor_C_a_F() #llamamos a la funcion
