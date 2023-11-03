from objects.aircraft import Aircraft
from signal import Signal


class CollisionDetector:
    def __init__(self, radar):
        self.radar = radar

    def scan_objects(self, signals: list[Signal], objects: list[Aircraft], time):
        return_signals = set()
        for signal in signals:
            for obj in objects:
                if (not signal.reflected) and abs(signal.direction + signal.position(time) - obj.position) < obj.reflection_radius:
                    signal.update(obj.position, -signal.speed, time)
                    print("*")
                elif (not signal.reflected) and abs(signal.direction + signal.position(time)) >= self.radar.emitter.range_of_action:
                    return_signals.add(signal)
        return list(return_signals)

    def scan_radar(self, signals: list[Signal], time):
        return_signals = []
        for signal in signals:
            if abs(signal.direction + signal.position(time) - self.radar.receiver.position) <= self.radar.receiver.radius:
                return_signals.append(signal)
        return return_signals