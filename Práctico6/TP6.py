import random


# Ejercicio 1
# list_numbers=[]
# while True:
#     number=int(input("ingrese un numero o 0 para terminar: "))
#     if number == 0:
#         break
#     list_numbers.append(number)

# print(list_numbers)

# # Ejercicio 2

# if len(list_numbers)>0:
#     number=int(input("ingrese un numero para eliminarlo de la lista: "))
#     if number in list_numbers:
#         list_numbers.remove(number)
#         print(f'se elimino la primera ocurrencia de {number}')
#     else:
#         print(f"el numero {number} no esta en la lista")
# print(list_numbers)

# #Ejercicio 3
# sum_numbers=sum(list_numbers)
# print(f"la suma de los numeros es: {sum_numbers}")

# # Ejercicio 4

# number=int(input("ingrese un numero: "))
# list_numbers_min=[]
# for element in list_numbers:
#     if element < number:
#         list_numbers_min.append(element)

# for element in list_numbers_min:
#     print(element,",")

# #5Ejercicio 5
# frequency_list =[(num,list_numbers.count(num))for num in set(list_numbers)]
# print("Lista de tuplas (elemento, frecuencia):")
# print(frequency_list)

# # Ejercicio 6

# primary_school_students=set()
# secondary_school_students=set()

# while True:
#     name_primary=input("Ingrese el nombre de cada estudiante de nivel primario (para finalizar escriba 'x'): ")
#     if name_primary == "x":
#         break
#     primary_school_students.add(name_primary)
    

# while True:
#     name_secondary=input("Ingrese el nombre de cada estudiante de nivel secundario (para finalizar escriba 'x'): ")
#     if name_secondary == "x":
#         break
#     secondary_school_students.add(name_secondary)
    
# print("Los nombres de los estudiantes de nivel primario son:")
# for name in primary_school_students:
#     print(name)

# print("Los nombres de los estudiantes de nivel secundario son:")
# for name in secondary_school_students:
#     print(name)

# repeated_names = primary_school_students & secondary_school_students
# print("Los nombres que se repiten entre nivel primario y secundario son:")
# for name in repeated_names:
#     print(name)

# unique_names_primary = primary_school_students - secondary_school_students
# print("Los nombres de nivel primario que no se repiten en nivel secundario son:")
# for name in unique_names_primary:
#     print(name)

# Ejercicio 7
# ocurrencias = {}

# # Contador para rastrear la cantidad de strings procesados
# strings_procesados = 0

# # Procesar strings hasta alcanzar un límite de 50
# while strings_procesados < 50:
#     entrada = input("Ingrese un string (o 'x' para finalizar): ")
#     if entrada == 'x':
#         break

#     # Incrementar el contador de strings procesados
#     strings_procesados += 1

#     # Contar las ocurrencias de caracteres en el string
#     for caracter in entrada:
#         if caracter in ocurrencias:
#             ocurrencias[caracter] += 1
#         else:
#             ocurrencias[caracter] = 1

# # Mostrar las ocurrencias de caracteres
# for caracter, cantidad in ocurrencias.items():
#     print(f"'{caracter}': {cantidad}")

# Ejercicio 8

# goles = [
#     [3, 2, 1, 3, 1, 2, 4, 1, 0, 2],
#     [1, 2, 0, 1, 2, 5, 2, 0, 3, 2],
#     [2, 7, 1, 0, 1, 3, 2, 0, 1, 3],
#     [1, 2, 0, 5, 1, 1, 0, 2, 3, 0],
#     [2, 1, 1, 0, 1, 1, 2, 0, 1, 1],
#     [1, 0, 1, 1, 2, 0, 1, 0, 2, 2],
#     [0, 1, 2, 0, 1, 1, 0, 0, 2, 3],
#     [2, 1, 1, 2, 1, 2, 1, 0, 2, 1],
#     [1, 0, 1, 1, 0, 1, 2, 2, 1, 0],
#     [1, 2, 1, 0, 1, 0, 2, 0, 1, 0]
# ]

# # Inicializar listas para triunfos, empates, derrotas, goles marcados y goles recibidos
# triunfos = [0] * 10
# empates = [0] * 10
# derrotas = [0] * 10
# goles_marcados = [0] * 10
# goles_recibidos = [0] * 10
# puntos = [0] * 10

# # Calcular estadísticas
# for i in range(10):
#     for j in range(10):
#         if i != j:
#             goles_equipo_i = goles[i][j]
#             goles_equipo_j = goles[j][i]
#             goles_marcados[i] += goles_equipo_i
#             goles_recibidos[i] += goles_equipo_j

