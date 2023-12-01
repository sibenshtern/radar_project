from modeling.model import Cube

from logic.radar import Radar
from objects.aircraft import Aircraft
from logic.signal import Signal
from logic.collision_detector import CollisionDetector
from logic.tracker import Tracker


class Scene:
    def __init__(self, app, radar: Radar, objects: list[Aircraft],
                 signals: list[Signal], duration: int, time):
        self.app = app

        self.radar = radar
        self.objects: list = objects
        self.signals: list = signals
        self.radar_model = None
        self.floor: list = []
        self.is_simulation = False
        self.time: int = time
        self.duration: int = duration
        self.collision_detector = CollisionDetector(self.radar)
        self.tracker = Tracker()

        self.show_signals = True
        self.show_trajectories = True

        self.trajectories = []
        self.reflected = []
        self.signals.extend(self.radar.emitter.send_signals(self.time))
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app

        # radar station`
        self.radar_model = Cube(app, pos=(1, 0, 0))

        # ground
        n, s = 30, 2
        for x in range(-n, n, s):
            for y in range(-n, n, s):
                self.floor.append(Cube(app, pos=(x, y, -2), tex_id=1))

    # update all objects in scene
    def update(self):
        if self.duration <= self.time or not self.is_simulation:
            return

        self.time += 1

        for aircraft in self.objects:
            aircraft.update()

        signals_detection_object = self.collision_detector.scan_objects(
            self.signals, self.objects, self.time)

        for signal in signals_detection_object:
            self.signals.remove(signal)

        signals_detection_radar = (
            self.collision_detector.scan_radar(self.signals, self.time))
        self.tracker.process_signals(signals_detection_radar, self.time)
        for signal in signals_detection_radar:
            self.signals.remove(signal)

    # emit signals
    def render_signals(self):
        for signal in self.signals:
            signal_position = signal.position(self.time)
            Cube(self.app, pos=signal_position,
                 scale=(0.1, 0.1, 0.1)).render()

    def render_trajectories(self):
        for obj in self.objects:
            for i in obj.get_trajectory()[::24]:
                Cube(self.app, pos=i, scale=(0.05, 0.05, 0.05)).render()

    def render(self):
        for obj in self.objects:
            obj.render()

        for obj in self.floor:
            obj.render()

        self.radar_model.render()

        if self.show_signals:
            self.render_signals()

        if self.show_trajectories:
            self.render_trajectories()

