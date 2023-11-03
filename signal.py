from collections import namedtuple
from typing import TypeVar

from coordinates.vectors import Vector3D, VectorGCS, VectorLECS
from coordinates.coordinates import Coordinates3D, CoordinatesGCS, CoordinatesLECS

V = TypeVar('V', Vector3D, VectorGCS, VectorLECS)
C = TypeVar('C', Coordinates3D, CoordinatesGCS, CoordinatesLECS)

Beam = namedtuple("Beam", ["power", "direction_angle"])


class Signal:

    def __init__(self, departure_time: int, direction: V,
                 speed: V):  # , beams: list[Beam]):
        self.departure_time: int = departure_time
        self.direction: V = direction
        self.speed: V = speed
        self.reflected: bool = False
        # self.beams: list[Beam] = beams

    def update(self, new_direction: V, new_speed: V, new_time: int): # +aircraft
        self.direction = new_direction
        self.speed = new_speed
        self.departure_time = new_time
        self.reflected = True

    def position(self, time: int) -> V:
        return self.direction + (abs(time - self.departure_time) * self.speed)