from typing import Optional
from collections import namedtuple
import signal


class Emitter:

    def __init__(self, characteristics: Optional[list] = None):
        self.characteristics: list = characteristics

    def send_signal(self, angle: int, departure_time: int, direction: Coordinates,
                 speed: Coordinates):
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
