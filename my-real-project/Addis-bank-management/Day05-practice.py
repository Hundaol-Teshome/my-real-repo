from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"This is a {self.make} {self.model}."

    @abstractmethod
    def wheels(self):
        """Return the number of wheels this vehicle has."""
        pass


class Car(Vehicle):
    def wheels(self):
        return 4

class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        # Exercise 2: Setting make and model via super().__init__()
        super().__init__(make, model)
        self.capacity = capacity

    def describe(self):
        return f"This is a {self.make} {self.model} with a capacity of {self.capacity} tons."

    def wheels(self):
        return 6

if __name__ == "__main__":
    print("=" * 50)
    print("Exercise 4: Polymorphism Demo")
    print("=" * 50)

    vehicles = [
        Car("Toyota", "Corolla"),
        Truck("Ford", "F-150", 2.5),
        Car("Honda", "Civic"),
        Truck("Volvo", "FH16", 40.0),
        Car("Tesla", "Model 3"),
    ]

    for vehicle in vehicles:
        print(f"\n{vehicle.describe()}")
        print(f"  → Wheels: {vehicle.wheels()}")

    print("\n" + "=" * 50)
    print("Summary")
    print("=" * 50)
    print(f"Total vehicles in the list: {len(vehicles)}")
    print("Each vehicle responded to describe() and wheels() with its own implementation.")