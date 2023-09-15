# Ejercicio 1

x = 0
while x < 30 :
    x=x+1
    if x == 15 :
        print("La ejecución del bucle se interrumpe cuando x vale", x)
        break
    if x == 4 or x == 6 or x == 10:
        print("El valor ", x, " de x fue omitido.")
        continue
    print("El valor del bucle es: ", x)

#Ejercicio 1.2

list_line = []

while True:
    line = input("Ingrese una línea: ")
    line=line.upper()
    if line == "":
        break
    list_line.append(line)
print(list_line)

# Ejercicio 2

D = 0
R = 0
count = 0

while True:
    line = input("Ingrese D/R: ")
    line=line.upper()
    if line == "":
        break
    if line == "D":
        monto_D = int(input("Ingrese el monto D: "))
        D += monto_D
    elif line == "R":
        monto_R = int(input("Ingrese el monto R: "))
        R += monto_R
    else:
        print("No se reconoce el comando")

count = D - R
print(count)

# Ejercicio 3

number_count=0
condi=True
def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True
while True :
    number=int(input("Ingrese un numero para saber si es primo, para finalizar ingrese 0: "))
    if (number==0):
        break
    elif(number>1):
        condi=is_prime(number)
        if(condi==True):
            number_count=number_count+1

print(number_count)

# Ejercicio 4

number1=int(input("Ingrese el primer año: "))
number2=int(input("Ingrese el segundo año: "))
if (number1>number2):
    bigger=number1
    minus=number2
else:
    bigger=number2
    minus=number1

for i in range (minus,bigger,1):
    if(i % 10 != 0):
        continue
    if (((i % 4 == 0 and i % 100 != 0) or i % 400 == 0)): 
        print(i)

#Ejercicio 5

for i in range(0,21,1):
    if(i % 2 != 0):
        continue
    print(i)

#Ejercicio 6

numbers=list(range(1, 101))
search=int(input("Ingrese un numero a buscar del 1 al 100"))
for i in numbers:
    if(i==search):
        print("Se encontro!")
        break

#Ejercicio 7

while True:
    number=int(input("En que menu desea ingresar? 1 2 o 3, ingrese 0 para salir: "))
    if(number==1):
        print("MENU UNO")
    elif(number==2):
        print("MENU DOS")
    elif(number==3):
        print("MENU TREIS")
    elif(number==0):
        break
