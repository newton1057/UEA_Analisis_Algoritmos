import matplotlib.pyplot as plt
import time

#En esta función, utilizamos un ciclo while que se ejecuta mientras n sea mayor que 1. En cada iteración, dividimos n entre 2 usando la división entera (operación n // 2), y luego incrementamos el contador count en 1.
def funcion_logaritmica(n):
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count
        
tiempos = []
valores_n = range(1,30000)

for n in valores_n:
    tiempo_inicial = time.time()
    funcion_logaritmica(n)
    tiempo_final = time.time()
    tiempo_total = tiempo_final - tiempo_inicial
    tiempos.append(tiempo_total)

plt.plot(valores_n,tiempos)
plt.xlabel("Valores n")
plt.ylabel("Tiempo total")
plt.title("Funcion Logaritmica")
plt.show()
