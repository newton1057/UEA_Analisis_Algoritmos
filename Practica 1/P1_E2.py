# Diccionarios de cada centro de adopción
gatos1 = {"munchkin": 3, "esfinge": 1, "bombay": 2}
gatos2 = {"bombay": 1, "manx": 2, "esfinge": 1}
gatos3 = {"ragdoll": 1, "munchkin": 1}
gatos4 = {"maine coon": 3}
gatos5 = {"munchkin": 1, "maine coon": 4}

# Diccionario que almacenará el resultado final
total_gatos = {}

# Recorremos cada centro de adopción y su diccionario correspondiente
for centro in [gatos1, gatos2, gatos3, gatos4, gatos5]:
    for raza, cantidad in centro.items():
        if raza in total_gatos:
            total_gatos[raza] += cantidad
        else:
            total_gatos[raza] = cantidad

print(total_gatos)
