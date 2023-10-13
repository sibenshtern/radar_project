from radar import Radar, Emitter, Receiver
from objects.aircraft import Aircraft
from signal import Signal
from collision_detector import CollisionDetector
from coordinates import Vector3D


class Scene:
    def __init__(self, radar: Radar, objects : list[Aircraft], 
                 signals: list[Signal], duration: int):
        self.radar = radar
        self.objects: list = objects
        self.signals: list = signals
        self.time: int = 0
        self.duration: int = duration
        self.collision_detector = CollisionDetector()

    def update(self):
        if self.duration <= self.time:
            return
        self.time += 1
        if len(self.signals) == 0:
            v3d = Vector3D(1, 0, 0) 
            sp3d = Vector3D(1, 0, 0)
            signal = self.radar.emitter.send_signal(0, self.time, v3d, sp3d)
            self.signals.append(signal)
        # TODO: rewrite
        signals_detection_object = self.collision_detector.scan_objects(self.signals, self.objects, self.time)
        for signal in signals_detection_object:
            self.signals.remove(signal)

        signals_detection_radar = self.collision_detector.scan_radar(self.signals, self.radar, self.time)
        for signal in signals_detection_radar:
            self.signals.remove(signal)