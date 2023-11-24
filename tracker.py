from typing import TypeVar

from objects import Tracked
from coordinates.coordinates import Coordinates3D, CoordinatesGCS, CoordinatesLECS
from radar import Signal

C = TypeVar('C', CoordinatesGCS, CoordinatesLECS, Coordinates3D)

EPSILON = 1
REQUIRED_MINIMUM_TIME = 10
STOP_TRACKING_TIME = 5


class Tracker:

    def __init__(self):
        self.objects: list[Tracked] = []
        self.archive_objects: list[Tracked] = []

    def calculate_coordinate(self, signals: list[Signal], current_time: int) -> list[C]:
        coordinates: list[C] = []

        for signal in signals:
            coordinates.append(signal.direction)
            print(signal.direction)

        return coordinates

    def process_signals(self, signals: list[Signal], current_time: int):
        coordinates: list[C] = self.calculate_coordinate(signals, current_time)

        for coordinate in coordinates:
            for obj in self.objects:
                if abs(obj.trajectory[-1] - coordinate) < EPSILON:
                    obj.trajectory.append(coordinate)
                    obj.last_tracked_time = current_time
                    break
            else:
                self.objects.append(Tracked(current_time))
                self.objects[-1].trajectory.append(coordinate)

        self.update_objects(current_time)

    def update_objects(self, current_time: int):
        for obj in self.objects:
            if current_time - obj.last_tracked_time < STOP_TRACKING_TIME:
                continue

            if obj.tracked_time >= REQUIRED_MINIMUM_TIME:
                self.archive_objects.append(obj)
            self.objects.remove(obj)
