from typing import TypeVar
from copy import deepcopy
from datetime import datetime

from coordinates.vectors import Vector3D, VectorGCS, VectorLECS
from coordinates.coordinates import Coordinates3D, CoordinatesGCS

import objects.maneuvers as maneuvers
import logger

V = TypeVar("V", Vector3D, VectorGCS, VectorLECS)
C = TypeVar("C", Coordinates3D, CoordinatesGCS)
M = TypeVar("M", maneuvers.ChangeHeight,
            maneuvers.ChangeSpeed, maneuvers.CenterFold)


class Aircraft:

    def __init__(self, name: str, position: C, speed: V, acceleration: V,
                 radius: float = 1):
        self.name: str = name
        self.position: C = deepcopy(position)
        self.speed: V = deepcopy(speed)
        self.acceleration: V = deepcopy(acceleration)

        self.effective_scattering_area = 10  # meters^2
        self.centerfold_radius: float = 10
        self.reflection_radius: float = radius

        self.__trajectory: list[C] = [deepcopy(position)]

        self.__current_maneuvers: list[M] = []
        self.__logger = logger.get_aircraft_logger(__name__)
        self.__filename = f"trajectories/'{name}'_{datetime.now()}.txt"
        open(self.__filename, "w").close()

    def __write_position(self):
        with open(self.__filename, "a") as file:
            c = self.position
            file.write(f"{c.x};{c.y};{c.z}\n")

    def make_maneuver(self, maneuver: M):
        self.__current_maneuvers.append(maneuver)
        self.__current_maneuvers[-1].prepare()

    def update(self, dt: float = 1.0) -> None:
        for_deletion = []

        # TODO: make better this code
        for i in range(len(self.__current_maneuvers)):
            if self.__current_maneuvers[i].is_finished:
                self.__logger.info(f"Finished maneuver "
                                   f"{self.__current_maneuvers[i].__class__}")
                for_deletion.append(i)
            else:
                self.__current_maneuvers[i].do()

        for index in for_deletion:
            self.__current_maneuvers.pop(index)
        # this code
        self.position += self.speed * dt + (self.acceleration * dt ** 2) / 2
        self.speed += self.acceleration * dt
        self.__logger.info(f"{self}")

        self.__trajectory.append(deepcopy(self.position))
        self.__write_position()

    def get_trajectory(self) -> list[C]:
        return deepcopy(self.__trajectory)

    def __str__(self):
        return (f"Aircraft(name: {self.name}, "
                f"position: {str(self.position)}, speed: {str(self.speed)}, "
                f"acceleration: {str(self.acceleration)})")

    def __repr__(self):
        return (f"AerialObject({self.name}, {self.position}, {self.speed}, "
                f"{self.acceleration})")
