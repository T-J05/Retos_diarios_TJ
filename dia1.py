def invertir_palabras(palabra):
    #len "revisa" cada letra que esta en letra y vemos si es 0 retorna un valor vacio
    if len(palabra) == 0 :
        return ""
    else :
        # letra [-1] toma la ultima letra de la palabra que que se ingresa,
        return palabra [-1] + invertir_palabras(palabra[:-1]) #operacion slicing

resultado = invertir_palabras(input ('ingrese la palabra que desea invertir ')) #pide el texto que desea ser invertido
print (len(invertir_palabras(resultado))) #imprime la cantidad de letras
print (resultado)