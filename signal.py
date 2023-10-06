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
        #self.beams: list[Beam] = beams
    