from collections import namedtuple
from typing import TypeVar

from coordinates.vectors import Vector3D, VectorGCS, VectorLECS
from coordinates.coordinates import Coordinates3D, CoordinatesGCS
import math

V = TypeVar('V', Vector3D, VectorGCS, VectorLECS)
C = TypeVar('C', Coordinates3D, CoordinatesGCS)

Beam = namedtuple("Beam", ["power", "direction_angle"])


class Signal:

    def __init__(self, departure_time: int, direction: V,
                 speed: V, power_multiply: int):
        self.departure_time: int = departure_time
        self.direction: V = direction
        self.speed: V = speed
        self.power_multiply = power_multiply
        self.reflected: bool = False
        self.init_power = 150000 * 40 / (2 * math.pi) #* 0.95
        # init power
        self.power: float = self.init_power

    # update signal if it collision with object
    def update(self, new_direction: V, new_speed: V, new_time: int):
        self.power = self.power / (2 * math.pi * abs(self.position(new_time)) ** 2) * 10
        self.direction = new_direction
        self.speed = new_speed
        self.departure_time = new_time
        self.reflected = True

    # get signal position
    def position(self, time: int) -> V:
        return self.direction + (abs(time - self.departure_time) * self.speed)


