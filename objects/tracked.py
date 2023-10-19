from typing import Union
from copy import deepcopy

from coordinates import Coordinates3D


class Tracked:

    def __init__(self, tracking_start_time: int):
        self.trajectory: list[Union[Coordinates3D]] = []
        self.tracking_start_time: int = 0
        self.last_tracked_time: int = 0

    def add_position(self, position: Union[Coordinates3D]):
        self.trajectory.append(deepcopy(position))
