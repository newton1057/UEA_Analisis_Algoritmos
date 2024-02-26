def calcular_tabla_hash(cadena):
    # Inicializa un diccionario para la tabla hash
    tabla_hash = {}
    
    # Recorre cada carácter en la cadena
    for caracter in cadena:
        # Incrementa el valor de la clave correspondiente en la tabla hash
        if caracter in tabla_hash:
            tabla_hash[caracter] += 1
        else:
            tabla_hash[caracter] = 1
    
    return tabla_hash

def son_anagramas(cadena1, cadena2):
    # Calcula la tabla hash para ambas cadenas
    tabla_hash1 = calcular_tabla_hash(cadena1)
    tabla_hash2 = calcular_tabla_hash(cadena2)
    
    print(tabla_hash1)
    print(tabla_hash2)
    # Compara las tablas hash
    return tabla_hash1 == tabla_hash2

# Ingresa las dos cadenas desde el usuario
cadena1 = input("Ingresa la primera cadena: ")
cadena2 = input("Ingresa la segunda cadena: ")

# Verifica si son anagramas e imprime el resultado
if son_anagramas(cadena1, cadena2):
    print("¡Son anagramas!")
else:
    print("No son anagramas.")