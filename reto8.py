#Pilas y colas: Implementa las operaciones básicas de una pila y/o una cola para 5 elementos.

def pila (accion):
    pila = []
    while accion:
        if accion == "off":
            
            break
        if accion == "eliminar":
            if pila:
                pila.pop(-1)
            else:
                print("No hay nada en la pila")
        if accion == "insertar":
            valor = int (input("ingrese el nr que desee agregar a la pila: "))
            pila.append(valor)
        if accion == "ver":
            pilanew = []
            for elemento in pila:
                pilanew.append(elemento)
            pilanew.reverse()
            for ele in pilanew:
                print (ele)
        accion = input ("Ingrese lo que desea realizar eliminar/off/insertar/ver: ")



def cola (accion):
    cola = []
    while accion:
        if accion == "off":
            
            break
        if accion == "eliminar":
            if cola:
                cola.pop(0)
            else:
                print("No hay nada en la cola")
        if accion == "insertar":
            valor = int (input("ingrese el nr que desee agregar a la cola: "))
            cola.append(valor)
        if accion == "ver":
            colanew = []
            for elemento in cola:
                colanew.append(elemento)
            colanew.reverse()
            for ele in colanew:
                print (ele)
        accion = input ("Ingrese lo que desea realizar eliminar/off/insertar/ver: ")

while True:
    pilas_colas= input ("Escriba que metodo desea utilizar pila/cola (si desea parar escriba off): ")
    if pilas_colas == "pila":
        accion =  input ("Ingrese lo que desea realizar eliminar/off/insertar/ver: ")
        pila(accion)
    if pilas_colas == "cola":
        accionn = input  ("Ingrese lo que desea realizar eliminar/off/insertar/ver: ")
        cola(accionn) 