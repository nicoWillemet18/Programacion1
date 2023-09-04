import math

# 1-	Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra=input("Ingrese la palabra a mostrar: ")
for i in range(10):
    print(palabra)

# 2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad=int(input("Ingrese su edad: "))
for i in range(edad):
    print("Ha cumplido: ",i+1)

# 3-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero= int(input("Ingrese un número positivo: "))
num= 0
while num != numero:
    num = num + 1
    if num % 2 != 0:
        print(num,end=", ")

# 4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero= int(input("Ingrese un número positivo: "))
num= 0
while num <= numero:
    print(numero, end=", ")
    numero = numero - 1

# 5-	Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

inversion=float(input("Ingrese el monto a invertir: "))
interes=float(input("Ingrese el minterés anual (%): "))
anios=int(input("Ingrese los años del plazo: "))
capital= inversion

for i in range(anios):
    capital = capital * (1 + (interes / 100))
    print("El capital obtenido en el año", i + 1, "es de: $", round(capital, 2))

# 6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

num= int(input("Ingrese un número: "))
lin="*"
sum=lin

for i in range(num):
    print(sum)
    sum=sum +lin

# 7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.

for i in range(10):
    num=i+1
    print("Tabla del ", num, ": ")
    for n in range(10):
        num2= n+1
        print(num*num2)

# 8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo. 

num = int(input("Ingrese un número: "))

for i in range(1, num * 2, 2):
    for j in range(i, 0, -2):
        print(j, end="")
    print()

# 9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

var="contraseña"
palabra=""

while palabra != var :
    palabra=str(input("Ingrese la contraseña: "))
    

# 10-	Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(numero)) + 1, 2):
            if numero % i == 0:
                return False
        return True
numero = int(input("Ingrese un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

# 11-	Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra=str(input("Ingrese la palabra: "))
palabra_al_reves = ""

for i in range(len(palabra) - 1, -1, -1):
    palabra_al_reves = palabra[i]
    print("Cadena al revés:", palabra_al_reves)

# 12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase=str(input("Ingrese la frase: "))
letra=str(input("Ingrese la letra: "))
num_letra=0

caracteres=len(frase)

for i in range(caracteres):
    if frase[i] == letra:
        num_letra += 1

print("El número de veces de la letra ", letra, " en la frase es: ", num_letra)

# # 13-	Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

palabra=""
while palabra != "salir":
    palabra=str(input("Escriba lo que quiera: "))
    print(palabra)

# 14-	Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.

num1=int(input("Ingrese el primer numero entero: "))
num2=int(input("Ingrese el segundo numero entero: "))
pares=[]
impares=[]


if num1 < num2:
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)       
else:
    for i in range(num2, num1 + 1):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)        

print("Los pares son: ",pares, ". Y los impares son: ", impares)

# 15-	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

num=int(input("Escriba un número entero positivo: "))
divisores=[]

for i in range(1, num):
    if num % i == 0:
        divisores.append(i)

print("Los divisores son: ",divisores)

# 16-	Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

cantidad=int(input("Escriba la cantidad de números a utilizar: "))
negativos=[]

for i in range(cantidad):
    nums=int(input(f"Ingrese el número posición {i+1}: "))
    if nums < 0 :
        negativos.append(nums)

print("Los números negativos ingresados son: ", negativos)

# 17-	Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).

frase=str(input("Ingrese una frase: "))
frase=frase.lower()
vocales=["a","e","i","o","u"]
vocales_si=[]

for i in range(0, 5):
    if vocales[i] in frase:
        vocales_si.append(vocales[i])

print(vocales_si)

# 18-	Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

a, b = 0, 1
print(a)
print(b)

for i in range(10):
    fibo = a + b
    print(fibo)
    a, b = b, fibo    

# 19-	Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.

total=float(input("Ingrese el total a ahorrar: "))
ahorro_actual=0

while ahorro_actual < total:
    ingreso=float(input("Ingrese dinero a la alcancía: "))
    if ingreso < 0 :
        print("Error, el ingreso debe ser positivo.")
    else:
        ahorro_actual= ahorro_actual+ingreso 
        if ahorro_actual < total : 
            print("El ahorro actual es de : $", ahorro_actual, ", faltan: $", total-ahorro_actual, " para el objetivo.")     
        else :
            print("El ahorro actual es de : $", ahorro_actual, ", se cumplió el objetivo.")

# 20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

num=int(input("Ingrese un número entero: "))
sum=num

while num != 0:
    num=int(input("Ingrese un numero entero: "))
    sum=sum+num

print(sum)

# 21-	Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

maximo=0
num=int(input("Ingrese un número entero: "))

while num != 0:
    if num > maximo:
        maximo = num
    num=int(input("Ingrese un numero entero: "))

print("El número máximo ingresado es: ", maximo) 

# 22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

num=int(input("Ingrese un número entero: "))
pares=0

while num != -1:
    sum=0
    while num > 0:
        digito = num % 10
        if digito % 2 == 0:
            pares += 1
        sum += digito
        num //= 10 
    print("La suma de los dígitos es: ", sum)    
    num=int(input("Ingrese un numero entero: "))
    
print("La cantidad de números pares ingresada fue: ", pares)

# 23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
# Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

monto=float(input("Ingrese el monto del producto: $"))
sum=monto

while monto != 0:
    monto=float(input("Ingrese el monto del producto: $"))
    if monto > 0:
        sum=sum+monto
if sum > 1000 :
    desc = sum * 10 / 100
    sum = sum - desc

print("El total a pagar es: $",sum)

# 25-	Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.

num=int(input("Ingrese un número entero positivo: "))
fact=1

for i in range(1, num + 1 ):
    fact *= i

print("El factorial de ", num, "es : ", fact)



'Es par' if num % 2 == 0 else 'Es impar'
num if num>0 else -num
num1 if num1>num2 else num2