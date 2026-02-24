
class Vehicle:
    def move(self):
        print("The vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("vroom-vroom")


class Bicycle(Vehicle):
    def move(self):
        print("tring-tring")


car = Car()
bicycle = Bicycle()

car.move()
bicycle.move()
