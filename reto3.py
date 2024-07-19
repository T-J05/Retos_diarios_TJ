#Recorrido en profundidad (DFS): Implementa un recorrido DFS para un grafo simple con 5 nodos.
grafo = {
    '1': ['2', '3'],
    '2': ['3', '1'],
    '3': ['2', '4'],
    '4': ['3', '5'],
    '5': ['4'],
}

visitado = set()

def recorrido(visitado, grafo, nodo_actual):
    if nodo_actual not in visitado:
        
        print(f'Nodo: {nodo_actual} Aristas: {','.join(grafo[nodo_actual])}') 
        visitado.add(nodo_actual)
        
         
        for vecino in grafo[nodo_actual]:
            recorrido(visitado, grafo, vecino)  


recorrido(visitado, grafo, '1')
