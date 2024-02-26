# Definir el grafo como una lista de listas
grafo_lista = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

# Inicializar el diccionario del grafo
grafo = {}

# Crear el diccionario del grafo a partir de la lista de listas
for i in range(len(grafo_lista)):
    nodo_padre = grafo_lista[i][0]
    nodos_hijos = grafo_lista[i][1:]
    grafo[nodo_padre] = nodos_hijos

# Imprimir el grafo como un diccionario
print(grafo)

