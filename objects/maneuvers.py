import math
from copy import deepcopy
from typing import TypeVar

import glm

import objects.aircraft as aircraft
from coordinates import Vector3D, VectorGCS, VectorLECS

V = TypeVar("V", Vector3D, VectorGCS, VectorLECS)


class Maneuver:

    def __init__(self, duration: int, obj: 'aircraft.Aircraft'):
        if duration <= 0:
            raise Exception("Duration must be greater than zero.")

        self.duration = duration
        self.object: 'aircraft.Aircraft' = obj
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
        self.angle = math.pi / duration

    def prepare(self):
        pass

    def do(self):
        self.current_time += 1

        if self.current_time >= self.duration:
            self.finish()
            self.is_finished = True

        abs_speed = abs(self.object.speed)

        self.object.speed.x = self.object.speed.x * math.cos(self.angle) - \
            self.object.speed.y * math.sin(self.angle)
        self.object.speed.y = self.object.speed.x * math.sin(self.angle) + \
            self.object.speed.y * math.cos(self.angle)

        self.object.speed = self.object.speed.norm() * abs_speed

        self.object.rot = glm.vec3(self.object.rot[0], self.object.rot[1],
                                   self.object.rot[2] + self.angle)

    def finish(self):
        pass


class ChangeHeight(Maneuver):

    def __init__(self, duration: int, obj: 'aircraft.Aircraft',
                 new_height: int):
        super().__init__(duration, obj)
        self.new_height = new_height
        self.__previous_speed: V = deepcopy(obj.speed)

        self.speed_z = ((self.new_height - self.object.position.z) /
                        self.duration)

    def prepare(self):
        if isinstance(self.object.speed, Vector3D):
            self.object.speed.z = self.speed_z

    def finish(self):
        self.object.speed = deepcopy(self.__previous_speed)


class ChangeSpeed(Maneuver):

    def __init__(self, duration: int, obj: 'aircraft.Aircraft', new_speed: V):
        if not isinstance(new_speed, type(obj.speed)):
            raise ValueError("New speed and object speed has different type.")

        super().__init__(duration, obj)
        self.new_speed: V = deepcopy(new_speed)
        self.acceleration: V = deepcopy(obj.acceleration)

    def prepare(self):
        new_acceleration = (self.new_speed - self.object.speed) / self.duration
        self.object.acceleration = deepcopy(new_acceleration)

    def finish(self):
        self.object.acceleration = deepcopy(self.acceleration)
