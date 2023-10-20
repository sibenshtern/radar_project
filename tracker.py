from typing import TypeVar

from objects import Tracked
from coordinates import Coordinates3D, CoordinatesGCS, CoordinatesLECS
from radar import Signal

C = TypeVar('C', CoordinatesGCS, CoordinatesLECS, Coordinates3D)

EPSILON = 1
REQUIRED_MINIMUM_TIME = 10
STOP_TRACKING_TIME = 5
 /

class Tracker:

    def __init__(self):
        self.objects: list[Tracked] = []
        self.archive_objects: list[Tracked] = []

    def calculate_coordinate(self, signals: list[Signal]) -> C:
        return Coordinates3D(0, 0, 0)

    def process_signal(self, signals: list[Signal], current_time: int):
        coordinates = self.calculate_coordinate(signals)

        for obj in self.objects:
            if abs(obj.trajectory[-1] - coordinates) < EPSILON:
                obj.trajectory.append(coordinates)
                obj.last_tracked_time = current_time
                break
        else:
            self.objects.append(Tracked(current_time))
            self.objects[-1].trajectory.append(coordinates)

        self.update_objects(current_time)

    def update_objects(self, current_time: int):
        for obj in self.objects:
            if current_time - obj.last_tracked_time < STOP_TRACKING_TIME:
                continue

            if obj.tracked_time >= REQUIRED_MINIMUM_TIME:
                self.archive_objects.append(obj)
            self.objects.remove(obj)
