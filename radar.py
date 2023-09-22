from typing import Optional
from collections import namedtuple


Beam = namedtuple("Beam", ["power", "direction_angle"])


class Signal:

    def __init__(self, angle: int, departure_time: int, duration: int,
                 beams: list[Beam]):
        self.angle: int = angle
        self.departure_time: int = departure_time
        self.duration: int = duration
        self.beams: list[Beam] = beams


class Emitter:

    def __init__(self, characteristics: Optional[list] = None):
        self.characteristics: list = characteristics
        self.signals: list[Signal] = []

    def send_signal(self, angle: int, departure_time: int, duration: int,
                    beams_count: int):
        pass


class Receiver:

    def __init__(self, characteristics: Optional[list] = None):
        self.characteristics: list = characteristics
        self.received_signals: list = []


class Radar:

    def __init__(self, emitter: Emitter = Emitter(),
                 receiver: Receiver = Receiver()) -> None:
        self.emitter: Emitter = emitter
        self.receiver: Receiver = receiver
