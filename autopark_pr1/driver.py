class Driver:
    def __init__(self, name: str, driving_experience: int):
        self.name = name
        self.driving_experience = driving_experience

    def __str__(self):
        return f"{self.name} (водійський стаж {self.driving_experience} років)"
