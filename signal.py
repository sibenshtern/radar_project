from collections import namedtuple

from coordinates import Vector

Beam = namedtuple("Beam", ["power", "direction_angle"])

class Signal:

    def __init__(self, angle: int, departure_time: int, direction: Vector,
                 speed: Vector): #, beams: list[Beam]):
        self.angle: int = 0 #angle
        self.departure_time: int = departure_time
        self.direction: Vector = direction
        self.speed: Vector = speed
        self.reflected: bool = False
        #self.beams: list[Beam] = beams

    def update(self, new_direction: Vector, new_speed: Vector, new_time: int): # +aircraft
        self.direction = new_direction
        self.speed = new_speed
        self.departure_time = new_time
        self.reflected = True