class Vehicle:
    def __init__(self, name, speed, size):
        self.name = name
        self.speed = speed
        self.size = size

    def switchOn(self):
         print("The Vehicle is switching on...")

    def drive(self):
        print("The Vehicle is driving...")

    def fix(self):
        print("The Vehicle is currently being fixed...")

class Car(Vehicle):

    def switchOn(self):
         print("VROOM")

    def drive(self):
        print("The Vechile is driving...")

    def fix(self):
        print("The Vechile is currently being fixed...")