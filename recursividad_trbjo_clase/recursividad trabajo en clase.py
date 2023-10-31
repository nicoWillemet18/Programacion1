# 1. Escribir una función que simule el siguiente experimento: Se tiene una rata en una
# jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma
# probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5
# minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula.
# La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero
# quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.
# La función debe devolver el tiempo que tarda la rata en salir de la jaula

import random

def tiempo_para_salir_de_jaula():
    tiempo_transcurrido = 0

    while True:
        eleccion = random.randint(1, 3)  # Elegir uno de los 3 caminos al azar

        if eleccion == 1:
            tiempo_transcurrido += 3
        elif eleccion == 2:
            tiempo_transcurrido += 5
        else:
            tiempo_transcurrido += 7
            break  # La rata ha salido de la jaula

    return tiempo_transcurrido

# Simula el experimento y muestra el tiempo que tarda la rata en salir
tiempo_total = tiempo_para_salir_de_jaula()
print(f"La rata tardó {tiempo_total} minutos en salir de la jaula.")

# Escribir una consigna apropiada para la siguiente función. Asumir que n es un número
# entero.
def f(n):
    s=str(n)
    if len(s)<=1:
        return s
    return s[-1]+f(int(s[:-1]))

print(f(1090))
#respuesta:
#Escribe una función recursiva llamada f que toma un número entero n como entrada y devuelve 
# una cadena que representa la versión inversa de n. La función debe implementar la inversión 
# del número utilizando recursión. Por ejemplo, si se llama a f(1234), la función debería devolver "4321".