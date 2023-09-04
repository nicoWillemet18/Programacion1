#1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección.
numero1=45
print("Número 1: ",numero1)

#2. No borres la variable número uno y crea una variable llamada "numero2" asignándole
#un número decimal de tu elección.
numero2=12.5
print("Número 2: ",numero2)

#3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2".
suma=numero1+numero2
print("La suma de los 2 números es: ",suma)

#4. Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para
#multiplicación y otra para división. Imprime estas variables.
resta=numero1-numero2
multiplicacion=numero1*numero2
division=numero1/numero2
print("La resta de los números es: ",resta," La multiplicación es: ", multiplicacion," Y la división es:", division)

#5. Crea una variable llamada "nombre" y asígnale tu nombre como valor.
nombre="Nicolás"
print("El nombre del alumno es: ",nombre)

#6. Crea una variable llamada "precio" y asígnale un valor decimal que represente el
#precio de un artículo ficticio.

precio=207.33
print("El precio del artículo es: $",precio)

#7. Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale
#un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le
#quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al
#100% y el valor 0 al 0%.
descuento=0.38
print("Descuento disponible: ", descuento*100, "porciento de descuento")

#8. Ahora, intenta calcular el precio final aplicando el descuento al precio original y
#almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que
#aplicar la lógica de matemáticas.
precio_final=precio-precio*descuento
print("El precio final es de: $", precio_final)

#9. Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu
#elección. Qué sea un string.
cadena="Hoy es un buen día para salir a correr."
print("Frase: ", cadena)

#10. Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas
#a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de
#Python.
longitud=len(cadena)
print("La longitud de la frase es de: ",longitud, "caracteres.")

#11. Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y
#conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo
#mismo.
precio=int(68.45)
print("Precio redondeado del artículo: ",precio)

#12. Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas
#en una tercera variable llamada "nombre_completo", el nombre y el apellido con un
#espacio entre medio. Puedes usar libremente la forma de concatenación que quieras.
nombre1="Federico"
apellido="Perez"
nombre_completo=nombre+" "+apellido
print("El nombre completo es: ",nombre_completo)

#13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.
edad=23
edad_incrementada_5=edad+5
edad_decrementada_10=edad_incrementada_5-10
print("Edad inicial: ", edad, " Edad incrementada en 5: ", edad_incrementada_5, ", y luego decrementada en 10: ", edad_decrementada_10)

#14. Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y
#centímetros. Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3.
altura=1.74
altura_mult=altura*4
altura_div=altura_mult/3
print("Altura inicial: ", altura,"cm. Altura multiplicada por 4: ", altura_mult, "cm, y luego dividida en 3: ", altura_div, "cm.")

#15. Crea una variable que contenga tu nombre completamente en mayúsculas. Después
#transfórmalo todo en minúsculas con algún método o función de Python.
nombre_may="NICOLÁS"
nombre_min=nombre_may.lower()
print(nombre_min)

#16. Por último, con la variable con el nombre en mayúsculas, aplica un método parecido
#para que se transforme todo en minúsculas excepto la primera letra
nombre2=nombre_may.title()
print(nombre2)
