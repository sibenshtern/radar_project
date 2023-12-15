import math
from typing import Optional, TypeVar

from coordinates.coordinates import Coordinates, Coordinates3D
from coordinates.vectors import Vector, Vector3D, VectorGCS, VectorLECS
from logic.signal import Signal

V = TypeVar('V', Vector, Vector3D, VectorGCS, VectorLECS)


# сlass for emitter from radar
class Emitter:

    def __init__(self, range_of_action: int,
                 characteristics: Optional[list] = None):
        self.range_of_action: int = range_of_action
        self.characteristics: list = characteristics
        self.fineness_of_coating = 50
        self.radiation_power = 150000  # Watt
        self.transmit_antenna_gain = 40  # decibel

    # send one signal to direction with speed
    def send_signal(self, departure_time: int, direction: V, speed: V,
                    power_multiply=0):
        signal = Signal(departure_time, direction, speed, power_multiply)
        return signal

    # send signals to half of sphere
    def send_signals(self, departure_time) -> list[Signal]:
        signals = []
        count, ci = 3, 2
        for j in range(self.fineness_of_coating + 1):
            radius = math.sin(j * math.pi / (2 * self.fineness_of_coating))
            z = math.cos(j * math.pi / (2 * self.fineness_of_coating))
            count += ci
            for i in range(count):
                first_angle = 2 * math.pi / count * i
                x, y = (math.cos(first_angle) * radius,
                        math.sin(first_angle) * radius)
                signals.append(self.send_signal(departure_time,
                                                Vector3D(x, y, z),
                                                Vector3D(x, y, z)))
        return signals


# сlass for receiver from radar
class Receiver:

    def __init__(self, radius: float, position: Coordinates,
                 characteristics: Optional[list] = None):
        self.characteristics: list = characteristics
        self.received_signals: list = []
        self.radius: float = radius
        self.position: Coordinates = position


class Radar:

    def __init__(self,
                 emitter: Emitter = Emitter(80),
                 receiver: Receiver =
                 Receiver(1, Coordinates3D(0, 0, 0))):
        self.emitter: Emitter = emitter
        self.receiver: Receiver = receiver
        self.radius = 40
