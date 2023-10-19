from radar import Radar
from objects.aircraft import Aircraft
from signal import Signal
from coordinates import Vector3D


class CollisionDetector:
    def __init__(self, radar):
        self.radar = radar

    def scan_objects(self, signals: list[Signal], objects: list[Aircraft], time):
        return_signals = set()
        for signal in signals:
            for obj in objects:
                if (not signal.reflected) and abs(signal.direction + signal.speed * (time - signal.departure_time) - obj.position) < obj.radius:
                    null_vector = Vector3D(0, 0, 0)
                    signal.update(obj.position, null_vector - signal.speed, time)
                    print("*")
                elif (not signal.reflected) and abs(signal.direction + signal.speed * (
                        time - signal.departure_time)) >= self.radar.emitter.range_of_action:
                    return_signals.add(signal)
        return list(return_signals)

    def scan_radar(self, signals: list[Signal], time):
        return_signals = []
        for signal in signals:
            if abs(signal.direction + signal.speed * (
                    time - signal.departure_time) - self.radar.receiver.position) <= self.radar.receiver.radius:
                return_signals.append(signal)
        return return_signals
