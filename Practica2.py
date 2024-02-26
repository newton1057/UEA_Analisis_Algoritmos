def encontrar_pares_con_suma(arr, suma_objetivo):
    # Crear un diccionario para almacenar los números que ya hemos visto
    vistos = {}
    pares = []

    for num in arr:
        # Calcular el número necesario para alcanzar la suma objetivo
        complemento = suma_objetivo - num

        # Verificar si el complemento ya está en el diccionario
        if complemento in vistos:
            # Si lo encontramos, agregamos el par a la lista de pares
            pares.append((num, complemento))

        # Agregamos el número actual al diccionario de números vistos
        vistos[num] = True

    return pares


# Convertir la cadena de entrada en una lista de enteros
lista_entrada = [2,10,3,7,9]

# Pedir al usuario que ingrese la suma objetivo
suma_objetivo = 12

# Encontrar los pares que suman la cantidad objetivo
resultado = encontrar_pares_con_suma(lista_entrada, suma_objetivo)

# Imprimir los pares encontrados
if resultado:
    print("Pares que suman la cantidad objetivo:")
    for par in resultado:
        print(par)
else:
    print("No se encontraron pares que sumen la cantidad objetivo.")