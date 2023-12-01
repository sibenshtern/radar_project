from typing import TypeVar
import logging

from objects import Tracked
from coordinates.coordinates import Coordinates3D, CoordinatesGCS
from logic.radar import Signal

C = TypeVar('C', Coordinates3D, CoordinatesGCS)

EPSILON = 1
REQUIRED_MINIMUM_TIME = 3 * 24
STOP_TRACKING_TIME = 10 * 24


class Tracker:

    def __init__(self):
        self.objects: list[Tracked] = []
        self.archive_objects: list[Tracked] = []
        self.__logger: logging.Logger = logging.getLogger(__name__)

    def __config_logger(self):
        pass

    def calculate_coordinate(self, signals: list[Signal]) -> list[C]:
        coordinates: list[C] = []

        for signal in signals:

            r = (signal.init_power / signal.power ** 1/4)
            coordinates.append(signal.direction)

        return coordinates

    def process_signals(self, signals: list[Signal], current_time: int):
        coordinates: list[C] = self.calculate_coordinate(signals)

        for coordinate in coordinates:
            for obj in self.objects:
                if (EPSILON / 1000 < abs(obj.trajectory[-1] - coordinate) <
                        EPSILON):
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