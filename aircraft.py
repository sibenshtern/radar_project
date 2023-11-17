from typing import Union, TypeVar
from copy import deepcopy

from coordinates import (Vector3D, VectorGCS, VectorLECS,
                         Coordinates3D, CoordinatesGCS, CoordinatesLECS)

import objects.maneuvers as maneuvers

V = TypeVar("V", Vector3D, VectorGCS, VectorLECS)
C = TypeVar("C", Coordinates3D, CoordinatesGCS, CoordinatesLECS)
M = TypeVar("M", maneuvers.ChangeHeight,
            maneuvers.ChangeSpeed, maneuvers.CenterFold)


class Aircraft:

    def __init__(self, name: str, position: C, speed: V, acceleration: V,
                 radius: float = 5):
        self.name: str = name
        self.position: C = deepcopy(position)
        self.speed: V = deepcopy(speed)
        self.acceleration: V = deepcopy(acceleration)

        self.effective_scattering_area = 10 # meters^2
        self.centerfold_radius: float = 10
        self.reflection_radius: float = radius

        self.__trajectory: list[C] = [deepcopy(position)]

        self.__current_maneuvers: list[M] = []

    def make_maneuver(self, maneuver: Union[M]):
        self.__current_maneuvers.append(maneuver)
        self.__current_maneuvers[-1].prepare()

    def update(self, dt: float = 1.0) -> None:
        for_deletion = []

        # TODO: make better this code
        for i in range(len(self.__current_maneuvers)):
            if self.__current_maneuvers[i].is_finished:
                for_deletion.append(i)
            else:
                self.__current_maneuvers[i].do()

        for index in for_deletion:
            self.__current_maneuvers.pop(index)
        # this code

        self.position += self.speed * dt + (self.acceleration * dt ** 2) / 2
        self.speed += self.acceleration * dt

        self.__trajectory.append(deepcopy(self.position))

    def get_trajectory(self) -> list[C]:
        return deepcopy(self.__trajectory)

    def __str__(self):
        return (f"AerialObject(name: {self.name}, "
                f"position: {str(self.position)}, speed: {str(self.speed)}, "
                f"acceleration: {str(self.acceleration)})")

    def __repr__(self):
        return (f"AerialObject({self.name}, {self.position}, {self.speed}, "
                f"{self.acceleration})")
