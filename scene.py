from model import *

from radar import Radar
from objects.aircraft import Aircraft
from signal import Signal
from modeling import Scene as ModelingScene
from copy import deepcopy
from collision_detector import CollisionDetector
from tracker import Tracker
from coordinates.coordinates import Coordinates3D

import pygame as pg


class Scene(ModelingScene):
    def __init__(self, app, radar: Radar, objects: list[Aircraft], signals: list[Signal], duration: int, time):
        super().__init__(radar, objects, signals, duration)
        self.app = app

        self.radar = radar
        self.objects: list = objects
        self.signals: list = signals
        self.radar_model = None
        self.floor: list = []
        self.time: int = time
        self.duration: int = duration
        self.collision_detector = CollisionDetector(self.radar)
        self.tracker = Tracker()

        self.show_signals = True

        self.trajectories = []
        self.reflected = []
        self.signals.extend(self.radar.emitter.send_signals(self.time))
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # radar station`
        self.radar_model = (Cube(app, pos=(1, 0, 0)))

        # ground
        n, s = 30, 2
        for x in range(-n, n, s):
            for y in range(-n, n, s):
                self.floor.append(Cube(app, pos=(x, y, -2), tex_id=1))

    def update(self):
        if self.duration <= self.time:
            return
        self.time += 1

        for aircraft in self.objects:
            aircraft.update()

        # self.signals.extend(self.radar.emitter.send_signals(self.time))
        self.trajectories.append([signal.position(self.time) for signal in self.signals])
        self.reflected.append([signal.reflected for signal in self.signals])

        signals_detection_object = self.collision_detector.scan_objects(self.signals, self.objects, self.time)

        for signal in signals_detection_object:
            self.signals.remove(signal)

        # signals_detection_radar = self.radar.receiver.ab_filter(self.collision_detector.scan_radar(self.signals, self.time))
        signals_detection_radar = self.collision_detector.scan_radar(self.signals, self.time)
        self.tracker.process_signals(signals_detection_radar, self.time)
        for signal in signals_detection_radar:
            self.signals.remove(signal)

        for signal in self.signals:
            if (abs(signal.position(self.time)) > self.radar.radius):
                self.signals.remove(signal)


    def render_signals(self):
        for signal in self.signals:
            signal_position = signal.position(self.time)
            Cube(self.app, pos=signal_position,
                 scale=(0.1, 0.1, 0.1)).render()

    def render(self):
        self.update()
        for obj in self.objects:
            obj.render()

        for obj in self.floor:
            obj.render()

        self.radar_model.render()

        if self.show_signals:
            self.render_signals()

