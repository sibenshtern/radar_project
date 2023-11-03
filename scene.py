from model import *

from radar import Radar
from objects.aircraft import Aircraft
from signal import Signal
# from collision_detector import CollisionDetector
# from tracker import Tracker
from coordinates.coordinates import Vector3D

import pygame as pg

class Scene:
    def __init__(self, app, radar: Radar, objects: list[Aircraft], signals: list[Signal], duration: int, time):
        self.app = app

        self.radar = radar
        self.objects: list = objects
        self.signals: list = signals
        self.time: int = time
        self.duration: int = duration
        # self.collision_detector = CollisionDetector(self.radar)
        # self.tracker = Tracker()

        self.trajectories = []
        self.reflected = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # radar station
        # add(Cube(app))

        # ground
        n, s = 30, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z), tex_id=1))

    def send_signals(self):
        self.signals.extend(self.radar.emitter.send_signals(self.time))
        self.trajectories.append([signal.position(self.time) for signal in self.signals])
        self.reflected.append([signal.reflected for signal in self.signals])

    def render(self):
        for obj in self.objects:
            obj.render()

        # signals_detection_object = self.collision_detector.scan_objects(self.signals, self.objects, self.time)

        # for signal in signals_detection_object:
        #    self.signals.remove(signal)

        # signals_detection_radar = self.radar.receiver.ab_filter(self.collision_detector.scan_radar(self.signals, self.time))
        # signals_detection_radar = self.collision_detector.scan_radar(self.signals, self.time)
        # self.tracker.process_signals(signals_detection_radar, self.time)
        # for signal in signals_detection_radar:
        #   self.signals.remove(signal)
