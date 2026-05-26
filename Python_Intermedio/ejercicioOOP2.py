class Person:
    def __init__(self, name):
        self.name = name
        print(f"Ha nacido, {self.name}!")

class Bus():
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"La persona {person.name} subió al bus")
        else:
            print(f"El bus va lleno, {person.name} no puede subir al bus")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} bajó del bus")
        else:
            print(f"{person.name} no va en el bus")

    def show_passengers(self):
        if not self.passengers:
            print("No hay pasajeros en el bus")
        else:
            print("Pasajeros en el bus")
            for passenger in self.passengers:
                print(f'{passenger.name} va en el bus')

def main():
    person1 = Person("Arturo")
    person2 = Person("Verónica")
    person3 = Person("Carlos")

    bus = Bus(2)

    bus.add_passenger(person1)
    bus.add_passenger(person2)
    bus.add_passenger(person3)

    bus.show_passengers()

    bus.remove_passenger(person1)

    bus.show_passengers()
if __name__ == '__main__':
    main()