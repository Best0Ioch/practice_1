from car import Car
from driver import Driver

class Minivan(Car):
    def __init__(self, model: str, speed: int, seats: int, driver: Driver, child_seat: bool):
        super().__init__(model, speed, seats)
        self.driver = driver
        self.child_seat = child_seat

    def info(self) -> None: 
        if self.child_seat :
            is_child_seat = " " 
        else :
            is_child_seat =   "не"
        print(f"Minivan: {self.model}, {self.seats} місць, дитяче крісло:{is_child_seat} присутнє, "
              f"швидкість: {self.speed}, водій: {self.driver}")
