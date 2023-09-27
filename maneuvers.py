from copy import deepcopy
from typing import Union
from abc import ABC, abstractmethod

from coordinates import Vector, Coordinates, Vector3D, Coordinates3D


class Maneuver(ABC):

    def __init__(self, duration: int, obj):
        if duration <= 0:
            raise Exception("Duration must be greater than zero.")

        self.duration = duration
        self.obj = obj

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def finish(self):
        pass


class CenterFold(Maneuver):

    def prepare(self):
        pass

    def finish(self):
        pass


class ChangeHeight(Maneuver):

    def prepare(self):
        pass

    def finish(self):
        pass


class ChangeSpeed(Maneuver):

    def prepare(self):
        pass

    def finish(self):
        pass

