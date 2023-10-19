from radar import Radar
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
        self.collision_detector = CollisionDetector(self.radar)

        self.__trajectories = []
        self.__reflected = []

    def update(self):
        if self.duration <= self.time:
            return
        self.time += 1
        # TODO: rewrite bad code to another file
        if len(self.signals) == 0:
            v3d = Vector3D(2, 0, 0)
            sp3d = Vector3D(1, 0, 0)
            signal = self.radar.emitter.send_signal(0, self.time, v3d, sp3d)
            self.signals.append(signal)

        signals_detection_object = self.collision_detector.scan_objects(self.signals, self.objects, self.time)

        self.__trajectories.append(self.signals[0].direction + self.signals[0].speed * (self.time - self.signals[0].departure_time))
        self.__reflected.append(self.signals[0].reflected)

        for signal in signals_detection_object:
            self.signals.remove(signal)

        signals_detection_radar = self.radar.receiver.ab_filter(self.collision_detector.scan_radar(self.signals, self.time))
        # send_to_tracker(self.radar.receiver.process(signals_detection_radar))
        for signal in signals_detection_radar:
            self.signals.remove(signal)
            print("D")