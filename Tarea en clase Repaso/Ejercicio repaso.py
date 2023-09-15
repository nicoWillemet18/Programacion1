import random

list_russian=[1,2,3,4,5,6]
random_number=0
random_number=random.randint(1,6)
names=[]

print("----- RULETA RUSA -----")
players=int(input("Ingrese la cantidad de jugadores (2 a 6): "))
while players < 2 or players > 6:
    players=int(input("Cantidad incorrecta, ingrese nuevamente: "))
for p in range(players):
    player_name = input(f"Ingrese el nombre del jugador {p+1}: ")
    names.append(player_name)

while True:
    number=int(input("Ingrese 1 para comenzar o 0 para cancelar el juego: "))
    if  number ==1 :
        while True:
            long=len(list_russian)
            if(long==1):
                print("Sobrevivieron, felicidades!")
                break
            print(f"Números disponibles :D {list_russian}")
            player_turn = len(list_russian) % players 
            player_name = names[player_turn]
            number=int(input(f"Turno de {player_name}, ingresá el numero para jugar: "))
            if number==random_number:
                print(f"Murió {player_name}")
                break
            elif number in list_russian:
                list_russian.remove(number)
            else:
                print("Número no válido, intentá de nuevo")
        break              
    elif number == 0:
        break
    else:
        print("Error: dígito no válido")            
print("El juego ha finalizado :D")   