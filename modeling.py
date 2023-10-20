from radar import Radar
from objects.aircraft import Aircraft
from signal import Signal
from collision_detector import CollisionDetector
from tracker import Tracker
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
        self.tracker = Tracker()

        self.trajectories = []
        self.reflected = []
        self.signals.extend(self.radar.emitter.send_signals(self.time))

    def update(self):
        if self.duration <= self.time:
            return
        self.time += 1
        # TODO: rewrite bad code to another file

        # self.signals.extend(self.radar.emitter.send_signals(self.time))
        self.trajectories.append([signal.position(self.time) for signal in self.signals])
        self.reflected.append([signal.reflected for signal in self.signals])

        signals_detection_object = self.collision_detector.scan_objects(self.signals, self.objects, self.time)

        for signal in signals_detection_object:
            self.signals.remove(signal)

        signals_detection_radar = self.radar.receiver.ab_filter(self.collision_detector.scan_radar(self.signals, self.time))
        self.tracker.process_signal(signals_detection_radar, self.time)
        for signal in signals_detection_radar:
            self.signals.remove(signal)