class Auto:
    def __init__(self, brand, age, mark, color=2, weight=1000):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("Move")

    def stop(self):
        print("Stop")

    def birthday(self):
        new_age = self.age + 1
        print(f"Car age is {new_age}")


auto_1 = Auto("BMW", 12, "sport")
