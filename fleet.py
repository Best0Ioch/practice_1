from typing import List
from car import Car

class Fleet:
    def __init__(self, name: str):
        self.name = name
        self.cars: List[Car] = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def show_fleet(self):
        print(f"\n Автопарк '{self.name}' має {len(self.cars)} автомобіля:")
        for car in self.cars:
            car.info()
