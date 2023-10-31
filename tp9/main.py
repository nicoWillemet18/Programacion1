from clases import Person, Account,Triangle,Agenda,Contact
#1
person1=Person()
person1.set_name("eduardo")
person1.set_age(30)
person1.set_dni("12345678")
person1.show()
print(f'es adulto? {person1.is_adult()}')
#2
account = Account("John Doe", 1000.0)
account.show()
account.deposit(500.0)
account.withdraw(200.0)
account.show()
#3
side1 = float(input("Ingresa la longitud del primer lado: "))
side2 = float(input("Ingresa la longitud del segundo lado: "))
side3 = float(input("Ingresa la longitud del tercer lado: "))

triangle = Triangle(side1, side2, side3)

print(f"El triángulo es de tipo {triangle.determinar_tipo()}")
print(f"El lado con la longitud mayor es: {triangle.obtener_lado_mayor()}")

#4
agenda = Agenda()

while True:
    print("\nMenú de Agenda:")
    print("1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")
    option = input("Elija una opción (1/2/3/4/5): ")

    if option == "1":
        name = input("Nombre del contacto: ")
        phone = input("Teléfono del contacto: ")
        email = input("Email del contacto: ")
        agenda.add_contact(name, phone, email)
    elif option == "2":
        agenda.list_contacts()
    elif option == "3":
        name = input("Nombre del contacto a buscar: ")
        agenda.search_contact(name)
    elif option == "4":
        name = input("Nombre del contacto a editar: ")
        new_phone = input("Nuevo teléfono: ")
        new_email = input("Nuevo email: ")
        agenda.edit_contact(name, new_phone, new_email)
    elif option == "5":
        agenda.close_agenda()
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida (1/2/3/4/5).")

