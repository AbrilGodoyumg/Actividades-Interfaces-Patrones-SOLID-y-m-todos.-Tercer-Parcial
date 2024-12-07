from abc import ABC, abstractmethod

class Servicio(ABC):
    @abstractmethod
    def ofrecer(self):
        pass

class Restaurante(Servicio):
    def __init__(self, costo):
        self.costo = costo

    def ofrecer(self):
        return f"Restaurante, costo adicional ${self.costo} por persona."

class Spa(Servicio):
    def __init__(self, costo):
        self.costo = costo

    def ofrecer(self):
        return f"Acceso a Spa, costo adicional ${self.costo} por día."

class Habitacion:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad

    def reservar(self):
        return f"Habitación {self.numero} para {self.capacidad} personas reservada."

class Hotel:
    def __init__(self, nombre_hotel, habitacion, servicios=None):
        self.nombre_hotel = nombre_hotel
        self.habitacion = habitacion
        self.servicios = servicios if servicios else []  

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def generar_reserva(self):
        print(f"Hotel: {self.nombre_hotel}")
        print(self.habitacion.reservar())
        for servicio in self.servicios:
            print(servicio.ofrecer())

habitacion = Habitacion("13", 3)
servicio_restaurante = Restaurante(100)
servicio_spa = Spa(50)

hotel_california = Hotel("Hotel California", habitacion, [servicio_restaurante, servicio_spa])
hotel_california.generar_reserva()