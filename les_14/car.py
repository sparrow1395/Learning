class Car:
    FUEL_TYPE = ['gas', 'diesel', 'electric', 'hybrid']
    COLORS = []
    NUMBER_OF_CARS = 0

    @staticmethod
    def is_valid_fuel_type(fuel_type):
        if fuel_type in Car.FUEL_TYPE:
            return fuel_type
        else:
            return Car.FUEL_TYPE[0]

    def __init__(self, model, year, fuel_type, color):
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = self.is_valid_fuel_type(fuel_type)
        Car.NUMBER_OF_CARS += 1
        self.number = Car.NUMBER_OF_CARS
        if self.color not in Car.COLORS:
            Car.COLORS.append(color)

    @property
    def numbers(self):
        return f"{self.number} from {Car.NUMBER_OF_CARS}"

    @classmethod
    def get_used_colors(cls):
        return len(Car.COLORS)

    @classmethod
    def get_number_of_cars(cls):
        return Car.NUMBER_OF_CARS

    def __str__(self):
        return f'{self.model} - {self.year} - {self.fuel_type} - {self.color}'


car_1 = Car('Zaz', 1979, 'diesel', 'black')

car_2 = Car('BMW', 2000, 'gas', 'red')

car_3 = Car('VOLVO', 2012, 'electric', 'black')

car_4 = Car('Mercedes', 2012, 'hybrid', 'black')

print('COLORS:', Car.get_used_colors())

print('NUMBER_OF_CARS:', Car.get_number_of_cars())

for item in (car_1, car_2, car_3, car_4):

    print('item:', item)

    print('numbers:', item.numbers)

