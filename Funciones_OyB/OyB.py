# Ordenamiento de burbuja (Bubble Sort)
def bubble_short (arr):
    n=len(arr)
    for i in range(n):
        swapped= False
        for j in range (0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]#intercambiar elementos
                swapped = True
        if not swapped:
            break # si no hay intercambios la lista esta ordenada

        

# Orden de selección (Selection Sort)

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        #cambiar el minimo encontardo por el primer elmento       
        arr[i],arr[min_index]=arr[min_index],arr[i]

# Tipo de inserción (Insert Sort)
def insetion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key = arr[i]
        j=i-1
        while j >=0 and key <arr[j]:
            arr[j +1]=arr[j]
            j-=1
        arr[j+1]= key


# Combinar ordenamiento (Merge Sort)



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def b_lineal (datos, element):
    for i in range(len(datos)):
        if str(datos[i]) == element:
            print("El elemento se encontró en la posición: ", i)
            break
    if str(datos[i]) != element:
        print("El elemento no se ha encontrado.")
        
def b_binaria(lista, elemento):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2 

        if str(lista[medio]) == elemento:
            return medio 
        elif str(lista[medio]) < elemento:
            izquierda = medio + 1 
        else:
            derecha = medio - 1

    return -1

