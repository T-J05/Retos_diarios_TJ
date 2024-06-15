#Obs: me presento algunos problemas al usar el teclado numerico recomiendo usar los numeros del
#covencional.


def ordenar_numeros_ascentente ():
    numero = [] #inicializamos una lista vacia 
    while numero != 0: #mientras el nr ingresado no sea 0 pregunta nuevamente

        #pide al usuario los nrs a ordenar 
        nr = input("ingrese los numeros que desee ordenar en forma ascentente e ingrese 0 para ver la lista: ")

        #verificamos si es en entero lo que ingreso e añadimos a la lista
        if nr.isdigit():
            nr = int(nr)
            numero.append(nr)
        
        #cuando la persona ingresa 0 le mostramos la lista ya ordenada
            if nr == 0:
                numero.sort() #usamos el .sort para ordenar los elementos
                print(f"lista de numeros ordenados : {numero}")
                break
        #si es que lo ingresado no es un numero natural no continua 
        else:
            print("debe ingresar un numero natural")

      
#llamamos a la funcion
ordenar_numeros_ascentente()


    
    
 
   
    
       
        
        