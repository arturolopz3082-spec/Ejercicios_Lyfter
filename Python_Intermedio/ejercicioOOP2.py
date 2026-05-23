class Person():
    def __init__(self, name):
        self.name = name
        print(f"Ha nacido {self.name}")

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"Se subió {person.name} al bus")
        else:
            print(f"El bus está lleno, ya no puede subir {person.name} ")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"Se bajó {person.name} del bus")
        else:
            print(f"La persona: {person.name} no está en el bus")

    def show_passengers(self):
        if self.passengers:
            for person in self.passengers:
                print(f'{person.name}, está en el bus')
        else:
            print("El bus está vacío")

def main():
    person1 = Person("Arturo")
    person2 = Person("Ramon")
    person3 = Person("Juan")

    bus = Bus(2)
    #print("El numero máximo de pasajeros",bus.max_passengers)
    bus.add_passger(person1)
    bus.add_passger(person2)
    bus.add_passger(person3) #Ya no debe poder subir al Bus
    bus.show_passengers()
    bus.remove_passenger(person3) #No está en el bus
    bus.remove_passenger(person2)
    bus.add_passger(person3)
    bus.show_passengers()

if __name__ == '__main__':
    main()