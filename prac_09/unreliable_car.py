from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """An unreliable car version class"""
    def __init__(self, name, fuel, reliability):
        """Initialize unreliable car version"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """"Drives the car only when it is reliable"""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven



