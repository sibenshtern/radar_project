from typing import Optional

from coordinates import Vector, Coordinates3D
from signal import Signal


class Emitter:

    def __init__(self, characteristics: Optional[list] = None):
        self.characteristics: list = characteristics

    def send_signal(self, angle: int, departure_time: int, direction: Vector,
                 speed: Vector):
        signal = Signal(angle, departure_time, direction, speed) #, beams)
        return signal


class Receiver:

    def __init__(self, characteristics: Optional[list] = None):
        self.characteristics: list = characteristics
        self.received_signals: list = []


class Radar:

    def __init__(self, emitter: Emitter = Emitter(),
                 receiver: Receiver = Receiver()) -> None:
        self.emitter: Emitter = emitter
        self.receiver: Receiver = receiver
        self.range_of_action: int = 80
        self.direction = Coordinates3D(0, 0, 0)
        self.radius = 1
