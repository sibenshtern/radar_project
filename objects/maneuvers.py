from copy import deepcopy
from typing import TypeVar
import math

import objects.aircraft as aircraft
from coordinates import Vector3D, VectorGCS, VectorLECS

V = TypeVar("V", Vector3D, VectorGCS, VectorLECS)


class Maneuver:

    def __init__(self, duration: int, obj: 'aircraft.Aircraft'):
        if duration <= 0:
            raise Exception("Duration must be greater than zero.")

        self.duration = duration
        self.obj: 'aircraft.Aircraft' = obj
        self.is_finished = False
        self.current_time: int = 0

    def prepare(self):
        pass

    def do(self):
        self.current_time += 1

        if self.current_time >= self.duration:
            self.finish()
            self.is_finished = True

    def finish(self):
        pass


class CenterFold(Maneuver):

    def __init__(self, duration: int, obj: 'aircraft.Aircraft'):
        super().__init__(duration, obj)
        self.center_point = (deepcopy(obj.position) + obj.speed.norm() *
                             obj.centerfold_radius)
        self.step = (2 * math.pi * abs(self.center_point - self.obj.position)) / duration
        self.start_speed = None

    def prepare(self):
        x = self.obj.speed.x
        y = self.obj.speed.y
        self.obj.speed = Vector3D(y, -x, self.obj.speed.z)
        self.start_speed = y

    def do(self):
        self.current_time += 1

        if self.current_time >= self.duration:
            self.finish()
            self.is_finished = True

    def finish(self):
        pass


class ChangeHeight(Maneuver):

    def __init__(self, duration: int, obj: 'aircraft.Aircraft',
                 new_height: int):
        super().__init__(duration, obj)
        self.new_height = new_height
        self.__previous_speed: V = deepcopy(obj.speed)

        self.speed_z = (self.new_height - self.obj.position.z) / self.duration

    def prepare(self):
        if isinstance(self.obj.speed, Vector3D):
            self.obj.speed.z = self.speed_z

    def finish(self):
        self.obj.speed = deepcopy(self.__previous_speed)


class ChangeSpeed(Maneuver):

    def __init__(self, duration: int, obj: 'aircraft.Aircraft', new_speed: V):
        if not isinstance(new_speed, type(obj.speed)):
            raise ValueError("New speed and object speed has different type.")

        super().__init__(duration, obj)
        self.new_speed: V = deepcopy(new_speed)
        self.acceleration: V = deepcopy(obj.acceleration)

    def prepare(self):
        new_acceleration = (self.new_speed - self.obj.speed) / self.duration
        self.obj.acceleration = deepcopy(new_acceleration)

    def finish(self):
        self.obj.acceleration = deepcopy(self.acceleration)
