from queue import Queue

# Definimos el árbol:
arbol = {
    "A": ["B", "F", "H"],
    "B": ["C", "D", "E"],
    "C": [],
    "D": [],
    "E": [],
    "F": ["G"],
    "G": [],
    "H": ["I", "J"],
    "I": [],
    "J": []
}

Busqueda = []
# Definir función para hacer búsqueda en anchura:
def ba(arbol, nodo_raiz):
    # Creamos una cola para el BFS
    cola = Queue()
    # Agregamos el nodo raíz a la cola
    cola.put(nodo_raiz)

    while not cola.empty():
        # Sacamos un nodo de la cola
        nodo_actual = cola.get()
        # Imprimimos el nodo actual
        print(nodo_actual, end="")
        # Agregamos los hijos del nodo actual a la cola
        for hijo in arbol[nodo_actual]:
            cola.put(hijo)

# Búsqueda en anchura en el árbol con el nodo raíz "A"
ba(arbol, "A")