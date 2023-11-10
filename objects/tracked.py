from typing import TypeVar
from copy import deepcopy

from coordinates import Coordinates3D, CoordinatesGCS, CoordinatesLECS

C = TypeVar('C', Coordinates3D, CoordinatesGCS, CoordinatesLECS)


class Tracked:

    def __init__(self, tracking_start_time: int):
        self.trajectory: list[C] = []
        self.start_tracked_time: int = tracking_start_time
        self.last_tracked_time: int = tracking_start_time
        self.filteredVelocity = 0
        self.extrapolatedValue = 0
        self.extrapolatedVelocity = 0

    def add_position(self, position: C):
        self.trajectory.append(deepcopy(position))

    @property
    def tracked_time(self):
        return self.last_tracked_time - self.start_tracked_time
