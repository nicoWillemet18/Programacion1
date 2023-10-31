# 1.	Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# •	mostrar(): Muestra los datos de la persona.
# •	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.


class Person:
    def __init__(self,name="",age=0,dni=""):
        self.name=name
        self.age=age
        self.dni=dni

    #metodos
    def set_name (self,name):
        if name.strip()!="":#validar que no sea nulo
            self.name=name
        else:
            print("el nombre no puede esatr vacio")

    def get_name (self):
        return self.name
    
    def set_age (self,age):
        if age >=0: #validar que no sea nulo
            self.age=age
        else:
            print("edad ingresada invalida")

    def get_age (self):
        return self.age
    
    def set_dni (self,dni):
        if dni.isdigit() and len(dni) == 8:#validar que no sea nulo
            self.dni=dni
        else:
            print("dni invalido")

    def get_dni (self):
        return self.dni
    
    def show(self):
        print(f'nombre: {self.name},edad: {self.age},dni: {self.dni}')
    def is_adult(self):
        if self.age>=18:
            return "si"
        else:
            return "no"
  
# 2.	Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. 
# Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# •	mostrar(): Muestra los datos de la cuenta.
# •	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# •	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Account:
    def __init__(self, holder, balance=0.0):
        self.holder = holder
        self.balance = balance

    def get_holder(self):
        return self.holder

    def set_holder(self, holder):
        self.holder = holder

    def get_balance(self):
        return self.balance
    def show(self):
        print(f"titular: {self.holder}")
        print(f"cantidad en la cuenta: {self.balance} $")

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'se deposito {amount}$ en la cuenta de {self.holder}')
        else:
            print('no se puede depositar valores negativos')

    def withdraw(self,amount):
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount
                print(f'se deposito {amount}$ en la cuenta de {self.holder}')
            else:
                print('dinero insuficiente en la cuenta')
        else:
            print('no se puede retirar valores negativos')        


    
# 3.	Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos,
#  imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def determinar_tipo(self):
        if self.side1 == self.side2 == self.side3:
            return "Equilátero"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Isósceles"
        else:
            return "Escaleno"
    def obtener_lado_mayor(self):
        return max(self.side1, self.side2, self.side3)

# 4.	Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:
# •	Añadir contacto
# •	Lista de contactos
# •	Buscar contacto
# •	Editar contacto
# •	Cerrar agenda

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Agenda:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print("Contacto añadido exitosamente.")

    def list_contacts(self):
        if not self.contacts:
            print("No hay contactos en la agenda.")
        else:
            print("Lista de contactos:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Nombre: {contact.name}, Teléfono: {contact.phone}, Email: {contact.email}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(f"Contacto encontrado - Nombre: {contact.name}, Teléfono: {contact.phone}, Email: {contact.email}")
                return
        print(f"Contacto con nombre {name} no encontrado.")

    def edit_contact(self, name, new_phone, new_email):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = new_phone
                contact.email = new_email
                print("Contacto actualizado exitosamente.")
                return
        print(f"Contacto con nombre {name} no encontrado.")

    def close_agenda(self):
        print("Agenda cerrada.")