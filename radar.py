import math
from typing import Optional

from coordinates import Vector, Vector3D, Coordinates, Coordinates3D
from signal import Signal


class Emitter:

    def __init__(self, range_of_action: int,  characteristics: Optional[list] = None):
        self.range_of_action: int = range_of_action
        self.characteristics: list = characteristics
        self.fineness_of_coating = 10

    def send_signal(self, departure_time: int, direction: Vector,
                    speed: Vector):
        signal = Signal(departure_time, direction, speed) #, beams)
        return signal

    def send_signals(self, departure_time) -> list[Signal]:
        signals = []
        for i in range(self.fineness_of_coating):
            first_angle = 2 * math.pi / self.fineness_of_coating * i
            for j in range(self.fineness_of_coating // 2):
                second_angle = (math.pi / self.fineness_of_coating // 2) * (i * 4)
                x, y, z = math.cos(first_angle), math.sin(second_angle), math.sin(second_angle)
                signals.append(self.send_signal(departure_time, Vector3D(x, y, z), Vector3D(1, 1, 1)))
        return signals

class Receiver:

    def __init__(self, radius: int, position: Coordinates, characteristics: Optional[list] = None):
        self.characteristics: list = characteristics
        self.received_signals: list = []
        self.radius: int = radius
        self.position: Coordinates = position

    def ab_filter(self, signals: list[Signal]):
        return signals


class Radar:

    def __init__(self, emitter: Emitter = Emitter(80),
                 receiver: Receiver = Receiver(1, Coordinates3D(0, 0, 0))) -> None:
        self.emitter: Emitter = emitter
        self.receiver: Receiver = receiver
