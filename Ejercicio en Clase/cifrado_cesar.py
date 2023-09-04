#Ejercicio 1

corrimiento = int(input("Ingrese el corrimiento deseado para los mensajes: "))
for i in range(5):
    mensaje = input(f"Ingrese el mensaje {i+1}: ")
    mensaje_may = mensaje.upper()
    resultado = ""
    for letra in mensaje_may:
        codigo = ord(letra) - ord('A')
        codigo = (codigo + corrimiento) % 26
        letra_cifrada = chr(codigo + ord('A'))
        resultado += letra_cifrada
    print(f"Oficial {i+1}: {resultado}")

#Ejercicio 2

total_pares= 0
total_impares= 0

while True:
    numero = int(input("Ingrese el número a analizar: "))
    pares= 0
    impares= 0

    if numero == 0:
        break

    while numero > 0:
        digito= numero % 10
        if digito % 2 == 0:
            pares += 1
        else: 
            impares += 1
        numero = numero // 10

    total_pares += pares
    total_impares += impares

    print(f"Pares: {pares}. Impares: {impares} .")
print(f"El total de dígitos pares es: {total_pares}. Y el total de dígitos impares es: {total_impares}.")