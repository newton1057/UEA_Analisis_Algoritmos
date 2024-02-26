import matplotlib.pyplot as plt
import time
#Esta funcion se trata de una funcion cubica debido a que su complejidad de cada for es  O(n) ya que depende la cantidad de elementos (n) al realizar el recorrido de For, al ser 3 For en la funcion este es n al cubo.

def funcion_cubica(n):
    suma = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                suma = 0
        


tiempos = []
valores_n = range(1,300)

for n in valores_n:
    tiempo_inicial = time.time()
    funcion_cubica(n)
    tiempo_final = time.time()
    tiempo_total = tiempo_final - tiempo_inicial
    tiempos.append(tiempo_total)

print(len(tiempos))
print(len(valores_n))



plt.plot(valores_n,tiempos)
plt.xlabel("Valores n")
plt.ylabel("Tiempo total")
plt.title("Funcion Cubica")
plt.show()
