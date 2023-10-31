#Ejercicio 1 
def contar_digitos(n):
    # Convierte el número a una cadena para contar los dígitos
    num_str = str(n)
    # Usa la función len() para contar la longitud de la cadena
    cantidad_de_digitos = len(num_str)
    return cantidad_de_digitos

# Ejemplo de uso
numero = int(input("Ingrese un numero entero positivo: "))
resultado = contar_digitos(numero)
print(f"El número {numero} tiene {resultado} dígitos.")

#Ejercicio 2
def es_potencia(n, b):
    if n == 1:
        return True  # Cualquier número elevado a la potencia 0 es 1
    if n < 1 or b < 1:
        return False  # No se admiten números no positivos

    exponente = 0
    resultado = 1
    while resultado < n:
        resultado = b ** exponente
        exponente += 1

    return resultado == n

# Ejemplo de uso
n = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
resultado = es_potencia(n, b)
if resultado:
    print(f"{n} es potencia de {b}.")
else:
    print(f"{n} no es potencia de {b}.")

#Ejercicio 3

def encontrar_posiciones(a, b, start=0, results=None):
    if results is None:
        results = []

    # Encuentra la primera aparición de b en a a partir de la posición start
    index = a.find(b, start)

    if index != -1:
        # Si se encontró una posición, la agregamos a la lista de resultados
        results.append(index)
        # Llamamos recursivamente a la función para buscar más ocurrencias
        encontrar_posiciones(a, b, index + 1, results)

    return results

# Ejemplo de uso
a = (input("Ingrese una palabra: "))
b = (input("Ingresa una letra de la palabra para ver su posicion: "))
posiciones = encontrar_posiciones(a, b)
print(f"Las posiciones de '{b}' en '{a}' son: {posiciones}")

#Ejercicio 4 

def par(n):
    if n == 0:
        return True  # 0 se considera par
    else:
        return impar(n - 1)

def impar(n):
    if n == 0:
        return False  # 0 no se considera impar
    else:
        return par(n - 1)

# Ejemplo de uso
numero = int(input("Ingrese un numero entero: "))
if impar(numero):
    print(f"{numero} es impar.")
else:
    print(f"{numero} es par.")

#Ejercicio 5 
def encontrar_mayor(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        sub_mayor = encontrar_mayor(lista[1:])
        if lista[0] > sub_mayor:
            return lista[0]
        else:
            return sub_mayor

# Ejemplo de uso
mi_lista = [10, 5, 20, 8, 15]
mayor = encontrar_mayor(mi_lista)
print(f"El mayor elemento de la lista es: {mayor}")

#Ejercicio 6 
def replicar(lista, n):
    if n <= 0:
        return []
    else:
        if lista:
            return lista + replicar(lista, n - 1)
        else:
            return replicar(lista, n - 1)

# Ejemplo de uso
mi_lista = [1, 3, 3, 7]
n = 2
replicada = replicar(mi_lista, n)
print(replicada)

#Ejercicio 7 
def summatory(n, p):
    if n == 1:
        return p
    else:
        return n * p + summatory(n - 1, p)
n = int(input("Ingrese un número n: "))
p = int(input("Ingrese un número p: "))
 
result = summatory(n, p)

print(f"El resultado de K({n}, {p}) es: {result}")

#Ejercicio 8 
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

# Ejemplo de uso
fila = 5
columna = 2
resultado = pascal(fila, columna)
print(f"El valor en la fila {fila} y columna {columna} del Triángulo de Pascal es: {resultado}")

#Ejercicio 9

def combinaciones(lista, k, cadena_actual="", indice=0):
  if k == 0:
      print(cadena_actual)
      return
  if indice == len(lista):
      return
  # Incluye el carácter actual en la cadena actual y llama recursivamente con k-1.
  combinaciones(lista, k - 1, cadena_actual + lista[indice], indice)
  # Omite el carácter actual y llama recursivamente con el mismo k.
  combinaciones(lista, k, cadena_actual, indice + 1)

# Ejemplo de uso:
caracteres = ['a', 'b', '3', '4']
k = 3
combinaciones(caracteres, k)


#Ejercicio 10
def medidas_hoja_A(N):
    if N == 0:
        return (841, 1189)  # Medidas de la hoja A0
    else:
        ancho_anterior, largo_anterior = medidas_hoja_A(N - 1)
        nuevo_ancho = largo_anterior
        nuevo_largo = ancho_anterior // 2  # Usamos división entera para obtener números enteros
        return (nuevo_ancho, nuevo_largo)

# Ejemplo de uso
N = int(input("Ingrese el numero de la hoja. Ejemplo A'4': "))
ancho, largo = medidas_hoja_A(N)
print(f"Medidas de la hoja A({N}): Ancho = {ancho} mm, Largo = {largo} mm")





