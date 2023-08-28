import math
#Ejercicio 1 y 2
anos = int(input("Ingrese la cantidad de años del ordenador: \n"))
if (anos<0):
        print("Error, los años ingresados no pueden ser negativos")
elif(anos>= 0 and anos<=2):
        print("El ordenador es nuevo")
elif(anos>2):
        print("El ordenador es viejo")

#Ejercicio 3
nombre1 = str(input("Ingrese el nombre de la primera persona: "))
nombre2 = str(input("Ingrese el nombre de la segunda persona: "))
if (nombre1[0] == nombre2[0]):
        print("Coincidencia")
else:
        print("No hay coincidencia")

#Ejercicio 4
print("Elección de candidato:")
print("A - Candidato del partido rojo")
print("B - Candidato del partido verdad")
print("C - Candidato del partido azul")

eleccion = input("Ingrese la letra del candidato por el cual desea votar: ")
eleccion = eleccion.upper()
if eleccion == 'A':
        print("Usted ha votado por el partido rojo.")
elif eleccion == 'B':
        print("Usted ha votado por el partido verdad.")
elif eleccion == 'C':
        print("Usted ha votado por el partido azul.")
else:
        print("Opción errónea.")

#Ejercicio 5
vocal = input("Ingrese la vocal")
vocal = vocal.upper()
cant = len(vocal)

if cant == 1 :
        if vocal == "A":
                print("Es una vocal")
        elif vocal == "E":
                print("Es una vocal")
        elif vocal == "I":
                print("Es una vocal")
        elif vocal == "O":
                print("Es una vocal")
        elif vocal == "U":
                print("Es una vocal")
        else:
                print("No es una vocal")
else:
        print("No se puede procesar el dato")

#Ejercicio 6

