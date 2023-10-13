from typing import Optional

from coordinates import Vector, Coordinates, Coordinates3D
from signal import Signal


class Emitter:

    def __init__(self, range_of_action: int,  characteristics: Optional[list] = None):
        self.range_of_action: int = range_of_action
        self.characteristics: list = characteristics

    def send_signal(self, angle: int, departure_time: int, direction: Vector,
                 speed: Vector):
        signal = Signal(angle, departure_time, direction, speed) #, beams)
        return signal


class Receiver:

    def __init__(self, radius: int, position: Coordinates, characteristics: Optional[list] = None):
        self.characteristics: list = characteristics
        self.received_signals: list = []
        self.radius: int = radius
        self.position: Coordinates = position


class Radar:

    def __init__(self, emitter: Emitter = Emitter(80),
                 receiver: Receiver = Receiver(1, Coordinates3D(0, 0, 0))) -> None:
        self.emitter: Emitter = emitter
        self.receiver: Receiver = receiver
