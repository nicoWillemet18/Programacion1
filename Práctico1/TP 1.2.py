import math

# #ejercicio 1 
base = float(input("Ingrese el valor de la base del rectangulo: "))
altura = float(input("Ingrese el valor de la altura del rectangulo: "))

area_rectangulo = base*altura
perim_rectangulo = (base*2) +(altura*2)

print(f'El area del rectangulo es: {area_rectangulo}.\nEl perimetro del rectangulo es:{perim_rectangulo}')

#ejercicio 2 

cateto1 = float(input("Ingrese el valor del primer cateto del triangulo: "))
cateto2 = float(input("Ingrese el valor del segundo cateto del triangulo: "))

hipotenusa = ((cateto1**2)+ (cateto2**2))**(1/2)

print(f'La hipotenusa del triangulo rectangulo es: {hipotenusa}')

#ejercicio 3

num1 = float(input("Ingrese el valor del primer numero: "))
num2 = float(input("Ingrese el valor del segundo numero: "))

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2
print(f'La suma de estos numeros es: {suma}.\nLa resta de estos numeros es: {resta}.'+ f'\nLa multiplicacion de estos numeros es: {mult}.\nLa division de estos numeros es: {div}')

# Ejercicio 4.
grado_fahren = float(input("Ingrese los grados en Fahrenheit: "))

grado_celsius = (grado_fahren - 32) * 5 / 9
print("Los grados convertidos a Celsius son: Cº", grado_celsius)

# 5. ¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?
# a) A = input(nombre, “¿Cuál es tu canción favorita?”)
# b) precio = input(“Precio: “)
# total = precio + (precio * 0.1)
# c) edad = int(input(“Edad: “))
# print(tu edad es, edad)
# d) edad = int(input(“Edad: “))
# print(“Veamos si tu edad es 18…”, edad=18)

#5.a
#nombre es una variable no definida y el metodo input espera solo 1 argumento

A = input("Cual es tu cancion favorita?")

#5.b
#Input por defecto convierte la entrada en un string, por lo que no permite multiplicar por un float
#solucion: convertir a int

precio = int(input("Precio: "))
total = precio + (precio * 0.1)

#5.c
#print imprime texto por pantalla, el argumento debe estar entre comillas para que sea un string

edad = int(input("Edad: "))
print("tu edad es", edad)

#5.d
#Se intenta hacer una validacion de la edad con el operador de asignacion =
#Para corregir se debe usar el de comparacion ==

edad = int(input("Edad: "))
print("Veamos si tu edad es 18…", edad==18)

#ej 6 media
num1=float(input("Ingrese el valor del primer numero:" "\n"))
num2=float(input("Ingrese el valor del segundo numero:" "\n"))
num3=float(input("Ingrese el valor del tercer numero:" "\n"))
print("La media es de: " ,((num1+num2+num3)/3))

#ej 7 minutos
tiempo=float(input("Ingrese  la cantidad de minutos: " "\n"))
hora=int((tiempo/60))
minutos=int(tiempo%60)
print ("La cantidad de horas es: ",hora, "hs" , " y la cantidad de minutos son: ", minutos, "min")

#Ejercicio 8.

sueldo_base = float(input("Ingrese su sueldo base: "))
comision = (sueldo_base * 0.1) * 3
print("El monto a comisionar es de: $", comision)
sueldo_total = sueldo_base + comision
print("El sueldo total a cobrar es de: $", sueldo_total)

#ejercicio 9

precio = float(input("Ingrese el precio del producto: "))
descuento = precio * 0.15
precio_final = precio - descuento

print(f'el precio total con el descuento es: {precio_final}' )

#ejercicio 10

parc1=float(input('ingrse la calificacion del primer parcial: '))
parc2=float(input('ingrse la calificacion del segundo parcial: '))
parc3=float(input('ingrse la calificacion del tercer parcial: '))
porc1=((parc1+parc2+parc3)/3)*0.55

examf=float(input('ingrse la calificacion del examen final: '))
porc2=examf*0.30

trabajof=float(input('ingrse la calificacion del trabajo final: '))
porc3=trabajof*0.15
calff=porc1+porc2+porc3
print(f'la calificacion final es: {calff}')

#Ejercicio 11.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
distancia = (num1 - num2)
print("La distancia entre los números es: ", distancia * -1) if distancia < 0 else print("La distancia entre los números es: ", distancia)

#ej 12 raiz
num=float(input("Ingrese un numero para saber su raiz cubica y cuadrada: "))
print ("Su raiz cubica es: ", (num//3), " y su raiz cuadrada es: ", (num//2))

#ej 13 
num=str(input("Ingrese un numero para saber su invertido: "))
print("El invertido de: ", num, " es: ", (num[::-1]))

#ej 14
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
aux=num1
num1=num2
num2=aux
print("La variable 1 vale: ", num1, " y la variable numero 2: ", num2)

#ej 15 
print("Ingrese la hora de partida del ciclista")
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
tiempo_viaje= int(input("Tiempo que se demoro en segundos: \n"))
segundos_1 = tiempo_viaje%60%60
minutos_1 = tiempo_viaje%60
horas_1 = math.floor(tiempo_viaje/60/60)
horas_llegada = horas_1 + horas
minutos_llegada = minutos_1 + minutos
segundos_llegada = segundos_1 + segundos
print("El tiempo de llegada es a las: ", horas_llegada, "hs con ", minutos_llegada, "min y ", segundos_llegada, "seg")

# Ejercicio 16.
nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")
print("Las iniciales son: ", nombre[0], apellido1[0], apellido2[0])

# Ejercicio 17.
usuario = input("Ingrese su nombre: ")
print("Ahora estás en la Matrix ", usuario)

# Ejercicio 18.	
cena = float(input("Ingrese el costo de la cena: "))
costo_servicio = cena * 0.062
propina = cena * 0.1
monto_final = cena + costo_servicio + propina
print("El monto final a abonar es de: ", monto_final)

#Ejercicio 19
print("Ingrese su fecha de nacimiento")
dia = input("Dia: ")
mes = input("Mes: ")
ano = input("Año: ")
print("Tu fecha de Nacimiento es: ", dia,"/", mes,"/", ano)

#Ejercicio 20
naciemiento = [(input("Ingrese tu dia de nacimineto: \n")), (input("Ingrese tu mes de nacimineto: \n")), (input("Ingrese tu año de nacimineto: \n"))]
print("Tu fecha de nacimiento es: ", naciemiento[0], "/", naciemiento[1], "/", naciemiento[2])

#Ejercicio 21

km = float(input("Ingrese la cantidad de km a reccorer: \n"))
km_x_litro = float(input("Ingrese la cantidad de km que recorre con 1 Litro de conbustible: \n"))
cap_tanque = float(input("Ingrese la capacidad de su tanque: \n"))

tanques_necesarios = math.ceil(km/(km_x_litro * cap_tanque))
print("La cantidad de tanques a rellenar es: ", tanques_necesarios)