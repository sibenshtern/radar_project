import math
from typing import Optional, TypeVar

import matplotlib.pyplot as plt
import coordinates.coordinates
from coordinates.vectors import Vector, Vector3D, VectorGCS, VectorLECS
from coordinates.coordinates import Coordinates, Coordinates3D
from signal import Signal

V = TypeVar('V', Vector, Vector3D, VectorGCS, VectorLECS)


class Emitter:

    def __init__(self, range_of_action: int,  characteristics: Optional[list] = None):
        self.range_of_action: int = range_of_action
        self.characteristics: list = characteristics
        self.fineness_of_coating = 10

    def send_signal(self, departure_time: int, direction: V, speed: V):
        signal = Signal(departure_time, direction, speed)  # , beams)
        return signal

    def send_signals(self, departure_time) -> list[Signal]:
        signals = []
        # count, ci = 3, 2
        # for j in range(self.fineness_of_coating + 1):
        #     radius = math.sin(j * math.pi / (2 * self.fineness_of_coating))
        #     z = math.cos(j * math.pi / (2 * self.fineness_of_coating))
        #     count += ci
        count = 2
        for j in range(self.fineness_of_coating + 1):
            radius = math.sin(j * math.pi / (2 * self.fineness_of_coating))
            z = math.cos(j * math.pi / (2 * self.fineness_of_coating))
            for i in range(count):
                first_angle = 2 * math.pi / count * i
                x, y = math.cos(first_angle) * radius, math.sin(first_angle) * radius
                signals.append(self.send_signal(departure_time, Vector3D(x, y, z), Vector3D(x, y, z)))

        # fig = plt.figure(1, figsize=(3, 3), dpi=100)
        # ax = fig.add_subplot(projection="3d")

        # for signal in signals:
        #     ax.scatter(signal.position(1).x, signal.position(1).y, signal.position(1).z)
        # plt.show()
        return signals


class Receiver:

    def __init__(self, radius: int, position: Coordinates, characteristics: Optional[list] = None):
        self.characteristics: list = characteristics
        self.received_signals: list = []
        self.radius: int = radius
        self.position: Coordinates = position

    def ab_filter(self, signals: list[Signal], time):
        '''
        return_signals = []
        for signal in signals:
            k = time - signal.departure_time

            if k == 1:
                filteredValue = measuredValue;
                return_signals.append(signal)
                continue
            elif k >= 2:
                filteredVelocity = signals - filteredValue) /T_0
                filteredValue = measuredValue

                extrapolatedValue = filteredValue + (filteredVelocity * T_0)
                extrapolatedVelocity = filteredVelocity
            return;

            alpha = 2 * (2 * k - 1) / (k * (k +1))
            beta = 6 / (k * (k + 1))

            filteredValue = extrapolatedValue + (alpha * (measuredValue - extrapolatedValue))
            filteredVelocity = extrapolatedVelocity + (beta / T_0 * (measuredValue - extrapolatedValue))

            extrapolatedValue = filteredValue + (filteredVelocity * T_0)
            extrapolatedVelocity = filteredVelocity
        '''
        return signals


class Radar:

    def __init__(self, emitter: Emitter = Emitter(80),
                 receiver: Receiver = Receiver(1, Coordinates3D(0, 0, 0))) -> None:
        self.emitter: Emitter = emitter
        self.receiver: Receiver = receiver
