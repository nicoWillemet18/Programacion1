from motorcycle import Motorcycle

moto1=Motorcycle("Azul", "ABC123", 20, 2, "Peru", "CBR1320RR", "2023-10-12", 300, 200)
#moto con 10 litros y 2 ruedas
moto2=Motorcycle("Rojo", "ABC123", 10, 2, "Honda", "CBR1000RR", "2023-10-24", 300, 200)
#pruebas de arranque y detencion
moto1.start()
moto1.start()
moto1.stop()
moto1.stop()
#Creación dinámica de un atributo
moto1.price = 10000
print(f'El precio de la motocicleta {moto1.brand} {moto1.model} es de {moto1.price} $')
moto1.consult()
#moto2.consult() larga error porque no tine precio



