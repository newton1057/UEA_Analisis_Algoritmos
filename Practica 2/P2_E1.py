import matplotlib.pyplot as plt
import time

#Esta funcion se trata de una funcion lineal debido a que su complejidad es O(n) ya que depende la cantidad de elementos (n) al realizar el recorrido de For
def funcion_lineal(n):
    suma = 0
    for i in range(n):
        suma = 0

tiempos = []
valores_n = range(1,30000)

for n in valores_n:
    tiempo_inicial = time.time()
    funcion_lineal(n)
    tiempo_final = time.time()
    tiempo_total = tiempo_final - tiempo_inicial
    tiempos.append(tiempo_total)

plt.plot(valores_n,tiempos)
plt.xlabel("Valores n")
plt.ylabel("Tiempo total")
plt.title("Funcion Lineal")
plt.show()
