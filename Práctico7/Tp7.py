#Ejercio 1
def bubble_short(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]= lista[j+1], lista[j]

bubble_list =[2,25,65,42,3,8,56,24,65]

print(f"Lista desordenada, {bubble_list}")
bubble_short(bubble_list)
print(f"Lista ordenada, {bubble_list}")
#Ejercio 2

def selection_sort_palabras(list):
    n = len(list)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]

words = input("Ingrese una lista de palabras separadas por espacio: ").split()
print(f"Lista desordenada, {words}")
selection_sort_palabras(words)
print(f"Lista ordenada, {words}")

#Ejercio 3

lista_libros = [
    {"titulo": "El Alquimista", "autor": "Paulo Coelho", "año": 1988},
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967},
    {"titulo": "Moby Dick", "autor": "Herman Melville", "año": 1851},
    {"titulo": "Orgullo y Prejuicio", "autor": "Jane Austen", "año": 1813}
]
def sort_books_by_year(books):
    return sorted(books, key=lambda x: x["año"])
def sort_books_by_autho(books):
    return sorted(books, key=lambda x: x["autor"])

# Ejemplo de uso
books_ordered_by_year = sort_books_by_year(lista_libros)
print("Libros ordenados por año:")
for book in books_ordered_by_year:
    print(book)

print("\n")

books_sorted_by_author = sort_books_by_autho(lista_libros)
print("Libros ordenados por autor:")
for book in books_sorted_by_author:
    print(book)

#Ejercio 4

def insert_sort(list):
    for i in range(1, len(list)):
        clave = list[i]
        j = i - 1
        while j >= 0 and len(clave) < len(list[j]):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = clave


list_cadena = ["manzana", "pera", "banana", "uva", "kiwi", "ciruela"]
insert_sort(list_cadena)
print("Lista ordenada por longitud:")
print(list_cadena)

#Ejercio 5

def insertion_sort(list):
    for i in range(1, len(list)):
        clave = list[i]
        j = i - 1
        while j >= 0 and len(clave) > len(list[j]):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = clave

list_cadena = ["manzana", "pera", "banana", "uva", "kiwi", "ciruela"]
insertion_sort(list_cadena)
print("Lista ordenada por longitud de manera descendente:")
print(list_cadena)



#Ejercio 6

def ordenamiento_por_conteo(list):
    maximum = max(list)
    addition = [0] * (maximum + 1)

    for num in list:
        addition[num] += 1

    resultado = []
    for i in range(len(addition)):
        resultado.extend([i] * addition[i])
    return resultado

lista_numeros = [4, 2, 1, 4, 2, 0, 3, 2]
lista_ordenada = ordenamiento_por_conteo(lista_numeros)
print("Lista ordenada:")
print(lista_ordenada)


#Ejercio 7

def ordenar_numeros_y_cadenas(lista):
    # Separar números y cadenas
    numeros = [elemento for elemento in lista if isinstance(elemento, (int, float))]
    cadenas = [elemento for elemento in lista if isinstance(elemento, str)]

    numeros.sort()
    cadenas.sort()
    
    lista_ordenada = numeros + cadenas
    return lista_ordenada


lista_mixta = [10.1, 'manzana', 5, 'pera', 3, 'banana', 8, 'uva', 'kiwi', 2, 'ciruela']
lista_ordenada = ordenar_numeros_y_cadenas(lista_mixta)
print("Lista ordenada:")
print(lista_ordenada)

#Ejercio 9

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    # Dividir la lista en mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    # Aplicar recursión a ambas mitades
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)
    # Combinar las dos mitades ordenadas
    return fusionar(izquierda, derecha)

def fusionar(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

lista_numeros = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = merge_sort(lista_numeros)
print("Lista ordenada:")
print(lista_ordenada)
