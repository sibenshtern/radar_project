from copy import deepcopy
from typing import Union
from abc import ABC, abstractmethod

from coordinates import Vector, Coordinates, Vector3D, Coordinates3D


class Maneuver:

    def __init__(self, duration: int, obj):
        if duration <= 0:
            raise Exception("Duration must be greater than zero.")

        self.duration = duration
        self.obj = obj

    def prepare(self):
        pass

    def do(self):
        pass

    def finish(self):
        pass


class CenterFold(Maneuver):

    def prepare(self):
        pass

    def finish(self):
        pass


class ChangeHeight(Maneuver):

    def __init__(self, duration: int, obj, new_height: int):
        super().__init__(duration, obj)
        self.new_height = new_height
        self.__previous_speed = deepcopy(obj.speed)

        self.current_time = 0

    def prepare(self):
        pass

    def finish(self):
        pass


class ChangeSpeed(Maneuver):

    def __init__(self, duration: int, obj, new_speed: Vector):
        if not isinstance(new_speed, type(obj.speed)):
            raise ValueError("New speed and object speed has different type.")

        super().__init__(duration, obj)
        self.new_speed = new_speed

    def prepare(self):
        pass

    def finish(self):
        pass

