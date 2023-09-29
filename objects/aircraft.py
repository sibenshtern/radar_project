from typing import Optional, Any
from copy import deepcopy

from coordinates import Vector, Coordinates, Vector3D, Coordinates3D
from maneuvers import Maneuver, ChangeHeight, ChangeSpeed, CenterFold


class AerialObject:

    def __init__(self, name: str, position: Coordinates, speed: Vector,
                 acceleration: Vector):
        self.name: str = name
        self.position: Coordinates = deepcopy(position)
        self.speed: Vector = deepcopy(speed)
        self.acceleration: Vector = deepcopy(acceleration)

        self.__trajectory: list[Coordinates] = [deepcopy(position)]

        self.__current_maneuver: Optional[Maneuver, CenterFold,
                                          ChangeHeight, ChangeSpeed] = None
        self.__making_maneuver: bool = False

    def make_maneuver(self, maneuver: Maneuver):
        self.__current_maneuver = maneuver
        self.__making_maneuver = True
        self.__current_maneuver.prepare()

    def update(self, dt: float = 1.0) -> None:
        if self.__making_maneuver and self.__current_maneuver is not None:
            self.__current_maneuver.do()

        if self.__current_maneuver is not None and \
                self.__current_maneuver.is_finished:
            self.__current_maneuver = None
            self.__making_maneuver = False

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


if __name__ == "__main__":
    obj = AerialObject("helicopter", Coordinates3D(0, 0, 0),
                       Vector3D(1, 1, 0), Vector3D(0, 0, 0))
    change_height = ChangeSpeed(10, obj, Vector3D(10, 10, 0))

    for i in range(20):
        obj.update()
        print(f"{i}:\t{obj}")
        if i == 5:
            obj.make_maneuver(change_height)


