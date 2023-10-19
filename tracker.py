from typing import TypeVar

from objects import Tracked
from coordinates import Coordinates3D, CoordinatesGCS, CoordinatesLECS

C = TypeVar('C', CoordinatesGCS, CoordinatesLECS, Coordinates3D)

EPSILON = 1


class Tracker:

    def __init__(self):
        self.objects: list[Tracked] = []

    def calculate_coordinate(self, signal) -> C:
        return Coordinates3D(0, 0, 0)

    def process_signal(self, signal: 'Signal', current_time: int):
        coordinates = self.calculate_coordinate(signal)

        for obj in self.objects:
            if abs(obj.trajectory[-1] - coordinates) < EPSILON:
                obj.trajectory.append(coordinates)
                obj.last_tracked_time = current_time
                break
        else:
            self.objects.append(Tracked(current_time))
            self.objects[-1].trajectory.append(coordinates)
