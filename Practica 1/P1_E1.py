
razas_gatos = ["munchkin", "ragdoll", "bombay", "maine coon", "esfinge"] #O(n)
total_gatos = [5, 3, 3, 5, 4] #O(n)
inventario = {} #O(C1) => O(1)

for i in range(len(razas_gatos)): #O(n)
    inventario[razas_gatos[i]] = total_gatos[i] # O(C2) => O(1)

print(inventario) # O(C3) => O(1)

# Dado a que la complejidad es dada por la cantidad de elementos en razas_gatos y tanto razas_gatos como total_gatos es de igual longitud, la complejidad es Lineal
# Por lo tanto, la complejidad total del programa sigue siendo O(n), ya que las operaciones dentro del bucle son constantes y no afectan la complejidad general del programa.
