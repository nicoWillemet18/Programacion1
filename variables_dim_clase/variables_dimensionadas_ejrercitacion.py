#EJERCICIO 1
list_data= [("Mateo Mercau", 46325074, "Chile"),("Juan Ignacio Lara", 41023056, "Brasil"),("Lautaro Yanzon", 42563963, "Estados Unidos"),("Nicolas Willemet", 42857964, "Francia")]
list_ubi= [("Mendoza", "Argentina"),("San Luis","Argentina"),("Cordoba","Argentina"),("Buenos Aires","Argentina")]

#funcion agregar pasajeros
def agregar_pasajeros():
    name=input("Ingrese el nombre del pasajero: ")
    dni=int(input("Ingrese el DNI del pasajero: "))
    destiny=input("Ingrese el destino del pasajero: ")
    list_data.append((name,dni,destiny))

#funcion agregar ciudades
def agregar_ciudad():
    city=input("Ingrese nombre de la ciudad: ")
    country=input("Ingrese el pais al que pertenece la ciuadad: ")
    list_ubi.append((city,country))
#funcion buscar ciudad por dni
def buscar_ciudad():
    dni=int(input("Ingrese DNI del pasajero: "))
    for name, dni_passenger, destiny in list_data:
        if dni_passenger == dni:
            for city,country in list_ubi:
                if destiny == city:
                    print(f"El pasajero {name} viaja a la ciudad de {city}")
                    return
    print("No se encontró ningún pasajero con ese DNI")

# Función para mostrar la cantidad de pasajeros que viajan a una ciudad
def cantidad_pasajeros_por_ciudad():
    city = input("Ingrese el nombre de la ciudad: ")
    count = 0
    for name, dni, destiny in list_data:
        if destiny == city:
            count += 1
    print(f"La cantidad de pasajeros que viajan a {city} es: {count}")    

# Función para buscar el país de un pasajero por DNI
def buscar_pais_por_dni():
    dni = int(input("Ingrese el DNI del pasajero: "))
    for name, dni_passenger, destiny in list_data:
        if dni_passenger == dni:
            for city, country in list_ubi:
                if destiny == city:
                    print(f"El pasajero {name} viaja al país de {country}.")
                    return
    print("No se encontró ningún pasajero con ese DNI.")   

# Función para mostrar la cantidad de pasajeros que viajan a un país
def cantidad_pasajeros_por_pais():
    country = input("Ingrese el nombre del país: ")
    count = 0
    for name, dni, destiny in list_data:
        for city, country_destiny in list_ubi:
            if destiny == city and country_destiny == country:
                count += 1
    print(f"La cantidad de pasajeros que viajan a {country} es: {count}")

while True:
    print("           MENU      ")
    print("1. Agregar pasajeros.")
    print("2. Agregar ciudades")
    print("3. Introducir el DNI para ver a qué ciudad viaja.")
    print("4. Introducir la ciudad para ver cantidad de pasajeros.")
    print("5. Introducir el DNI para ver a qué país viaja.")
    print("6. Introducir el pais para ver cantidad de pasajeros.")
    print("7. Salir del programa.")

    option= int(input("Ingrese una opcion: "))

    if option == 1:
        agregar_pasajeros()
    elif option == 2:
        agregar_ciudad() 
    elif option == 3:
        buscar_ciudad()       
    elif option == 4:
        cantidad_pasajeros_por_ciudad() 
    elif option == 5:
        buscar_pais_por_dni() 
    elif option == 6:
        cantidad_pasajeros_por_pais() 
    elif option == 7:
        break
    else:
        print("La opción ingresada no es valida")

# Ejercicio 2

def obtain_domicile_bill(purchases):
    domiciles=set()
    for purchase in purchases:
        costumer, _, _, domicile = purchase
        domiciles.add(domicile)
    return list(domiciles)

purchases=[('Nuria Costa', 5, 1234.5,'Calle 1 – 456'), ('Jorge Russo', 7, 3999, 'Calle 2 – 741'), ("Federico Gomez", 15, 42000, "Beltran Sur 2145"), ('Jorge Russo', 26, 1599, 'Calle 2 – 741')]

domicile_bill=obtain_domicile_bill(purchases)

print(domicile_bill)

# Ejercicio 3

# Inicializar el diccionario con los socios fundadores
socios = {
    1: {"nombre": "Amanda", "apellido": "Núñez", "ingreso": "17/03/2009", "cuota_al_dia": True},
    2: {"nombre": "Bárbara", "apellido": "Molina", "ingreso": "17/03/2009", "cuota_al_dia": True},
    3: {"nombre": "Lautaro", "apellido": "Campos", "ingreso": "17/03/2009", "cuota_al_dia": True}
}

# Función para informar la cantidad de socios
def cantidad_de_socios():
    return len(socios)

# Función para registrar que un socio ha pagado todas las cuotas adeudadas
def pagar_cuotas(socio_numero):
    if socio_numero in socios:
        socios[socio_numero]["cuota_al_dia"] = True
        print(f"El socio n°{socio_numero} ha pagado todas las cuotas adeudadas.")
    else:
        print("Socio no encontrado.")

# Función para modificar la fecha de ingreso de los socios
def modificar_fecha_de_ingreso(fecha_vieja, fecha_nueva):
    for numero, datos in socios.items():
        if datos["ingreso"] == fecha_vieja:
            datos["ingreso"] = fecha_nueva
            print(f"Fecha de ingreso del socio n°{numero} modificada a {fecha_nueva}.")

# Función para dar de baja a un socio por nombre y apellido
def dar_de_baja(nombre, apellido):
    for numero, datos in socios.items():
        if datos["nombre"] == nombre and datos["apellido"] == apellido:
            del socios[numero]
            print(f"{nombre} {apellido} ha sido dado de baja del club.")
            return
    print("Socio no encontrado.")

# Función para imprimir el listado completo de socios
def imprimir_listado_de_socios():
    for numero, datos in socios.items():
        estado_cuota = "al día" if datos["cuota_al_dia"] else "pendiente"
        print(f"Socio n°{numero}: {datos['nombre']} {datos['apellido']}, ingresó: {datos['ingreso']}, cuota {estado_cuota}.")

# Programa principal
while True:
    print("\nMenú:")
    print("1. Informar cantidad de socios")
    print("2. Registrar pago de cuotas de un socio")
    print("3. Modificar la fecha de ingreso de los socios")
    print("4. Dar de baja a un socio")
    print("5. Imprimir listado de socios")
    print("6. Salir")
    
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        print(f"El club tiene {cantidad_de_socios()} socios.")
    elif opcion == "2":
        numero_socio = int(input("Ingrese el número de socio que ha pagado todas las cuotas adeudadas: "))
        pagar_cuotas(numero_socio)
    elif opcion == "3":
        fecha_vieja = "13/03/2018"
        fecha_nueva = "14/03/2018"
        modificar_fecha_de_ingreso(fecha_vieja, fecha_nueva)
    elif opcion == "4":
        nombre = input("Ingrese el nombre del socio que desea dar de baja: ")
        apellido = input("Ingrese el apellido del socio que desea dar de baja: ")
        dar_de_baja(nombre, apellido)
    elif opcion == "5":
        print("\nListado de Socios:")
        imprimir_listado_de_socios()   
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