ano = int(input("Ingrese el año que quiere saber si es bisiesto: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("Es bisiesto")
else:
        print("No es bisiesto")

#Ejercicio 7
print("Ingrese 3 numeros a continuacion")
numeros = [input("Primero: "), input( "\nSegundo: "),input ("\nTercero: ")]
if (numeros[0]< numeros[1] and numeros[0]< numeros[2]):
        print("El menor numero es:", numeros[0])
elif(numeros[1]< numeros[0] and numeros[1]< numeros[2]):
        print("El menor numero es:", numeros[1])
else:
        print("El menor numero es:", numeros[2])

#Ejercicio 8

usuario = input("Ingrese el usuario: ")
contrasena = input("Ingrese la contraseña: ")

if (usuario == "Gwenevere" and contrasena == "excalibur"):
        print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
        print("Acceso denegado")

#Ejercicio 9

nombre = input("Ingrese el nombre: ")
sexo = input("Ingrese el sexo F/M: ")

if(sexo == 'F' and nombre.lower() < 'm') or (sexo == 'M' and nombre.lower() > 'n'):
        grupo = "A"
        print("Usted pertenece al grupo A")
else:
        print("Usted pertenece al grupo B")

#Ejercicio 10

edad = int(input("Ingrse la edad: "))
if (edad < 4):
        print("Puede entrar gratis")
elif(edad > 4 and edad < 18):
        print("Debe pagar $500")
else:
        print("Debe pagar $1000")

#Ejercicio 11


print("Bienvenido a la pizzería Bella Napoli!")
print("Opciones de pizza:")
print("1. Vegetariana")
print("2. No vegetariana")

opcion = int(input("Seleccione el tipo de pizza (1/2): "))

if opcion == 1:
        pizza = "Vegetariana"
        print("Usted a elegido la pizza Vegetariana")
        ingredientes_disponibles = ["Pimiento", "Tofu"]
elif opcion == 2:
        pizza = "No vegetariana"
        print("Usted a elegido la pizza No Vegetariana")
        ingredientes_disponibles = ["Peperoni", "Jamón", "Salmón"]
else:
        print ("Opcion mal")
print(f"Excelente elección: Pizza {pizza}!\nIngredientes disponibles:")
for i, ingrediente in enumerate(ingredientes_disponibles, start=1):
        print(f"{i}. {ingrediente}")
seleccion = int(input(f"Seleccione un ingrediente: "))
if seleccion < 1 or seleccion > len(ingredientes_disponibles):
        print("Selección inválida.")
ingrediente_elegido = ingredientes_disponibles[seleccion - 1]
print(f"Usted ha elegido una pizza {pizza} con los siguientes ingredientes:")
print("Mozzarella, Tomate,", ingrediente_elegido)

#Ejercicio 12

ano_actual_igresado = int(input("Ingrese el año actual: "))
ano_cualquiera = int(input("Ingrese el año cualqueria: "))
if(ano_actual_igresado>ano_cualquiera):
        diferencia = ano_actual_igresado - ano_cualquiera
        print(f"La cantidad de años que han pasado son: {diferencia}")
else:
        diferencia = ano_cualquiera - ano_actual_igresado
        print(f"La cantidad de año que faltan son: {diferencia}" )

#Ejercicio 13
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if num1 <= 0 or num2 <= 0:
        print("Por favor ingrese valores positivos y no nulos.")
else:
        if num1 > num2:
                mayor = num1
                menor = num2
        else:
                mayor = num2
                menor = num1

if mayor % menor == 0:
        print(f"El mayor número ({mayor}) es múltiplo del menor número ({menor}).")
else:
        print(f"El mayor número ({mayor}) no es múltiplo del menor número ({menor}).")

#Ejercicio 14
a = float(input("Ingrese el primer valor: "))
b = float(input("Ingrese el segundo valor: "))

if (a == 0):
        if (b == 0):
                print("La ecuacion tiene infinitas soluciones")
        else:
                print("La ecuacion no tiene solucion")
else:
        resultado = ((-b)/a)
        if (resultado == -0.0):
                print("El resultado es: 0")
        else:
                print(f"El resultado es: {resultado}")

#Ejercicio 15

calcular = input("Que area desea calcular, la de un triangulo o un circulo (T/A): ")
calcular = calcular.upper()
if calcular == "T":
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = (base*altura)/2
        print(f"El area del triangulo es: {area}")
elif calcular == "A":
        radio = float(input("Ingrese el radio del circulo: "))
        area = math.pi * radio ** 2
        print(f"El area del circulo es: {area}")
else:
        print("Ingrese una opcion correcta")

#Ejercicio 16

a = float(input("Ingrese el primer valor"))
b = float(input("Ingrese el segundo valor"))
print("Eligue la operacion a realizar")
print("1. Suma")
print("2. Multiplicacion")
print("3. Resta")
print("4. Division")
operacion= float(input("Ingrese el numero de la operacion a realizar: "))
if(operacion>1 and operacion<4):
        if operacion == 1:
                resultado = a + b
        elif operacion == 2:
                resultado = a * b
        elif operacion == 3:
                resultado = a - b
        elif operacion == 4:
                resultado = a / b
else:
        print("Ingrese una opcion correcta")
print(f"El resultado de la operacion es: {resultado}")

#Ejercicio 17

dia = str(input("Ingrese el dia: "))
dia = dia.lower()

if dia == "lunes":
        print("El dia es Lunes")
elif dia == "viernes":
        print("El dia es Viernes")
elif dia == "sabado" or dia == "domingo":
        print("El dia es Sabado o Domingo")
else:
        print("El dia es Martes, Miercoles o Jueves")

#Ejercicio 18

horas = int(input("Ingrese la cantidad de horas trabajadas: "))
salario_hora = float(input("Ingrese su salario por hora: "))

if horas > 48:
        horas_extras = horas - 48
        horas = horas - horas_extras
        print(f"Usted trabajo un total de {horas_extras} hs extras")
        salario = horas * salario_hora + (((salario_hora*0.10)+salario_hora)*horas_extras)
        print(f"Su salario es de: {salario}")
else:
        salario = horas * salario_hora
        print(f"Su salario es de: {salario}")

#Ejercicio 19
cant_lapiz = int(input("Ingrese la cantidad de lapices a comprar: "))
if cant_lapiz >= 1000:
        descuento = 60-(60*0.07)
        total = cant_lapiz * descuento
        print(f"El total a pagar con el descuento por la compra de mas de 1000 lapices es de: {total}")
else:
        total = cant_lapiz * 60
        print(f"El total a pagar es de: {total}")

#Ejercicio 20
nota = 0
cantidad = 0
for i in range(4):
        nota_i = int(input("Ingrese la nota del alumno: "))
        nota = nota + nota_i
        cantidad = cantidad + 1
promedio = nota / (cantidad)
print(f"El promedio de notas es de: {promedio}")

if promedio<6:
        print("Desaprobado")
else:
        print("Aprobado")