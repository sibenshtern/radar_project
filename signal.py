Beam = namedtuple("Beam", ["power", "direction_angle"])

class Signal:

    def __init__(self, angle: int, departure_time: int, direction: Coordinates,
                 speed: Coordinates)#, beams: list[Beam]):
        self.angle: int = 0 #angle
        self.departure_time: int = departure_time
        self.direction: Coordinates = direction
        self.speed: Coordinates = speed
        #self.beams: list[Beam] = beams
    