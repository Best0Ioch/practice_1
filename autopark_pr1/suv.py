from car import Car
from driver import Driver

class SUV(Car):
    def __init__(self, model: str, speed: int, seats: int, driver: Driver, awd: bool):
        super().__init__(model, speed, seats)
        self.driver = driver
        self.awd = awd  

    def info(self) -> None:
        if self.awd :
            drive_type = "повний привід"  
        else :
            drive_type =   "передній привід"
        print(f"SUV: {self.model}, {self.seats} місць, {drive_type}, "
              f"швидкість: {self.speed}, водій: {self.driver}")
