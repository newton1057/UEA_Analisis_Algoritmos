import numpy as np
import heapq

def branch_and_bound(cost_matrix):
    num_people, num_tasks = cost_matrix.shape
    best_cost = float('inf')
    best_assignment = None

    # Nodo del grafo: (costo acumulado, asignación parcial, tarea actual)
    initial_node = (0, [], 0)
    priority_queue = [initial_node]

    while priority_queue:
        current_cost, current_assignment, current_task = heapq.heappop(priority_queue)

        # Si ya hemos asignado todas las tareas, comparamos el costo con el mejor encontrado hasta ahora
        if current_task == num_tasks:
            if current_cost < best_cost:
                best_cost = current_cost
                best_assignment = current_assignment
        else:
            # Ramificar el nodo actual: asignar la tarea actual a cada persona posible
            for person in range(num_people):
                if person not in current_assignment:
                    new_cost = current_cost + cost_matrix[person][current_task]
                    if new_cost < best_cost:
                        new_assignment = current_assignment + [person]
                        heapq.heappush(priority_queue, (new_cost, new_assignment, current_task + 1))

    return best_assignment, best_cost

# Ejemplo de uso
cost_matrix = np.array([
    [9, 2, 7, 8], #P0
    [6, 4, 3, 7], #P1
    [5, 8, 1, 8], #P2
    [7, 6, 9, 4] 
])

best_assignment, best_cost = branch_and_bound(cost_matrix)
print("Asignación óptima de tareas a personas:", best_assignment)
print("Costo mínimo:", best_cost)