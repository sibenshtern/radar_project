from copy import deepcopy
from typing import TypeVar
from datetime import datetime

from coordinates import Coordinates3D, CoordinatesGCS, CoordinatesLECS

C = TypeVar('C', Coordinates3D, CoordinatesGCS, CoordinatesLECS)


class Tracked:

    def __init__(self, tracking_start_time: int):
        self.trajectory: list[C] = []
        self.start_tracked_time: int = tracking_start_time
        self.last_tracked_time: int = tracking_start_time

        self.filteredVelocityAB = Coordinates3D(0, 0, 0)
        self.extrapolatedValueAB = Coordinates3D(0, 0, 0)
        self.extrapolatedVelocityAB = Coordinates3D(0, 0, 0)

        self.extrapolatedValue = Coordinates3D(0, 0, 0)
        self.extrapolatedVelocity = Coordinates3D(0, 0, 0)

        self.obj_name = None
        self.mse = 0
        self.__filename = f"trajectories/'Tracked_{datetime.now()}_{self.start_tracked_time}.txt"
        open(self.__filename, "w").close()

    def add_position(self, position: C):
        self.trajectory.append(deepcopy(position))

    def update_time(self, new_time):
        self.last_tracked_time = new_time
        with open(self.__filename, "a") as file:
            position = self.trajectory[-1].x, self.trajectory[-1].y, self.trajectory[-1].z
            extr_position = self.extrapolatedValueAB.x, self.extrapolatedValueAB.y, self.extrapolatedValueAB.z
            file.write(f"{position[0]},{position[1]},{position[2]},{extr_position[0]},{extr_position[1]},{extr_position[2]},{self.mse / len(self.trajectory)}\n")

    @property
    def tracked_time(self):
        return self.last_tracked_time - self.start_tracked_time

    def __repr__(self):
        return f"Tracked({self.start_tracked_time}, {self.last_tracked_time}, {self.trajectory[-1]})"
