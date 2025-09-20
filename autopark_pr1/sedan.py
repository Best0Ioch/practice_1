from car import Car
from driver import Driver

class Sedan(Car):
    def __init__(self, model: str, speed: int, seats: int, driver: Driver, trunk_volume: int):
        super().__init__(model, speed, seats)
        self.driver = driver
        self.trunk_volume = trunk_volume

    def info(self) -> None:
        print(f"Седан: {self.model}, {self.seats} місць, багажник: {self.trunk_volume} л, "
              f"швидкість: {self.speed}, водій: {self.driver}")
