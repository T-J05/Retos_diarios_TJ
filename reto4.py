#Recorrido en amplitud (BFS): Implementa un recorrido BFS para un grafo simple con 5 nodos

grafo = {
    '1': ['2', '3'],
    '2': [ '1','3'],
    '3': [ 'A'],
    'A': ['3', '5'],
    '5': ['A']
}

cola= []
visitado = {}

def bfs (grafo,visitado,cola,nodo):
        
        for nodos in grafo:
            visitado[nodos]= False
        visitado[nodo]= True
        cola.append(nodo)
        while cola:
              nodo = cola.pop(0)
              print (f'nodo actual: {nodo}')
              for vecinos in grafo[nodo]:
                    print(vecinos)
                    if visitado[vecinos]:
                          continue
                    else: 
                          visitado[vecinos] = True

                          cola.append(vecinos)
       
                    nodo = vecinos
        
        
bfs (grafo,visitado,cola,'1')