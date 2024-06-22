#Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable 
# (entre 8 y 16 caracteres) que incluya letras mayúsculas, minúsculas, números y símbolos.
import random


def contraseña ():
    pregunta = input("si desea generar una contraseña escriba generar, si no presione cualquier tecla y luego enter: " )
    if pregunta == "generar":
          preguntaf = True
          contrasenha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","k","r","s","t","u","v","w","x","y","z",
                         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ",
                              "O", "P", "K", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","1","2","3","4","5","6","7","8","9",
                              "#","&","%","$","?","*","!","¡","¿"]
          
          conr = random.randint(8,16)
          connn = random.choices(contrasenha ,k = conr)
          consin = " ".join(connn)
     
          print (consin)
     

          while preguntaf == True:
               contraseña()
          
contraseña()
    