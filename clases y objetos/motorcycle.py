class Motorcycle:
    #atributo
    new=True
    engine=False
    #metodo
    def __init__(self,color,tution,fuel_liters,number_wheels,brand,model,fabrication_date,top_speed,weight) -> None:
        self.color=color
        self.tution=tution
        self.fuel_liters=fuel_liters
        self.number_wheels=number_wheels
        self.brand=brand
        self.model=model
        self.fabrication_date=fabrication_date
        self.top_speed=top_speed
        self.weight=weight
    def start(self):
        if self.engine:
            print("el motor ya estaba encendido")
        else:
            self.engine=True
            print("se encendio el motor")
    def stop(self):
        if self.engine:
            self.engine=False
            print("el motor se apago")
        else:
            self.engine=True
            print("el motor ya estaba apagado")
    def consult(self):
        print(f'El precio de la motocicleta {self.brand} {self.model} es de {self.price} $')







