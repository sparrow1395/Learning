from oop_1 import Auto
import time


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=2, weight=1000):
        super().__init__(brand, age, mark, color=2, weight=1000)
        self.max_load = max_load

    def move(self):
        print("Attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("Load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=2, weight=1000):
        super().__init__(brand, age, mark, color=2, weight=1000)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"Max speed is {self.max_speed}")


truck_1 = Truck("BMW", 12, "truck", 500)
truck_2 = Truck("MAN", 10, "truck", 200)
truck_1.load()
truck_2.birthday()
car_1 = Car("Porshe", 5, "sportcar", 250)
car_2 = Car("BMW", 6, "car", 300)
car_1.move()
car_2.stop()