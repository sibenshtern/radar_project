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
        self.is_finished = False

    def prepare(self):
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
        self.speed_z = (self.new_height - self.obj.position.z) / self.duration

    def prepare(self):
        if isinstance(self.obj.speed, Vector3D):
            self.obj.speed.z = self.speed_z

    def do(self):
        self.current_time += 1

        if self.current_time >= self.duration:
            self.finish()
            self.is_finished = True

    def finish(self) -> None:
        self.obj.speed = deepcopy(self.__previous_speed)


class ChangeSpeed(Maneuver):

    def __init__(self, duration: int, obj, new_speed: Vector):
        if not isinstance(new_speed, type(obj.speed)):
            raise ValueError("New speed and object speed has different type.")

        super().__init__(duration, obj)
        self.new_speed = deepcopy(new_speed)

    def prepare(self):
        self.obj.speed = deepcopy(self.new_speed)
        self.finish()
        self.is_finished = True

    def do(self):
        pass

    def finish(self):
        pass

