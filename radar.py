import math
from typing import Optional, TypeVar

import matplotlib.pyplot as plt
from coordinates.vectors import Vector, Vector3D, VectorGCS, VectorLECS
from coordinates.coordinates import Coordinates, Coordinates3D
from signal import Signal

V = TypeVar('V', Vector, Vector3D, VectorGCS, VectorLECS)


class Emitter:

    def __init__(self, range_of_action: int, characteristics: Optional[list] = None):
        self.range_of_action: int = range_of_action
        self.characteristics: list = characteristics
        self.fineness_of_coating = 30
        self.radiation_power = 150000  # Watt
        self.transmit_antenna_gain = 40  # decibel

    def send_signal(self, departure_time: int, direction: V, speed: V, power_multiply=0):
        signal = Signal(departure_time, direction, speed, power_multiply)  # , beams)
        return signal

    def send_signals(self, departure_time) -> list[Signal]:
        signals = []
        count, ci = 3, 2
        for j in range(self.fineness_of_coating + 1):
            radius = math.sin(j * math.pi / (2 * self.fineness_of_coating))
            z = math.cos(j * math.pi / (2 * self.fineness_of_coating))
            count += ci
            for i in range(count):
                first_angle = 2 * math.pi / count * i
                x, y = math.cos(first_angle) * radius, math.sin(first_angle) * radius
                signals.append(self.send_signal(departure_time, Vector3D(x, y, z), Vector3D(x, y, z)))
        return signals


class Receiver:

    def __init__(self, radius: int, position: Coordinates, characteristics: Optional[list] = None):
        self.characteristics: list = characteristics
        self.received_signals: list = []
        self.radius: int = radius
        self.position: Coordinates = position

    def get_signal_noise(self, signal: Signal, radius: int, time: int):
        return signal.power * (time - signal.departure_time) * (0.035 * 40) ** 2 * 10 * 2 / (
        (4 * math.pi) ** 3 * radius ** 4 * 5 * 1, 38 * 10 ** -23 * 290)
    # add coefficient


class Radar:

    def __init__(self, emitter: Emitter = Emitter(80),
                 receiver: Receiver = Receiver(1, Coordinates3D(0, 0, 0))) -> None:
        self.emitter: Emitter = emitter
        self.receiver: Receiver = receiver
        self.radius = 40
