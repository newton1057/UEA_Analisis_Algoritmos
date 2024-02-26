from queue import Queue

class Nodo:
    def __init__(self,Persona, Tarea, Costo, Padre):
        self.Persona = Persona
        self.Tarea = Tarea
        self.Costo = Costo
        self.Hijos = []
        self.Padre = Padre

def Solucion_Optimista (Matriz_Costos, Persona):  #Persona = 0
    Costo_Optimista = 0
    Mejor_Costo_Persona = 0

    Tareas_Ocupadas = [0,3]
    
    for Persona in range (Persona , len(matriz_costos)):
        for Tarea in range (len(matriz_costos[Persona])):
            if Tarea in Tareas_Ocupadas:
                print("Tarea ocupadad" + str(Tarea))
            #print(Tarea)
        

def BB (matriz_costos):
    Tareas = len(matriz_costos)
    Personas = len(matriz_costos[0])

    MA = 0
    #Indice_Tarea_PreAsignada = 0
    for Indice_Tarea_Preasignada in range(len(matriz_costos)):
        print (Indice_Tarea_Preasignada)
        Costo = matriz_costos[0][Indice_Tarea_Preasignada]
        print (Costo)

        
    #Tarea_PreAsignada = matriz_costos[0][Indice_Tarea_PreAsignada]
    Costos_Temporales = matriz_costos[1] 

    #del Costos_Temporales [Indice_Tarea_PreAsignada]
    Posible_Tarea = min(matriz_costos[1])
    print(Costos_Temporales)
    #Costos_Temporales.remove(6)
    #//print(Costos_Temporales)

def Asignar_Hijos( Nodo_Padre : Nodo, Tareas_Asignadas, Tareas_Ocupadas, Persona):
    for Tarea in range(len(Tareas_Asignadas)):
        if Tarea not in Tareas_Ocupadas:
            Nodo_Hijo = Nodo(Persona, Tarea, Tareas_Asignadas[Tarea], Nodo_Padre)
            Nodo_Padre.Hijos.append(Nodo_Hijo)
    
    return Nodo_Padre

def Imprimir_Hijos (Nodo: Nodo):
    print("Persona " + str(Nodo.Persona))
    print("Tarea: " + str(Nodo.Tarea))
    print("Costo: " + str(Nodo.Costo))
    for x in range(len(Nodo.Hijos)):
        print(Nodo.Hijos[x].Costo, end=" ")
    
    print("")
    print("")

def Crear_Hijos (Matriz_Hijos, Nodo: Nodo):
    Nodo.Hijos = Matriz_Hijos
    print("Hijos asignados")


def Crear_Grafo (Matriz_Costos):
    Nodo_Raiz = Nodo(None,None,None,None)
    #Nodo_Padre = Nodo_Raiz
    
     
    for Persona in range(len(Matriz_Costos)-1):
        for Tareas in range(len(Matriz_Costos[Persona])):
            
            Costo = Matriz_Costos[Persona][Tareas]
            Nodo_ = Nodo(Persona, Tareas, Costo, None)
            
            Hijos = [] 

            for Tarea in range(len(Matriz_Costos[Persona+1])):
                Costo = Matriz_Costos[Persona+1][Tarea]
                Nodo_i = Nodo(Persona+1, Tarea, Costo, Nodo_)
                Hijos.append(Nodo_i)
            
            Nodo_.Hijos = Hijos

            Imprimir_Hijos(Nodo_)
    

        

        

Nodo_Raiz = Nodo(None,None,None,None)
    
matriz_costos = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

Crear_Grafo(matriz_costos)