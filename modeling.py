from radar import Radar, Emitter, Receiver
from objects import Aircraft
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
        self.time += 1
        v3d = Vector3D(1, 2, 3) 
        sp3d = Vector3D(3, 3, 3)
        signal = self.radar.emitter.send_signal(0, self.time, v3d, sp3d)
        self.signals.append(signal)
        # TODO: rewrite 
        signals_detection_object = self.collisionDetector.scan_objects(self.signals, self.objects)
        #update_signals(new_signals)#UpdateSignals

        signals_detection_radar = self.collision_detector.scan_radar(self.signals, self.radar)
        self.radar.receiver.process(signals_detection_radar)
        for signal_f in signals_detection_radar:
            self.signals.remove(signal_f)

