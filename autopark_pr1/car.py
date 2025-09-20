from abc import ABC, abstractmethod
from functools import singledispatchmethod

class Car(ABC):
    def __init__(self, model: str, speed: int, seats: int):
        self.model = model
        self.speed = speed
        self.seats = seats
        self.__id = id(self)   

    def get_id(self) -> int:
        return self.__id

        # Перевантажений метод drive
    @singledispatchmethod
    def drive(self, arg):
        raise NotImplementedError("Непідтримуваний тип аргументу")

    @drive.register
    def _(self, distance: int):
        print(f"Автомобіль {self.model} з {self.driver} їде {distance} км ")

    @drive.register
    def _(self, city: str):
        print(f"Автомобіль {self.model} з {self.driver} їде в місто {city} ")
    @abstractmethod
    def info(self) -> None:
        pass
