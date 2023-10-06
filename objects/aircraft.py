from typing import Optional
from copy import deepcopy

from coordinates import Vector, Coordinates
from objects.maneuvers import Maneuver, ChangeHeight, ChangeSpeed, CenterFold


class Aircraft:

    def __init__(self, name: str, position: Coordinates, speed: Vector,
                 acceleration: Vector):
        self.name: str = name
        self.position: Coordinates = deepcopy(position)
        self.speed: Vector = deepcopy(speed)
        self.acceleration: Vector = deepcopy(acceleration)

        self.centerfold_radius: float = 10

        self.__trajectory: list[Coordinates] = [deepcopy(position)]

        self.__current_maneuvers: list[Optional[Maneuver, CenterFold,
                                       ChangeHeight, ChangeSpeed]] = []
        self.__making_maneuver: bool = False

    def make_maneuver(self, maneuver: Maneuver):
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

    def get_trajectory(self) -> list[Coordinates]:
        return deepcopy(self.__trajectory)

    def __str__(self):
        return (f"AerialObject(name: {self.name}, "
                f"position: {str(self.position)}, speed: {str(self.speed)}, "
                f"acceleration: {str(self.acceleration)})")

    def __repr__(self):
        return (f"AerialObject({self.name}, {self.position}, {self.speed}, "
                f"{self.acceleration})")
