from objects.aircraft import Aircraft
from logic.signal import Signal


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
                        signal.direction + signal.position(
                                time) - obj.position) < obj.reflection_radius:
                    signal.update(obj.position, -signal.speed, time)
                elif (not signal.reflected) and abs(
                        signal.direction + signal.position(
                                time)) >= self.radar.emitter.range_of_action:
                    return_signals.add(signal)
        return list(return_signals)

    # search for collision between radar and reflective signals
    def scan_radar(self, signals: list[Signal], time):
        return_signals = []
        for signal in signals:
            if (abs(signal.position(time) - self.radar.receiver.position) <=
                    self.radar.receiver.radius):
                signal.power = signal.power / (abs(signal.position(time)) ** 2)
                return_signals.append(signal)
        return return_signals
