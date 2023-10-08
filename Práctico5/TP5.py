from funciones import *

# Ejercicio 1

indentification=str(input("Ingrese el número de DNI: "))

result=dni_valido(indentification)
print(result)

# Ejercicio 2

phrase=str(input("Ingrese una frase: "))

result=length_last_word(phrase)
print("La longitud de la última palabra es de: ", result, " letras.")


# Ejercicio 3

print("Bienvenido a SportClub")

while True:
    print("Para salir ingrese un nombre vacío.")
    name=input("Ingrese su nombre: ")
    name=name.strip()
    names=name.split()

    if len(name)==0:
        break

    last_name=input("Ingrese su apellido: ")
    last_name=last_name.strip()
    one_last_name=last_name.split()
    
    if len(names)<=2 and len(one_last_name)==1: 
        dni=input("Ingrese su DNI: ")
        dni_valido(dni)
    else:
        print("Por favor ingrese 2 nombres como máximo y un único apellido")

    identifier(names, last_name, dni)    

# Ejercicio 4

number_one=int(input("Ingrese el primer número:"))
number_two=int(input("Ingrese el segundo número: "))

multiplier(number_one, number_two)

# Ejercicio 5

days = int(input("Ingrese el número de días a calcular: "))

for i in range(days):
    temp_max = float(input(f"Ingrese la temperatura máxima del día {i+1}: "))
    temp_min = float(input(f"Ingrese la temperatura mínima del día {i+1}: "))

    medium_temperature = calculate_average_temperature(temp_max, temp_min)
    print(f"La temperatura media del día {i+1} es: {medium_temperature}°C")

# Ejercicio 6

phrase = input("Ingrese un texto: ")
spaces = space_between(phrase)
print("Frase con espacio entre letras:", spaces)

# Ejercicio 7

numbers = []

while True:
    inp = input("Ingrese un número (o presione Enter para terminar): ")
    if inp == "":
        break
    try:
        number = float(inp)
        numbers.append(number) #Se almacenan los números ingresados por el usuario en la lista "numbers"
    except ValueError:
        print("Número no válido. Intente otra vez.")

max, min = max_min(numbers)
if max is not None and min is not None:
    print("Máximo:", max)
    print("Mínimo:", min)
else:
    print("No se ingresaron números válidos.")

# Ejercicio 8

try:
    radio = float(input("Ingrese el radio de la circunferencia: "))
    area, perimeter = circumference_perimeter(radio)
    if area is not None and perimeter is not None:  #Se controla que  los valores ingresados sean correctos para mostrar los mensajes de resultados
        print("Área de la circunferencia:", area)
        print("Perímetro de la circunferencia:", perimeter)
    else:
        print("El radio debe ser un valor positivo.") #Error que se muestra si el usuario no ha ingresado números positivos
except ValueError:
    print("Entrada no válida. Ingrese un número válido como radio.") #Error que se muestra si el usuario no ha ingresado números

# Ejercicio 9

attempts = 0
while attempts < 3:
    user = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    acces_correct, attempts = login(user, password, attempts)
    if acces_correct:
        print("Inicio de sesión exitoso.")
        break
    else:
        print("Nombre de usuario o contraseña incorrectos. Intentos restantes: ", 3 - attempts)
    
if attempts == 3: 
    print("Has agotado tus intentos. Cierre de sesión.")

# Ejercicio 10

shopping_cart = {}  # Inicializamos un diccionario vacío para el carrito de compra

while True:
    product_name = input("Ingrese el nombre del producto (o 'fin' para terminar): ") #El usuario ingresa todos los productos que desea hasta que escriba la palabra "fin"
    if product_name == 'fin':
        break 

    price = float(input("Ingrese el precio del producto: ")) #Ingresa el precio del producto nombrado anteriormente
    discount = float(input("Ingrese el descuento (si no hay descuento, ingrese 0): "))

    product_info = {'precio': price}

    if discount != 0:  
        product_info['descuento'] = discount 

    shopping_cart[product_name] = product_info


final_price = calculate_final_price(shopping_cart)
print("Precio final de la compra:", final_price)

# Ejercicio 11

price_products=[]
products=int(input("Ingrese la cantidad de productos para calcular su aumento el siguiente mes: "))

for i in range(products): #Se solicita al usuario el precio de la cantidad de productos que haya introducido anteriormente
    price=float(input(f"Ingrese el precio del producto {i+1}: "))
    price_products.append(price)

increase_november=calculation(increase, price_products) #Se obtienen los precios con el aumento del 20%

print(f"Los precios actuazlizados para el mes de noviembre con un aumento del 20% son: {increase_november}")

# Ejercicio 12

sentence = input("Ingrese una frase: ")
result = words_length_dictionary(sentence)
print(result)

# Ejercicio 13

input_vector = input("Ingrese un vector(separe los valor con comas , ): ")
vector = [float(x) for x in input_vector.split(',')]

modulus = vector_modulus(vector)

print("El módulo del vector es: ", modulus)

# Ejercicio 14

number = int(input("Ingrese un número para corroborar si es primo o no lo es: "))
if is_prime(number):
    print(f"{number} es un número primo.")
else:
    print(f"{number} no es un número primo.")

# Ejercicio 15

total_numbers_read = 0

while True:
    try:
        number = int(input("Ingrese un número (o 0 para salir): "))
        
        if number == 0:
            break
        
        result = factorial(number) # Se calcula el factorial llamando a la función
        print(f"El factorial de {number} es: {result}")
        
        total_numbers_read += 1
    
    except ValueError:
        print("Número no válido. Ingrese un número entero.") #Error si no se ingresa un número entero

print(f"Se leyeron un total de: {total_numbers_read} números.")

# Ejercicio 16

try:
    number = int(input("Ingrese un número entero: "))
    digit = int(input("Ingrese un dígito: "))
    freq = digit_frequency(number, digit)
    print(f"El dígito {digit} aparece {freq} veces en el número {number}.")
except ValueError:
    print("Número incorrecto, por favor ingrese un número entero.")

# Ejercicio 17

largest_prime = 0
while True:
    try:
        number = int(input("Ingrese un número primo (o uno no primo para terminar): "))
        if not is_prime(number):
            break # Se corta el programa si no se ingresa un número primo
        
        if number > largest_prime:  # Se obtiene el mayor número primo
            largest_prime = number

        sum = sum_digits(number)
        print(f"La suma de dígitos es: {sum}")

        digit = int(input("Ingrese un dígito para contar su frecuencia: "))
        freq = digit_frequency(number, digit)
        print(f"La frecuencia de {digit} es: {freq}")
    except ValueError:
        print("Número inválido. Intente otra vez") #Error si no se ingresa un número entero

if largest_prime > 0:
    factorial_result = factorial(largest_prime) #Cálculo del factorial del número primo de mayor valor
    print(f"El factorial de ({largest_prime}) es: {factorial_result}")
else:
    print("No se ingresaron números primos.")