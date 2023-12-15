from copy import deepcopy
from typing import TypeVar

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

    def add_position(self, position: C):
        self.trajectory.append(deepcopy(position))

    @property
    def tracked_time(self):
        return self.last_tracked_time - self.start_tracked_time

    def __repr__(self):
        return f"Tracked({self.start_tracked_time}, {self.last_tracked_time}, {self.trajectory[-1]})"
