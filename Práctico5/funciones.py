import math

def dni_valido (dni):
    while True:
        if len(dni) != 7 and len(dni) != 8:
            print("Error: DNI inválido.")
            dni=input("Ingrese un DNI válido: ")
            dni_valido(dni)
            return False
        else:
            return True

def length_last_word (phrase):
    phrase=phrase.strip() # Elimina espacios al final y principio de la frase.
    words=phrase.split() # Obtiene cantidad de palabras

    if words:
        last_word=words[-1]
        length_last_word=len(last_word)

        return length_last_word
    else:
        return 0

def identifier (name, length, dni):
    identifier=(f"Su identificador es: {name[0]}{len(length)}{dni[:3]}")
    return print(identifier)

def multiplier (x, y):
    if x % y == 0:
        return print(f"{x} es múltiplo de {y}")
    elif y % x == 0:
        return print(f"{y} es múltiplo de {x}")
    else:
        return print("Ninguno de los números es múltiplo del otro.")

def calculate_average_temperature(temp_max, temp_min):
    medium_temperature = (temp_max + temp_min) / 2
    return medium_temperature

def space_between(phrase):
    spaces = ""
    for letter in phrase:
        if letter != " ":
            spaces += letter + " "
        else:
            spaces += letter
    return spaces

def max_min(lista):
    if len(lista) == 0:
        return None, None
    max = min = lista[0]
    for value in lista:
        if value > max:
            max = value
        if value < min:
            min = value
    return max, min

def circumference_perimeter(radio):
    if radio <= 0:
        return None, None
    area = math.pi * radio ** 2
    perimeter = 2 * math.pi * radio
    return area, perimeter

def login(user, password, attempts):
    user_correct = "user1"
    password_correct = "asdasd"

    if user == user_correct and password == password_correct:
        return True, attempts
    else:
        attempts += 1
        return False, attempts
    
def calculate_final_price(cart):
    final_price = 0

    for product, product_info in cart.items():
        if 'descuento' in product_info:
            discount = product_info['descuento']
            price_discount = product_info['precio'] * (1 - discount / 100)
            final_price += price_discount
        else:
            final_price += product_info['precio']

    return final_price

def increase(list):
    final = []
    for i in range(len(list)):
        increased = list[i] + list[i]*0.2
        final.append(increased)
    return final

def calculation (fun, array):
    result= fun(array)
    return result 

def words_length_dictionary(sentence):
    words = sentence.split()
    
    dictionary = {}
    
    for word in words:
        dictionary[word] = len(word)
    
    return dictionary

def vector_modulus(vector):
    sum_of_squares = 0
    
    for component in vector:
        sum_of_squares += component ** 2
    
    modulus = math.sqrt(sum_of_squares)
    
    return modulus

def is_prime (number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def digit_frequency(number, digit):
    frequency = 0
    while number > 0:
        last_digit = number % 10
        if last_digit == digit:
            frequency += 1
        number = number // 10
    return frequency

def sum_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10
    return sum