from copy import deepcopy

from logic.signal import Signal
from objects.aircraft import Aircraft


# class for detect collision in scene
class CollisionDetector:
    def __init__(self, radar):
        self.radar = radar

    # search for collision between objects and signals
    def scan_objects(self, signals: list[Signal], objects: list[Aircraft],
                     time):
        return_signals = set()
        for signal in signals:
            for obj in objects:
                if (not signal.reflected) and abs(
                        signal.position(time) - obj.position) < obj.reflection_radius:
                    signal.update(deepcopy(obj.position), -deepcopy(signal.speed), time)
                elif ((not signal.reflected) and
                      abs(signal.position(time))
                      >= self.radar.emitter.range_of_action):
                    return_signals.add(signal)
        return list(return_signals)

    # search for collision between radar and reflective signals
    def scan_radar(self, signals: list[Signal], time):
        return_signals = []
        for signal in signals:
            if abs(signal._position(time) - self.radar.receiver.position) <= self.radar.receiver.radius and signal.reflected:
                signal.power /= abs(signal.position(time)) ** 2
                return_signals.append(signal)
                # print(signal.power * (abs(signal.position(time)) ** 4) , signal.init_power)
        return return_signals
