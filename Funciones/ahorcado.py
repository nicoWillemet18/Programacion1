import random
from funcion_ahorcado import mostrar_word


words=["hospital", "canguro", "esperar", "programador", "prueba", "grupos", "escritorio"]
word = random.choice(words)
print(word)
print("Bienvenido al juego \"Ahorcado\", puedes tener hasta 7 errores antes de adivinar la palabra")

adivinadas = []
error=0

while True:
    palabra_mostrada = mostrar_word(word, adivinadas)
    if not "_" in palabra_mostrada:
        print(f"¡Has adivinado la palabra! {word}")
        break
    elif error == 7:
        print("Has perdido el juego. La palabra era: " + word)
        break


    print("Palabra a adivinar: " + palabra_mostrada)
    while True:
        letra = input("Ingresa una letra: ")
        if len(letra) == 1 and letra.isalpha():
            break
        else:
            print("Por favor, ingresa una única letra válida.")

    if letra in word:
        adivinadas.append(letra)
        print("¡Adivinaste una letra!")
    else:
        error += 1
        print("Esa letra no está en la palabra. Intentos incorrectos: " + str(error))