#             if goles_equipo_i > goles_equipo_j:
#                 triunfos[i] += 1
#                 puntos[i] += 3
#             elif goles_equipo_i == goles_equipo_j:
#                 empates[i] += 1
#                 puntos[i] += 1
#             else:
#                 derrotas[i] += 1

# # Mostrar las estadísticas para cada equipo
# for equipo in range(10):
#     print(f"Equipo {equipo + 1}:")
#     print(f"Triunfos: {triunfos[equipo]}")
#     print(f"Empates: {empates[equipo]}")
#     print(f"Derrotas: {derrotas[equipo]}")
#     print(f"Goles marcados: {goles_marcados[equipo]}")
#     print(f"Goles recibidos: {goles_recibidos[equipo]}")
#     print(f"Diferencia de goles: {goles_marcados[equipo] - goles_recibidos[equipo]}")
#     print(f"Puntos: {puntos[equipo]}\n")

#Ejercicio 9	Escribir un programa que simule el juego clásico de Memoria (Memotest)
# utilizando matrices. El juego consiste en un tablero de cartas 
# boca abajo y el objetivo es encontrar todas las parejas de cartas iguales.

def crear_tablero(filas, columnas):
    numeros = list(range(1, (filas * columnas) // 2 + 1))
    cartas = numeros + numeros
    random.shuffle(cartas)
    tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            tablero[i][j] = cartas.pop()
    return tablero

def mostrar_tablero(tablero, cartas_volteadas):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if (i, j) in cartas_volteadas:
                print(tablero[i][j], end=" ")
            else:
                print("X", end=" ")
        print()

filas = 4
columnas = 4
tablero = crear_tablero(filas, columnas)
cartas_volteadas = []
parejas_encontradas = 0
intentos = 0

while parejas_encontradas < (filas * columnas) // 2:
    mostrar_tablero(tablero, cartas_volteadas)
    try:
        fila1 = int(input("Ingrese la fila de la primera carta: ")) - 1
        columna1 = int(input("Ingrese la columna de la primera carta: ")) - 1
        fila2 = int(input("Ingrese la fila de la segunda carta: ")) - 1
        columna2 = int(input("Ingrese la columna de la segunda carta: ")) - 1
    except (ValueError, IndexError):
        print("Entrada inválida. Intente nuevamente.")
        continue

    if (fila1, columna1) == (fila2, columna2):
        print("No puedes seleccionar la misma carta dos veces.")
        continue

    if tablero[fila1][columna1] == tablero[fila2][columna2]:
        parejas_encontradas += 1
        cartas_volteadas.append((fila1, columna1))
        cartas_volteadas.append((fila2, columna2))
        print("¡Encontraste una pareja!")
    else:
        cartas_volteadas = []
        print("No coinciden. Inténtalo de nuevo.")
        
    intentos += 1

print("¡Has ganado! Encontraste todas las parejas en", intentos, "intentos.")



# #Ejercicio 10

# # Definir una matriz cuadrada como una lista de listas
# matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

# # Obtener la diagonal principal
# diagonal_principal = [matriz[i][i] for i in range(len(matriz))]

# # Obtener la diagonal inversa
# diagonal_inversa = [matriz[i][len(matriz) - i - 1] for i in range(len(matriz))]

# print("Diagonal Principal:", diagonal_principal)
# print("Diagonal Inversa:", diagonal_inversa)

# # Ejercicio 11
# money={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# dato = input("Ingrese la moneda a buscar")
# if dato in money:
#     for e in money:
#         if dato == e:
#             print(money[e])
# else:
#     print("La moneda no esta en el diccionario")

# #Ejercicio 12

# name=input("Ingrese su nombre: ")
# edad=int(input("Ingrese su edad: "))
# direccion=input("Ingrese su direccion: ")
# telefono=int(input("Ingrese su numero de telefono: "))

# usuario_info={"nombre":name, "edad": edad, "direccion": direccion, "telefono": telefono}
# print(f'{usuario_info["nombre"]} tiene {usuario_info["edad"]} años, vive en {usuario_info["direccion"]} y su numero de telefono es {usuario_info["telefono"]}')

# #Ejercicio 13

# precio_frutas={"mandarina":100,"manzana":150,"banana":200,"naranja":150,"pera":200}
# fruta=input("Ingrese el nombre de la fruta: ").lower()
# kilos=float(input("Ingrese la cantidad de kilos: "))
# precio_total=0
# if fruta in precio_frutas:
#     precio_total = (precio_frutas[fruta] * kilos)
#     print(f"El precio de {kilos} kilos de {fruta} es ${precio_total:.2f}")
# else:
#     print(f"Lo siento, la fruta {fruta} no está en la lista de precios.")
